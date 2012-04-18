#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from FileHelper import getFilenameFromURL, writeBinFile
import urllib2

def getStream(url, timeout=10):
  # 返回一个url流或者False
  request = urllib2.Request(url)
  request.add_header('User-Agent', UserAgent.Mozilla)
  try:
    stream = urllib2.urlopen(request, timeout=timeout)
  except (Exception, SystemExit): # catch SystemExit to keep running
    print "URL open error. Probably timed out."
    return False
  return stream

def downloadFromQueue(queue, failure, directory='.', timeout=10):
  """Get files from a list of urls.
  return : list, contained the failure fetch"""
  while not queue.empty():
    url = queue.get()
    stream = getStream(url, timeout=timeout)
    file_name = getFilenameFromURL(url)
    if stream and writeBinFile(stream, file_name, directory):
      queue.task_done()
      print "Fetching", url, 'done.'
      continue
    failure.append(url)
    queue.task_done()
  return failure

class UserAgent:
  Mozilla = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'
