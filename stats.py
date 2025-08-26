def sort_on(items):
    return items["num"]

def word_count(document):
    total =0
    for word in document.split():
        total += 1
    return total

def char_count_per_letter(document):
    char_count = {}
    for c in document.lower():
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sorted_characters(letter_dict):
    letter_num_list = []
    #letter_dict.sort(reverse=True, key=sort_on)
    for letter, count in letter_dict.items():
        if not letter.isalpha():
            continue
        new_dict = {"letter": letter, "num": count}
        letter_num_list.append(new_dict)
    letter_num_list.sort(reverse=True, key=sort_on)
    return letter_num_list
