#(Online Fit trainer) APP
#----------------------------- Includes section ------------------------#
from datetime import datetime, timedelta
import mysql.connector
import flask
from flask import Flask, render_template, send_from_directory
import os

#----------------------------- Initialize the coed section ------------------------#
#init flask
app =flask.Flask(__name__)
app = Flask(__name__, template_folder="views")
if __name__=='__main__':
    app.run(debug=True)

#init the mysql database
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'K1d02370@2024',
    'database': 'fittrackdb'
}

#----------------------------- Classes section ------------------------#
"""
this class will contain the main info about each member
"""
class Member:
    id=None
    def __init__(self, name, birthdate,height,weight,gender,phone,email,member_id=None):
        try:
            self.name = name
            self.gender = gender.lower()
            if isinstance(birthdate, str):
                self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
            else:
                self.birthdate = birthdate  
            self.height=height
            self.weight=weight
            self.phone=phone
            self.email=email
        except Exception as e:
            print(f"Error adding member: {str(e)}")
        if member_id == None:
            #this section will be executed if the member is not existed in the database so it will be added
            #and inside the finction members's ID will be assigned
            self.add_to_DB()    
        else:
            #this line will be executed if the member already exited in the database
            self.id=member_id

#this function add the member to the databse and retrieve it's ID 
    def add_to_DB(self):
        query = """ INSERT INTO members (name, birthdate, height, weight, gender, phone, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (self.name, self.birthdate, self.height, self.weight, self.gender, self.phone, self.email)
        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(query, values)
            db.commit()
            self.id=cursor.lastrowid
            print("member id =" + str(self.id))
        except Exception as e:
            print(f"Error adding member to the database: {str(e)}")
    
    """
        this function return the subscription of the member (package name , start date,end date)
        and if he is not subscriped it will return empty array
    """
    def get_subscription(self):
        subscription=[]

        query = f""" SELECT package.name, subscription.startDate, subscription.endDate
                        FROM subscription
                        JOIN package ON subscription.package_id = package.id
                        WHERE subscription.memberId = {self.id};
                    """

        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(query)
            #this must return tuple contains every subscriped backage and every name
            # so here we will have only one row and will take the only value in it
            subscription = cursor.fetchall()[0]
        except Exception as e:
            print(f"Error getting package: {str(e)}")
        finally:
            cursor.close()
            print(f"subscription: {subscription}")
        return subscription
    
    
    """
        this function used to calculate the age of the member based on his birthdate
    """
    def calculate_age(self):
         today = datetime.now().date()
         age = today.year - self.birthdate.year
         return age
    
    """
    this function calculate the member's bmr based on his weight, height, gender and age
    """
    def calculate_bmr(self):
        if self.gender == "male":
            bmr = 88.362 + (13.397 * self.weight)+(4.799 * self.height)-(5.677 * self.calculate_age())
        elif self.gender == "female":
            bmr = 447.593 + (9.247 * self.weight)+(3.098 * self.height)-(4.330 * self.calculate_age())
        return int(bmr)









#this class will contain the main info about each package
class Package:
    def __init__(self, name, value,duration,package_id=None):
        self.name = name
        self.value=value
        self.duration=duration
#the condition will be valid if the package already existed in the database
        if package_id:
             self.package_id =package_id

#this function will add the package to the database and retrieve it's ID
    def add_to_DB(self):
        query = """INSERT INTO Package ( name, duration, value)
                   VALUES ( %s, %s, %s)"""
        values = ( self.name, self.duration,self.value)
        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(query, values)
            db.commit()
            self.package_id=cursor.lastrowid
            print(f"Package added to the database with ID = {str(self.package_id)}")
        except Exception as e:
            print(f"Error adding Package to the database: {str(e)}")
        finally:
            cursor.close()

#this class will contain the vital details info about each member
class VitaDetails:
    def __init__(self, allergy,disease,bodyFatPercentage, fitnessGoals,medications,member_id=None):
        self.member_id =  member_id
        self.fitnessGoals = fitnessGoals
        self.medications = medications
        self.allergy=allergy
        self.disease=disease
        self.bodyFatPercentage=bodyFatPercentage

#this function will add the info the database    
    def add_to_DB(self):
        query = """INSERT INTO VitalDetails (memberId, allergy, disease, bodyFatPercentage, fitnessGoals, medications)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (self.member_id, self.allergy, self.disease, self.bodyFatPercentage, self.fitnessGoals, self.medications)

        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(query, values)
            db.commit()
            print("VitaDetails added to the database for member ID =", str(self.member_id))
        except Exception as e:
            print(f"Error adding VitaDetails to the database: {str(e)}")


