def recur_fibo(n):  # returns fibonacci series
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


i = 0  # iterator
fibosum = 0

while True:  # an infinite loop
    last_number = recur_fibo(i)  # stores last digit of the series
    if last_number <= 4000000:  # runs loop if last number < 4 million
        # print(last_number) # prints the last number everytime
        if last_number % 2 == 0:  # Checks if the number is divisible by 2
            fibosum += last_number  # Adds latest number to sum
        i += 1  # increases iterator value
    else:  # checks if last number of series is less than 4 million
        break  # breaks loop if reached

print(fibosum)
