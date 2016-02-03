def poly1(x, k):

    result_y = 0
    for i, coefficients in enumerate(k):
        y = coefficients * x**i
        result_y = result_y + y
    return result_y


print poly1(4, [3, -10, 4, 3])

