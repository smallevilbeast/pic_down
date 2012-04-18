#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from cookielib import LWPCookieJar
class Config:
  keyword = '吉泽明步' # 要搜索的关键字 注意不要改变文件编码
  addtional = {} # 宽度和高度 可以为空 {}
  directory = r'../../image'  # 存放的位置
  count = 300     # 要下载的数量，自动进到20的倍数
  thread_count = 15 # 线程数
  timeout = 20 # 下载超时限制 使用超时20 10好像小了点
  # 代理设置
  proxy = 'http://localhost:7071'
  use_proxy = False
  proxy_user = 'user_name'
  proxy_pass = 'password'
  proxy_auth = False
  cookies = 'cookies.txt'
  use_cookies = True
  cj = LWPCookieJar(cookies)
  site = 'baidu'  #site='jandan'
