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