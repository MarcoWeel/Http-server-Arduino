"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from HTTP_example import app


@app.route('/test')
def contact():
    """Renders the contact page."""
    return "This is a test"
