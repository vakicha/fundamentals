def length_check(password):
    if len(password) < 6 or len(password) > 10:
        list_of_def.append("Password must be between 6 and 10 characters")
        return False
    return True


def letters_digit_check(password):
    if not password.isalnum():
        list_of_def.append("Password must consist only of letters and digits")
        return False
    return True


def min_two_digit_check(password):
    digit_count = 0
    for character in password:
        if character.isdigit():
            digit_count += 1
    if digit_count < 2:
        list_of_def.append("Password must have at least 2 digits")
        return False
    return True


def validation_password(def1, def2, def3):
    if def1 and def2 and def3:
        return print("Password is valid")
    return print("\n".join(list_of_def))


input_password = input()
list_of_def = []
validation_password(length_check(input_password), letters_digit_check(input_password),
                    min_two_digit_check(input_password))
