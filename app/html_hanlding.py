
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
this function will take array of member's objects andd make them in shape of
members table to be placed in the homepage instead of placeholder
"""
def get_members_table_text(all_members):
    text = ""
   # print("all members = "+str(all_members))
    if all_members==[]:
        text+=" </tbody></table><div class='notFound'><h2>No Member Found</h1></div>"
    for member in all_members:
        text += "<tr>"
        text += "<td>" + str(member.id) + "</td>"
        text += "<td>" + member.name + "</td>"
        text += "<td>" + str(member.calculate_age()) + "</td>"
        #text += "<td>" + str(member.height) + "</td>"
        #text += "<td>" + str(member.weight) + "</td>"
        #text += "<td>" + member.gender + "</td>"
        text += "<td class='mob'>" + member.phone + "</td>"
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
        text += "<td><a href='/editmember?id=" + str(member.id) + "' class='profile'>Edit</a></td>"
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

