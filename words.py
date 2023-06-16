# def print_upper_words(words):
#     for word in words:
#         if word.lower().startswith("e"):
#             return word.upper()
#     return "no word starts with the letter E"


def print_upper_words(words, letters):
    for word in words:
        for letter in letters:
            if word.lower().startswith(letter.lower()):
                print(word.upper())

            # print(f"no word starts with the letter {letter}")

    # return "any word starts with any letter provided"


print(
    print_upper_words(
        [";lkjsfijipfwakhsf", "casa", "planta", "mitomania"], ["c", "b", "m"]
    )
)
