# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import datetime
import logging
import os

from flask import abort, Flask, render_template, url_for
from flask_flatpages import FlatPages, pygments_style_defs

logging.basicConfig(level="DEBUG" if os.environ.get("FLASK_DEBUG") else "INFO")


# pages is an instance of the FlatPages extension
# it's essentially a list of Page objects with some fancy wrapping
# on top. Almost like a query result object really.
pages = FlatPages()


def create_app(config_object="settings"):
    """Create the application factory."""
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    # We want Flask to allow no slashes after paths, because they get turned into flat files
    app.url_map.strict_slashes = False
    pages.init_app(app)
    return app


app = create_app()


@app.route("/pygments.css")
def pygments_css():
    return pygments_style_defs("tango"), 200, {"Content-Type": "text/css"}


# Route to FlatPages at our root, and route any path that ends in ".html"
# Basically, try to match SOMETHING.html with a corresponding SOMETHING.md
# in our pages directory
@app.route("/")
def index():
    active_posts = get_active_posts(pages)
    page = pages.get_or_404("index")
    post_tuples = [
        (p.meta["title"], url_for(".entries", path=p.path)) for p in active_posts
    ]
    return render_template(
        "index.html", page=page, title=page.meta["title"], post_tuples=post_tuples
    )


@app.route("/<path:path>.html")
def entries(path=None):
    # Look for the page with FlatPages, or find "index" if we have no path
    page = pages.get_or_404(path)

    # so this structure basically restricts "next" and "previous"
    # to posts within the same folder. That allows to store next and
    # previous in the page meta data without explicitly defining the root.
    # Flexibility to change root/topic in one spot feels more important
    # than cross-folder sequencing right now
    page_root = page.path.rsplit("/", 1)[0]

    previous_post = page.meta.get("previous-post")
    next_post = page.meta.get("next-post")

    if previous_post:
        previous_path = page_root + "/" + previous_post
        previous_page = pages.get(previous_path)
        if not post_is_active(previous_page):
            previous_page = None
    else:
        previous_page = None

    if next_post:
        next_path = page_root + "/" + next_post
        next_page = pages.get(next_path)
        if not post_is_active(next_page):
            next_page = None
    else:
        next_page = None

    # Render the template "page.html" with our page and title
    return render_template(
        "page.html",
        page=page,
        title=page.meta["title"],
        previous_page=previous_page,
        next_page=next_page,
    )


def post_is_active(post):
    # filter out unpublished posts by date
    logging.debug(f"Checking whether {post.path} is active.")
    if post.meta.get("publish-datetime") > datetime.datetime.utcnow():
        logging.debug(f"Post publish date: {post.meta.get('publish-datetime')}")
        logging.debug(f"Today's Date: {datetime.date.today()}")
        return False
    # filter out unpublished posts by boolean
    if not post.meta.get("publish"):
        logging.debug(f"Post publish: {post.meta.get('publish')}")
        return False
    return True


def get_active_posts(pages, sort=True, sort_by_meta="publish-datetime"):
    active_posts = []
    for p in pages:
        # filter out the index
        if p.path == "index":
            logging.debug("Page not included because it is the index")
            continue
        if not post_is_active(p):
            logging.debug("Post is not included because it is not active")
            continue
        active_posts.append(p)
    logging.info(f"{ len(active_posts) } active posts found")
    if sort:
        active_posts.sort(key=lambda x: x.meta[sort_by_meta])
    return active_posts
