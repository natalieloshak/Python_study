import string
import keyword


def is_valid_variable_name(name):
    if not name:
        return False

    if name in keyword.kwlist:
        return False

    if name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    allowed_chars = string.ascii_lowercase + string.digits + "_"
    if any(char not in allowed_chars for char in name):
        return False

    if set(name) == {"_"}:
        return len(name) == 1

    return True


user_input = input()
print(is_valid_variable_name(user_input))
