/**
 * This file is for the workout program, Nutrition plan table
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
            btn.textContent = 'Hide Day '+dayNum;
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

