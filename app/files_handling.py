import os
#this function will return the text stored in nutrition,workout files
def get_workout_nutrition(id):
    #workout
    try:
        workout_file_path = f"members/{id}/workout_summary.txt"
        with open(workout_file_path, 'r') as file:
            workout_file_content = file.read()    
    except Exception as e:
        workout_file_content="Workout not Added Yet"
    #Nutrition
    try:
        nutrition_file_path = f"members/{id}/nutrition_plan.txt"
        with open(nutrition_file_path, 'r') as file:
            nutrition_file_content = file.read()    
    except Exception as e:
        nutrition_file_content="Nutrition not Added Yet"
    return workout_file_content,nutrition_file_content


# Function to write nutrition plan to a file
def write_nutrition_plan_to_file(form_data, member_id):
     # Create a directory if it doesn't exist for the member
    member_directory = f"members/{member_id}"
    os.makedirs(member_directory, exist_ok=True)

    # Create a single file for all workout data
    file_path = os.path.join(member_directory, "nutrition_plan.txt")
    with open(file_path, 'w') as nutrition_plan_file:
        nutrition_plan_file.write(f"Member ID: {member_id}\n\n")
        for day in range(1, 6):
            # Check if there is at least one meal existed for each day
            if form_data.get(f"meal{day}_{1}"):
                nutrition_plan_file.write(f"{'Day':<4}{day:<10}\n{'Meal:':<40}{'Quantity:':<20}")
                for j in range(1, 4):
                    # Get meal and quantity for each day and meal
                    meal = form_data.get(f"meal{day}_{j}")
                    quantity = form_data.get(f"quantity{day}_{j}")
                    nutrition_plan_file.write(f"\n{meal:<40}{quantity:<20}")
                nutrition_plan_file.write("\n\n\n")

# Function to write workout data to a file
def write_workout_to_file(form_data, member_id):
     # Create a directory and file if it doesn't exist for the member
    member_directory = f"members/{member_id}"
    os.makedirs(member_directory, exist_ok=True)
    file_path = os.path.join(member_directory, "workout_summary.txt")
    with open(file_path, 'w') as workout_file:
        workout_file.write(f"Member ID: {member_id}\n\n")
        for day in range(1, 6):
            # Check if there is at least one exercise existed for each day
            if form_data.get(f"exercise_day{day}_{1}"):
                workout_file.write(f"{'Day':<4}{day:<10}\n{'Exercise:':<40}{'Sets:':<20}{'Reps:':<20}{'Video Link:':<40}")
                for j in range(1, 4):
                    # Get exercise, sets, reps, and video_link for each day and exercise
                    exercise = form_data.get(f"exercise_day{day}_{j}")
                    sets = form_data.get(f"sets_day{day}_{j}")
                    reps = form_data.get(f"reps_day{day}_{j}")
                    video_link = form_data.get(f"video_link_day{day}_{j}")
                    workout_file.write(f"\n{exercise:<40}{sets:<20}{reps:<20}{video_link:<40}")
                workout_file.write("\n\n\n")
