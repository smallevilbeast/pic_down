#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import urllib2
from Config import Config

def proxy_handler(proxy, use_proxy, proxy_auth=False, puser='', ppass=''):
  if use_proxy:
    return urllib2.ProxyHandler({"http" : proxy})
  return urllib2.ProxyHandler({})

def cookie_handler(cj):
  try:
    cj.revert(cj)
  except Exception:
    pass
  cj.clear_expired_cookies()
  return urllib2.HTTPCookieProcessor(cj)

def prepare():
  ch = cookie_handler(Config.cj)
  ph = proxy_handler(Config.proxy, Config.use_proxy)
  if Config.proxy_auth:
    pm = urllib2.HTTPPasswordMgrWithDefaultRealm()
    pm.add_password(None, Config.proxy, Config.proxy_user, Config.proxy_pass)
    urllib2.install_opener(urllib2.build_opener(ch, ph, urllib2.ProxyBasicAuthHandler(pm)))
    return
  urllib2.install_opener(urllib2.build_opener(ch, ph))
