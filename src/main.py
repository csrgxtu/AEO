#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer Reilly
# Date: 19/Jan/2014
# File: main.py
# Desc: main program that download the apk from the market
# the IP things leaves to the Google APP Engine.
#
# Produced By CSRGXTU
import sys
from os.path import dirname
sys.path.insert(0, dirname(__file__) + '/../lib')

from DownloadHTTPSProxy import Download
from Download import Download as D

# download
#
# @param url string
# @param times int
# @return count int
def download(url, times):
  d = Download(url)
  count = 0
  
  for i in range(times):
    if d.doRequest():
      print 'ERROR: ', d.getHTTPCODE(), ' ', url
    else:
      count = count + 1
      print 'SUCCESS: ', count
  
  return count

# downloada
#
# @param url string
# @param times int
# @return count int
def downloada(url, times):
  d = D(url)
  count = 0
  
  for i in range(times):
    if d.doRequest():
      print 'ERROR: ', d.getHTTPCODE(), ' ', url
    else:
      count = count + 1
      print 'SUCCESS: ', count
  
  return count

# main
def main():
  if len(sys.argv) != 2:
    print "Usage: main.py times"
    return
  times = int(sys.argv[1])

  # 豌豆荚
  url = "http://112.90.148.141/m.wdjcdn.com/apk.wdjcdn.com/a/02/232b517fb99b31c65eb92f4e3490002a.apk"
  print "******starting 豌豆荚*****"
  rtv = download(url, times)
  print "******result: ", rtv

  # 应用宝
  url = "http://113.6.236.35/dd.myapp.com/16891/232B517FB99B31C65EB92F4E3490002A.apk?mkey=54bc788df8e4e33f&f=178a&fsname=com%2Ejutu%2Edragonfly%5F1%2E36%5F8.apk&asr=8eff&p=.apk"
  print "******starting 应用宝*****"
  rtv = download(url, times)
  print "******result: ", rtv

  # 360应用市场
  url = "http://shouji.360tpcdn.com/150109/908c7e34961467cd2cfdf4b54a9d6148/com.jutu.dragonfly_8.apk"
  print "******starting 360应用市场****"
  rtv = download(url, times)
  print "******result: ", rtv

  # 小米商店
  url = ""
  # 应用汇
  url = ""
  # 移动商城
  url = ""
  # 联想乐商店
  url = "http://apk.lenovomm.com/201501190943/8e57e050967ed6ce2883c9dee8a5c3ae/dlserver/fileman/crawler@cluster-1/ams/fileman/jar/2015-01-07100541-_1420596341613_0801.apk?v=5&clientid=15808-1a2-2-9999-1-3-1_240_iamp5UID9b1454f15a672d613de3ba3bat19700101077847047_c303d1p30"
  print "******starting 联想乐商店****"
  rtv = download(url, times)
  print "******result: ", rtv

  # 华为市场
  url = ""
  # n多市场
  url = "http://static.nduoa.com/apk/843/843676/1560760/com.jutu.dragonfly.apk"
  print "*****startingn多市场****"
  #rtv = download(url, times)
  rtv = downloada(url, times)
  print "****result: ", rtv

  # 优易网
  url = ""
  # pp助手
  url = ""
  # 淘宝手机市场
  url = "http://rj.m.taobao.com/wap/appmark/app_detail.htm?dir=native&appID=8095363&spm=a210u.7167065.0.0.R5HM6T"
  print "*****starting淘宝手机市场****"
  rtv = download(url, times)
  print "****result: ", rtv

  # 手赚网
  url = "http://sohu-cdn.dianjoy.com/pkg/ion/c_80279206-web_union/zhuan_c_80279206-web_union_1.2.5.0.apk"
  print "*****starting手赚网****"
  rtv = download(url, times)
  print "*****result: ", rtv

  # 百度应用市场
  url = "http://gdown.baidu.com/data/wisegame/ec908e75f24750d2/zhuanqianmizhan_8.apk"
  print "*****starting 百度应用市场****"
  #rtv = download(url, times)
  rtv = downloada(url, times)
  print "*****result: ", rtv

  # 91
  url = "http://bcs.91.com/pcsuite-dev/apk/f8609666c14a021c806ae7f7f858123e.apk"
  print "*****starting91****"
  #rtv = download(url, times)
  rtv = downloada(url, times)
  print "******result: ", rtv

  # 安卓市场
  url = "http://apk.r1.market.hiapk.com/data/upload/apkres/2015/1_8/11/com.jutu.dragonfly_114516.apk"
  print "******starting 安卓市场***"
  rtv = download(url, times)
  print "****result: ", rtv

if __name__ == '__main__':
  main()
