input = open("input.txt", "r")

def rucksackInput(input):
    output = 0
    count = 0
    input = input.readlines()
    for line in input:
        count += 1
        line = line.strip()
        if count % 3 == 0:
            input1 = input[count-3].strip()
            input2 = input[count-2].strip()
            input3 = input[count-1].strip()
            for x in input1:
                for y in input2:
                    if x == y:
                        for z in input3:
                            if z == y:
                                commonChar = y
                                break
            if ord(commonChar) in range(65, 91):
                subtract = 64
                subtract = subtract - 26
            else:
                subtract = 96
            output += ord(commonChar)-subtract
    return output

#def splitString(string):
#    input1, input2 = string[:len(string)//2], string[len(string)//2:]
#    return input1, input2

print(rucksackInput(input))