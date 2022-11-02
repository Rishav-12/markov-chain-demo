# markov-chain-demo

This is heavily based on Daniel Shiffman's [YouTube video](https://youtu.be/eGFJ8vugIWA).

The contents of the text files here is taken from the [Corpora project](https://github.com/dariusk/corpora).

## How the algorithm works

Our goal is to create new text randomly, in the style of a body of text already available.

- Obtain a body of text (read it in from a file).
- Build up a dictionary with every ngram as the keys, and a list of every possible character which can follow it as the values
	- Loop through the text.
	- Look at every set of n characters (ngram).
	- Add the next character to the list corresponding to that ngram.
- Choose a random starting ngram from the text, this is our current gram. Also set it as the result string.
- Build up the result string of length k by looping k times
	- Look up the current gram from the dictionary.
	- Pick a random character from the possibilities in the list.
	- Add the character to the result.
	- Reset the current gram to the last 3 characters of the result.

## Sample text

- Sample text files are in the `files` directory. Functions to load these files are provided in the code.
- If you want to have your own text, you can either put it in a separate file (and write a function to load it in) or directly in the code.
