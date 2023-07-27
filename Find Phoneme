from typing import Sequence

#Purpose: Find all possible combinations of words that can be formed using the given list of phonemes.
#Logic: Iterate possible words list and set words[i] as a primary of the first list, iterate second for loop to look for rest of the phoneme
#       if all phoneme_list is used and no more phoneme to put in, jump to next word[i]
# Args:
#     words: A sequence of words and their corresponding phonemes.
#     phoneme_list: A sequence of phonemes.
# Returns:
#     A list of word combinations formed using the provided phonemes.
def phonemes_to_words(words: Sequence[str], phoneme_list: Sequence[str]):
    combinations_words = []
    temp_phone = phoneme_list[:]
    array = []
    for i in words:
        if all(element in temp_phone for element in i[1]):
            for phone in i[1]:
                if phone in temp_phone:
                    temp_phone.remove(phone)
            remaining_phone = temp_phone[:]
            for y in words:
                if all(element in remaining_phone for element in y[1]):
                    array.append(y[0])
                    for phone in remaining_phone:
                        if phone in remaining_phone:
                            remaining_phone.remove(phone)
                else:
                    array.insert(0, i[0])
                    combinations_words.append(array)
                    remaining_phone = temp_phone[:]
                    array = []
                    
            temp_phone = phoneme_list[:]
    return combinations_words

# Purpose: Find all possible words that can be formed using the given sequence of phonemes.
#Logic: Open the dataset aka 'dictionary.csv' and remove all unnecessary elements such as     '\n', ' '...
#       keep all phonemes that contain phoneme we have
# Args:
#     phonemes: A sequence of phonemes.
# Returns:
#     A list of words that can be formed using the provided phonemes.
def find_possible_words(phonemes: Sequence[str]):
    with open('dictionary.csv', 'r') as datasheet:
        words = []
        pos_words = []
        list_phone = []
        for line in datasheet:
            split = line.split(',')
            split[-1] = split[-1].strip()
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
