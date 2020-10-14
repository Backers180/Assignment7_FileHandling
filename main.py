text = open("my_second_file.txt", "r")
paragraph = [text.read()]
text.close()

words = paragraph[0].split()

thecount = 0

for x in words:
  if x == "The" or x == "the":
    thecount += 1

print("The word 'the' appears in this paragraph %d times" % thecount)
