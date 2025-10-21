class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, value):
        self.__stack_list.append(value)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


    def push(self, value):
        self.__sum += value
        Stack.push(self, value)


    def pop(self):
        val = Stack.pop(self)
        self.__sum -= 1
        return val

    def get_sum(self):
        return self.__sum



stack_object = AddingStack()

print(stack_object.__dict__)
print(AddingStack.__module__)

# for i in range(5):
#     stack_object.push(i)
#
# print(stack_object.get_sum())
#
# for i in range(2):
#     stack_object.pop()

print(stack_object.get_sum())