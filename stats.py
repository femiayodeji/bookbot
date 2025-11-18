def count_words(text):
    words = text.split()
    return len(words)    

def count_characters(text):
    data = {}
    for char in text.lower():
        if char in data:
            data[char] += 1
        else:
            data[char] = 1
    return data

def sort_on(items):
    return items["num"]

def sort_list(data):
    characters = []
    for char, count in data.items():
        if not char.isalpha():
            continue
        characters.append({"char": char, "num": count})
    
    characters.sort(key=sort_on, reverse=True)
    return characters