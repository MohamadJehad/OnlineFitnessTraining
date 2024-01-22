/**
 * this code used to open window to user when subscripe for member who is 
 * already subscriped and his subscription is not expired
 * 
 * note that this section will be viewd in the page when the backend
 * send that there is a remaining days, months with the url 
 */
const remainingMonths=document.getElementById("remainingMonths");
const remainingDays=document.getElementById("remainingDays");
const popUp=document.getElementById("popUp");
const dropDownPackage=document.getElementById("packageDropdown");
const selectedPackage=document.getElementById("selected_package");

//first check at refresh if backend sent something about remaining days, months
document.addEventListener('DOMContentLoaded', function () {
    href= window.location.href;
    //first check if the url already contains days and months
    if(href.indexOf("remaining_months")>-1 &&href.indexOf("remaining_months")>-1 ){
        //if the condition is true then take days, months from url 
        const monthsStart = href.indexOf("remaining_months=") + ("remaining_months=").length;
        const monthsEnd = href.indexOf("&", monthsStart);
        const months = Number(href.substring(monthsStart, monthsEnd));


    // Find the index of "remaining_days" and extract the substring after it
        const daysStart = href.indexOf("remaining_days=") + ("remaining_days=").length;
        const days = Number(href.substring(daysStart));
        //pass the days, months to the pop up window and show it it trainer
        viewPopUpWindow(months,days);   
    }

});
function viewPopUpWindow(months,days){
    remainingDays.innerText=days;
    remainingMonths.innerText=months;
    popUp.style.display='block';
    selectedPackage.value=localStorage.getItem('selected package');
    //reset local storage
    localStorage.setItem("selected package"," ")

}
document.getElementById("close-popup").onclick=function(){
    popUp.style.display='none'
}


/**
 * here is the main usage of the local storage
 * so when user choose to subscripe in package and then perform bacend operation to check 
 * if the user already subscriped or not 
 * then we need something to hold the value of package id wich user wants to suscripe in
 */
dropDownPackage.addEventListener("change", function () {
    //set local storage with the selected value
    localStorage.setItem("selected package",dropDownPackage.value)
});

/**
 * this section for validate that user choosed a package before submission 
 */
document.getElementById("subscribe-form").addEventListener("submit",()=>{
    console.log(selectedPackage.value)
//if the user did not choose any backage and pressed submit this code will block him until he choose one
    if(dropDownPackage.value==""){
        document.getElementById("choose-package").style.display='block';
        event.preventDefault(); 
    }
});
