import random
import string

# Normal alphabet
alphabet = string.ascii_lowercase

# Create a random alphabet
secret_alphabet = list(alphabet)
random.shuffle(secret_alphabet)

# Create encoding dictionary
encode_dict = {}

for i in range(len(alphabet)):
    encode_dict[alphabet[i]] = secret_alphabet[i]

# Create decoding dictionary
decode_dict = {}

for key, value in encode_dict.items():
    decode_dict[value] = key


def encode(text):
    result = ""

    for ch in text:
        if ch in encode_dict:
            result += encode_dict[ch]
        else:
            result += ch

    return result


def decode(text):
    result = ""

    for ch in text:
        if ch in decode_dict:
            result += decode_dict[ch]
        else:
            result += ch

    return result


message = input("Enter your message: ")

secret = encode(message)
print("Secret code:", secret)

original = decode(secret)
print("Decoded message:", original)
