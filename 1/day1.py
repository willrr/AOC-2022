input = open("input.txt", "r")

def calorieInput(input):
    elfArray = []
    totalCalories = 0
    count = 0
    input = input.readlines()
    length = len(input)
    for line in input:
        count += 1
        calories = line.rstrip()
        if calories != "":
            totalCalories += int(calories)
            if count == length:
                elfArray.append(totalCalories)
                totalCalories = 0
                sort(elfArray)
        else:
            elfArray.append(totalCalories)
            totalCalories = 0

def sort(elfArray):
    elfArray.sort(reverse=True)
    print(elfArray[0])
        
calorieInput(input)