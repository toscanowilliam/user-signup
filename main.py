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
    welcome_temp = jinja_env.get_template('welcome.html')
    name = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    user_error = ""
    pass_error = ""
    v_error = ""
    error_happend = False
    if request.method == 'POST':

        if checkString(name) == True:
            user_error = "Please enter good username"
            error_happend = True
        if checkString(password) == True:
            pass_error = "Please enter good password"
            error_happend = True
        if password != verify:
            v_error = "Password does not match"
            error_happend = True
        if error_happend == True:
            return render_template(template, user_error=user_error, pass_error=pass_error, v_error=v_error)

        username = request.form['username']
        template = jinja_env.get_template('welcome.html')
        return render_template(template, username=username,)
    


@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return render_template(template, username=username)

def checkString(word):
    if len(word) < 3 or len(word) > 20 or  ' ' in word:
            return True
    else:
        return False

app.run()    