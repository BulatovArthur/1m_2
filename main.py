import fileinput


class Stack:
    def __init__(self, max_size):
        self.max = max_size
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.size() >= self.max:
            print('overflow')
        else:
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('underflow')
        else:
            print(self.items[-1])
            self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        if self.size() > 0:
            print(*self.items, sep=" ")
        else:
            print('empty')


bank = []
check = False

for line in fileinput.input():
    text = line.split('\n')
    bank += text

while bank.count('') != 0:
    bank.remove('')

if not bank:
    size = 0

i = int(0)

while i < len(bank):
    if 'set_size' in bank[i]:
        if not check:
            check = True
            spl_text = bank[i].split()
            size = int(spl_text[1])
            stack = Stack(size)
        else:
            print('error')
        i += 1
    elif 'push' in bank[i]:
        if check:
            str_push = bank[i].split()
            if str_push[0] == 'push' and len(str_push) == 2:
                element = str_push[1]
                stack.push(element)
            else:
                print('error')
        else:
            print('error')
        i += 1
    elif 'pop' in bank[i]:
        if check:
            if ' ' in bank[i]:
                print('error')
            elif bank[i] != 'pop':
                print('error')
            else:
                stack.pop()
        else:
            print('error')
        i += 1
    elif 'print' in bank[i]:
        if check:
            if ' ' in bank[i]:
                print('error')
            elif bank[i] != 'print':
                print('error')
            else:
                stack.print()
        else:
            print('error')
        i += 1
    else:
        print('error')
        i += 1