#----------------------------- Functions section ------------------------#

"""
this function will get the html content from any page 
and send it to browser
"""
def get_html(pagename):
    html_file = open("views/"+pagename+".html")
    content =html_file.read()
    html_file.close()
    return content
"""
this function will retrieve all members data from the database and create 
objects of member's class for each one of them
and will return array of members objects
"""
def get_all_members_data():
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
    except Exception as e:
        print(f"Error retrieving members: {str(e)}")
        members=[]
    finally:
        cursor.close()
    all_members = []
    for member in members:
        member_data = member
        member_obj = Member(member_data[1],(member_data[2]) , int(member_data[3]), int(member_data[4]), member_data[5], member_data[6], member_data[7],member_data[0])
        all_members.append(member_obj)
    
    return all_members

"""
this function will retrieve all pacages data from the database and create 
objects of package's class for each one of them
and will return array of packages objects
"""
def get_all_packages_data():
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM package;")
        packages = cursor.fetchall()
    except Exception as e:
        print(f"Error retrieving package: {str(e)}")
        packages=[]
    finally:
        cursor.close()
    all_packages = []
    for package in packages:
        package_obj = Package(package[1], int(package[3]),int(package[2]) , int(package[0]))
        all_packages.append(package_obj)
    return all_packages

"""
this function will delete the member from database based on it's ID
note the function is not created inside the class because it will be called using post 
method which will pass only member's ID
"""
def deleteMemberFromDB(member_id):
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()

        # Check if the member has vital details
        cursor.execute(f"SELECT * FROM vitaldetails WHERE memberId = {member_id}")
        vital_details = cursor.fetchall()

        if vital_details:
            # If the member has vital details, delete them first
            cursor.execute(f"DELETE FROM vitaldetails WHERE memberId = {member_id}")

        # Check if the member has subscriptions
        cursor.execute(f"SELECT * FROM subscription WHERE memberId = {member_id}")
        subscriptions = cursor.fetchall()

        if subscriptions:
            # If the member has subscriptions, delete them first
            cursor.execute(f"DELETE FROM subscription WHERE memberId = {member_id}")

        # Now delete the member
        cursor.execute(f"DELETE FROM members WHERE member_id = {member_id}")

        db.commit()
        print(f"Member with ID {member_id} deleted successfully")
    except mysql.connector.Error as error:
        print(f"Error deleting member: {error}")
    finally:
        cursor.close()

"""
this function will delete the package from database based on it's ID
note the function is not created inside the class because it will be called using post 
method which will pass only package's ID
"""
def delete_package_from_DB(package_id):
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()

        # Check if the package exist in subscription
        cursor.execute(f"SELECT * FROM subscription WHERE package_id = {package_id}")
        package = cursor.fetchall()

        if package:
            # If the package already exist in subscription table then delete it from this table first 
            cursor.execute(f"DELETE FROM subscription WHERE package_id = {package_id}")

        # Now delete the package from it's table
        cursor.execute(f"DELETE FROM package WHERE id = {package_id}")

        db.commit()
    except mysql.connector.Error as error:
        print(f"Error deleting package: {error}")
    finally:
        cursor.close()
"""
this function will take array of member's objects andd make them in shape of
members table to be placed in the homepage instead of placeholder
"""
def get_members_table_text(all_members):
    text = ""
    for member in all_members:
        text += "<tr>"
        text += "<td>" + str(member.id) + "</td>"
        text += "<td>" + member.name + "</td>"
        text += "<td>" + str(member.calculate_age()) + "</td>"
        #text += "<td>" + str(member.height) + "</td>"
        #text += "<td>" + str(member.weight) + "</td>"
        #text += "<td>" + member.gender + "</td>"
        text += "<td>" + member.phone + "</td>"
        #text += "<td>" + member.email + "</td>"
       # text += "<td>" + str(int(member.calculate_bmr()))+ "</td>"
        subscription_data = member.get_subscription()
        if subscription_data:
            text += "<td>" + subscription_data[0] + "</td>"
            text += "<td>" + str(subscription_data[1]) + "</td>"
            text += "<td>" + str(subscription_data[2]) + "</td>"
        else:
            text += "<td>" + "Not subscriped" + "</td>"
            text += "<td>"  + " " + "</td>"
            text += "<td>"  + " " + "</td>"
        text += "<td><a href='/deletemember?id=" + str(member.id) + "' class='delete'>Delete</a></td>"
        text += "<td><a href='/member_profile?id=" + str(member.id) + "' class='profile'>Profile</a></td>"
        text += "</tr>"
    return text

