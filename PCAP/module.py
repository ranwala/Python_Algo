#!/user/bin/env python3

"""module.py => this is a sample Python module """

__counter = 0

def suml(the_list):
    global __counter
    __counter += 1

    total = 0
    for element in the_list:
        total += element
    return total

def prodl(the_list):
    global __counter
    __counter += 1

    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == '__main__':
    print('I am been called directly. Useful for internal testing')
    my_list = [i+1 for i in range(5)]
    print(suml(my_list))
    print(prodl(my_list))
else:
    print('Someone is using me.')