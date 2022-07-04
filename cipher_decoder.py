""" message decoder
Take a key and message, which represent a cipher key 
and a secret message. Use the first appearance of all 26 lowercase 
English letters in key as the order of the substitution table.
Then, Align the substitution table with the alphabet.
Each letter in message is then substituted using the table.

Constraints...

    26 <= key.length <= 2000
    key consists of lowercase English letters and ' '.
    key contains every letter in the English alphabet ('a' to 'z') at least once.
    1 <= message.length <= 2000
    message consists of lowercase English letters and ' '.

"""
import string

def decodeMessage(key: str, message: str) -> str:
    
    # remove whitespace
    key = key.replace(' ', '')

    # remove each duplicate character in the message
    # logic is if I didn't sequentially already add it 
    # to this new list, go ahead and add it   
    dedup_key = []
    for char in key:
        if char not in dedup_key:
            dedup_key.append(char)
#    return(dedup_key)

    # now write out the substitution using a dict
    sub_matrix = {}
    for i, j in zip(dedup_key, string.ascii_lowercase):
        sub_matrix[i]=j
    sub_matrix[' ']=' ' # there was no element in key for spaces
    return ''.join(sub_matrix[i] for i in message)




key = "the quick brown fox jumps over the lazy dog"
message = "vkbs s uepuv"

print(decodeMessage(key, message))

