#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import HTMLParser

class MyParser(HTMLParser.HTMLParser):
  def __init__(self):
    HTMLParser.HTMLParser.__init__(self)
    self.toggle_script_parse = False
    self.toggle_form_parse = False
    self.scriptList = []
    self.formParams = {}
    self.result = 0

  def handle_starttag(self, tag, attrs):
    HTMLParser.HTMLParser.handle_starttag(self, tag, attrs)
    attrs = dict(attrs)
    if tag == 'script':
      self.toggle_script_parse = True
    # parse start parse form to get attrs in input tag
    if tag == 'form' and attrs.has_key('name') and attrs['name'] == 'f1':
      self.toggle_form_parse = True
    if tag == 'input' and self.toggle_form_parse:
      if attrs.has_key('type') and attrs['type'] == 'hidden':
        key = attrs['name'];value = attrs['value']
        self.formParams[key] = value

  def handle_endtag(self, tag):
    HTMLParser.HTMLParser.handle_endtag(self, tag)
    if tag == 'form' and self.toggle_form_parse:
      self.toggle_form_parse = False

  def handle_data(self, data):
    HTMLParser.HTMLParser.handle_data(self, data)
    if self.toggle_script_parse:
      self.scriptList.append(data)
      self.toggle_script_parse = False

  def reset(self):
    HTMLParser.HTMLParser.reset(self)
    self.toggle_script_parse = False
    self.toggle_form_parse = False
    self.scriptList = []
    self.formParams = {}
    self.result = 0
