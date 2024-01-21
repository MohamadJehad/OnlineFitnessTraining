/**
 * this function will be used in login page 
 */

const btn=document.getElementById("loginbtn");

//this part of code  used to diplay welocme message to coach once he enter his name anc click login
const text_filed =document.getElementById("text_filed");
const messaage=document.getElementById("messaage");
btn.addEventListener("click",()=>{
    messaage.innerText ="Welcome Coach: "+text_filed.value;
    localStorage.setItem("username", text_filed.value);
    text_filed.style.display = "none";
    btn.style.display = "none";
    //wait 1.5 sec then go to home page
    setTimeout(() => {  
        window.location.href = "/home";
        
    }, 1500);
}); 

//if the trainer already logged in before so his name will be stored
if(localStorage.getItem("username")){
    text_filed.style.display = "none";
    btn.style.display = "none";
    messaage.innerText ="Welcome Back Coach:  "+ localStorage.getItem("username");
    setTimeout(() => {  
        window.location.href = "/home";
        
    }, 1500);
}
