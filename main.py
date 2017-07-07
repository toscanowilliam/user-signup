from flask import Flask, request, redirect, url_for, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['Debug'] = True




@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return render_template(template)


@app.route("/", methods=['POST']) 
def validate_form():
    template = jinja_env.get_template('form.html')
    name = ""
    name = request.form['username']
    password = ""
    email = ""
    if request.method == 'POST':
        return welcome()
    


@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return render_template(template, username=username)

app.run()    