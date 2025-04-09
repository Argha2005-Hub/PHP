def is_armstrong_number(num):
    str_num = str(num)
    n = len(str_num)
    sum_of_powers = sum(int(digit) ** n for digit in str_num)
    return sum_of_powers == num
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
