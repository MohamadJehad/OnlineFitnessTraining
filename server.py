#(Online Fit trainer) APP
import uuid
from datetime import datetime
import flask
app =flask.Flask("server")

"""
this class will contain the main info about each member
"""
class Member:
    def __init__(self, name, birthdate,height,weight,gender,phone,email,member_id=None):
        self.id = generate_new_id() if not member_id else  member_id
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
    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Getter and setter for 'gender'
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender.lower()

    # Getter and setter for 'birthdate'
    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, new_birthdate):
        if isinstance(new_birthdate, str):
            self._birthdate = datetime.strptime(new_birthdate, '%Y-%m-%d').date()
        else:
            self._birthdate = new_birthdate  
    # Getter and setter for 'height'
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    # Getter and setter for 'weight'
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    # Getter and setter for 'phone'
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        self._phone = new_phone

    # Getter and setter for 'email'
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    # Rest of the class methods

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
        return bmr
    """
    this function will add the member into the file
    """
    def addmembertofile(self):
        file = open("MembersData.txt","a")
        member_data=self.name+";"+str(self.birthdate)+";"+str(self.height)+";"+str(self.weight)+";"+self.gender+";"+str(self.phone)+";"+str(self.email)+";"+str(self.id)+";"+"\n"
        file.write(member_data)
        file.close()
    def deletemember(self):
        deleteMemberFromFile(self.id)

        

    

def getAllMembersData():
    file = open("MembersData.txt")
    members = file.read().strip()
    file.close()
    members = members.split("\n")
    all_members = []
    #if members=='':
    for member in members:
        member_data = member.split(";")
        member_obj = Member(member_data[0],(member_data[1]) , int(member_data[2]), int(member_data[3]), member_data[4], member_data[5], member_data[6], int(member_data[7]))
        all_members.append(member_obj)
    return all_members

def deleteMemberFromFile(member_id):
    print("id to delete "+str(member_id))
    members = getAllMembersData()
    member_to_delete = None
    for member in members:
        if str(member.id) == str(member_id):
            print("hereeeee")
            member_to_delete = member
            break
    if member_to_delete:
        members.remove(member_to_delete)
        file=open("MembersData.txt", "w")
        for member in members:
            member_data = f"{member.name};{str(member.birthdate)};{str(member.height)};{str(member.weight)};{member.gender};{str(member.phone)};{str(member.email)};{str(member.id)};\n"
            file.write(member_data)
        file.close()


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



@app.route("/") 
def homepage():
    members = getAllMembersData()
    text = ""
    for member in members:
        text += "<tr>"
        text += "<td>" + str(member.id) + "</td>"
        text += "<td>" + member.name + "</td>"
        text += "<td>" + str(member.calculate_age()) + "</td>"
        text += "<td>" + str(member.height) + "</td>"
        text += "<td>" + str(member.weight) + "</td>"
        text += "<td>" + member.gender + "</td>"
        text += "<td>" + member.phone + "</td>"
        text += "<td>" + member.email + "</td>"
        text += "<td><a href='/delete?id=" + str(member.id) + "' class='delete'>Delete</a></td>"
        text += "</tr>"
    return get_html("index").replace("$$MEMBERS$$", text)


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
    member.addmembertofile()
    return flask.redirect("/") 
@app.route ("/delete") 
def deletemember():
    id= flask.request.args.get("id")
    deleteMemberFromFile(id)
    return flask.redirect("/") 

"""
this function will get the html content from any page 
and send it to browser
"""
def get_html(pagename):
    html_file = open(pagename+".html")
    content =html_file.read()
    html_file.close()
    return content