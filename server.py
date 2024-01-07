#(Online Fit trainer) APP

from datetime import datetime
import flask
app =flask.Flask("server")

"""
this class will contain the main info about each member
"""
class Member:
    def __init__(self, name, birthdate,height,weight,gender,phone,email):
        self.name = name
        self.gender = gender.lower()
        self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()  
        self.height=height
        self.weight=weight
        self.phone=phone
        self.email=email
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
    def addmember(self):
        file = open("MembersData.txt","a")
        member_data=self.name+";"+self.gender+";"+str(self.birthdate)+";"+str(self.height)+";"+str(self.weight)+";"+str(self.phone)+";"+"\n"
        file.write(member_data)
        file.close()
    


class User:
    name=""



@app.route ("/") 
def homepage():
    return get_html("index")

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
    member.addmember()
    return get_html("add_member")


"""
this function will get the html content from any page 
and send it to browser
"""
def get_html(pagename):
    html_file = open(pagename+".html")
    content =html_file.read()
    html_file.close()
    return content