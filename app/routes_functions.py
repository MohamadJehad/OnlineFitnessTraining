import flask
from flask import Flask, render_template, send_from_directory,redirect,request
from app.functions import *
from app.classes import *
from app.search import *
from app.html_hanlding import *
from app.files_handling import *
from server import *

#this function return home page where view member's, packages, subscriptions main info
def homepage():
    members = get_all_members_data()
    text = get_members_table_text(members)
        
    packages=get_all_packages_data()
    text2=get_packages_table_text(packages)
    return get_html("index").replace("$$MEMBERS$$", text).replace("$$PACKAGES$$",text2)

#here the function take the info of member entered by the trainer and create instance of member class
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

#here the function take the vital info of member entered by the trainer and create instance of vitalDetails class
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

#this function will delete the member based on his id
def deletemember():  
    id= flask.request.args.get("id")
    err_msg=delete_member_from_DB(id)
    if(err_msg):
        return get_html("error_page").replace("&&ERROR&&",err_msg) 
    else:
        return flask.redirect("/home") 

#this function will delete the package based on it's id
def deletepackage():
    id= flask.request.args.get("package_id")
    delete_package_from_DB(id)
    print ("delete package with id = " + str(id))
    return flask.redirect("/home") 

#this function will be called to search for member by name or id
def search_for_member():
    nameOrId= flask.request.args.get("search") 
#check iff trainer entered an ID
    if nameOrId.isdigit():
        id=nameOrId
        members=search_by_id(id)   
#if it is not by id so search by member's name    
    else:
        name=nameOrId
        members=search_by_name(name)   
         
    all_members = []
    for member in members:
        member_data = member
        member_obj = Member(member_data[1],(member_data[2]) , int(member_data[3]),
                            int(member_data[4]), member_data[5], member_data[6], member_data[7], (member_data[0]))
        all_members.append(member_obj)
#now get the data (the html element of the member's table) which will be replaced with the placeholder in the home page(index.html)
    members_table = get_members_table_text(all_members)

#this section will be called any way to view packages table in the home page
    packages=get_all_packages_data()
    packages_table=get_packages_table_text(packages)
    return get_html("index").replace("$$MEMBERS$$", members_table).replace("$$PACKAGES$$",packages_table)

#this function will get the info of the member and pass it to the profile page
def get_member_profile():
    id = flask.request.args.get("id")
#this will get main info of the member
    member_data=search_by_id(id)[0]
    
#this section will get Vitaldetails of the member
    member_vital_data=get_vital_info(id)
    
#if the member already exist and has vital data then get his subscription data if he has previous one
#then pass all of them to the template of member profile
    if member_vital_data and member_data:
        member = Member(member_data[1],(member_data[2]),int(member_data[3]),int(member_data[4])
            ,member_data[5],member_data[6],member_data[7],int(member_data[0]),
        )
        vitaDetails = VitaDetails(member_vital_data[1],member_vital_data[2],member_vital_data[3],member_vital_data[4],
                                  member_vital_data[5],int(member_data[0])
        )
        subscription_data=get_member_subscription(member)
        
#get all packages data for the trainer if he want to subscribe or resubscripe for the memebr in package
        packages=get_all_packages_data()

#this line to get workout info and nutrition plan for the member
        workout_file_content,nutrition_file_content=get_workout_nutrition(id)

        return render_template("member_profile.html", member=member, vitaDetails=vitaDetails, packages=packages, subscription_data=subscription_data,workout_file_content=workout_file_content,nutrition_file_content=nutrition_file_content)
#this condition will be valid if the member already exist but does not has vital data   
    elif member_data:
        return flask.redirect("/newVital?id="+str(id))
    else:
        return get_html("error_page").replace("&&ERROR&&","Error") 

#this function takes the info of package and create instance of it's class
def addnewpackage():
    name= flask.request.args.get("name")
    value= flask.request.args.get("value")
    duration= flask.request.args.get("duration")

    package=Package(name, value,duration)
    package.add_to_DB()
    return flask.redirect("/home")

#this function will pass already existed member data to the page to view it in front of the trainer
#to let him edit only data he wanted while keeping the not edited data 
def editmember():  
    id= flask.request.args.get("id")
    member=search_by_id(id)
    vital_info=get_vital_info(id)
    return render_template("edit_member.html",member=member,vital_info=vital_info)

#this function will insert the new data to the memebr after editting it
def submit_edit_member():
    id= flask.request.args.get("id")
    name= flask.request.args.get("name")
    height= flask.request.args.get("height")
    email= flask.request.args.get("email")
    weight= flask.request.args.get("weight")
    phone= flask.request.args.get("phone")
    birthdate= flask.request.args.get("birthdate")
    gender= flask.request.args.get("gender")
    member=Member(name,birthdate,height,weight,gender,phone,email,id)

    bodyFatPercentage= flask.request.args.get("bodyFatPercentage")
    disease= flask.request.args.get("disease")
    medications= flask.request.args.get("medications")
    allergy= flask.request.args.get("allergy")
    fitnessGoals= flask.request.args.get("fitnessGoals")
    vitaDetails=VitaDetails(allergy, disease,bodyFatPercentage,fitnessGoals,medications,id)

    if edit_member_data(member,vitaDetails):
        return redirect("member_profile?id=" + str(id))
    else:
        return get_html("error_page").replace("&&ERROR&&","Edit Failed") 
    
#here will subscripe in package for member 
def subscribe():
    package_id = flask.request.form.get("package_id")
    member_id = flask.request.form.get("member_id")
   
    flag,remaining_months,remaining_days=subscribe_to_package(package_id,member_id)
    if not flag:
        return flask.redirect("/member_profile?id="+str(member_id)+"&remaining_months="+str(remaining_months)+"&remaining_days="+str(remaining_days))
    else:
        return flask.redirect("/member_profile?id="+str(member_id))

#here will resubscripe to package if the memebr subscriped and his subscription still valid    
def resubscribe():
    package_id = flask.request.form.get("package_id")
    member_id = flask.request.form.get("member_id")
   
    re_subscribe_to_package(package_id,member_id)
    return flask.redirect("/member_profile?id="+str(member_id))

#here will add new workout program to memebr
def add_workout():
    member_id = request.form.get("member_id")
    write_workout_to_file(flask.request.form, member_id)
    return redirect(f"/member_profile?id=" + str(member_id))

#here will add new nutrition plan to memebr
def add_nutrition_plan():
    member_id = flask.request.form.get("member_id")
    # Call the function to write nutrition plan to the file
    write_nutrition_plan_to_file(flask.request.form, member_id)
    return flask.redirect(f"/member_profile?id=" + str(member_id))