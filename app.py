from flask import Flask, render_template
from views import main_blueprint
from task import *

app = Flask(__name__)

# Register blueprint for routes
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)