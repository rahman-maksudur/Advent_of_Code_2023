"""
Written by Maksudur Rahman,
a self-taught Machine Learning Engineer (https://rahman-maksudur.github.io/)
"""
import re
file1 = open('input_day_1.txt', 'r')
Lines = file1.readlines()

# PART ONE

total = []

for line in Lines:
    numbers = []
    for c in line:
        if c.isdigit():
            numbers.append(c)
    cal_value = int(str(numbers[0]) + str(numbers[-1]))
    total.append(cal_value)

print(sum(total))

#PART TWO
total_2 = 0
numbers = ['1','2','3','4','5','6','7','8','9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
help_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
}
count = 0
for line in Lines:
    count += 1
    first_number = ''
    last_number = ''
    new_dict = {}
    for num in numbers:
        pattern = re.compile(num)
        result = pattern.search(line)
        while result:
            #print(result)
            #print(result.start())
            new_dict[result.start()] = num
            result = pattern.search(line, result.start()+1)

    sorted_dict = dict(sorted(new_dict.items()))
    #print(sorted_dict)
    #print(list(sorted_dict)[0], list(sorted_dict)[-1])
    first = list(sorted_dict)[0]
    last = list(sorted_dict)[-1]
    if sorted_dict[first].isdigit():
        first_number = str(sorted_dict[first])
    elif type(sorted_dict[first]) == str:
        first_number = help_dict[sorted_dict[first]]
    if sorted_dict[last].isdigit():
        last_number = str(sorted_dict[last])
    elif type(sorted_dict[last]) == str:
        last_number = help_dict[sorted_dict[last]]
    #print(first_number, last_number)
    #print(first_number+last_number)

    final_num = int(first_number + last_number)
    print(final_num, type(final_num))

    total_2 += final_num

print(total_2)
print('count=', count)