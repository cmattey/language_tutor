from tutor_app import app
from flask import render_template, session
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/instructions')
def instructions():
    initialise_slide_num()
    return render_template('instructions.html')

@app.route('/tutor')
def tutor():

    slide_num = get_slide_number()

    prompts = ["a","b","c","d","e","f"]
    # prompts = {"अ":"a (as in *a*bacus)","म्":"m (as in *m*ust)","घ्":"gh (as in *gh*ost)",
    # "र्":"r (as in *r*ace)"}
    # questions_answers = {"म्":"m","घ्":"gh"}
    questions_answers = [1,2,3,4,5,6,7,8]

    return render_template("tutor.html", prompts = prompts, q_a = questions_answers,
    index = slide_num)

def get_slide_number():
    session['slide_number'] = 1+session['slide_number']
    return session['slide_number']

def initialise_slide_num():
    session['slide_number'] = 0
