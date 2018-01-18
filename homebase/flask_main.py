# server for website

import flask
from flask import render_template
#from flask import request
#from flask import url_for
import json
import logging

app = flask.Flask(__name__)
app.debug=True
app.logger.setLevel(logging.DEBUG)
app.secret_key="P3a9n71Dlb8Pkb3Qv481nk5PjnD"
APPLICATION_NAME = 'blog page'

"""
###############################  Pages (routed from URLs)
"""
@app.route("/")
@app.route("/index")
def index():
	app.logger.debug("ENTERING INDEX")

	app.logger.debug("LEAVING INDEX")
	return render_template('index.html')


# app gets created so it'll exist if it's main or not
if __name__ == "__main__":
	app.run(port=8000,host="0.0.0.0")
