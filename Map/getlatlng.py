"""
date: 2019.9.13
author: yaming
IDE: Sublime Text 

fun: 通过地理位置获取经纬度
"""


import json
from urllib.request import urlopen, quote
import requests


def getgeocoding(address):
	url = 'http://api.map.baidu.com/geocoding/v3/?'
	address = quote(address)
	output = 'json'
	ak = 'hZIW1Ij2vHKtITApWBiL0UGycyKF0cZb'
	callback = 'showLocation'
	uri = url + 'address=' + address + '&output=' + output + '&ak=' + ak
	
	req = urlopen(uri)
	res = req.read().decode()

	print(type(res))

	temp = json.loads(res)
	lat = temp['result']['location']['lat']
	lng = temp['result']['location']['lng']
	
	return lat, lng


def main():
	address = '天津市南开区卫津路92号天津大学'

	print(getgeocoding(address))


main()