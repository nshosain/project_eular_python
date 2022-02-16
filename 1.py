#projectEuler
def get_sum_of_digit(digit):
    f_sum = 0
    if digit == 3:
        for i in range(1000):
            if i % digit == 0:
                f_sum += i
        return f_sum

    if digit == 5:
        for i in range(1000):
            if i % digit == 0 and i % 3 != 0:
                f_sum += i
        return f_sum


print(get_sum_of_digit(3) + get_sum_of_digit(5))

