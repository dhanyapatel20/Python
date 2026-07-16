def match_word(words):
  ctr=0
  lst=[]
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
      lst.append(word)
  print(" list of words that start and end with first and last charecter same\n",lst)
  return ctr

count=match_word(["dad","omm","zyx","1243"])
print("numder of words hvehaving first and last charecters same:",count)

