#!/usr/bin/env python2
# -*- coding:utf-8 -*-
def determinCoding(content, header):
  """Determin a coding of a given url content and it's header.
  params headers : HTMLHeader instance"""
  content_type = header['Content-Type']
  tag = 'charset='
  if content_type:
    if tag in content_type:
      pos = content_type.index(tag)
      pos += 8
      return content_type[pos:]
  content = content.lower()
  if tag in content:
    startpos = content.index(tag)
    endpos = content[startpos:].index('"')
    return content[startpos:endpos][startpos + 8:]

def getCodingContent(stream):
  # 获取stream的编码
  """Return a string in which is the content of given url.
  return - content : unicode string"""
  content = stream.read()
  coding = determinCoding(content, stream.headers)
  stream.close()
  return content.decode(coding)

def longestString(alist):
  """Return the longest string of a list of strings."""
  a_new_list = [len(a_str) for a_str in alist]
  pos = a_new_list.index(max(a_new_list))
  return alist[pos]

def cutTo(str_1, str_2):
  """Cut str_1 to the position just befor str_2."""
  # 不包含 str_2
  if not str_2 in str_1 :
    return str_1
  pos = str_1.index(str_2)
  return str_1[0:pos]

def cutBegin(str_1, str_2):
  # 在MyParser中使用
  if not str_2 in str_1:
    return None
  pos = str_1.index(str_2) + len(str_2)
  return str_1[pos:]
