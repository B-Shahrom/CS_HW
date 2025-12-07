text = input("Text: ")

letters = 0
words = 1
sentences = 0

for c in text:
    if c.isalpha():
        letters += 1
    if c == " ":
        words += 1
    if c == "." or c == "?" or c == "!":
        sentences += 1

L = letters * 100 / words
S = sentences * 100 / words

index = 0.0588 * L - 0.296 * S - 15.8
index = round(index)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
