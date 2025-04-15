<think>
Okay, I need to write a Python script that counts words, sentences, and characters in a given text. Let's think about how to approach each part.

First, for the character count. That seems straightforward—just take the length of the text. So len(text) would give the number of characters including spaces. Wait, does the task count spaces as characters? Usually, yes, because in programming terms, len() includes all characters. So that's easy.

Next, words. How to count words? Splitting the text into words using split() method. But wait, split by default splits on any whitespace, which includes spaces, newlines, etc. So that's okay. But what about punctuation? Like, if a word has a period or comma attached, would that count as part of the word? The problem says to count words, so maybe we should split on whitespace and consider punctuation as part of the words. Unless specified otherwise, but since the user didn't mention removing punctuation, I think the standard split() is okay. So words = len(text.split())

Then sentences. Sentences usually end with . ! or ?. So we can count the number of occurrences of these punctuation marks. But need to be careful about things like Mr. or Dr. where the period is part of an abbreviation. Hmm, but the problem might expect a simple approach. So maybe count each occurrence of . ! ? in the text. But also, maybe some sentences end with other punctuation? Or maybe just consider each occurrence of those three as sentence terminators. So sentences = sum(1 for c in text if c in ['.', '!', '?']) ?

Alternatively, split the text into sentences. But splitting on .!?, but that might not be accurate. Alternatively, iterate through each character and count when one of those appears. So sentences would be the sum of each occurrence of those characters.

Wait, but maybe some sentences end with multiple punctuation, like "Wow!!!" or "Hmm...". In such cases, each exclamation point would be counted, but perhaps that's overcounting. However, without more complex rules, the simplest way is to count each occurrence of . ! ? as a sentence end. So that's probably what the problem expects.

Putting it all together:

The code structure would be:

def count_text(text):
    words = len(text.split())
    sentences = sum(1 for c in text if c in {'.', '!', '?'})
    characters = len(text)
    return words, sentences, characters

Wait but the problem says to write a Python script. So maybe not a function but a script that reads input. Wait, the user says "given text"—but how is the text provided? The problem isn't clear. Maybe the user expects the script to take input from the user via input(), or maybe from a variable?

Probably, since it's a script, perhaps the text is provided via command-line input, but the question doesn't specify. Alternatively, the code might be written to process a given text variable. Wait, the problem says "given text"—maybe the user expects to have a variable with the text, and the code will process that. The user might have provided the code in a way that expects the text to be input, but since the problem doesn't specify, perhaps the code should read from standard input?

Alternatively, perhaps the code is written in a way that takes a text variable, but since the task says "given text" but doesn't specify how, maybe the code uses input() to get the text.

Wait, the problem says "Write a Python script that counts...", so the script needs to read the text from somewhere. The most straightforward way is to read from standard input. So:

text = input().strip()

But maybe the user expects the code to process a variable. Hmm, but the problem isn't clear. Since the user wants code only, perhaps the code uses a function that takes the text as input, but the problem says "given text"—maybe the code should read from stdin.

Alternatively, maybe the code is written as a function, but the problem says "script", so perhaps the code should read text from the user. Let me think of the code as:

text = input("Enter text: ")
words = len(text.split())
sentences = text.count('.') + text.count('!') + text.count('?')
characters = len(text)
print(f"Words: {words}, Sentences: {sentences}, Characters: {characters}")

Wait, but the problem says to return only the code. But the output should be the counts. However, the user says "return only the code"—so the code should output the numbers? Or perhaps the code is supposed to print them?

Wait the problem says:

Task: Write a Python script that counts the number of words, sentences, and characters in a given text. The output is to return only the code.

Hmm, perhaps the code should read the text from input, compute the three counts, and print them. So the code should be:

text = input().strip()
words = len(text.split())
sentences = sum(1 for c in text if c in '.!?')
characters = len(text)
print(f"Words: {words}, Sentences: {sentences}, Characters: {characters}")

But maybe the sentences count is better done via counting each occurrence of the punctuation. The code above uses a generator expression that counts each occurrence of any of the characters in '.!?'. Wait, the in operator for a string is per character. So for each character in text, if it's in the string '.!?'. So that's correct. Alternatively, using text.count('.') + text.count('!') + text.count('?') could be another way. Both would work.

Alternatively, the first approach is better because it's more concise.

Wait, but in the first approach, sentences = sum(1 for c in text if c in '.!?'), that counts every occurrence of those characters. So if a sentence ends with "Hello! How?", that would count two sentences. But in "Hello... ?", that would count 3 periods and 1 question mark, leading to 4 sentences, which might be incorrect. But perhaps the problem expects that as the method.

Alternatively, maybe splitting on those punctuation, but that's more complex. Since the problem says "a simple script", perhaps the intended approach is to count each occurrence of . ! ? as a sentence. So that's acceptable.

So the code would be:

text = input().strip()

words = len(text.split())
sentences = sum(1 for c in text if c in '.!?')
chars = len(text)

print(f"Words: {words}, Sentences: {sentences}, Characters: {chars}")

Wait, but the user wants the code without explanations or comments. So the code should be written as:

text = input().strip()
words = len(text.split())
sentences = sum(1 for c in text if c in '.!?')
characters = len(text)
print(f"Words: {words}, Sentences: {sentences}, Characters: {characters}")

But maybe the sentences count is wrong when the punctuation is not at the end. Like in "What's up? He asked." The sentences would be 2, which is correct. So this approach works in that case.

Alternatively, if the text starts with a punctuation, like ".test", it would count the '.' as a sentence, which is incorrect. But perhaps the problem expects that approach.

Alternatively, maybe the user expects sentences to be split by the punctuation followed by space or end of line. But that's more complex.

The problem says "write a Python script that counts...", so perhaps the simplest approach is acceptable.

Alternatively, maybe the sentences should be split by splitting the text on any of the punctuation marks, then counting the non-empty splits. But that might be better.

Wait, like:

sentences = len(re.split(r'[.!?]+', text)) -1 ?

But that requires importing re. The problem didn't mention using regular expressions, but perhaps it's okay.

Wait, but the user wants clean code without explanations. Let me think again.

The problem says "given text"—maybe the text is passed as a variable, but the code must be a script. So perhaps the code is written as:

text = input()
words = len(text.split())
sentences = text.count('.') + text.count('!') + text.count('?')
print(f"Words: {words}, Sentences: {sentences}, Characters: {len(text)}")

But perhaps the sentences could be done with the sum over the count of each punctuation.

Alternatively, maybe the code should read from stdin and output the counts. The user's output says to return only the code. So the code should be the entire script.

Wait, but the problem says "given text"—maybe the code should process a variable, but since it's a script, perhaps the code is written to take input via input().

Hmm, but maybe the user expects the code to process a variable. But since it's a script, probably the code uses input().

Alternatively, perhaps the code is written in a way that takes a string and returns the counts, but the problem says "script", so it must be a standalone script.

Putting it all together, the code could be:

text = input().strip()
words = len(text.split())
sentences = sum(1 for c in text if c in '.!?')
characters = len(text)
print(f"Words: {words}, Sentences: {sentences}, Characters: {characters}")

Wait, but the user wants the code to return the counts. But the problem says "output: write a Python script that counts...", so the script should print the results.

Alternatively, maybe the code should compute and print all three values.

I think this is the correct approach. Thus, the code is as above.

Another possible issue: the sentences count might include punctuation within the text, like in abbreviations. For example, "Mr. Smith works at U.S.A." would have three periods, leading to three sentences, but actually, it's one sentence. But perhaps the problem does not require handling such cases, so the code is acceptable.

Therefore, the code should be as above.