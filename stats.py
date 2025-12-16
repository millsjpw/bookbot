def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_count = {}
    for char in text:
        if not char.isalpha():
            continue
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_char_counts(char_counts):
    sorted = [{"char": char, "num": num} for char, num in char_counts.items()]
    sorted.sort(key=sort_on, reverse=True)
    return sorted
    