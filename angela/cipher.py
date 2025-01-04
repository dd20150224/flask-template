alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
alphabet2 = alphabet * 2

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def find_index(text):
#     for index, string in alphabet:
#         if text in string:
#             return index
#     return -1


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)

        # target_index = (
        #     index + shift_amount if direction == "encode" else index - shift_amount
        # )

        cipher_text += alphabet[shifted_position]
    return cipher_text


print(f"output: {encrypt(text, shift if direction=='encode' else -shift)}")
