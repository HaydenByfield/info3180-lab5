"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file, redirect, url_for, flash, send_from_directory
from app.forms import LoginForm, MovieForm
from app.models import UserProfile, MovieProfile
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf



app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_crsf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()
    print("FORM:", form)
    if form.validate_on_submit():
        m_title = form.m_title.data
        m_desc = form.m_desc.data
        m_poster = form.m_poster.data
        filename = secure_filename(m_poster.filename)
        m_poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_movie = MovieProfile(
            m_title = m_title,
            m_desc = m_desc,
            m_poster = filename
        )
        db.session.add(new_movie)
        db.session.commit()
    return jsonify({"movies": [{"m_title": new_movie.m_title,"m_desc": new_movie.m_desc,"m_poster": new_movie.m_poster }],"message": "Movie Successfully Added"}), 201
    
    

@app.route('/api/v1/movies', methods=['GET'])
def movieList():
    movies = MovieProfile.query.all()
    movie_list = [
        {
            "m_title": m.m_title,
            "m_desc": m.m_desc,
            "m_poster": m.m_poster
        } for m in movies
    ]

    return jsonify({"movies": movie_list}), 200

@app.route("/api/v1/images/<path:filename>")
def getImage(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404