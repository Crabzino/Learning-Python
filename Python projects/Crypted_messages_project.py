coded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
coded_message2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
coded_message3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"   #offset 14
coded_message4 = "VW AOHS HVOBY MCI TCF HVS ASGGOUS HVWG WG AM CBS!"
coded_message5 = "VW AOHS HVOBY MCI TCF HVS ASGGOUS AOMO WG O GDM!"
coded_message_with_unknown_offset = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#THIS DECODES ANY MESSAGE WITH ANY OFFSET
def decode_message_offset(coded_message, offset_number):
    
    offset = offset_number % 26
    offset_alphabet = alphabet[-offset:] + alphabet[:-offset]

    
    coded_message_split = coded_message.split(" ")
    coded_message_strip1 = []
    for word in coded_message_split:
        coded_message_strip1.append(word.strip("!"))
    coded_message_strip2 = []
    for word in coded_message_strip1:
        coded_message_strip2.append(word.strip("."))
    coded_message_strip3 = []
    for item in coded_message_strip2:
        coded_message_strip3.append(item.strip("?"))

    decoded_words = []
    for word in coded_message_strip3:
        decoded_word = ""
        for letter in word:
            if letter.upper() in offset_alphabet:
                index = offset_alphabet.index(letter.upper())
                decoded_word += alphabet[index].lower()
            else:
                decoded_word += letter
        decoded_words.append(decoded_word)

    decoded_message = " ".join(decoded_words)
    return decoded_message

#print(decode_message_offset(coded_message = coded_message5, offset_number = 12))

#IF OFFSET IS UNKNOWN, USE BRUTE FORCE OR JUST PRINT OUT A STRING FOR EACH OFFSET LIKE THIS
#for i in range(26):
    #print(decode_message_offset(coded_message = coded_message_with_unknown_offset, offset_number = i))






#MY ENCRYPTER. THIS CODES MY MESSAGE
my_decoded_message = "Hi mate thank you for the message maya is a spy"


def encrypt_message(my_decoded_message, offset_number):

    offset = offset_number % 26
    offset_alphabet = alphabet[-offset:] + alphabet[:-offset]
    
    my_decoded_message_split = my_decoded_message.split(" ")
    my_offset_message = []
    for word in my_decoded_message_split:
        offset_words = ""
        for letter in word:
            if letter.upper() in alphabet:
                index = alphabet.index(letter.upper())
                offset_words += offset_alphabet[index]
        my_offset_message.append(offset_words)
    my_offset_message_final = " ".join(my_offset_message)
    my_offset_message_final += "!"
    return my_offset_message_final
    

#print(encrypt_message(my_decoded_message, 12))






#VIGINERE CIPHER              

alphabet_string = "abcdefghijklmnopqrstuvwxyz"

def vigenere_decode(coded_message, keyword):
    decoded_message = ""
    keyword_index = 0

    for letter in coded_message:
        if letter not in alphabet_string:
            decoded_message += letter
        else:
            key_letter = keyword[keyword_index % len(keyword)]
            letter_index = alphabet_string.find(letter)
            key_index = alphabet_string.find(key_letter)
            decoded_index = (letter_index + key_index) % 26
            decoded_message += alphabet_string[decoded_index]
            keyword_index += 1

    return decoded_message

vig_coded_message_to_decode = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"   #keyword = friends
print(vigenere_decode(vig_coded_message_to_decode, "friends"))

      

