
/**
 * in this section weill chaeck if the user is not subscriped in package yet
 * then will disable the text of start and end dates
 * the check will be done by reading the values of start,end date
 */

const packageStart = document.getElementById("package_start_date");
const packageEnd = document.getElementById("package_end_date");
const packageName=document.getElementById("package_name");

// Function to check if a given string is a valid date
function isValidDate(dateString) {
  const isValid = !isNaN(Date.parse(dateString));
  return isValid;
}

// Check if packageEnd.innerText is not a valid date
if (!isValidDate(packageEnd.innerText.trim()) || !isValidDate(packageStart.innerText.trim())) {
  packageEnd.style.display = 'none';
  packageStart.style.display = 'none';
  packageName.style.display = 'none';
}


/**
 * This section is for the workout program, Nutrition plan table
 * here when user press on the btn he will see two tables each of 5 days 
 * and each day will has his own button to view or hide the rows of the day
 * and finally two buttons to submit the actions of adding nutrition plan or workout program
 */
//the main button
const btn=document.getElementById("btn");

//the five buttons of workout program
const btn1=document.getElementById("btn1");
const btn2=document.getElementById("btn2");
const btn3=document.getElementById("btn3");
const btn4=document.getElementById("btn4");
const btn5=document.getElementById("btn5");

//the five buttons of the nutrition plan
const plan_btn1=document.getElementById("plan_btn1");
const plan_btn2=document.getElementById("plan_btn2");
const plan_btn3=document.getElementById("plan_btn3");
const plan_btn4=document.getElementById("plan_btn4");
const plan_btn5=document.getElementById("plan_btn5");

//btn to submit adding workout program
const workout_btn=document.getElementById("workoutbtn");

//btn to submit adding nutrition plan
const plan_btn=document.getElementById("plan_btn");

//this will return array of the two tables
const table=document.getElementsByClassName("excel-table");

/**
 * now in this section i will add the actions to each button which will be (hide or show) 
 * a sprecific element even another button or row of the table
 */

btn.onclick = function () {
    toggleBtns();
    toggleTable();
    if(btn.textContent == 'Show Tables'){
        btn.textContent = 'Hide Tables';
    }
    else{
        btn.textContent = 'Show Tables';
    }
};

//workout plan buttons
const workoutButtons = [btn1, btn2, btn3, btn4, btn5];
workoutButtons.forEach((button, index) => {
    button.onclick = function () {
        toggleDay(`row${index + 1}`, button);
    };
});

// Nutrition Plan btns
const planButtons = [plan_btn1, plan_btn2, plan_btn3, plan_btn4, plan_btn5];
planButtons.forEach((button, index) => {
    button.onclick = function () {
        toggleDay(`row${index + 1}_plan`, button);
    };
});

function toggleDay(day,btn) {
    // Convert HTMLCollection to an array
    let rows = Array.from(document.getElementsByClassName(`${day}`));
    const dayNum = parseInt(day.slice(3), 10);
    // Toggle the display of rows
    rows.forEach(row => {
        if (row.style.display === 'none' || row.style.display === '') {
            row.style.display = 'table-row';
            btn.textContent = 'Hide Day'+dayNum;
        } else {
            row.style.display = 'none';
            btn.textContent = 'Show Day '+dayNum;
        }
    });
}
function toggleBtns() {
    // Convert HTMLCollection to an array
    console.log("toggle btns");
    const btns = [btn1, btn2, btn3, btn4, btn5,workout_btn,plan_btn1,plan_btn2,plan_btn3,plan_btn4,plan_btn5,plan_btn];

    for (let btn of btns) {
        if (btn.style.display != 'block') {
            btn.style.display = 'block';
        } else {
            btn.style.display = 'none';
        }
    }
}

function toggleTable() {
// Toggle the display of rows
        if(table[0].style.display == ''){
            table[0].style.display = 'table';
        }
        else if(table[0].style.display == 'table'){
            table[0].style.display = '';
        }
        if(table[1].style.display == ''){
            table[1].style.display = 'table';
        }
        else if(table[1].style.display == 'table'){
            table[1].style.display = '';
        }
}


/**
 * This section is for the print buttons which will print the workout program
 * or will print the nutrition plan
 */
//locating the two buttoms
const print_workoutbtn = document.getElementById("print_workoutbtn");
const print_nutrition = document.getElementById("print_nutrition");
//adding action to both of them
print_workoutbtn.onclick = function () {
    printWorkoutPlan();
};
print_nutrition.onclick = function () {
    printNutritionPlan();
};
function printWorkoutPlan() {
    const workoutContent = document.getElementById("workoutContent").innerText;
        console.log(workoutContent);
        // Create a new window
        let printWindow = window.open('', '_blank');

        // Write the workout content to the new window
        printWindow.document.write('<html><head><title>Workout Plan</title></head><body>');
        printWindow.document.write('<pre>' + workoutContent + '</pre>');
        printWindow.document.write('</body></html>');


        printWindow.print();
    }
    

function printNutritionPlan() {
    const nutritionContent = document.getElementById("nutritionContent").innerText;

    // Create a new window
    let printWindow = window.open('', '_blank');

    // Write the workout content to the new window
    printWindow.document.write('<html><head><title>Nutrition Plan</title></head><body>');
    printWindow.document.write('<pre>' + nutritionContent + '</pre>');
    printWindow.document.write('</body></html>');


    printWindow.print();
}

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

