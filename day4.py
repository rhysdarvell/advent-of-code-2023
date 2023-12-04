input_file = 'input4.txt'
total = 0

with open(input_file) as input:
    for line in input.readlines():
        matches = 0

        #remove leading title from string
        line = line.split(":")[1]

        #split string into lists of winning and ticket numbers
        line = line.split("|")
        winning_numbers = line[0]
        ticket_numbers = line[1]
        winning_numbers = winning_numbers.split()
        ticket_numbers = ticket_numbers.split()

        #iterate through 'your' numbers and check for matches
        for number in ticket_numbers:
            if number in winning_numbers:
                matches += 1

        #convert matches to score and add to total
        if matches <= 0:
            continue
        score = pow(2, matches-1)
        total += score
    print(total)