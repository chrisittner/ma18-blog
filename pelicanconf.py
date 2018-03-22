#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CH'
SITENAME = 'Inferentialist Semantics for Mathematics'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'


# get date and slug from filename, rather than only the date. By default slug is derived from 'title'.
DEFAULT_CATEGORY = 'general'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
DEFAULT_PAGINATION = False

LINKS = ()
SOCIAL = (('envelope-o', 'mailto:ma18@chrisittner.de'),
          ('rss', '/feed.rss'),
          ('github', 'https://github.com/chrisittner'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['render_math',]  # 'md_yaml']
MD_EXTENSIONS = ['codehilite', 'extra', 'smarty', 'toc']

STATIC_PATHS = ['extra', 'images', 'pdfs']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

THEME = 'themes/Flex'  # from pelican-themes; pelican-blue or Flex (nice-blog, twenty-html5up, free-agent)

# Theme specific config below
SUMMARY_MAX_LENGTH = 0
SITETITLE = 'Inferentialist Semantics & Math'
SITESUBTITLE = 'Collection of thesis-relevant references & snippets'
#SITEDESCRIPTION = 'A GSoC blog about Bayesian Network Structure Learning with pgmpy'
#SITELOGO = 'http://pgmpy.readthedocs.org/en/latest/_images/logo.png'
MAIN_MENU = False
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'
COPYRIGHT_YEAR = 2018
CC_LICENSE = {'name': 'Creative Commons Attribution-ShareAlike', 'version': '4.0', 'slug': 'by-sa'}
