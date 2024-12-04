from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

#import models and forms
from models import project
from forms import contactform

#Route
@app.route ('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = project.query.all()  #Fetch projects from the database
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = contactform()
    if form.validate_on_submit():
        # Handle form submission (e.g., send an email or save to DB)
        return "Thank you for reaching out!"
    return render_template('contact.html', form=form)

if __name__== '__main__':
    app.run(debug=True)

