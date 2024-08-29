def large_power(base, exponent):
    # Calculate the result of base raised to the power of exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# usage:
print(large_power(2, 13))  # True, because 2^13 = 8192, which is greater than 5000
print(large_power(2, 12))  # False, because 2^12 = 4096, which is not greater than 5000

def divisible_by_ten(num):
    # Check if the remainder of num divided by 10 is 0
    if num % 10 == 0:
        return True
    else:
        return False

# Example usage:
print(divisible_by_ten(50))  # True, because 50 is divisible by 10
print(divisible_by_ten(53))  # False, because 53 is not divisible by 10
