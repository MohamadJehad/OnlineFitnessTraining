#(Online Fit trainer) APP
#----------------------------- Imports section ------------------------#
import flask
from flask import Flask, send_from_directory
from app.html_hanlding import *
from app.routes_functions import *


#----------------------------- Initialize the coed section ------------------------#
#init flask
app =flask.Flask(__name__)
app = Flask(__name__, template_folder="views")
if __name__=='__main__':
    app.run(debug=True)

#----------------------------- Routes section ------------------------#
#this route used for the icon of the website
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

#the first route in the website whech is welcome page
@app.route ("/") 
def login():
    return get_html("login")

#the home page route which will view member's, packages, subscriptions main info
@app.route("/home") 
def home():
    return homepage()
    
#this route will return the page where trainer will insert the main info of the member
@app.route ("/newmember") 
def newmemberpage():
    return get_html("add_member")
"""
this route will be called after inserting the main info to create object
for the member and then will go to page where  trainer insert member's vital details
"""
@app.route ("/addnewmember") 
def addmember():
   return addnewmember()

#this route will return the page where trainer will insert the vital details of the member
@app.route ("/newVital") 
def newVitalpage():
    id= flask.request.args.get("id")
    return get_html("add_vital_details").replace("&&ID&&",id)
   
"""
this route will be called after inserting the Vital Details to create object
for the Vital Details and then will go to the home page
"""
@app.route ("/addVitalDetails") 
def addVDetails():
    return addVitalDetails()

#this route will used to pass id for member to the delete from database function
@app.route ("/deletemember") 
def deletemem():  
    return deletemember() 

#this route wi  ll used to pass id for package to the delete from database function
@app.route ("/deletepackage") 
def deletepack():
    return deletepackage()

#this route will be called once user entered the name or id of the member he wanted to search for
@app.route ("/search") 
def search():
    return search_for_member()

"""
this route responsible for viewing all the details of the member in his profile page
so it will render the profile page with all member's data (info, vital info, sunscription info, workout info)
"""
@app.route("/member_profile")
def member_profile():
    return get_member_profile() 
#this route send the new package page
@app.route ("/newpacakge") 
def newpackage():
    return get_html("add_package")

#this route recieve the new package data and create instance of it's class then add to database
@app.route ("/addnewpackage") 
def addpackage():
    return addnewpackage()


#this route will used reender page with the current data of member 
@app.route ("/editmember") 
def editmemberdata():  
   return editmember()


#this route will be called when trainer submit his changes to member's data
@app.route("/submit_edit_member")
def submit_edit():
    return submit_edit_member()
    

# New route to handle subscription form submission
@app.route("/subscribe", methods=["POST"])
def subscribe_to_package():
    return subscribe()
    
# New route to handle subscription form submission
@app.route("/resubscribe", methods=["POST"])
def resubscribe_to_package():
    return resubscribe()


# Function to handle adding workout to a member
@app.route("/add_workout", methods=["POST"])
def add_workout_to_member():
    return add_workout()
  

# Function to handle adding nutrition plan to a member
@app.route("/add_nutrition_plan", methods=["POST"])
def add_nutrition_plan_member():
    return add_nutrition_plan()