"""
this function will take array of package's objects and make them in shape of
packages table to be placed in the homepage instead of placeholder
"""
def get_packages_table_text(packages):
    text=""
    for package in packages:
        text += "<tr>"
        text += "<td>" + str(package.package_id) + "</td>"
        text += "<td>" + package.name + "</td>"
        text += "<td>" + str(package.value) + "</td>"
        text += "<td>" + str(package.duration) + "</td>"
        text += "<td><a href='/deletepackage?package_id=" + str(package.package_id) + "' class='delete'>Delete " + "</a></td>"
        text += "</tr>"
    return text

#this function subscribe the member in specific package
def subscribe_to_package(package_id,member_id):
    #first chack if memebr already subscriped
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM subscription WHERE memberId={member_id}")
        existing_subscription = cursor.fetchone()
        current_date = datetime.now().date()
#this condition if the member is not subscriped or if his subscriptin expired then let's subscripe
        if not existing_subscription or (existing_subscription)[2] < current_date:
            # Get package duration from the package table
            cursor.execute(f"SELECT duration FROM package WHERE id={package_id}")
            duration = cursor.fetchone()[0]

            # Calculate start date (today) and end date (today + duration months)
            start_date = datetime.now().date()
            end_date = start_date + timedelta(30 * duration)

            # Subscribe the member to the selected package with start and end dates
            cursor.execute("INSERT INTO subscription (memberId, package_id, startDate, endDate) VALUES (%s, %s, %s, %s)",
                           (member_id, package_id, start_date, end_date))
            db.commit()
            cursor.close()
            ret= True,0,0
#this section if the member have subscripe and still valid So confirm to him with the remaining duration
        else:
            existing_end_date=((existing_subscription)[2])
            remaining_days = (existing_end_date - current_date).days # total number of days remaining 
            remaining_months=remaining_days//30     # total number of Months remaining 
            remaining_days=remaining_days-remaining_months*30   #  number of days remaining after months
            cursor.close()
            ret= False,remaining_months,remaining_days

    except Exception as e:
        print(f"Error retrieving : {str(e)}")
        
    finally:
        cursor.close()
        return ret

#here if the member wants to subscribe even if his subscription still valid
def re_subscribe_to_package(package_id,member_id):
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT duration FROM package WHERE id={package_id}")
        duration = cursor.fetchone()[0]

        # Calculate start date (today) and end date (today + duration months)
        start_date = datetime.now().date()
        end_date = start_date + timedelta(30 * duration)   

      
        cursor.execute(" UPDATE subscription SET package_id = %s, startDate = %s, endDate = %s WHERE memberId = %s",
                    (package_id, start_date, end_date,member_id))
        db.commit()
        cursor.close()
    except Exception as e:
        print(f"Error Updating : {str(e)}")
        
    finally:
        cursor.close()
    

#----------------------------- Routes section ------------------------#

#this route used for the icon of the website
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

#the first route in the website whech is welcome page
@app.route ("/") 
def login():
    return get_html("login")
#the home page route which will view member's, packages, subscriptions main info
@app.route("/home") 
def homepage():
    members = get_all_members_data()
    text = get_members_table_text(members)
        
    packages=get_all_packages_data()
    text2=get_packages_table_text(packages)
    return get_html("index").replace("$$MEMBERS$$", text).replace("$$PACKAGES$$",text2)


#this route will return the page where trainer will insert the main info of the member
@app.route ("/newmember") 
def newmemberpage():
    return get_html("add_member")
"""
this route will be called after inserting the main info to create object
for the member and then will go to page where  trainer insert member's vital details
"""
@app.route ("/addnewmember") 
def addnewmember():
    name= flask.request.args.get("name")
    height= flask.request.args.get("height")
    email= flask.request.args.get("email")
    weight= flask.request.args.get("weight")
    phone= flask.request.args.get("phone")
    birthdate= flask.request.args.get("birthdate")
    gender= flask.request.args.get("gender")
    member=Member(name,birthdate,height,weight,gender,phone,email)

    return flask.redirect(f"/newVital?id={member.id}")

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
def addVitalDetails():
    member_id= flask.request.args.get("id")
    bodyFatPercentage= flask.request.args.get("bodyFatPercentage")
    disease= flask.request.args.get("disease")
    medications= flask.request.args.get("medications")
    allergy= flask.request.args.get("allergy")
    fitnessGoals= flask.request.args.get("fitnessGoals")

    vitaDetails=VitaDetails(allergy, disease,bodyFatPercentage,fitnessGoals,medications,member_id)
    vitaDetails.add_to_DB()
    return flask.redirect("/home")


