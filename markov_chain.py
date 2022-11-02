import random

def load_shakespeare():
    with open("files/shakespeare_sonnets.txt", 'r') as textfile:
        txt_list = textfile.readlines()

    return " ".join(txt_list).replace("\n", "")

def load_oprah():
    with open("files/oprah_quotes.txt", 'r') as textfile:
        txt_list = textfile.readlines()

    return " ".join(txt_list).replace("\n", "").replace("\x00", "").replace("\x19", "")

def load_subjects():
    with open("files/subjects.txt", 'r') as textfile:
        txt_list = textfile.readlines()

    return " ".join(txt_list).replace("\n", "").replace("\x00", "")


txt = load_shakespeare()
order = 4
ngrams = {}

# `ngrams` will have all the ngrams as keys and the possible next letters in a list as values

for i in range(0, len(txt) - order + 1):
    gram = txt[i:i + order]
    if not gram in ngrams:
        ngrams[gram] = []
    if i + order >= len(txt):
        break
    ngrams[gram].append(txt[i + order])

# Choose a random starting point to generate new text
start_index = random.randint(0, len(txt) - 1)
current_gram = txt[start_index:start_index + order]
result = current_gram

gen_text_len = 200 # length of the generated text
for i in range(gen_text_len):
    if current_gram not in ngrams:
        break
    p = ngrams[current_gram]
    next_letter = random.choice(p)
    result += next_letter
    current_gram = result[len(result) - order:len(result)]

print(result)
