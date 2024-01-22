"""
this function will return the text stored in nutrition,workout files
"""
def get_workout_nutrition(id):
    try:
        workout_file_path = f"members/{id}/workout_summary.txt"
        with open(workout_file_path, 'r') as file:
            workout_file_content = file.read()    
    except Exception as e:
        workout_file_content="Workout not Added Yet"
    try:
        nutrition_file_path = f"members/{id}/nutrition_plan.txt"
        with open(nutrition_file_path, 'r') as file:
            nutrition_file_content = file.read()    
    except Exception as e:
        nutrition_file_content="Nutrition not Added Yet"
    return workout_file_content,nutrition_file_content
   