def calculate_love_score(man, woman):
    score1 = 0
    score2 = 0
    com_name = man + woman
    name = com_name.lower()
    tr = "true"
    lv = "love"
    for x in name:
        if x in tr:
            score1 += 1
    
    for x in name:
        if x in lv:
            score2 += 1 
    
    score_t = str(score1)
    score_l = str(score2)
    love_score = score_t + score_l
    
    print(love_score)
    
man = input("Name of the man: ")
woman = input("Name of the woman: ")
calculate_love_score(man, woman)