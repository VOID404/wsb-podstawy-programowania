if __name__ == "__main__":
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = weight / height ** 2
    print(f"BMI: {bmi:.2f}")
    print("BMI: %f.2" % bmi)
    print("BMI: {0:.2f}".format(bmi))

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obesity")
