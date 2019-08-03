import random

movies = ['anand', 'drishyam', 'anbe sivam', 'gol mal', 'vikram vedha', 'black friday', 'dangal']

def create_question(movie):
    n=len(movie)
    letter=list(movie)
    temp=[]
    for i in range(n):
        if letter[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True


def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=="*":
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
    

def play():
    p1 = input("enter the name of the first player: ")
    p2 = input("enter the name of the second player: ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1,'Your Turn')
            picked_movie = random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn

            not_said=True
            while not_said:
                letter=input("Your Letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie or 2 to unlock another letter"))
                    if d==1:
                        ans=input('your answer: ')
                        if ans==picked_movie:
                            pp1=pp1+1
                            print('Correct')
                            not_said=False
                            print(p1,'Your score: ',pp1)
                        else:
                            print("Wrong answer. Try again.")

                    
                else:
                    print(letter, "not found")
            c=int(input('Press 1 to continue or 0 to quit: '))
            if c==0:
                print(p1,'Your score: ', pp1)
                print(p2,'Your score: ', pp2)
                print("Thanks for playing")
                print("Have a nice day")
                willing=False

            

        else:
            print(p2,'Your Turn')
            picked_movie = random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn

            not_said=True
            while not_said:
                letter=input("Your Letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie or 2 to unlock another letter"))
                    if d==1:
                        ans=input('your answer: ')
                        if ans==picked_movie:
                            pp2=pp2+1
                            print('Correct')
                            not_said=False
                            print(p2,'Your score: ',pp2)
                        else:
                            print("Wrong answer. Try again.")

                    
                else:
                    print(letter, "not found")
            c=int(input('Press 1 to continue or 0 to quit: '))
            if c==0:
                print(p1,'Your score: ', pp1)
                print(p2,'Your score: ', pp2)
                print("Thanks for playing")
                print("Have a nice day")
                willing=False

        turn = turn+1

play()
