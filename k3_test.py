# -*- coding: utf-8 -*-
"""
Copyright (c) 2017

@author: wangdan
Created on 2017/4/30 17:19
"""
import json
import urllib2


def format_code(code):
    if code[0] in ["0", "3"]:
        return "sz" + code
    elif code[0] in ["6"]:
        return "sh" + code


def format_url(code, type="m60"):
    _code = format_code(code)
    url = "http://ifzq.gtimg.cn/appstock/app/kline/mkline?" \
          "param=%s,%s,,640&_var=%s_today&r=0.8528988508953326" \
          % (_code, type, type)
    return url


def get_all_stock_data(code, type="m60"):
    try:
        uri = format_url(code, type)
        req = urllib2.urlopen(uri, timeout=3)
        content = req.read()
        if content:
            data = json.loads(content.split("=")[-1])
            return data["data"][format_code(code)]["m60"]
        else:
            return None
    except:
        return None


def unit_weight_calculate(_data):
    """
    计算某天k线的多空PK能
    :param _data: 一组数据：day, open, close, high, low, volume
    :return: 权值，float
    """
    hour = _data[0]
    open = float(_data[1])
    close = float(_data[2])
    high = float(_data[3])
    low = float(_data[4])
    volume = float(_data[5])

    base = abs(high - low)
    if base == 0:
        return 0, 0
    middle = round((close - open) / base, 3)
    if middle >= 0:
        up = round((close - high) / base, 3)
        down = round((open - low) / base, 3)
    else:
        up = round((open - high) / base, 3)
        down = round((close - low) / base, 3)
    return hour, up + middle + down, volume


def k3_weight_calculate(data3_list):
    unit0 = unit_weight_calculate(data3_list[0])
    unit1 = unit_weight_calculate(data3_list[1])
    unit2 = unit_weight_calculate(data3_list[2])
    # return unit2[0], (unit0[1]*unit0[2] + unit1[1]*unit1[2] + unit2[1]*unit2[2])/(unit0[2]+unit1[2]+unit2[2])
    return unit0[1] + unit1[1] + unit2[1]


lista = get_all_stock_data("600801")

result = {
    "catch": 0,
    "miss": 0
}

for i in xrange(len(lista) - 4):
    k3 = k3_weight_calculate(lista[i:i + 3])
    hour = lista[i + 4][0]
    open = float(lista[i + 4][1])
    close = float(lista[i + 4][2])
    high = float(lista[i + 4][3])
    low = float(lista[i + 4][4])
    volume = float(lista[i + 4][5])
    if k3 >= 0:
        if close > open:
            result['catch'] += 1
        else:
            result['miss'] += 1
    else:
        if close < open:
            result['catch'] += 1
        else:
            result['miss'] += 1

print result

