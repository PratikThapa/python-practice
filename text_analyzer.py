#Declaring variables to hold analysis result
Total_Word_Count = 0
Total_Chars_Count = 0
Char_No_Spaces= 0
frequency_of_letter = {}
Common_Word = ""
Common_Word_Count = 0
Palindrome = []
Word_Length = 0

#Prompt the user for input
Dummy_text = input("Please enter the desired text to be analyzed: ")


def text_analyzer(Dummy_text):
  global Total_Word_Count, Total_Chars_Count, Char_No_Spaces, frequency_of_letter, Palindrome, Total_Word_Length
    
# Total Word Count in Text
word_count = Dummy_text.split()
Total_Word_Count = len(word_count)
print("Total Word Count in " + Dummy_text + " is " + str(Total_Word_Count))

# Total Characters in Text
Total_Chars_Count = len(Dummy_text)
print("Total Character Count in " + Dummy_text + " is " + str(Total_Chars_Count))
Char_No_Spaces = len(Dummy_text.replace(" "," "))
print("Total Character Count with no spaces " + Dummy_text + " is " + str(Char_No_Spaces))

# Frequency of each letter in text
frequency_of_letter = {}
for character in Dummy_text: 
  if character.isalpha():
    frequency_of_letter[character.lower()] = frequency_of_letter.get(character.lower(), 0) + 1
print("Frequency of each letter in " + Dummy_text + " is " + str(frequency_of_letter))

# Most common word and count in text
frequent_words = {}
for common_word in Dummy_text.split():
  frequent_words[common_word.lower()] = frequent_words.get(common_word.lower(), 0) + 1
Common_Word = max(frequent_words, key=frequent_words.get)
Common_Word_Count = frequent_words[Common_Word]
print("Most Common Word in " + Dummy_text + " is " + str(frequent_words))

# To check whether the words are palindrome or not in text
for word in Dummy_text:
  if word.lower() == word[::-1].lower():
    Palindrome.append(word)
if Palindrome:
  print("Palindormes in given text " + Dummy_text + " is " + str(Palindrome))
else:
  print("There are no palindromes in given " + Dummy_text)

# To calculate the average word length in text
Total_Characters = sum(len(word)for word in Dummy_text)
Word_Length = Total_Characters/ Total_Word_Count
print("Total Word Length in " + Dummy_text + " is " + str(Word_Length))

text_analyzer(Dummy_text)

  

    

    

