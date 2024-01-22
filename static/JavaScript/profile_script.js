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


