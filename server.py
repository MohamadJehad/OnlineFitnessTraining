#(Online Fit trainer) APP
from datetime import datetime, timedelta
import mysql.connector
import flask
from flask_mysqldb import MySQL
from flask import Flask, render_template, send_from_directory
import os

app =flask.Flask(__name__)
app = Flask(__name__, template_folder="views")
if __name__=='__main__':
    app.run(debug=True)

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'K1d02370@2024',
    'database': 'fittrackdb'
}



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
            return get_html("errorPage").replace("$$MSG$$", "Enter Valid Data")
        if member_id == None:
            self.add_to_DB()    
        else:
            self.id=member_id

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
        this function return the package that the member subscriped in
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
        return subscription
    
    
    """
        this function used to calculate the age of the member based on his birthdate
    """
    def calculate_age(self):
         today = datetime.now().date()
         age = today.year - self.birthdate.year
         return age
    
    """
    this function calculate the member's bmr
    """
    def calculate_bmr(self):
        if self.gender == "male":
            bmr = 88.362 + (13.397 * self.weight)+(4.799 * self.height)-(5.677 * self.calculate_age())
        elif self.gender == "female":
            bmr = 447.593 + (9.247 * self.weight)+(3.098 * self.height)-(4.330 * self.calculate_age())
        return int(bmr)

    def deletemember(self):
        deleteMemberFromDB(self.id)
        del self

class Package:
    def __init__(self, name, value,duration,package_id=None):
        self.package_id = generate_new_id() if not package_id else  package_id
        self.name = name
        self.value=value
        self.duration=duration

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


class VitaDetails:
    def __init__(self, allergy,disease,bodyFatPercentage, fitnessGoals,medications,member_id=None):
        self.member_id =  member_id
        self.fitnessGoals = fitnessGoals
        self.medications = medications
        self.allergy=allergy
        self.disease=disease
        self.bodyFatPercentage=bodyFatPercentage

        
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




def getAllMembersData():
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
    #if members=='':
    for member in members:
        member_data = member
        member_obj = Member(member_data[1],(member_data[2]) , int(member_data[3]), int(member_data[4]), member_data[5], member_data[6], member_data[7],member_data[0])
        all_members.append(member_obj)
    
    return all_members

def getAllPackagesData():
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
    #if members=='':
    for package in packages:
        package_obj = Package(package[1], int(package[3]),int(package[2]) , int(package[0]))
        all_packages.append(package_obj)
    return all_packages


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


def deletePackageFromDB(package_id):
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()

        # Check if the package exist in subscription
        cursor.execute(f"SELECT * FROM subscription WHERE package_id = {package_id}")
        package = cursor.fetchall()

        if package:
            # If the member has vital details, delete them first
            cursor.execute(f"DELETE FROM subscription WHERE package_id = {package_id}")

        # Now delete the package
        cursor.execute(f"DELETE FROM package WHERE id = {package_id}")

        db.commit()
        print(f"Package with ID {package_id} deleted successfully")
    except mysql.connector.Error as error:
        print(f"Error deleting package: {error}")
    finally:
        cursor.close()


def generate_new_id():
    file = open("latestID.txt")
    id = int(file.read().strip())
    file.close()
    file = open("latestID.txt",'w')
    file.write(str(id+1))
    file.close()
    return id
class User:
    name=""


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/home") 
def homepage():
    members = getAllMembersData()
    text = get_members_table_text(members)
        
    packages=getAllPackagesData()
    text2=get_packages_table_text(packages)
    return get_html("index").replace("$$MEMBERS$$", text).replace("$$PACKAGES$$",text2)


@app.route ("/newmember") 
def newmemberpage():
    return get_html("add_member")

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

@app.route ("/newVital") 
def newVitalpage():
    id= flask.request.args.get("id")
    return get_html("add_vital_details").replace("&&ID&&",id)
   
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



@app.route ("/deletemember") 
def deletemember():  
    id= flask.request.args.get("id")
    deleteMemberFromDB(id)
    return flask.redirect("/home") 

@app.route ("/deletepackage") 
def deletepackage():
    id= flask.request.args.get("package_id")
    deletePackageFromDB(id)
    print ("delete package with id = " + str(id))
    return flask.redirect("/home") 
@app.route ("/search") #the next function will be called once user entered the name of contact he wanted to search for
def search():
    result=[]
    nameOrId= flask.request.args.get("search") 
    print("nameOrId = "+str(nameOrId))
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
            return flask.redirect("/home") 
            
        finally:
            cursor.close()
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
    
    text = get_members_table_text(all_members)

    packages=getAllPackagesData()
    text2=get_packages_table_text(packages)
    return get_html("index").replace("$$MEMBERS$$", text).replace("$$PACKAGES$$",text2)

def get_members_table_text(all_members):
    text = ""
    for member in all_members:
        text += "<tr>"
        text += "<td>" + str(member.id) + "</td>"
        text += "<td>" + member.name + "</td>"
        #text += "<td>" + str(member.calculate_age()) + "</td>"
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

@app.route("/member_profile")
def member_profile():
    result = []
    id = flask.request.args.get("id")
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
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM package")
        packages_data = cursor.fetchone()
    except Exception as e:
        print(f"Error retrieving vital: {str(e)}")
        cursor.close()
        return flask.redirect("/home")
    
    
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
        packages=getAllPackagesData()
        try:
            workout_file_path = f"members/{id}/workout_summary.txt"
            with open(workout_file_path, 'r') as file:
                file_content = file.read()
            return render_template("member_profile.html", member=member, vitaDetails=vitaDetails, packages=packages, subscription_data=subscription_data,file_content=file_content)
        except Exception as e:
            return render_template("member_profile.html", member=member, vitaDetails=vitaDetails, packages=packages,subscription_data=subscription_data,file_content="Workout Not Added Yet")

                
    else:
        return "No vital details found for this member."



"""
this function will get the html content from any page 
and send it to browser
"""
def get_html(pagename):
    html_file = open("views/"+pagename+".html")
    content =html_file.read()
    html_file.close()
    return content

@app.route ("/") 
def login():
    return get_html("login")

@app.route ("/newpacakge") 
def newpackage():
    return get_html("add_package")

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
    

# New route to handle add workout to member
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
        break_flag = False
        for day in range(1, 6):
            #check if there is at least one exercise existed 
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




def subscribe_to_package(package_id,member_id):
    #first chack if memebr already subscriped

    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM subscription WHERE memberId={member_id}")
        existing_subscription = cursor.fetchone()
        current_date = datetime.now().date()
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
            print("Member subscribed successfully ---------------------------------")
            cursor.close()
            ret= True,0,0
        else:
            existing_end_date=((existing_subscription)[2])
            remaining_days = (existing_end_date - current_date).days # total number of days remaining 
            remaining_months=remaining_days//30     # total number of Months remaining 
            remaining_days=remaining_days-remaining_months*30   #  number of days remaining after months
            print("---abc--------------"+str(remaining_days)+"-----------------"+str(remaining_months))
            cursor.close()
            ret= False,remaining_months,remaining_days

    except Exception as e:
        print(f"Error retrieving : {str(e)}")
        
    finally:
        cursor.close()
        return ret

def re_subscribe_to_package(package_id,member_id):
    #first chack if memebr already subscriped

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
    