from classes import Stack
from bs import strings
from func import find_opposite_bracket
from data import url

if __name__ == '__main__':
    for string in strings:
        my_stack = Stack()
        for i in string:
            if my_stack.isEmpty():
                my_stack.push(i)
            elif find_opposite_bracket(i) == my_stack.peek():
                my_stack.pop()
            else:
                my_stack.push(i)
        if my_stack.isEmpty():
            print(f'Строка со скобками "{string}" сбалансированна')
        else:
            print(f'Строка со скобками "{string}" не сбалансированна')