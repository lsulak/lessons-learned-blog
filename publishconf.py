#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""This is a configuration of the publishing/production side of my Pelican-based blog.

For more information, please read the official documentation:
    https://docs.getpelican.com/en/stable/index.html.
"""
from __future__ import unicode_literals

import os
import sys

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.


sys.path.append(os.curdir)

# pylint: disable=wrong-import-position,wildcard-import,unused-wildcard-import
from pelicanconf import *  # noqa: E402

# pylint: enable=wrong-import-position,wildcard-import,unused-wildcard-import

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://lsulak.github.io"
RELATIVE_URLS = True

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = "feed/all.rss.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
# GOOGLE_ANALYTICS = ""
# DISQUS_SITENAME = ""
