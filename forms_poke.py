# WTF
# using flask wt-forms
# run command 
# pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import  SubmitField, SelectField,StringField
from wtforms.validators import InputRequired

def tuple_list_maker(user_list):
    result = []
    for item in user_list:
        my_list=[]
        my_list.append(str(item))
        my_list.append(str(item))
        my_tuple = tuple(my_list)
        result.append(my_tuple)
    return result

class PokeForm(FlaskForm):
   category = SelectField(u'Category', 
   choices=[('pokemon','Pokemon (1-1154)'),('move','Move (1-844)'),('nature','Nature (1-25)'),('berry','Berry (1-64)'),('type','Type (1-20)'),('item','Item (1-1607)')])
   
   name=StringField("Enter number within range of drop down or Name of a specific criteria in the drop down", 
   validators=[InputRequired(message="You Must Enter Search Criteria")])
   
   
   

   #SUBMIT
   submit = SubmitField("Enter")