import ds.stack.A_stack


def check_braces_sequence(s: str) -> bool:
    """
    Проверяет коррекность скобочной последовательности
    из круглых и квадратных скобок () []

    check_braces_sequence("(([()]))[]")
    True
    check_braces_sequence("(]")
    False
    check_braces_sequence("(")
    False
    check_braces_sequence("]")
    False
    :param s: str
    :return: bool
    """
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            ds.stack.A_stack.push(brace)
        else:
            assert brace in ")]", "Ожидалась закрывающая но там: " + str(brace)
            if ds.stack.A_stack.is_empty():
                return False
            left = ds.stack.A_stack.pop()
            right = ""
            assert left in "([", "Ожидалась открывающая но там: " + str(left)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    if ds.stack.A_stack.is_empty():
        return True
    else:
        return False





