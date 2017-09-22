# import render_templates
import app

__author__ = 'joe'

import flask

app = flask


@app.route("/templates.index.html/")
def index():
    return render_templates('templates.index.html')


@app.route('/signup', methods=['POST'])
def signup():
    if __name__ == '__main':
        app.run()