from ex3_poly1 import poly1


def poly_eval(x, k):
    for elements in x:
        print poly1(elements, k)

poly_eval([-2, 0, 2, 4], [3, -10, 4, 3])
