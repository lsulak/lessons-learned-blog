#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""This is a configuration of my Pelican-based blog.

For more information, please read the official documentation:
    https://docs.getpelican.com/en/stable/index.html.
"""
from __future__ import unicode_literals

from datetime import datetime

AUTHOR = "Ladislav Sulak"
SITENAME = "Ladislav's Blog"
SITEURL = "http://localhost:8000"
SITETITLE = AUTHOR
SITEDESCRIPTION = """
    software development, programming,
    data science, databases, machine learning,
    python, AWS, linux
"""

COPYRIGHT_NAME = AUTHOR
BLOGGING_BEGAN_YEAR = 2021

# Paths
PATH = "content"

# Main Menu
USE_LESS = True
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives"),
    ("Categories", "/categories"),
    ("About", "/pages/about"),
)

DIRECT_TEMPLATES = ["index", "archives", "categories"]

# Locations / Formatting for URLS
ARTICLE_URL = "{slug}"
PAGE_URL = "pages/{slug}"
CATEGORY_URL = "category/{slug}"

# Timezone / Language
TIMEZONE = "Europe/Prague"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM_RENDER = False
FEED_ALL_RSS_RENDER = False

# Social widget
SOCIAL = (
    ("linkedin", "https://linkedin.com/in/ladislav-sulak"),
    ("github", "https://github.com/lsulak"),
    ("medium", "https://medium.com/@lsulak"),
    ("goodreads ", "https://www.goodreads.com/user/show/114351959-ladislav-ul-k"),
)

# Plugins, see: http://docs.getpelican.com/en/latest/plugins.html
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ["sitemap", "post_stats"]

# Sitemap Settings
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.6, "indexes": 0.6, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
    "exclude": ["tag/"],
}

STATIC_PATHS = [
    "images",
    "extras/count.js",
    "extras/custom.css",
    "extras/robots.txt",
]

CUSTOM_CSS = "extras/custom.css"

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 7
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

DATE_FORMATS = {
    "en": "%b %d, %Y",
}
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Theme Settings
FAVICON = "/images/favicon.ico"

THEME = "themes/Flex"
THEME_COLOR_ENABLE_USER_OVERRIDE = False
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {
            "title": "Table of Contents",
        },
    },
    "output_format": "html5",
}
