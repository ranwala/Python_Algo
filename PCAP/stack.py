stack = []

def push(data):
    stack.append(data)


def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())