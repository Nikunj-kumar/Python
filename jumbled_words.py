import random

def choose():
    words=['rainbow','computer','science','programing','player','condition','reverse']
    pick=random.choice(words)
    return pick

def jumble(words):
    jumbled="".join(random.sample(words,len(words)))
    return jumbled

def thanks(p1name,p2name,point_p1,point_p2):
    print(p1name,'score is',point_p1)
    print(p2name, 'score is', point_p2)
    print("thanks for playing")



def play():
    p1name=input("Player 1, please enter your name: ")
    p2name=input("Player 2, please enter your name: ")
    point_p1 = 0
    point_p2 = 0
    turn = 0
    while(1):
        picked_word=choose()
        question=jumble(picked_word)
        print(question)
        if turn%2==0:
            print(p1name, 'your turn')
            ans=input("what is in my mind: ")
            if ans==picked_word:
                point_p1=point_p1+1
                print("Your score is", point_p1)
            else:
                print("Incorrect answer. Correct answer is -", picked_word)
            c=int(input("Press 1 to continue and 0 is for quit"))
            if c==0:
                thanks(p1name,p2name,point_p1,point_p2)
                break
        else:
            print(p2name, 'your turn')
            ans=input("what is in my mind: ")
            if ans==picked_word:
                point_p2=point_p2+1
                print("Your score is", point_p2)
            else:
                print("Incorrect answer. Correct answer is -", picked_word)
            c=int(input("Press 1 to continue and 0 is for quit"))
            if c==0:
                thanks(p1name,p2name,point_p1,point_p2)
                break
        turn=turn+1

play()
    
