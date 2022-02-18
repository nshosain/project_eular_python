def get_sum_of_digit(digit):  # return the value of sum
    f_sum = 0
    if digit == 3:  # assign the value of digit
        for i in range(1000):   # Create a sequence of numbers from 0 to 999
            if i % digit == 0:  # finding the value which is fully divided by 3
                f_sum += i  # adding those value in f_sum
        return f_sum

    if digit == 5:
        for i in range(1000):
            if i % digit == 0 and i % 3 != 0:   # finding the value which is fully divided by 5 and not by 3
                f_sum += i
        return f_sum


print(f"The sum is {get_sum_of_digit(3) + get_sum_of_digit(5)}")    # printing results by adding both value 
