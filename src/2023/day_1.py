with open('input.txt', 'r') as file:
    input_lines = file.readlines()
    total = 0
    for line in input_lines:
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2t")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        line = line.strip()
        c = 0
        for char in line:
            if char.isdigit():
                c += int(char)*10
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                c += int(line[i])
                total += c
                print(c)
                break

    print(total)
