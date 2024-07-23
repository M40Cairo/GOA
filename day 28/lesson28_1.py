def bmi(weight, height):
    bmi = weight/height**2

    if bmi <= 18.5:
        return 'underweight'
    elif bmi <= 25:
        return 'normal'
    elif bmi <= 30:
        return 'overweight'
    else:
        return 'obese'
