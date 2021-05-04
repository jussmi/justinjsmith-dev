from flask_frozen import Freezer
from app import app
from app import pages, post_is_active

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
