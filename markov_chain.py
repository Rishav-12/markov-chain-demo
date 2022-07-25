import random

# Text our chain will be based off of
txt = "Computer programming is the process of performing a particular computation (or more generally, accomplishing a specific computing result), usually by designing and building an executable computer program. Programming involves tasks such as analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms (usually in a chosen programming language, commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus usually requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic."

order = 4
ngrams = {}

for i in range(0, len(txt) - order + 1):
    gram = txt[i:i + order]
    if not gram in ngrams:
        ngrams[gram] = []
    if i + order >= len(txt):
        break
    ngrams[gram].append(txt[i + order])

# `ngrams` has all the ngrams and the possible next letters in the form of a table

current_gram = txt[0:order]
result = current_gram

# 200 is the length of the generated text
for i in range(200):
    if current_gram not in ngrams:
        break
    p = ngrams[current_gram]
    next_letter = random.choice(p)
    result += next_letter
    current_gram = result[len(result) - order:len(result)]

print(result)
