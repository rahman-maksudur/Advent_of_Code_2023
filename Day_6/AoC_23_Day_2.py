"""
Written by Maksudur Rahman,
a self-taught Machine Learning Engineer (https://rahman-maksudur.github.io/)
"""
# PART 1
# input format = (race duration, record distance)

race_info = [(53, 275), (71, 1181), (78, 1215), (80, 1524)]
result = [0, 0, 0, 0]

for tup in race_info:
    win = 0
    for i in range(tup[0]):
        if i == 0 or i == tup[0]:
            pass
        else:
            if ((tup[0] - i) * i) > tup[1]:
                win += 1
    result[race_info.index(tup)] = win

product = 1
for j in result:
    product = product * j

print("Part 1 result: ", product)

# PART 2
race_duration = 53717880
record_distance = 275118112151524

win = 0
for i in range(race_duration):
    if i == 0 or i == race_duration:
        pass
    else:
        if ((race_duration - i) * i) > record_distance:
            win += 1
print("Part 2 result: ", win)
