from typing import Sequence
def phonemes_to_words(words: Sequence[str], phoneme_list: Sequence[str]):
    # Find all possible combinations of words that can be formed using the given list of phonemes.

    # Args:
    #     words: A sequence of words and their corresponding phonemes.
    #     phoneme_list: A sequence of phonemes.

    # Returns:
    #     A list of word combinations formed using the provided phonemes.

    combinations_words = []
    temp_phone = phoneme_list[:]

# Iterate first loop to look for first elements
# eliminate used phoneme for first element
# Save the remaining phoneme for later
    for i in words:
        if all(element in temp_phone for element in i[1]):
            for phone in i[1]:
                temp_phone.remove(phone)
            remaining_phone = temp_phone[:]

# Iterate second loop to find matching combination with 1st element 'i'
# Create array that going to store combination
# Store 1st element 'i' and start looking for next element and repeat

# After found all possible element initialize reamining phoneme (A phonemes without first elemet phonemes)
# Initilize temporary phonemes and move on to next 1st element

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


def find_possible_words(phonemes: Sequence[str]):
    # Find all possible words that can be formed using the given sequence of phonemes.

    # Args:
    #     phonemes: A sequence of phonemes.

    # Returns:
    #     A list of words that can be formed using the provided phonemes.
    
    with open('dictionary.csv', 'r+') as datasheet:
        words = []
        pos_words = []
        list_phone = []
        for line in datasheet:
            split = line.split(',')
            split[-1] = split[-1].replace('\n','')
            words.append(split)
        for word in words:
            list_phone = word[1 :]
            if all(element in phonemes for element in list_phone):
                pos_words.append([word[0], list_phone])
        return pos_words
# Example usage
phoneme_list = ["DH", "EH1", "R", "DH", "EH1", "R"]
pos_words = find_possible_words(phoneme_list)
words = phonemes_to_words(pos_words, phoneme_list)
print(words)
