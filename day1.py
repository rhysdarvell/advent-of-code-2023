input_file = 'input1.txt'


with open(input_file) as input:
    first_digit = None
    last_digit = None

    total = 0

    for line in input.readlines():
        #get first digit
        for char in line:
            if(char.isdigit()):
                first_digit = char
                break

        #get second digit
        for i in range(len(line)-1, -1, -1):
            if(line[i].isdigit()):
                last_digit = line[i]
                break

        value = first_digit + last_digit
        total = total + int(value)

    print(total)