#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""This is a configuration of the publishing/production side of my Pelican-based blog.

For more information, please read the official documentation:
    https://docs.getpelican.com/en/stable/index.html.
"""
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)

# pylint: disable=wrong-import-position,wildcard-import,unused-wildcard-import
from pelicanconf import *  # noqa: E402

# pylint: enable=wrong-import-position,wildcard-import,unused-wildcard-import

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://ladislav.codes"
# SITEURL = 'https://ls.codes'
# SITEURL = 'https://lsulak.codes'
# SITEURL = 'https://ladislavsulak.codes'

# SITEURL = 'https://ls.com'
# SITEURL = 'https://ladislavsulak.com'
# SITEURL = 'https://meetladislav.com'
# SITEURL = 'https://joinladislav.com'

# SITEURL = 'https://ladislavsulak.tech'
# SITEURL = 'https://lacosulak.tech'
# SITEURL = 'https://ladislav.tech'

RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
# GOOGLE_ANALYTICS = "UA-73000395-1"
# GOOGLE_TAG_MANAGER = "GTM-5K6D7ZG"
# MICROSOFT_CLARITY = "7cfbr3w8ss"
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'design': 6, 'rumid': 1234 }
# DISQUS_SITENAME = ""
