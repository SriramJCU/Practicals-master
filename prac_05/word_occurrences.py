WORD_TO_COUNT = {}

Text = input("Text: ").split(" ")
for word in Text:
    if word not in WORD_TO_COUNT:
        WORD_TO_COUNT[word] = Text.count(word)

sorted_keys = sorted(WORD_TO_COUNT)
for key in sorted_keys:
    print(f"{key:10} : {WORD_TO_COUNT[key]}")