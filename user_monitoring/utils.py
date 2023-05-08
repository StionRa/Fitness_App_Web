from datetime import date


def calculate_age(birth_day):
    today = date.today()
    birth_date = birth_day
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def calculate_bmi(body_height, body_weight):
    height = float(body_height)
    weight = float(body_weight)
    bmi = weight / (height * height)
    return round(bmi, 2)


def calculate_bmr(age, gender, body_weight, body_height, activity_level):
    age_x = int(age)
    body_weight_x = float(body_weight)
    body_height_x = float(body_height)
    if gender == "M":
        bmr = 88.362 + (13.397 * body_weight_x) + (4.799 * body_height_x * 100) - (
                5.677 * age_x)
    else:
        bmr = 447.593 + (9.247 * body_weight_x) + (3.098 * body_height_x * 100) - (
                4.330 * age_x)
    if activity_level == "Bed":
        bmr *= 1.1
    elif activity_level == "Sed":
        bmr *= 1.2
    elif activity_level == "Lig":
        bmr *= 1.375
    elif activity_level == "Mod":
        bmr *= 1.55
    elif activity_level == "Hea":
        bmr *= 1.175
    elif activity_level == "Ver":
        bmr *= 1.9
    return round(bmr, 2)


def recommended_weight(gender, bmi):
    if gender == 'M':
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 24.9:
            return "Normal weight"
        elif 25 <= bmi <= 29.9:
            return "Pre-obesity"
        elif 30 <= bmi <= 34.9:
            return "Obesity class I"
        elif 35 <= bmi <= 39.9:
            return "Obesity class II"
        elif bmi > 40:
            return "Obesity class III"
    elif gender == 'F':
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 24.9:
            return "Normal weight"
        elif 25 <= bmi <= 29.9:
            return "Pre-obesity"
        elif 30 <= bmi <= 34.9:
            return "Obesity class I"
        elif 35 <= bmi <= 39.9:
            return "Obesity class II"
        elif bmi > 40:
            return "Obesity class III"
    else:
        return
