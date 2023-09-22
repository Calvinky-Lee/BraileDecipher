def parse_braille_file():
    data_list = []
    with open("data22.txt") as file_in:
        for i in file_in:
            i = i.strip()
            data_list.append(i)
    return data_list
        
def decode_phrase(data):
    deciphDict = {"xooooo":"a","xoxooo":"b","xxoooo":"c","xxoxoo":"d","xooxoo":"e", \
                  "xxxooo":"f","xxxxoo":"g","xoxxoo":"h","oxxooo":"i","oxxxoo":"j","xoooxo":"k","xoxoxo" \
:"l","xxooxo":"m","xxoxxo":"n","xooxxo":"o","xxxoxo":"p","xxxxxo":"q","xoxxxo":"r","oxxoxo":"s","oxxxxo":"t", \
"xoooxx":"u","xoxoxx":"v","oxxxox":"w","xxooxx":"x","xxoxxx":"y","xooxxx":"z","oooooo":" "}

    for line in range(0,len(data),3):
        word = ""
        braileList = [data[line],data[line+1],data[line+2]]
        for braile in range(0,len(braileList[0]),2):
            letter = ""
            letter+=  braileList[0][braile:braile+2]
            letter+=  braileList[1][braile:braile+2]
            letter+=  braileList[2][braile:braile+2]
        
            letter = deciphDict[letter]
            word += letter
        print(word)
                
                            
a = parse_braille_file()
decode_phrase(a)

