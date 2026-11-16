

def find_word_count(text):
    text = str(text).lower()
    split_text = text.split()
    length = len(split_text)
    return length


def find_char_count(text):
    words = {}
    text = str(text).lower()
    split_text = text.split()
    for word in split_text:
        for char in word:
            if char in words:
                words[char] += 1
            else:
                words[char] = 1
    sorted_words = dict(sorted(words.items()))
    return sorted_words

