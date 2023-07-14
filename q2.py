from nltk.corpus import cmudict
from typing import Sequence
import nltk

# Load the CMU Pronouncing Dictionary
nltk.download('cmudict')

# Initialize the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

# Function to Find all possible combination with list of phoneme
def phonemes_to_words(words:Sequence[str], phoneme_list:Sequence[str]):
    #Initialize and copy variables we need
    combinations_words = []
    temp_phone = phoneme_list[:]
    #Iterate first loop to look for first element
    #eliminate used phoneme for first element
    #Save the remaining phoneme for later
    for i in words:
        if all(element in temp_phone for element in i[1]):
            for phone in i[1]:
                temp_phone.remove(phone)
            remaining_phone = temp_phone[:]
            #Iterate second loop to find matching combination with 1st element 'i'
            #Create array that going to store combination
            #Store 1st element 'i' and start looking for next element and repeat
            
            #After found all possible element initialize reamining phoneme (A phonemes without first elemet phonemes)
            #Initilize temporary phonemes and move on to next 1st element
            for y in words:
                array = []
                array.append(i[0])
                if i != y and all(element in remaining_phone for element in y[1]):
                    array.append(y[0])
                    for phone in remaining_phone:
                        remaining_phone.remove(phone)
                    combinations_words.append(array)    
                    remaining_phone = temp_phone[:]
            temp_phone = phoneme_list[:]
    return combinations_words

# Function to Find all possible words with Phoneme
def find_possible_words(phonemes:Sequence[str]):
    words = []
    for word, pronunciations in pronouncing_dict.items():
        for pronounce in pronunciations:
            if all(element in phonemes for element in pronounce):
                words.append([word, pronounce])
    return words
# Example usage
phoneme_list = ["DH", "EH1", "R", "DH", "EH1", "R"]
pos_words = find_possible_words(phoneme_list)
words = phonemes_to_words(pos_words, phoneme_list)
print(words)
