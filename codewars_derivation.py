def diff(poly):
    derivative_list = []
    highest_order = len(poly)
    for x in poly:
        derivative_list.append(x*highest_order)
        highest_order -= 1
    return derivative_list[0:highest_order-1]

print(diff([3,2,2,2]))