#this route will used to pass id for member to the delete from database function
@app.route ("/deletemember") 
def deletemember():  
    id= flask.request.args.get("id")
    deleteMemberFromDB(id)
    return flask.redirect("/home") 

#this route will used to pass id for package to the delete from database function
@app.route ("/deletepackage") 
def deletepackage():
    id= flask.request.args.get("package_id")
    delete_package_from_DB(id)
    print ("delete package with id = " + str(id))
    return flask.redirect("/home") 

#this route will be called once user entered the name or id of the member he wanted to search for
@app.route ("/search") 
def search():
    nameOrId= flask.request.args.get("search") 
#check iff trainer entered an ID
    if nameOrId.isdigit():
        id=nameOrId
        #search by id
        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM members where member_id={id}")
            members = cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving members: {str(e)}")
            #if there is an error so go to home page 
            return flask.redirect("/home") 
            
        finally:
            cursor.close()
#if it is not by id so search by member's name    
    else:
        name=nameOrId
        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM members where name='{name}'")
            members = cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving members: {str(e)}")
            return flask.redirect("/home")
         
    all_members = []
    for member in members:
        member_data = member
        member_obj = Member(member_data[1],(member_data[2]) , int(member_data[3]), int(member_data[4]), member_data[5], member_data[6], member_data[7], (member_data[0]))
        all_members.append(member_obj)
#now get the data (the html element of the member's table) which will be replaced with the placeholder in the home page(index.html)
    text = get_members_table_text(all_members)

#this section will be called any way to view packages table in the home page
    packages=get_all_packages_data()
    text2=get_packages_table_text(packages)
    return get_html("index").replace("$$MEMBERS$$", text).replace("$$PACKAGES$$",text2)


"""
this route responsible for viewing all the details of the member in his profile page
so it will render the profile page with all member's data (info, vital info, sunscription info, workout info)
"""
@app.route("/member_profile")
def member_profile():
    id = flask.request.args.get("id")
#this section will get main info of the member
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM members WHERE member_id={id}")
        member_data = cursor.fetchone()
    except Exception as e:
        print(f"Error retrieving members: {str(e)}")
        return flask.redirect("/home")
    finally:
        cursor.close()
    
#this section will get Vitaldetails of the member
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM Vitaldetails WHERE memberId={id}")
        member_vital_data = cursor.fetchone()
    except Exception as e:
        print(f"Error retrieving vital: {str(e)}")
        return flask.redirect("/home")
    finally:
        cursor.close()

#if the member already exist and has vital data then get his subscription data if he has previous one
#then pass all of them to the template of member profile
    if member_vital_data and member_data is not None:
        member = Member(
            member_data[1],
            (member_data[2]),
            int(member_data[3]),
            int(member_data[4]),
            member_data[5],
            member_data[6],
            member_data[7],
            int(member_data[0]),
        )
        subscription=member.get_subscription()
        if subscription:
            subscription_data = {'name':subscription[0],'startDate': subscription[1] ,'endDate':subscription[2]}
        else:
            subscription_data = {'name':'Subscribe first','startDate': '' ,'endDate':''}

        vitaDetails = VitaDetails(
            member_vital_data[1],
            member_vital_data[2],
            member_vital_data[3],
            member_vital_data[4],
            member_vital_data[5],
            int(member_data[0])
        )
#get all packages data for the trainer if he want to subscribe or resubscripe for the memebr in package
        packages=get_all_packages_data()
#this section to get workout info for the member
        try:
            workout_file_path = f"members/{id}/workout_summary.txt"
            with open(workout_file_path, 'r') as file:
                workout_file_content = file.read()    
        except Exception as e:
            workout_file_content="Workout not Added Yet"
        try:
            nutrition_file_path = f"members/{id}/nutrition_plan.txt"
            with open(nutrition_file_path, 'r') as file:
                nutrition_file_content = file.read()    
        except Exception as e:
            nutrition_file_content="Nutrition not Added Yet"
        return render_template("member_profile.html", member=member, vitaDetails=vitaDetails, packages=packages, subscription_data=subscription_data,workout_file_content=workout_file_content,nutrition_file_content=nutrition_file_content)
