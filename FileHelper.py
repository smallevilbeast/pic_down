#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import re, os
def getFilenameFromURL(url):
  # 在 Downloader 中使用
  pos = url.rfind('/')
  shorted = url[pos + 1:]
  pattern = re.compile(r'\w*[\.\w]*')
  f_name = pattern.findall(shorted)[0]
  return f_name

def addExtension(fname, ext):
  # 在 App 中使用，添加扩展名
  # 没有后缀才添加
  if '.' not in fname:
    rename(fname, ext)
def rename(old, ext):
  # ext='.jpg'
  if os.path.isfile(old + ext):
    ext = '2' + ext
    rename(old, ext)
    return None
  print 'rename', old, old + ext
  os.rename(old, old + ext)

def makedir(directory):
  if not os.path.isdir(directory):
    os.mkdir(directory) # 不捕获_directory是文件时的异常，让程序自己退出

def writeBinFile(stream, file_name, directory='.', mode='wb'):
  """Read from the given url and write to file_name."""
  file_name = directory + os.sep + file_name
  if os.path.isfile(file_name):
    print 'File %s exist.' % file_name
    return False
  CHUNCK_SIZE = 1024
  with open(file_name, mode) as fp:
    while True:
      try:
        chunck = stream.read(CHUNCK_SIZE)
      except (Exception, SystemExit):
        print 'Fetching error. Probably timed out.'
        fp.close()
        os.remove(file_name)
        return False
      if not chunck:break
      fp.write(chunck)
  return True
