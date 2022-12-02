input = open("input.txt", "r")

def gameInput(input):
    score = 0
    input = input.readlines()
    for line in input:
        for element in line.rstrip():
            #print(element)
            if element == "A" or element == "B" or element == "C":
                opponent = element
                #print(opponent)
            elif element == "Y" or element == "X" or element == "Z":
                you = element
                #print(you)
        score += battle(opponent, you)
    print(score)
        #print(opponent)
        #print(you)
        #battle(opponent, you)

def battle(opponent, you):
    match opponent:
        case "A":
            match you:
                case "X":
                    return 4
                case "Y":
                    return 8
                case "Z":
                    return 3
        case "B":
            match you:
                case "X":
                    return 1
                case "Y":
                    return 5
                case "Z":
                    return 9
        case "C":
            match you:
                case "X":
                    return 7
                case "Y":
                    return 2
                case "Z":
                    return 6
    #print(opponent)
    #print(you)

gameInput(input)