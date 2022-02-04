with open("main.py\words.txt", "r") as file:
    words = [word.strip("\n") for word in file]
    wordle_words = [word.lower() for word in words if len(word) == 5]

           
        
known_spots = input("Enter known wordle letters using '-' to seperate unknown blanks: ")



possible_words = []

indexes = []
ind = 0
for letter in known_spots:
    if letter != "-":
        indexes.append((ind,letter))
    ind += 1



for word in wordle_words:
    word_inds = []
    for char in word:
        if (word.index(char),char) in indexes:
            word_inds.append((word.index(char),char))
    if word_inds == indexes:
        print(word)

        
    


            