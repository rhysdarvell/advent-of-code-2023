input_file = 'input1.txt'


with open(input_file) as input:
    first_digit = None
    last_digit = None

    total = 0

    #zero is omitted because it wasn't in the specification, index of written text is used to convert to digit
    numerals_text = [
        "9",
        "one",
        "two",
        "three",
        "four",
        "five", 
        "six",
        "seven",
        "eight",
        "nine",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8"
    ]

    for line in input.readlines():
        #find first written digit
        index = len(line)
        for i in numerals_text:
            i_index = line.find(i)
            if i_index == -1:
                continue

            if i_index < index:
                index = i_index
                first_digit = i
                if not first_digit.isdigit():
                    first_digit = numerals_text.index(i)

        #find last written digit
        index = -1
        for i in numerals_text:
            i_index = line.rfind(i)
            if i_index > index:
                index = i_index
                last_digit = i
                if not last_digit.isdigit():
                    last_digit = numerals_text.index(i)

        value = str(first_digit) + str(last_digit)
        total = total + int(value)

    print(total)