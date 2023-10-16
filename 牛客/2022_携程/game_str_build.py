def generate_string_with_you(n, k):
    if n < 3 * k or n > 3 * k + 2:
        return "Impossible"

    remaining_you = k
    remaining_o = 1
    remaining_u = 1
    result = ""

    for i in range(n):
        if remaining_you > 0:
            result += "y"
            remaining_you -= 1
        elif remaining_o > 0:
            result += "o"
            remaining_o -= 1
        else:
            result += "u"
            remaining_u -= 1

    return result

n = 9
k = 1
result = generate_string_with_you(n, k)
print(result)
