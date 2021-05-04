from flask_frozen import Freezer
from app import app
from app import pages, post_is_active

freezer = Freezer(app)


@freezer.register_generator
def entries():
    for page in pages:
        if post_is_active(page):
            yield {"path": page.path}


if __name__ == "__main__":
    freezer.freeze()
