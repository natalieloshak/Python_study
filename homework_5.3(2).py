import string


def to_hashtag(text):
    clean_text = "".join(
        char if char not in string.punctuation else " " for char in text
    )
    words = clean_text.split()

    hashtag = "#" + "".join(word.capitalize() for word in words)

    return hashtag[:140]


user_input = input()
print(to_hashtag(user_input))
