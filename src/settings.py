# -*- coding: utf-8 -*-
"""Application configuration.
"""
# Tell Flatpages to auto reload when a page is changed, and look for .md files
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = ".md"
FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite", "fenced_code"]
# the default is actually pages, I just like it explicit so you know where to look
FLATPAGES_ROOT = "pages"

# Set frozen flask to go up a folder
FREEZER_DESTINATION = "../build"
