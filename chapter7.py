numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = round(sum(numlist) / len(numlist), 1)
print('Average:', average)
