'''This program checks whether the given number is Armstrong or not'''
def is_armstrong(num):
    #Convert the number to a string to count digits
    num_str =str(num)
    num_digits = len(num_str) #Count the number of digits

    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == num
num = int(input("Enter a number: "))


if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")