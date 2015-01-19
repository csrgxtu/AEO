#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 14/Jan/2014
# File: OPPODownloader.py
# Desc: just download apk from OPPO APP Market
#
# Produced By CSRGXTU
from time import sleep
import sys
from os.path import dirname
sys.path.insert(0, dirname(__file__) + '/../lib')

from Download import Download

# main
def main():
  url = "http://storedl1.nearme.com.cn/uploadFiles/Pfiles/201501/07/e45a13c4cb8949f5b8b749f23a3b3b1d.apk?n=com.jutu.dragonfly_1.36"

  d = Download(url)
  count = 0
  for i in range(1000):
    if d.doRequest():
      print "Cant Do Request", d.getHTTPCODE()
    count = count + 1
    print count
    #sleep(60)

if __name__ == '__main__':
  main()
