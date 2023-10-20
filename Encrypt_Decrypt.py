
from characterDict import char_dict

class Encrypt:

    def __init__(self, Message, key) -> None:
        """
        Encrypt class constructor
        message -> String to be Encrypted
        key -> Encryption key {Required for Encryption}
        """
        self.text = Message
        self.KEY = key
        self.char_dict = char_dict
        self.encryptedMessage = self.get_encrypted()

    def convert_message_to_integers(self) -> str:
        '''
        converts provided string to int values
        according to the word_dict with '|' as letter seperator
        and _ as word seperator
        eg- ab cd -> 1|2_3|4|
        '''
        list_int = []
        for word in self.text:
            # -------------------------------------------------------
            for letter in word:  # |-> converting string's letter to int
                list_int.append(f"|{self.char_dict[letter]}")  # |-
            # --------------------------------------------------------
        list_int[len(list_int) - 1] += "|"  # ---- adding a pipe after last character of every word

        return "".join(list_int)

    def get_encrypted(self) -> str:
        '''
        returns encrypted string from int string
        eg- ab cd -> 1|2_3|4| ->_1|1|2|3_2|3|4|6
        here if KEY = 13
        13*1 = 13
        so 1 at first 3 at last of int string
        13*2 = 26
        so 2 at first 6 at last of int string
        '''
        messageIntegers = self.convert_message_to_integers()
        list_enc = []
        for m,i in enumerate(messageIntegers.split("_")):
            phrase = str(self.KEY * (m+1))
            list_enc.append(f"{phrase[0]}{i}{phrase[1]}")

        enc_text = str("")
        for text in list_enc:
            enc_text += f"_{text}"  # list to string conversion with _ as word seperator
        return enc_text

    def get_decrypted(_text):
        """
        get_decrypted function that decrypts the encrypted text using the key,
        The key is the first and last letter of the word. and you could find the key from the encrypted text, first and last letter of the word,
        So , just pick the first word, get the key, and decrypt the rest of the words.
        The Key in the Encrypt Class is not taking any part of the encryption, it is just a random number.
        """
        # get the count of words in the encrypted text
        wordsList = _text.replace("_", " ").strip().split(" ")
        decrypted_text = ""

        # loop through the words and decrypt them
        for word in wordsList:
            # get the key from the encrypted word
            key = word[0] + word[-1]
            word = word[1:-1]

            # decrypt the word
            decrypted_word = ""
            lettersList = word.replace("|", " ").strip().split()
            for letter in lettersList:
                if letter != "":
                    decrypted_word += "".join([k for k, v in char_dict.items() if str(v) == letter])
            decrypted_text += decrypted_word + " "
        return decrypted_text



class Decrypt:

    def __init__(self, encryptedMessage) -> None:
        # TODO: add decrypt function that decrypts the encrypted text using the key
        self.encryptedMessage = encryptedMessage
        self.KEY = self.get_key()
        self.char_dict = char_dict


    def get_key(self):
        # get the key from the encrypted text
        wordsList = self.encryptedMessage.replace("_", " ").strip().split(" ")
        key = wordsList[0][0] + wordsList[0][-1]
        return int(key)
    def get_decrypted(self) -> int:
        # get the count of words in the encrypted text
        wordsList = self.encryptedMessage.replace("_"," ").strip().split(" ")
        decrypted_text = ""

        # loop through the words and decrypt them
        for word in wordsList:
            # strip the key from the encrypted word
            key = word[0] + word[-1]
            word = word[1:-1]

            # decrypt the word
            decrypted_word = ""
            lettersList = word.replace("|"," ").strip().split()
            for letter in lettersList:
                if letter != "":
                    decrypted_word += "".join([k for k,v in self.char_dict.items() if str(v) == letter])
            decrypted_text += decrypted_word + " "
        return decrypted_text








