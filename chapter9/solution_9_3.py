def main():
    f = input().split(' ')
    print(f)

    stack = []
    for item in f:
        if item == '+':
            x = float(stack.pop())
            y = float(stack.pop())
            stack.append(y + x)
        elif item == '-':
            x = float(stack.pop())
            y = float(stack.pop())
            stack.append(y - x)
        elif item == '*':
            x = float(stack.pop())
            y = float(stack.pop())
            stack.append(y * x)
        elif item == '/':
            x = float(stack.pop())
            y = float(stack.pop())
            if x == 0:
                print('error')
                return
            stack.append(y / x)
        else:
            stack.append(float(item))

    print(stack[0])


main()
