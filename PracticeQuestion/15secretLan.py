def encode(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch == "x" or ch == "y" or ch == "z":
                result += ch
            else:
                result += chr(ord(ch) + 3)
        else:
            result += ch

    return result


def decode(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch == "x" or ch == "y" or ch == "z":
                result += ch
            else:
                result += chr(ord(ch) - 3)
        else:
            result += ch

    return result


message = input("Enter your message: ")

secret = encode(message)
print("Secret code:", secret)

original = decode(secret)
print("Decoded message:", original)

# print(ord("a"))
# print(chr(97))