const errorMsg=document.getElementById("errorMsg");

export function checkContainsNumbers(value,msg){
    let containsNumber=false;
    for (const char of value) {
        if (!isNaN(Number(char)) && char!=' ') {
             containsNumber = true;
            break;
        }
    }
    if(containsNumber){
        errorMsg.innerText=msg
        return true; 
    }
    return false;
}

export function checkEmpty(value,msg){
    if(value==''){
        errorMsg.innerText=msg;  
        return true; 
    }
    return false;
}
export function checkMinLength(value,MinLength,msg){
    if(value.trim().length < MinLength){
        errorMsg.innerText=msg;
        return true;
    }
    return false;
}
