def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    data = {}
    for l in text:
        l_formatted = l.lower()
        if l_formatted not in data:
            data[l_formatted] = 0
        data[l_formatted] += 1
    return data

def sort_on(item):
    return item["num"]

def sort_characters_dictionary(dictionary):
    dict_list = []
    for i in dictionary:
        dict_list.append({"char": i, "num": dictionary[i]})

    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
