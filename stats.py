def num_words(string):
    sentence = string.split()
    count = len(sentence)
    print(f"Found {count} total words")

def char_count(string):
    my_dict = {}
    sentence = string.lower()
    sentence = sentence.split()
    for word in sentence:
        for char in word:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
    return my_dict

def sort_on(my_dict):
    desc = sorted(my_dict.items(), key=lambda k: k[1], reverse=True)
    for k, v in desc:
        print(f"{k}: {v}")
    
