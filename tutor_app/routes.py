from tutor_app import app
from tutor_app.forms import AnswerForm
from flask import render_template, session, redirect, url_for, flash
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/instructions')
def instructions():
    initialise_slide_num()
    initialise_score()
    return render_template('instructions.html')

@app.route('/exit')
def exit():
    score = get_score()
    return render_template('exit.html', score = score)


@app.route('/tutor', methods = ['GET','POST'])
def tutor():

    responseForm = AnswerForm()
    slide_num = get_slide_number()

    slides = ["अ -> a (as in *a*bacus)","म् -> m (as in *m*ust)",
            "घ् -> gh (as in *gh*ost)","र् -> r (as in *r*ace)",
                ["अ","a"],
                ["म्","m"],
                ["घ्","gh"],
                ["र्","r"]]

    if responseForm.validate_on_submit() and responseForm.answer.data:
        answer = responseForm.answer.data
        if answer == slides[slide_num][1]:
            flash('Correct')
            increment_score()

    increment_slide_number()
    if get_slide_number()==len(slides):
        return redirect(url_for('exit'))

    return render_template("tutor.html", slides = slides,
    index = get_slide_number(), form = responseForm)

    # prompts = {"अ":"a (as in *a*bacus)","म्":"m (as in *m*ust)","घ्":"gh (as in *gh*ost)",
    # "र्":"r (as in *r*ace)"}
    # questions_answers = {"म्":"m","घ्":"gh"}

def increment_slide_number():
    session['slide_number'] +=1

def decrement_slide_number():
    session['slide_number'] -=1

def get_slide_number():
    return session['slide_number']

def initialise_slide_num():
    session['slide_number'] = -1

def initialise_score():
    session['score'] = 0

def increment_score():
    session['score']+=1

def decrement_score():
    session['score']-=1

def get_score():
    return session['score']
