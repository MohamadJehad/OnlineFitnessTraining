/**
 * 
 * this function will be used in login page
 */

const btn=document.getElementById("loginbtn");
const text_filed =document.getElementById("text_filed");
const messaage=document.getElementById("messaage");
btn.addEventListener("click",()=>{
    localStorage.setItem("username", " ");
    messaage.innerText ="Welcome Coach: "+text_filed.value;
    localStorage.setItem("username", text_filed.value);
    text_filed.style.display = "none";
    btn.style.display = "none";
    setTimeout(() => {  
        window.location.href = "/home";
        
    }, 1500);
}); 


if(localStorage.getItem("username")){
    messaage.innerText ="Welcome Back Coach:  "+ localStorage.getItem("username");
    //text_filed.style.display = "none";
    //btn.style.display = "none";
}
