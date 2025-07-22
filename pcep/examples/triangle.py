def is_a_triangle(a,b,c):
    # First algo
    # if a + b <= c:
    #     return False
    # elif b + c <= a:
    #     return False
    # elif a + c <= b:
    #     return False
    # return True

    # Second algo
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return False
    # return True

    # Third algo
    return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False

    elif a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    elif b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    elif c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    return False

def heron(a,b,c):
    s = (a + b + c) / 2
    return (s * (s-a) * (s-b) * (s-c)) ** 0.5

def area(a,b,c):
    if not is_a_triangle(a,b,c):
        return None
    return heron(a,b,c)

print(area(1,1,2))
print(area(3,4,5))