#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from jinja2 import contextfilter

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

AUTHOR = 'Bogdan Titomir'
SITENAME = 'Application'
SITEURL = 'http://static-site.com'

PATH = 'content'

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

TIMEZONE = 'Asia/Yekaterinburg'

DEFAULT_LANG = 'ru'

THEME = 'themes/weight-loss'

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

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# OUTPUT_PATH = os.path.join(os.path.dirname(BASE_DIR), 'public_html')
OUTPUT_PATH = '../public_html'

DELETE_OUTPUT_DIRECTORY = True

PLUGINS = [
    'plugins.pelican_sitemap.sitemap',
    'plugins.pelican_image_header.image_header',
    'plugins.pelican_related_posts.related_posts',
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'extensions.markdown.meta_yaml': {},
        # 'markdown.extensions.meta': {},
        'extensions.markdown.image_path_modify': {},
    },
    'output_format': 'html5',
}

DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags']

INDEX_URL = 'articles/'
INDEX_SAVE_AS = 'articles/index.html'

ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

"""
YEAR_ARCHIVE_URL = 'archives/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
"""

DEFAULT_PAGINATION = 3

PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

STATIC_PATHS = [
    'static',
    'media',
    'extra/robots.txt',
    'extra/.htaccess',
    'extra/pages/.htaccess',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/pages/.htaccess': {'path': 'pages/.htaccess'},
}

RELATED_POSTS_MAX = 4


"""
Jinja filters
"""
@contextfilter
def example(ctx, value):
    pass


@contextfilter
def strftime(ctx, value):
    return value.strftime('%B %d, %Y')


JINJA_FILTERS = {
    'example': example,
    'strftime': strftime,
}