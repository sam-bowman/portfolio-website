from flask import Flask, url_for, render_template
from tools import generate_cv_files

generate_cv_files()

app = Flask(__name__)

@app.route('/homepage')
@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html",title="Home")

@app.route('/cv')
def cv():
    return render_template("index.html",title="CV")

@app.route('/contact')
def contact():
    return render_template("index.html",title="Contact")

@app.route('/projects')
def projects():
    return render_template("index.html",title="Projects")

@app.route('/proj1')
def proj1():
    return render_template("index.html",title="Project 1")

@app.route('/proj2')
def proj2():
    return render_template("index.html",title="Project 2")

@app.route('/proj3')
def proj3():
    return render_template("index.html",title="Project 3")

@app.route('/tools')
def projects():
    return render_template("index.html",title="Tools")

@app.route('/tool1')
def proj1():
    return render_template("index.html",title="Tool 1")

@app.route('/tool2')
def proj2():
    return render_template("index.html",title="Tool 2")

@app.route('/tool3')
def proj3():
    return render_template("index.html",title="Tool 3")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)