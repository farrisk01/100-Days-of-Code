def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    true_score = 0
    love_score = 0

    for letter in combined_names.lower(): #Loops thru the lower case combined_names
        if letter in 'true': #For each letter in combined_names that is also in the word 'true' a 1 is added to true_score
            true_score += 1
        if letter in 'love': #For each letter in combined_names that is also in the word 'love' a 1 is added to love_score
            love_score += 1
    print(str(true_score) + str(love_score)) #Combines true_score and love_score into a 2 digit number

calculate_love_score('Tina', 'Terry')