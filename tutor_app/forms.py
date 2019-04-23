from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AnswerForm(FlaskForm):
    answer = StringField("Your Answer")
    next = SubmitField("Next Question")
    # previous = SubmitField("Previous Question")
