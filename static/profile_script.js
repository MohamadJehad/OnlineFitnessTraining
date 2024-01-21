/**
 * in this section weill chaeck if the user is not subscriped in package yet
 * then will disable the text of start and end dates
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
 * This section is for the workout table
 * 
 */
const btn=document.getElementById("btn");
const btn1=document.getElementById("btn1");
const btn2=document.getElementById("btn2");
const btn3=document.getElementById("btn3");
const btn4=document.getElementById("btn4");
const btn5=document.getElementById("btn5");

const plan_btn1=document.getElementById("plan_btn1");
const plan_btn2=document.getElementById("plan_btn2");
const plan_btn3=document.getElementById("plan_btn3");
const workout_btn=document.getElementById("workoutbtn");
const plan_btn=document.getElementById("plan_btn");

const table=document.getElementsByClassName("excel-table");
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
btn1.onclick = function () {
    toggleDay('row1',btn1);
};

btn2.onclick = function () {
    toggleDay('row2',btn2);
};

btn3.onclick = function () {
    toggleDay('row3',btn3);
};

btn4.onclick = function () {
    toggleDay('row4',btn4);
};

btn5.onclick = function () {
    toggleDay('row5',btn5);
};
plan_btn1.onclick = function () {
    toggleDay('plan_row1',plan_btn1);
};

plan_btn2.onclick = function () {
    toggleDay('plan_row2',plan_btn2);
};

plan_btn3.onclick = function () {
    toggleDay('plan_row3',plan_btn3);
};
function toggleDay(day,btn) {
    // Convert HTMLCollection to an array
    let rows = Array.from(document.getElementsByClassName(`${day}`));
    const dayNum = parseInt(day.slice(3), 10);
    // Toggle the display of rows
    rows.forEach(row => {
        if (row.style.display === 'none' || row.style.display === '') {
            row.style.display = 'table-row';
            btn.textContent = 'Hide Day';
        } else {
            row.style.display = 'none';
            btn.textContent = 'Show Day '+dayNum;
        }
    });
}
function toggleBtns() {
    // Convert HTMLCollection to an array
    console.log("toggle btns");
    const btns = [btn1, btn2, btn3, btn4, btn5,workout_btn,plan_btn1,plan_btn2,plan_btn3,plan_btn];

    for (let btn of btns) {
        if (btn.style.display != 'block') {
            btn.style.display = 'block';
        } else {
            btn.style.display = 'none';
        }
    }
}

function toggleTable() {
    // Convert HTMLCollection to an array
    
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
 * 
 */
const print_workoutbtn = document.getElementById("print_workoutbtn");
const print_nutrition = document.getElementById("print_nutrition");
print_workoutbtn.onclick = function () {
    printWorkoutPlan();
};
print_nutrition.onclick = function () {
    printNutritionPlan();
};
function printWorkoutPlan() {
    var workoutContent = document.getElementById("workoutContent").innerText;

    // Create a new window
    var printWindow = window.open('', '_blank');

    // Write the workout content to the new window
    printWindow.document.write('<html><head><title>Workout Plan</title></head><body>');
    printWindow.document.write('<pre>' + workoutContent + '</pre>');
    printWindow.document.write('</body></html>');


    printWindow.print();
}

function printNutritionPlan() {
    var nutritionContent = document.getElementById("nutritionContent").innerText;

    // Create a new window
    var printWindow = window.open('', '_blank');

    // Write the workout content to the new window
    printWindow.document.write('<html><head><title>Nutrition Plan</title></head><body>');
    printWindow.document.write('<pre>' + nutritionContent + '</pre>');
    printWindow.document.write('</body></html>');


    printWindow.print();
}

/**
 * this code used to open window to user when subscripe for member who is already subscriped
 */
const remainingMonths=document.getElementById("remainingMonths");
const remainingDays=document.getElementById("remainingDays");
const popUp=document.getElementById("popUp");
const dropDownPackage=document.getElementById("packageDropdown");
const selectedPackage=document.getElementById("selected_package");

document.addEventListener('DOMContentLoaded', function () {
    // Function to get URL parameters
    function getParameterByName(name, url) {
      if (!url) url = window.location.href;
      name = name.replace(/[\[\]]/g, '\\$&');
      var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
      if (!results) return null;
      if (!results[2]) return '';
      return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }

    // Check for URL parameters
    var memberId = getParameterByName('id');
    var remainingMonths = getParameterByName('remaining_months');
    var remainingDays = getParameterByName('remaining_days');

    // If the parameters are present, show a pop-up
    if (memberId && remainingMonths && remainingDays) {
      viewPopUpWindow(remainingMonths,remainingDays);   
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

dropDownPackage.addEventListener("change", function () {
    //set local storage with the selected value
    localStorage.setItem("selected package",dropDownPackage.value)
});

/**
 * this section for validate that user choosed a package before submission 
 */
document.getElementById("subscribe-form").addEventListener("submit",()=>{
    console.log(selectedPackage.value)
    if(dropDownPackage.value==""){
        document.getElementById("choose-package").style.display='block';
        event.preventDefault(); 
    }
});

