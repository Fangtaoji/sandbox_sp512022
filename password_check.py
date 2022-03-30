def is_password(text):
    return 8 <= len(text) <= 20


def main():
    new_password = "hollowed"
    print("{} is valid password".format(new_password))


if __name__ == '__main__':
    main()
