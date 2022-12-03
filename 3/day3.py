input = open("input.txt", "r")

def rucksackInput(input):
    output = 0
    count = 0
    input = input.readlines()
    for line in input:
        count += 1
        line = line.strip()
        input1, input2 = splitString(line)
        for x in input1:
            for y in input2:
                if x == y:
                    commonChar = y
                    break
        if ord(commonChar) in range(65, 91):
            subtract = 64
            subtract = subtract - 26
        else:
            subtract = 96
        output += ord(commonChar)-subtract
    return output

def splitString(string):
    input1, input2 = string[:len(string)//2], string[len(string)//2:]
    return input1, input2

print(rucksackInput(input))