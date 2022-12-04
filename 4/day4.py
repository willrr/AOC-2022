input = open("input.txt", "r")

def assignmentInput(input):
    input = input.readlines()
    count = 0
    for line in input:
        line = line.strip()
        set1 = line.split(",")
        set1value1 = int(set1[0].split("-")[0])
        set1value2 = int(set1[0].split("-")[1])
        set2value1 = int(set1[1].split("-")[0])
        set2value2 = int(set1[1].split("-")[1])
        if set1value1 <= set2value2 and set1value2 >= set2value1:
            count += 1
            #print(str(set1value1) + "-" + str(set1value2) + " is fit in by " + str(set2value1) + "-" + str(set2value2))
        elif set1value1 >= set2value2 and set1value2 <= set2value1:
            count += 1
            #print(str(set1value1) + "-" + str(set1value2) + " fits in " + str(set2value1) + "-" + str(set2value2))
    return count

print(assignmentInput(input))
