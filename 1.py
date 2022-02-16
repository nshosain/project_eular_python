our_sum = 0

for i in range(1000):
    if i % 3 == 0:
        our_sum += i
        i += 3

i = 0
for i in range(1000):
    if i % 5 == 0 and i % 3 != 0:
        our_sum += i
        i += 5

print(our_sum)

