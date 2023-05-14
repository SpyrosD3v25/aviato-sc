def get_response(name, age, sex, height, weight, free_time, current_nutrition, health_problems,
                  current_workout_plan, current_meditation, current_volunteering, tireness_history,
                  sleep_schedule, sleep_history, diet_history, nutrition_history, happiness_history,
                  workout_history, meditation_history, volunteering_history, user_query):

    
    greeting_keywords = ['hello', 'good morning', 'hey']
    if any(keyword in user_query.lower() for keyword in greeting_keywords):
        return "Hello sir how can i help you?"


    diet_keywords = ['diet plan', 'nutrition plan', 'daily nutrition']
    if any(keyword in user_query.lower() for keyword in diet_keywords):
        # calculate normal calorie intake
        normal_calorie_intake = height * 10

        # check age range and suggest calorie intake and ratio accordingly
        if age < 2:
            return "It is not recommended to suggest a diet plan for children under 2. Please consult with a doctor."
        elif age < 7:
            if height / weight > 1.5:
                calorie_intake = normal_calorie_intake * 1.2
            else:
                calorie_intake = normal_calorie_intake * 0.8
            protein = calorie_intake * 0.1 / 4
            carbs = calorie_intake * 0.3 / 4
            fat = calorie_intake * 0.1 / 9
        elif age < 12:
            if height / weight > 1.5:
                calorie_intake = normal_calorie_intake * 1.3
            else:
                calorie_intake = normal_calorie_intake * 0.9
            protein = calorie_intake * 0.15 / 4
            carbs = calorie_intake * 0.3 / 4
            fat = calorie_intake * 0.1 / 9
        elif age < 25:
            if height / weight > 1.5:
                calorie_intake = normal_calorie_intake * 1.5
            else:
                calorie_intake = normal_calorie_intake * 1.1
            protein = calorie_intake * 0.2 / 4
            carbs = calorie_intake * 0.2 / 4
            fat = calorie_intake * 0.1 / 9
        else:
            if height / weight > 1.5:
                calorie_intake = normal_calorie_intake * 1.6
            else:
                calorie_intake = normal_calorie_intake * 1.2
            protein = calorie_intake * 0.15 / 4
            carbs = calorie_intake * 0.4 / 4
            fat = calorie_intake * 0.1 / 9

        # calculate total calories
        total_calories = protein * 4 + carbs * 4 + fat * 9

        # create nutrition plan table
        nutrition_plan = f"""
        |-----------------------|-------|
        | Parameter             | Value |
        |-----------------------|-------|
        | Age                   | {age}  |
        | Sex                   | {sex} |
        | Height                | {height} cm |
        | Weight                | {weight} kg |
        | Current Nutrition     | {current_nutrition} |
        | Health Problems       | {health_problems} |
        | Current Workout Plan  | {current_workout_plan} |
        |-----------------------|-------|
        | Nutrition Plan        |       |
        |-----------------------|-------|
        | Protein               | {protein:.2f} g   |
        | Carbs                 | {carbs:.2f} g   |
        | Fat                   | {fat:.2f} g   |
        | Total Calories        | {total_calories:.2f} kcal |
        |-----------------------|-------|
        """
        return nutrition_plan

    # check if the user is asking about working out or exercise
    workout_keywords = ['workout', 'exercise']
    if any(keyword in user_query.lower() for keyword in workout_keywords):
        # provide workout tips based on the user's current workout plan and free time
        # return the response
        response = "Here are some workout tips for you."
        return response

    # check if the user is asking about business
    business_keywords = ['business', 'entrepreneurship']
    if any(keyword in user_query.lower() for keyword in business_keywords):
        # provide some business tips to help the user
        # return the response
        response = "Here are some business tips for you."
        return response

    # check if the user is asking about mental health
    mental_health_keywords = ['mental health', 'depression', 'anxiety']
    if any(keyword in user_query.lower() for keyword in mental_health_keywords):
        # provide some tips to improve the user's mental health based on their current status
        # return the response
        response = "Here are some tips to improve your mental health."
        return response

    # if the user's intent is not clear, ask for more information or suggest seeking professional help
    response = "I'm sorry, I'm not sure what you're asking. Can you please provide more information or consider seeking professional help?"
    return response



name = "John"
age = 30
sex = "Male"
height = 170
weight = 75
free_time = "Evenings"
current_nutrition = "Balanced"
health_problems = None
current_workout_plan = "3-day split"
current_meditation = "None"
current_volunteering = "1 hour per week"
tireness_history = None
sleep_schedule = "11 PM - 7 AM"
sleep_history = 7
diet_history = "No major changes"
nutrition_history = "Trying to eat more vegetables"
happiness_history = 8
workout_history = 2
meditation_history = None
volunteering_history = "Regular"

while True:
    message = input("Please enter your question or type 'exit' to quit: ")
    if message.lower() == "exit":
        break

    response = response = get_response(name, age, sex, height, weight, free_time, current_nutrition, health_problems,
                         current_workout_plan, current_meditation, current_volunteering, tireness_history,
                         sleep_schedule, sleep_history, diet_history, nutrition_history, happiness_history,
                         workout_history, meditation_history, volunteering_history, user_query=message)
    print(response)