#this condition will be valid if the member already exist but does not has vital data   
    elif member_data is not None:
        return flask.redirect("/newVital?id="+str(id))
    else:
        return flask.redirect("/home"+str(id))

#this route send the new package page
@app.route ("/newpacakge") 
def newpackage():
    return get_html("add_package")

#this route recieve the new package data and create instance of it's class then add to database
@app.route ("/addnewpackage") 
def addnewpackage():
    name= flask.request.args.get("name")
    value= flask.request.args.get("value")
    duration= flask.request.args.get("duration")

    package=Package(name, value,duration)
    package.add_to_DB()
    return flask.redirect("/home")



# New route to handle subscription form submission
@app.route("/subscribe", methods=["POST"])
def subscribe():
    package_id = flask.request.form.get("package_id")
    member_id = flask.request.form.get("member_id")
   
    flag,remaining_months,remaining_days=subscribe_to_package(package_id,member_id)
    if not flag:
        return flask.redirect("/member_profile?id="+str(member_id)+"&remaining_months="+str(remaining_months)+"&remaining_days="+str(remaining_days))
    else:
        return flask.redirect("/member_profile?id="+str(member_id))
    
# New route to handle subscription form submission
@app.route("/resubscribe", methods=["POST"])
def resubscribe():
    package_id = flask.request.form.get("package_id")
    member_id = flask.request.form.get("member_id")
   
    re_subscribe_to_package(package_id,member_id)
    return flask.redirect("/member_profile?id="+str(member_id))
    


# this route to handle add workout to member
@app.route("/add_workout", methods=["POST"])
def add_workout():
    # Get member_id from the form data
    member_id = flask.request.form.get("member_id")
    print("member_id is =" + str(member_id))

    # Create a directory if it doesn't exist for the member
    member_directory = f"members/{member_id}"
    os.makedirs(member_directory, exist_ok=True)

    # Create a single file for all workout data
    file_path = os.path.join(member_directory, "workout_summary.txt")
    
    
    with open(file_path, 'w') as workout_file:
        workout_file.write(f"Member ID: {member_id}\n\n")
        for day in range(1, 6):
            #check if there is at least one exercise existed for each day
            if flask.request.form.get(f"exercise_day{day}_{1}"): 
                workout_file.write(f"{'Day':<4}{day:<10}\n{'Exercise:':<40}{'Sets:':<20}{'Reps:':<20}{'Video Link:':<40}")
                for j in range(1, 4):
                    # Get exercise, sets, reps, and video_link for each day and exercise
                    exercise = flask.request.form.get(f"exercise_day{day}_{j}")
                    sets = flask.request.form.get(f"sets_day{day}_{j}")
                    reps = flask.request.form.get(f"reps_day{day}_{j}")
                    video_link = flask.request.form.get(f"video_link_day{day}_{j}")
                    workout_file.write(f"\n{exercise:<40}{sets:<20}{reps:<20}{video_link:<40}")
                workout_file.write("\n\n\n")   
            
                
    # Redirect to the member profile or another destination after subscription
    return flask.redirect(f"/member_profile?id=" + str(member_id))


# this route to handle add nutrition_plan to member
@app.route("/add_nutrition_plan", methods=["POST"])
def add_nutrition_plan():
    # Get member_id from the form data
    member_id = flask.request.form.get("member_id")
    print("member_id is =" + str(member_id))

    # Create a directory if it doesn't exist for the member
    member_directory = f"members/{member_id}"
    os.makedirs(member_directory, exist_ok=True)

    # Create a single file for all workout data
    file_path = os.path.join(member_directory, "nutrition_plan.txt")
    
    
    with open(file_path, 'w') as nutrition_plan_file:
        nutrition_plan_file.write(f"Member ID: {member_id}\n\n")
        for day in range(1, 6):
            #check if there is at least one exercise existed for each day
            if flask.request.form.get(f"meal{day}_{1}"): 
                nutrition_plan_file.write(f"{'Day':<4}{day:<10}\n{'Meal:':<40}{'Quantity:':<20}")
                for j in range(1, 4):
                    # Get exercise, sets, reps, and video_link for each day and exercise
                    meal = flask.request.form.get(f"meal{day}_{j}")
                    quantity = flask.request.form.get(f"quantity{day}_{j}")
                    nutrition_plan_file.write(f"\n{meal:<40}{quantity:<20}")
                nutrition_plan_file.write("\n\n\n")  
            
                
    # Redirect to the member profile or another destination after subscription
    return flask.redirect(f"/member_profile?id=" + str(member_id))
