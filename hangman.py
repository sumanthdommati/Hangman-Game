import random
import time

user_name=input('Hello user !! Enter your Name : ')
print('Hey '+ user_name +' Welcome to Hangman Game !!')
time.sleep(2)
print('Your Game is about to Start ....')
time.sleep(2)

def main():
    global count
    global words
    global already_guessed
    global playgame
    global length
    global display
    global word
    words=["elephant", "rainbow", "computer", "sunlight", "bicycle", "mountain", "coconut", "happiness"]
    word=random.choice(words)
    already_guessed=[]
    length=len(word)
    playgame=''
    display='_'*length
    count=0

def replay():
    print('Do you want to play game again: ')
    playgame=input('Enter "Y" or "y" if you like to play else "N" or "n" : ')
    while playgame not in ['Y','y','N','n']:
        playgame=input('Enter "Y" or "y" if you like to play else "N" or "n"')
    if playgame in ['Y', 'y']:
        hangman()
    elif playgame in ['N','n']:
        print('You will be missed , See you again !!!' )
        exit()

def hangman():
    global count
    global word
    global already_guessed
    global display
    global playgame
    limit=6
    user_guess=input('Game is started '+ display + ' Enter your Guess : ')
    user_guess=user_guess.strip()
    if len(user_guess.strip())==0 or len(user_guess.strip())>=2 or user_guess<="9" :
        print('Please enter the Valid input.')
        hangman()
    elif user_guess in word:
        already_guessed.extend([user_guess])
        index=word.find(user_guess)
        word=word[:index] + "_" + word[index+1:]
        display=display[:index] + user_guess + display[index+1:]
    elif user_guess in already_guessed:
        print('Already exist , Enter another Word')
    else:
        count+=1
        if count==1:
            print('--------------\n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n')
            print('You Guessed Wrong : '+ str(limit-count) + ' Remaining Chances..')
        elif count==2:
            print('--------------\n'
                  '|          |  \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n')
            print('You Guessed Wrong : '+ str(limit-count) + ' Remaining Chances..')
        elif count==3:
            print('--------------\n'
                  '|          |  \n'
                  '|          |  \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n')
            print('You Guessed Wrong : '+ str(limit-count) + ' Remaining Chances..')
        elif count==4:
            print('--------------\n'
                  '|          |  \n'
                  '|          |  \n'
                  '|          |  \n'
                  '|             \n'
                  '|             \n'
                  '|             \n'
                  '|             \n')
            print('You Guessed Wrong : '+ str(limit-count) + ' Remaining Chances..')
        elif count==5:
            print('--------------\n'
                  '|          |  \n'
                  '|          |  \n'
                  '|          |  \n'
                  '|          o  \n'
                  '|             \n'
                  '|             \n'
                  '|             \n')
            print('You almost going to Hang')
            print('You Guessed Wrong : '+ str(limit-count) + ' Remaining Chances..')
        elif count==6:
            print('--------------\n'
                  '|          |  \n'
                  '|          |  \n'
                  '|          |  \n'
                  '|          o  \n'
                  '|         /|\ \n'
                  '|         / \ \n'
                  '|             \n')
            print('You Guessed Wrong')
            print('You lost all chances.')
            outstr=""
            remstr=""
            for i in already_guessed:
                outstr=outstr+i
            for j in word:
                if j != '_':
                    remstr+=j
            finstr=outstr+remstr
            print('Correct Word is :',finstr)
            replay()
        
    if word=='_'*length:
        print('Congractulations.... You won the game !!!!')
        print()
        replay()
    elif count!=limit:
        hangman()
main()
hangman()

            
        


        



    
