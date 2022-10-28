# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

draculaText = readBook()

# Split the words in the draculaText variable so they can be counted
wordList = draculaText.split()

# Create an empty list so that each 4 letter word can be added
fourLetterWords = []

# Create an empty dictionary so that all words can be added
draculaDict = { }

# Create an empty variable to hold the count number
count = 0

# Create an empty variable to store a text value
mostOften = ""

# Create a for loop that loops through all the words in the wordList
for word in wordList:
  # Make sure each word is lower case
  word = word.lower()

  # If the word is NOT in the dictionary, add it
  if(word not in draculaDict):
    draculaDict[word] = 0

  # Count how many times the same word appears in the dictionary
  draculaDict[word] += 1
    
  # If the word is 4 letters long and NOT already in fourLetterWords list, add it
  if(len(word) == 4 and word not in fourLetterWords):
    fourLetterWords.append(word)

# Create a for loop to iterate through the dictionary
for key, value in draculaDict.items():
  
  # If the value is greater than count, make count the new value mostOften the key
  if value > count:
    count = value
    mostOften = key

# Display the 'Results' header
print("==== Results ====")
print()

# Display the word that appears the most
print(f"'{mostOften}' is the word that appears the most throughout the text")
print(f"a total of {count} times")
print()

# Display the number of 4 letter words in the book
print(f"There are {len(fourLetterWords)} words that are four letters long")
print()

# Display the numbers of word that showed up 500 times or more
print("I noticed that these words show up 500 or more times:")
print()
for key, value in draculaDict.items():
  if(value >= 500):
    print(f"{key} - {value}")
