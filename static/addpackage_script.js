/**
 * package name     :: at least 3 char 
 * package value    :: must not be empyt or char
 * package duration :: must not be empyt or char
 */
let message='';
const errorMsg=document.getElementById("errorMsg");
document.getElementById("add-package-form").addEventListener("submit",()=>{
    
    //validate the Package name
    const name=(document.getElementById("package-name").value);
    if(name.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter Package Name";
        return
    }
    else if(name.length < 2){
        event.preventDefault(); 
        errorMsg.innerText="Package Name must be at least 3 characters";
        return
    }
    //validate the Package value
    const value=(document.getElementById("package-value").value);
    if(value.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter Package value";
        return
    }
    //validate the Package duration
    const duration=(document.getElementById("package-duration").value);
    if(duration.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter Package duration";
        return
    }
    
      
});
