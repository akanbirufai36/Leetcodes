# Example 1
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

# Example 2
l1 = [2, 4, 3]
l2 = [5, 6, 4]


def check_longest(l1: list, l2: list):
    if len(l1) > len(l2):
        return l1
    else:
        return l2


long = check_longest(l1, l2)


def decUnits(a, b, carry=0):
    total = int(a) + int(b) + int(carry)
    return total // 10, total % 10


carry = 0
result = ''
for i in range(len(long)):
    try:
        a = l1[i]
    except IndexError:
        a = 0
    try:
        b = l2[i]
    except IndexError:
        b = 0

    carry, digit = decUnits(a, b, carry)
    result += str(digit)


# leftover carry after the loop becomes one more digit
if carry != 0:
    result += str(carry)

result = result[::-1]
print(result)
