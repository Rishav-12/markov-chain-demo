# TODO: Write down a detailed step-by-step on how this works

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

# Text our chain will be based off of
#txt = "Computer programming is the process of performing a particular computation (or more generally, accomplishing a specific computing result), usually by designing and building an executable computer program. Programming involves tasks such as analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms (usually in a chosen programming language, commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus usually requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic."

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
