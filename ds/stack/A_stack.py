"""
Модуль описывающий структуру данных - стек LIFO

clear()
is_empty()
True
push(1)
push(2)
push(3)
is_empty()
False
pop()
3
pop()
2
pop()
1
is_empty()
True

"""
import void

_stack = []


def push(x) -> void:
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x


def clear() -> void:
    _stack.clear()


def is_empty() -> bool:
    return len(_stack) == 0

