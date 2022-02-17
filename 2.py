def recur_fibo(n):  # returns fibonacci series
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


i = 0  # iterator
while True:  # an infinite loop
    last_number = recur_fibo(i)  # stores last digit of the series
    if last_number > 50:  # checks if last number of series is less than 4 million
        break  # breaks loop if reached
    else:  # runs loop if last number < 4 million
        print(last_number)  # prints last number
        i += 1  # increases iterator value
