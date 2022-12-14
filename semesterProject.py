import json
import urllib.request
import requests
from forms_poke import PokeForm
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect, make_response, session,jsonify
#pip install flask-wtf
app = Flask(__name__)

app.config["SECRET_KEY"]='This is a test'

@app.route("/")
def myrediret():
   return redirect(url_for('pokemon_form'))

@app.route('/pokemon_form', methods=['GET', 'POST'])
def pokemon_form():
   form = PokeForm()
   if form.is_submitted():
      result = request.form

      url = "https://pokeapi.co/api/v2/"+result["category"]+"/"+ result["name"].lower()
      print(url)
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()

      #status code form the api, NOT FLAKS STATUS CODE
      print(response.status_code)

      if(result["category"]=="pokemon"):
         render=make_response(render_template('data_pokemon_handler.html', title="Pokemon Search", header="Pokemon Searched:",  data=data))   
      elif(result["category"]=="move"):
         render=make_response(render_template('data_move_handler.html', title="Move Search", header="Move Searched:",  data=data)) 
      elif(result["category"]=="nature"):
         render=make_response(render_template('data_nature_handler.html', title="Nature Search", header="Nature Searched:",  data=data))    
      elif(result["category"]=="type"):
         render=make_response(render_template('data_type_handler.html', title="Type Search", header="Type Searched:",  data=data))
      elif(result["category"]=="item"):
         render=make_response(render_template('data_item_handler.html', title="Item Search", header="Item Searched:",  data=data))
      elif(result["category"]=="berry"):
         render=make_response(render_template('data_berry_handler.html', title="Berry Search", header="Berry Searched:",  data=data))
      else:
         print("Error")
      
      
      #setting the cookie
      render.set_cookie('searched', result['category']+" "+result["name"])  
      #renders the page
      return render
   
   return render_template('pokemon_form.html', title="Search Tool", header="Search", form=form)

@app.route('/Error/')
def other():
   return render_template('error.html')

@app.errorhandler(500)
def handle_500(e):
   #returns error as a json format
   #return jsonify(error=str(e)), 500
   return redirect(url_for('other'))
 
if __name__ == "__main__":
   app.run(debug=True)