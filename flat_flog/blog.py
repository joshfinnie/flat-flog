import cssmin
import glob
import sys
import os

from flask import (
    Flask,
    render_template
    )
from flask_flatpages import (
    FlatPages,
    pygments_style_defs
    )
from flask_frozen import (
    Freezer
    )

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = '_content'
POST_DIR = '_posts'
PAGE_DIR = '_pages'
FREEZER_DESTINATION = '../_site'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route('/static/css/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@app.route('/static/css/main.min.css')
def minified_main_css():
    return cssmin.cssmin(open('static/css/main.css').read()), 200, {'Content-Type': 'text/css'}


@app.context_processor
def inject_pages():
    result = []
    pages = glob.glob('_content/_pages/*')
    for page in pages:
        path, file = os.path.split(page)
        name = file.rstrip('.md')
        page_dict = {"url": name, "title": name.title()}
        result.append(page_dict)
    return dict(pages=result)


@app.route('/')
def home():
    """ Renders the home page as a regular `page` """
    path = '{}/{}'.format(PAGE_DIR, 'home')
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)


# @app.route('/')
# def home():
#     """ Renders the home page as own template `home.html` """
#     return render_template('home.html')


@app.route('/posts/')
def posts():
    """ Renders the list of blog posts. """
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=False)
    return render_template('posts.html', posts=posts)


@app.route('/posts/<name>/')
def post(name):
    """ Renders an individual blog post """
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


@app.route('/tags/<name>/')
def tag(name):
    """ Renders a list of blog posts per tag `name` """
    posts = [p for p in flatpages if p.path.startswith(POST_DIR) and name in p.meta['tags']]
    posts.sort(key=lambda item: item['date'], reverse=False)
    return render_template('tag.html', tag=name, posts=posts)


@app.route("/<name>/")
def page(name):
    """ Renders a `page` """
    path = '{}/{}'.format(PAGE_DIR, name)
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=DEBUG)
