from flask import Blueprint, render_template, redirect, url_for
from flask import request

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

TASKS = []

@main_blueprint.route('/', methods=['GET', 'POST'])
def todo():

    return render_template('todo.html')