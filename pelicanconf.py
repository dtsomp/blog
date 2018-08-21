#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dtsomp'
SITENAME = u"dtsomp's blog"
SITEURL = 'https://blog.dtsomp.net'
SITESUBTITLE = 'No keyboards were harmed during the making of this site.'

PATH = 'content'
THEME = 'pelican-clean-blog'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('RSS feed', 'https://blog.dtsomp.net/feeds/all.rss.xml'),
            ('Twitter', 'https://twitter.com/dtsomp'),
            ('Keybase', 'https://keybase.io/dtsomp'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# pelican-clean-blog theme
HEADER_COVER = 'images/terminal.png'

DISQUS_SITENAME = "dtsomps-blog"
