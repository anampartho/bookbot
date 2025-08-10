def get_word_count(text):
    words = text.split()
    return len(words)

def sorted_char_count(char_count):
    return dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

def get_char_count(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in char_count:
                char_count[lower_char] += 1
            else:
                char_count[lower_char] = 1
    return char_count

def get_stats(text, book_name):
    num_words = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_char_count_dict = sorted_char_count(get_char_count(text))
    for char, count in sorted_char_count_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")
