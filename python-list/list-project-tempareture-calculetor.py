my_day = int(input('How many days temperature?\n'))
total = 0
temp = []

for i in range(1, my_day + 1):
    next_day = int(input(f"Day {i+1}'s high temperature: "))
    temp.append(next_day)
    total += next_day

avrg = round(total / my_day, 2)
print(f"Average = {avrg}")

above = 0
for t in temp:
    if t > avrg:
        above += 1

print(str(above) + " day(s) above Average")
