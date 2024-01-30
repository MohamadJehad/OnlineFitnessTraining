import { checkEmpty } from "./constrains.js";
import { checkContainsNumbers, checkMinLength } from "./constrains.js";

/**
 * Constrains on member's data
 * name  ::  length > 3 , any number rejected 
 * hight ::   must be number  ,230 > hight  > 135  
 * weight::   must be a number 30 > weight > 230
 * email ::   must contains @ , bigger than length 8
 * birthDate :: after 1950 and before 2020
 * gender ::  only male, female 
 * phone :: must be 11 number with no strings
 */
/**
 * Body fat percentage  :: float number between 5 and 60   
 * diseasse ::   at least 2 char 
 * medication ::   at least 2 char
 * allergy ::  at least 2 char
 * fitness goal :: at least 2 char
 * 
 */
/**
 * Constrains:
 * package name     :: at least 3 char must not be empty
 * package value    :: must not be empyt or char
 * package duration :: must not be empyt or char
 */
//this message is empty by default and will be used to tell the trainser what data is wrong
const errorMsg=document.getElementById("errorMsg");

document.getElementsByClassName("form")[0].addEventListener("submit",()=>{
const elementsArray = document.getElementsByClassName('input');
for(var i=0 ;i<elementsArray.length ; i++){
    let name=elementsArray[i].name;
    let value=elementsArray[i].value;
    console.log(name+" "+value);
    
    if(checkEmpty(value,"Empty "+name+": Please Enter "+name)){
        event.preventDefault();
    }
    else if(name == 'name' && checkContainsNumbers(value,"member's Name must not contains any numbers")){
        event.preventDefault(); 
    }
    else if(name == 'name' && checkMinLength(value,3,"Name length must be more than 3")){
        event.preventDefault();
    }
    else if (name == 'height' && isNaN(value)) {
        event.preventDefault(); 
        errorMsg.innerText="height must be a number";      
    }
    else if(name == 'height' && (Number(value) > 230 || Number(value)< 135)){
        event.preventDefault(); 
        errorMsg.innerText="height must be bigger than 135 and smaller than 230";       
    }
    else if ((name=='phone' || name=='bodyFatPercentage') && isNaN(Number(value)) ) {
        event.preventDefault(); 
        errorMsg.innerText=name+" must be a number";
    }
    else if (name=='phone' && (value).length !=11) {
        event.preventDefault(); 
        errorMsg.innerText="Phone must be 11 number";   
    }
    else if (name=='weight' && isNaN(Number(value))) {
        event.preventDefault(); 
        errorMsg.innerText="Weight must be a number";
    }
    else if(name == 'weight' && (Number(value) > 230 || Number(value)< 30)){
        event.preventDefault(); 
        errorMsg.innerText="Weight must be bigger than 30 and smaller than 230";       
    }
    else if(name=='email' && !value.includes("@")){
        event.preventDefault(); 
        errorMsg.innerText="Email must contains @";
    }
    else if(name=='email' && value.trim().length <= 8){
        event.preventDefault(); 
        errorMsg.innerText="Email length must be more than 8 ";
    }
    else if(name == 'birthdate' && (Number(value.slice(0,4))<1950 || Number(value.slice(0,4))>2020)){
        errorMsg.innerText="Enter valid birthdate"; 
        console.log("value");
        event.preventDefault();  
    }
    else if((name == "disease" || name =="medications" || name=="allergy" || name =="fitnessGoals") && checkMinLength(value,2,"Min length of "+name+" at least 2 char")){
        event.preventDefault();
    }

    else if( name=='bodyFatPercentage' && (Number(value) > 60 || Number(value)< 5)){
        event.preventDefault(); 
        errorMsg.innerText="vital_fat_prcent must be bigger than 5 and smaller than 60";
    }
}
})