# 1. while loop
print("1. while loop (count from 1 to 5):")
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. for loop with range
print("\n2. for loop (range from 1 to 5):")
for j in range(1, 6):
    print(j)

# 3. for loop over a list
print("\n3. for loop over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 4. while loop with break
print("\n4. while loop with break (stop at 3):")
k = 1
while True:
    print(k)
    if k == 3:
        break
    k += 1

# 5. for loop with continue
print("\n5. for loop with continue (skip 3):")
for n in range(1, 6):
    if n == 3:
        continue
    print(n)
