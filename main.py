import random
numbers = [] * 10
for i in range(10):
    numbers.append(random.randint(0,100))

min = min(numbers)
min_index = numbers.index(min)

print(f"Min: {min}")
print(f"Min Index: {min_index}")