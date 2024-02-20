# Practical Task 2
# saved a sentence as a string and output it a few different ways

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence = sentence.replace('!', ' ')
print("sentence.replace('!', ' ')): {}".format(sentence))

sentence = sentence.upper()
print(f"sentence.upper(): {sentence}")

print(sentence[::-1])