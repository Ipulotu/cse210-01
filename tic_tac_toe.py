'''
Class: CES210-13
assignmen: W01 Prove: Developer - Solo Code Submission
author names: Ikaika Pulotu 
Date: 1/6/2022
'''

def main():
    # Defining array & population array 
    numbers = ['1','2','3','4','5','6','7','8','9']
    game = numbers[0]+'|'+numbers[1]+'|'+numbers[2]+' \n-+-+- \n'+numbers[3]+'|'+numbers[4]+'|'+numbers[5]+' \n-+-+- \n'+numbers[6]+'|'+numbers[7]+'|'+numbers[8]
    print(game)


    #Function to set x in numbers array 
    def set_x(number):
            number -= 1
            numbers[number] = 'x'

        #Function to set o in numbers array 
    def set_o(number):
            number -= 1
            numbers[number] = 'o'

        #Function to test if x or o has won 
    def test_win(numbers, letter):
            if numbers[0] == letter and numbers[1] == letter  and numbers[2] == letter:
                return 1
            elif numbers[3] == letter and numbers[4] == letter and numbers[5] == letter:
                return 1
            elif numbers[6] == letter and numbers[7] == letter and numbers[8] == letter:
                return 1
            elif numbers[0] == letter and numbers[3] == letter and numbers[6] == letter:
                return 1
            elif numbers[1] == letter and numbers[4] == letter and numbers[7] == letter:
                return 1
            elif numbers[2] == letter and numbers[5] == letter and numbers[8] == letter:
                return 1
            elif numbers[0] == letter and numbers[4] == letter and numbers[8] == letter:
                return 1                    
            elif numbers[2] == letter and numbers[4] == letter and numbers[6] == letter:
                return 1   
            else:  
                return 0 

        #while loop that runs until all truns have be taken. 
    i = 0
    while i <= 5:
            i += 1
            t1 = int(input ('x\' turn to choose a square (1-9):'))
            set_x(t1)
            game = numbers[0]+'|'+numbers[1]+'|'+numbers[2]+' \n-+-+- \n'+numbers[3]+'|'+numbers[4]+'|'+numbers[5]+' \n-+-+- \n'+numbers[6]+'|'+numbers[7]+'|'+numbers[8]
            print(game)
            # An if statment that check if x won. If so end game
            if test_win(numbers, 'x') == 1: 
                print('Congratulations Player One, you win! Thanks for playing!')
                break
            if i == 5:
               print('It\'s a tie! better luck next time. ')
               break 
            
            t2 = int(input ('o\' turn to choose a square (1-9):'))
            set_o(t2)
            game = numbers[0]+'|'+numbers[1]+'|'+numbers[2]+' \n-+-+- \n'+numbers[3]+'|'+numbers[4]+'|'+numbers[5]+' \n-+-+- \n'+numbers[6]+'|'+numbers[7]+'|'+numbers[8]
            print(game)
            # An if statment that check if o won. If so end game
            if test_win(numbers, 'o') == 1: 
                print('Congratulations Player Two, you win! Thanks for playing!')
                break
            
main()
