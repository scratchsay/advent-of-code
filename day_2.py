import re

with open('input.txt', 'r') as file:
    input_lines = file.readlines()
    game_total = 0
    power = 0
    for text in input_lines:
        text = text.split(';')
        game_pattern = re.compile("Game\s+\d+")
        game_num = int(game_pattern.findall(text[0])[0].strip('Game '))

        fewest_red = fewest_green = fewest_blue = 0

        for section in text:
            red = green = blue = 0

            blue_pattern = re.compile("\d+\s+blue")
            red_pattern = re.compile("\d+\s+red")
            green_pattern = re.compile("\d+\s+green")

            arr = blue_pattern.findall(section)
            for i in arr:
                blue = int(i.strip(' blue'))

            arr = red_pattern.findall(section)
            for i in arr:
                red = int(i.strip(' red'))

            arr = green_pattern.findall(section)
            for i in arr:
                green = int(i.strip(' green'))


            fewest_red = max(fewest_red, red)
            fewest_green = max(fewest_green, green)
            fewest_blue = max(fewest_blue, blue)

        power += fewest_red*fewest_green*fewest_blue

    print(power)
