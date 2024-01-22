from datetime import datetime
import mysql.connector
from app.database import mysql_config

#----------------------------- Classes section ------------------------#
#this class will contain the main info about each member
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
            print(f"member is not suscriped so: {str(e)}")
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

