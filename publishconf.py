#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or `make github` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://chrisittner.github.io/ma18-blog' #'http://ma18.chrisittner.de'  # 'http://chrisittner.github.io/ma18-blog'
RELATIVE_URLS = False
FEED_ALL_ATOM = 'feed.rss'
DELETE_OUTPUT_DIRECTORY = True
# DISQUS_SITENAME = ""
