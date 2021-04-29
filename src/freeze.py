from flask_frozen import Freezer
from app import app
from app import pages

freezer = Freezer(app)

@freezer.register_generator
def entries():
    for page in pages:
        yield {'path': page.path}

if __name__ == '__main__':
    freezer.freeze()
