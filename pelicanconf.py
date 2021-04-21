# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Репозиторий открытых данных в гуманитарных науках'
SITENAME = 'DATAH. Data for Humanities'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = [('Репозиторий', 'https://dataverse.datah.ru')]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME='nice-blog'
#THEME='built-texts'
LOAD_CONTENT_CACHE = False

## nice-blog attributes
LOGO = 'DATAH2.png'
FAVICON = 'DATAH1.png'
THEME_COLOR = 'red'
SIDEBAR_DISPLAY = ['about', 'categories']
SIDEBAR_ABOUT = 'DATAH — платформа для размещения открытых данных для исследований в области гуманитарных наук. Хостинг и техническое обслуживание платформы осуществляет Институт русской литературы (Пушкинский Дом) РАН. <a href="pages/about.html">Подробнее...</a>'
