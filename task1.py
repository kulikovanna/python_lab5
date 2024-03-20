import re

def is_valid_email(email):
    email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
    if email_pattern.match(email):
        return True
    else:
        return False

def validate_email(email):
    if not is_valid_email(email):
        raise ValueError("Некорректный адрес электронной почты: {}".format(email))
    else:
        return email

def main():
    email = input("Введите адрес электронной почты: ")
    try:
        validated_email = validate_email(email)
        print("Введенный адрес электронной почты {} корректен.".format(validated_email))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
