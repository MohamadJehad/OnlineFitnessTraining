/**
 * Body fat percentage  :: float number between 5 and 60   
 * diseasse ::   at least 2 char 
 * medication ::   at least 2 char
 * allergy ::  at least 2 char
 * fitness goal :: at least 2 char
 * 
 */
let message='';
const errorMsg=document.getElementById("errorMsg");
document.getElementById("add_vital_form").addEventListener("submit",()=>{
    
    //validate the vital_fat_prcent
    const vital_fat_prcent=parseFloat(document.getElementById("vital_fat_prcent").value);
    if (isNaN(vital_fat_prcent)) {
        event.preventDefault(); 
        errorMsg.innerText="vital_fat_prcent must be number";
        return
    }
    else if(vital_fat_prcent > 60 || vital_fat_prcent< 5){
        event.preventDefault(); 
        errorMsg.innerText="vital_fat_prcent must be bigger than 5 and smaller than 60";
        return
    }

    //valiadte the vital_disease
    const vital_disease=document.getElementById("vital_disease").value;
    if(vital_disease.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter vital_disease";
        return
    }
    else if(vital_disease.length < 2){
        event.preventDefault(); 
        errorMsg.innerText="vital_disease length must be 2";
        return
    }
    
    //valiadte the vital_medication
    const vital_medication=document.getElementById("vital_medication").value;
    if(vital_medication.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter vital_medication";
        return
    }
    else if(vital_medication.length < 2){
        event.preventDefault(); 
        errorMsg.innerText="vital_medication length must be 2";
        return
    }
    
    //validate the vital_fit_goal
    const vital_fit_goal=document.getElementById("vital_fit_goal").value;
    if(vital_fit_goal.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter vital_fit_goal";
        return
    }
    else if(vital_fit_goal.length < 2){
        event.preventDefault(); 
        errorMsg.innerText="vital_fit_goal length must be 2";
        return
    }

    //validate the vital_allergy
    const vital_allergy=document.getElementById("vital_allergy").value;
    if(vital_allergy.trim() == ''){
        event.preventDefault(); 
        errorMsg.innerText="Enter vital_allergy";
        return
    }
    else if(vital_allergy.length < 2){
        event.preventDefault(); 
        errorMsg.innerText="allergy length must be 2";
        return
    }
      
});
