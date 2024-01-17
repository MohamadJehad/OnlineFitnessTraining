/**
 * name  ::  length > 3 , any number rejected 
 * hight ::   must be number  ,230 > hight  > 135  
 * weight::   must be a number 30 > weight > 230
 * email ::   must contains @ , bigger than length 6
 * birthDate :: after 1950 and before 2020
 * gender ::  only male, female 
 * phone :: must be 11 number with no strings
 */
let errorMsg='';
document.getElementById("add_member_form").addEventListener("click",()=>{
    
    //validate the name
    const MemberName=document.getElementById("member_name").value;
    containsNumber=false
    for (const char of MemberName) {
        if (!isNaN(Number(char))) {
            containsNumber = true;
            break;
        }
    }
    if(containsNumber){
        console.log("containsNumber  "); 
        event.preventDefault();  
        return; 
    }
    if(MemberName.trim().length <3){
        event.preventDefault(); 
        console.log("nooo");
        return;
    }

    //valiadte the height
    const MemberHeight=Number(document.getElementById("member_height").value);
    if (isNaN(MemberHeight)) {
        event.preventDefault(); 
        console.log("not  a number");
        return
    }
    else if(MemberHeight > 230 || MemberHeight< 135){
        event.preventDefault(); 
        console.log("must be bigger than 135 and smaller than 230");
        return
    }
    //valiadte the weight
    const MemberWeight=Number(document.getElementById("member_weight").value);
    if (isNaN(MemberWeight)) {
        event.preventDefault(); 
        console.log("not  a number");
        return
    }
    else if(MemberWeight > 230 || MemberWeight< 30){
        event.preventDefault(); 
        console.log("weight must be bigger than 30 and smaller than 230");
        return
    }
    
    //validate the phone
    const MemberPhone=document.getElementById("member_phone").value;
    if (isNaN(Number(MemberPhone))) {
        event.preventDefault(); 
        console.log("phone not  a number");
        return
    }
    else if(MemberPhone.length != 11){
        event.preventDefault(); 
        console.log("phone must be 11 number");
        return
    }

    //validate the email
    const MemberEmail=document.getElementById("member_email").value;
    if(!MemberEmail.includes("@")){
        event.preventDefault(); 
        console.log("Email must include @");
        return
    }
    else if(MemberEmail.trim().length <= 6){
        event.preventDefault(); 
        console.log("Email length must be bigger than 6");
        return
    }
    
    //validate the member_birthdate
    const member_birthdate=Number(document.getElementById("member_birthdate").value.slice(0,4));
    if(member_birthdate<1950 || member_birthdate>2020){
        console.log("wrong birth date  "); 
        event.preventDefault();  
        return; 
    }
    //validate the member_gender
    const member_gender=document.getElementById("member_gender").value.toLowerCase();
    if(member_gender==''){
        console.log("Choose gender  "); 
        event.preventDefault();  
        return; 
    }
  
});
