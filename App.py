#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from Baidu import getImageUrlList, search, nextPage, searchResult
from Downloader import downloadFromQueue
from FileHelper import getFilenameFromURL, addExtension, makedir
from Queue import Queue
from thread import start_new_thread
from  Config import Config
from NetworkPrepare import prepare
import os, sys

def baseURL():
  if Config.site == 'baidu':
    return search(Config.keyword, Config.addtional)
  if Config.site == 'jandan':
    return 'http://jandan.net/ooxx'

def main():
  # 开始准备
  prepare()
  while_n = 0 # 循环计数器
  imglist = []
  makedir(Config.directory)
  print 'Generate search url'
  URL = baseURL()
  # 下载 #############
  # 获取搜索结果数量并与_count比较取其较小值
  count = min(searchResult(URL), Config.count)
  # 没有搜索结果时退出
  if not count:
    print "No search result at current condition."
    sys.exit(1)
  # 获得指定数量的url, 存放于list  
  print 'Fetching page',
  while len(imglist) < count:
    print while_n,
    while_n += 1
    tmplist = getImageUrlList(URL)
    imglist = imglist + tmplist
    URL = nextPage(URL, len(tmplist))
  print '' # 换行
  count = len(imglist)
  print "There're %d files to download" % count
  # 将已有文件从imglist中去除
  imglist = [url for url in imglist
             if not getFilenameFromURL(url) in os.listdir(Config.directory)]
  print "There's %d files already downloaded." % (count - len(imglist))
  # 下载该list 
  print 'Fetching list of %d files' % len(imglist)
  queue = Queue()
  for url in imglist:
    queue.put(url)
  failure = []
  for i in range(Config.thread_count):
    start_new_thread(downloadFromQueue, (
                                         queue, failure, Config.directory, Config.timeout))
  queue.join()
  print "%d failed to fetch." % len(failure)

def clean():
  # 清理
  # 1.添加后缀
  print 'Adding extension ...'
  for fname in os.listdir(Config.directory):
    addExtension(Config.directory + os.sep + fname, '.jpg')
  print 'done.'
  # 2.保存cookie
  Config.cj.save()

if __name__ == "__main__":
  main()
  clean()
