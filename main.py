inp = input("message to be encrypted:\n ->")
KEY = 13

class Encrypt:

    def __init__(self,Message,key) -> None:
        """
        Ecrypt class constructor
        message -> String to be Encrypted
        key -> Ecryption key {Required for Encryption}
        """
        self.text = Message
        self.KEY = key
        self.word_dict = {"a":1,
                        "b":2,
                        "c":3,
                        "d":4,
                        "e":5,
                        "f":6,
                        "g":7,
                        "h":8,
                        "i":9,
                        "j":10,
                        "k":11,
                        "l":12,
                        "m":13,
                        "n":14,
                        "o":15,
                        "p":16,
                        "q":17,
                        "r":18,
                        "s":19,
                        "t":20,
                        "u":21,
                        "v":22,
                        "w":23,
                        "x":24,
                        "y":25,
                        "z":26,
                        " ":"_",
                        "!":27,
                        "@":28,
                        "#":29,
                        "$":30,
                        "%":31,
                        "^":32,
                        "&":33,
                        "*":34,
                        "(":35,
                        ")":36,
                        "_":37,
                        "+":38,
                        "-":39,
                        "/":40,
                        "?":41,
                        ">":42,
                        "<":43,
                        ",":44,
                        ".":45,
                        "`":46,
                        "~":47,
                        "|":48,
                        "{":49,
                        "}":50,
                        "[":51,
                        "]":52,
                        "1":53,
                        "2":54,
                        "3":55,
                        "4":56,
                        "5":57,
                        "6":58,
                        "7":59,
                        "8":60,
                        "9":61,
                        "0":62,
                        "A":63,
                        "B":64,
                        "C":65,
                        "D":66,
                        "E":67,
                        "F":68,
                        "G":69,
                        "H":70,
                        "I":71,
                        "J":72,
                        "K":73,
                        "L":74,
                        "M":75,
                        "N":76,
                        "O":77,
                        "P":78,
                        "Q":79,
                        "R":80,
                        "S":81,
                        "T":82,
                        "U":83,
                        "V":84,
                        "W":85,
                        "X":86,
                        "Y":87,
                        "Z":88,
                        ":":89,
                        ";":90
                        }
        self.int_text=self.convert_int()


    def convert_int(self)->str:
        '''
        converts provided string to int values 
        according to the word_dict with '|' as letter seperator 
        and _ as word seperator
        eg- ab cd -> 1|2_3|4|
        '''
        list_int = []
        for word in self.text:
        # -------------------------------------------------------
            for letter in word:                                # |-> conveting string's letter to int
                list_int.append(f"|{self.word_dict[letter]}")  # |-
        #-------------------------------------------------------- 
        list_int[len(list_int)-1]+="|" # ---- adding a pipe at lats of every word
        
        int_text = str("")
        for i in list_int:
            int_text = int_text + i #-----list to string conversion
        return int_text
    
    def get_encrypted(self) ->str:
        '''
        returns encryprted string from int string
        eg- ab cd -> 1|2_3|4| ->_1|1|2|3_2|3|4|6
        here if KEY = 13
        13*1 = 13
        so 1 at first 3 at last of int string
        13*2 = 26
        so 2 at first 6 at last of int string
        '''
        m = 1
        list_enc = []
        for i in self.int_text.split("_"):
            phrase = str(self.KEY*m)
            m += 1
            list_enc.append(f"{phrase[0]}{i}{phrase[1]}")
        
        enc_text = str("")
        for text in list_enc:
            enc_text += f"_{text}"# list to string conversion with _ as word seperator
        return enc_text

enc = Encrypt(inp,KEY)
Encrypted = enc.get_encrypted()
print(f"\nencryted text Is\n-> {Encrypted} ")

class Decrypt:
    def __init__(self,message,key,dct) -> None:
        '''
        decrypt class constructor
        message -> String to be Decrypted
        key -> Ecryption key {Required for decryption}
        '''
        self.KEY = key
        self.text = message
        self.word_dict=self.reverse_dict(dct)
        self.list_dec=self.remove()
    
    def remove(self) -> list:
        '''
        removes all the encrypted data and returns a int_text
        eg if KEY = 13
        _1|2|3_2|5|6 -> ['|2|','|5|']
        '''
        m=0
        list_dec = []

        for i in self.text.split("_"):
            phrase = str(self.KEY*m)
            m += 1
            if len(i) != 0 and i[0]+i[len(i)-1] == phrase[0]+phrase[1]:# removing all the encrypted data
                a=i.removeprefix(phrase[0])
                b=a.removesuffix(phrase[1])
                list_dec.append(b)
        return list_dec
    
    def get_decrypted(self)->str:
        """
        int_string{list_dec} to normal string conversion
        eg ["|1|","|5|"] -> b e 
        """
        lst_let=[]
        for wrd in self.list_dec:
            for let in wrd.split("|"):
                if let.isdecimal():
                    lst_let.append(f"{self.word_dict[int(let)]}")
            lst_let.append(" ")
        dec_word=""
        for i in lst_let:
            dec_word+=i
        return dec_word
    
    def reverse_dict(self,input_dict):
        reversed_dict = {}
        for key, value in input_dict.items():
            reversed_dict[value] = key
        return reversed_dict

dec = Decrypt(Encrypted,KEY,enc.word_dict)
dec_word=dec.get_decrypted()
print(f"\n the decrypted message is \n ->{dec_word}")