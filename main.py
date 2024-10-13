def power4(number):
    if number <= 0:
        return False
    # Check if it's a power of 2 and if the only set bit is in an even position
    return (number & (number - 1)) == 0 and (number & 0xAAAAAAAA) == 0

n = int(input("Enter a number: "))
if power4(n):
    print("\nThe number is a power of 4")
else:
    print("\nThe number is not a power of 4")