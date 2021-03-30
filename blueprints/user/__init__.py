from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

user = Blueprint('simple_page', __name__,template_folder='templates')


@user.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)