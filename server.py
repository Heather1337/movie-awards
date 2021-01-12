"""Server for The Shoppies app."""
from flask import (Flask, render_template, request, session, jsonify)

app = Flask(__name__)

#===============================*    PAGE ROUTES   *========================================#

@app.route('/')
def my_index():
    """ Show homepage with form to register."""

    return render_template('base.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)