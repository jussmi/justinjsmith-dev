import datetime
import logging
import os

from flask import abort, Flask, render_template, url_for
from flask_flatpages import FlatPages

logging.basicConfig(level="DEBUG" if os.environ.get("FLASK_DEBUG") else "INFO")

# Tell Flatpages to auto reload when a page is changed, and look for .md files
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
# the default is actually pages, I just like it explicit so you know where to look
FLATPAGES_ROOT = 'pages'

# Set frozen flask to go up a folder
FREEZER_DESTINATION = '../build'

# Create our app object, use this page as our settings (will pick up DEBUG)
# Not using the blueprint factory pattern or anything like that because
# well... no need
app = Flask(__name__)

# For settings, we just use this file itself, very easy to configure
app.config.from_object(__name__)

# We want Flask to allow no slashes after paths, because they get turned into flat files
app.url_map.strict_slashes = False

# pages is an instance of the FlatPages extension
# it's essentially a list of Page objects with some fancy wrapping
# on top. Almost like a query result object really.
pages = FlatPages(app)

# Route to FlatPages at our root, and route any path that ends in ".html"
# Basically, try to match SOMETHING.html with a corresponding SOMETHING.md
# in our pages directory
@app.route("/")
def index():
    active_posts = get_active_posts(pages)
    page = pages.get_or_404('index')
    post_tuples = [(p.meta['title'], url_for(".entries", path=p.path)) for p in active_posts]
    return render_template("index.html", page=page, title=page.meta['title'], post_tuples=post_tuples)


@app.route("/<path>.html")
def entries(path=None):
    # Look for the page with FlatPages, or find "index" if we have no path
    page = pages.get_or_404(path)

    # Render the template "page.html" with our page and title
    return render_template("page.html", page=page, title=page.meta['title'])

def post_is_active(post):
    # filter out unpublished posts by date
    if post.meta.get("publish-date") >= datetime.date.today():
        logging.debug(f"Post publish date: {post.meta.get('publish-date')}")
        logging.debug(f"Today's Date: {datetime.date.today()}")
        return False
    # filter out unpublished posts by boolean
    if not post.meta.get("publish"):
        logging.debug(f"Post publish: {post.meta.get('publish')}")
        return False
    return True


def get_active_posts(pages):
    active_posts = []
    for p in pages:
        # filter out the index
        if p.path == 'index':
            logging.debug("Page not included because it is the index")
            continue
        if not post_is_active(p):
            logging.debug("Post is not included because it is not active")
            continue
        active_posts.append(p)
    logging.info(f"{ len(active_posts) } active posts found")
    return active_posts
