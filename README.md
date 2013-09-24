flat-flog
=========

An flat-page blog written in Python using the Flask Microframework and its extensions. It comes with [Twitter Boostrap](https://getbootstrap.com) and some default template to get you started. This idea was stemmed from a blog post by [James Harding](http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/).


Installation
------------

Create a virtualenv and install the requirements.

    virtualenv .
    source bin/activate
    pip install -r requirements.txt

Create a Post
-------------

To create a new post, simplely create a new file in the `flat_flog/_content/_posts` folder. Flat Flog will automatically pull it out and render the Markdown into a blog post. The `flat_flog/_content/_drafts` folder is where you can put drafts of blog posts you are not ready to publish.

The format of a post entry is as followed:

    title: ** YOUR TITLE HERE **
    date: ** TODAY'S DATE **
    tags: ['** TAG 1 **', '** TAG 2 **', etc…]

    ** THE BODY OF THE POST HERE **

Create a Page
-------------

Creating a page is very similar to creating a new blog post. You would want to put the content of the page you want to create in the `flat_flog/_content/_pages` folder.

The format of a page is as followed:

    title: ** YOUR TITLE HERE **

    ** THE BODY OF THE PAGE HERE **

Serve in development
--------------------

To serve your blog while developing, you can simplely run it as a Flask application. Run the following command to serve the content of your blog dynamically:

    cd flat_flog
    python blog.py

This will allow you to see your blog at <http://0.0.0.0:5000/>. Since `DEBUG=True` any changes made to your blog will auto-reload allowing for easier developement.

Freeze your blog
----------------

After you are done development of your blog, you want to freeze your blog to create a static version of it for deployment. This is done by the following command:

    cd flat_flog
    python blog.py build

This will create a `_site` folder with your static blog. You can then host these files anywhere.

You can also easily test your static website by entering the following:

    c./_site
    python -m SimpleHTTPServer 8000

This should serve your site at <http://0.0.0.0:8000>.

TODO
----

List of things I want to get done:

* Make tags work better.
* Implement time-sorted archive (maybe...)
* Expand on `Config` file for more personalization.

Find more todo items [here](https://github.com/joshfinnie/flat-flog/issues) and feel free to submit [Pull Requests](https://github.com/joshfinnie/flat-flog/pulls)!

License
-------

The MIT License (MIT)

Copyright (c) 2013 Josh Finnie

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
