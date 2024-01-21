/**
 * Constrains on member's data
 * name  ::  length > 3 , any number rejected 
 * hight ::   must be number  ,230 > hight  > 135  
 * weight::   must be a number 30 > weight > 230
 * email ::   must contains @ , bigger than length 6
 * birthDate :: after 1950 and before 2020
 * gender ::  only male, female 
 * phone :: must be 11 number with no strings
 */
let message='';
//this message is empty by default and will be used to tell the trainser what data is wrong
const errorMsg=document.getElementById("errorMsg");
document.getElementById("add_member_form").addEventListener("submit",()=>{
    
    //validate the name
    const MemberName=document.getElementById("member_name").value;
    containsNumber=false
    if(MemberName.trim().length == ''){
        event.preventDefault(); 
        errorMsg.innerText="You must enter the name";
        return;
    }
    for (const char of MemberName) {
        if (!isNaN(Number(char)) && char!=' ') {
            containsNumber = true;
            break;
        }
    }
    if(containsNumber){
        errorMsg.innerText="Name must not contain any number";
        event.preventDefault();  
        return; 
    }
    else if(MemberName.trim().length <3){
        event.preventDefault(); 
        errorMsg.innerText="Name length must be more than 3";
        return;
    }

    //valiadte the height
    const MemberHeight=Number(document.getElementById("member_height").value);
    if(MemberHeight==''){
        errorMsg.innerText="enter a heighy first";
        event.preventDefault();  
        return; 
    }
    else if (isNaN(MemberHeight)) {
        event.preventDefault(); 
        errorMsg.innerText="height must be a number";
        return
    }
    else if(MemberHeight > 230 || MemberHeight< 135){
        event.preventDefault(); 
        errorMsg.innerText="height must be bigger than 135 and smaller than 230";
        return
    }
    //validate the phone number
    const MemberPhone=document.getElementById("member_phone").value;
    if (isNaN(Number(MemberPhone))) {
        event.preventDefault(); 
        errorMsg.innerText="phone must be a number";
        return
    }
    else if(MemberPhone.length != 11){
        event.preventDefault(); 
        errorMsg.innerText="phone length must be 11 numbers";
        return
    }
    //valiadte the weight
    const MemberWeight=Number(document.getElementById("member_weight").value);
    if (isNaN(MemberWeight)) {
        event.preventDefault(); 
        errorMsg.innerText="weight must be number";
        return
    }
    else if(MemberWeight > 230 || MemberWeight< 30){
        event.preventDefault(); 
        errorMsg.innerText="weight must be bigger than 30 and smaller than 230";
        return
    }
    
    

    //validate the email
    const MemberEmail=document.getElementById("member_email").value;
    if(!MemberEmail.includes("@")){
        event.preventDefault(); 
        errorMsg.innerText="Email must contains @";
        return
    }
    else if(MemberEmail.trim().length <= 6){
        event.preventDefault(); 
        errorMsg.innerText="Email length must be more than 6 ";
        return
    }
    
    //validate the member_birthdate
    const member_birthdate=Number(document.getElementById("member_birthdate").value.slice(0,4));
    if(member_birthdate<1950 || member_birthdate>2020){
        errorMsg.innerText="Enter right birthdate"; 
        event.preventDefault();  
        return; 
    }
    //validate the member_gender
    const member_gender=document.getElementById("member_gender").value.toLowerCase();
    if(member_gender==''){
        errorMsg.innerText="select a gender first";
        event.preventDefault();  
        return; 
    }
  
});
