# DISPLAY FUNCTION
def display_func():
    print('Welcome to the Tic Tac Toe game! \n')
    p1 = 'H'
    l1=['7','8','9']
    l2=['4','5','6']
    l3=['1','2','3']
    count=0
    while p1 not in ['X','O']:
        p1 = input('Player 1: Do you want to be X or O? \n')
        if p1 not in ['X','O']:
            print('You need to choose between X or O')
        
    print('Great! Player 1 starts first!')
    val = 'Maybe'
    while val not in ['Yes','No']:
        val = input('Are you ready to play? (Yes or No)')
        if val not in ['Yes','No']:
            print("I don't understand. Please choose Yes or No!")
    if val == 'No':
        return 'Sorry to hear that!',l1,l2,l3,count
    else:
        return p1,l1,l2,l3,count

# afisare tabla de joc
def display_board(l1, l2, l3):
    new_l1=[' ' if (x != 'X' and x != 'O') else x for x in l1]
    new_l2=[' ' if (x != 'X' and x != 'O') else x for x in l2]
    new_l3=[' ' if (x != 'X' and x != 'O') else x for x in l3]
    l1=' | '.join(new_l1)
    l2=' | '.join(new_l2)
    l3=' | '.join(new_l3)
    l=['-','-','-','-','-','-','-','-','-']
    l=''.join(l)
    print(l1)
    print(l)
    print(l2)
    print(l)
    print(l3)

from IPython.display import clear_output
def choose_num(l1,l2,l3):
    nr=''
    while nr not in ['1','2','3','4','5','6','7','8','9']:
        nr = input('Choose your position: (1-9)')
        if nr not in ['1','2','3','4','5','6','7','8','9']:
            print('You need to choose a number between 1 and 9!')
        else:
            return nr

def place_position(l1,l2,l3,nr,p1, count):
    L=[l1,l2,l3]
    if nr in l1 or nr in l2 or nr in l3:
        for x in range(0,3):
            for y in range(0,3):
                if L[x][y]==nr:
                   L[x][y]=p1
                   if p1 == 'X':
                       p1 = 'O'
                   else:
                       p1 = 'X'
    else:
        while (nr in l1 or nr in l2 or nr in l3)==False:
            print('This position is taken. Please try again!')
            nr = choose_num(l1,l2,l3)
            if nr in l1 or nr in l2 or nr in l3:
                for x in range(0,3):
                    for y in range(0,3):
                        if L[x][y]==nr:
                           L[x][y]=p1
                           if p1 == 'X':
                               p1 = 'O'
                           else:
                               p1 = 'X'
                break
                
            
    l1=L[0]
    l2=L[1]
    l3=L[2]
    count=count+1
    clear_output()
    display_board(l1,l2,l3)
    return l1,l2,l3,p1, count

def game(l1,l2,l3,l_x,l_o,p1, count):
    nr = choose_num(l1,l2,l3)
    l1,l2,l3,p1,count=place_position(l1,l2,l3,nr,p1,count)
    if (l1 == l_x or l1 == l_o) or (l2 == l_x or l2 == l_o) or (l3 == l_x or l3 == l_o) or (l1[0] == l2[0] == l3[0]) or (l1[1] == l2[1] == l3[1]) or (l1[2] == l2[2] == l3[2]) or (l1[0]==l2[1]==l3[2]) or (l1[2]==l2[1]==l3[0]): 
        print('Congratulations! You are the winner.')
        v=verif()
        if v == False:
            p1,l1,l2,l3,count=display_func()
            return False, p1, l1,l2,l3,count
        else:
            return True, p1, l1,l2,l3,count        
    else:
        if count == 9:
            print('This game has no winner.')
            v=verif()
            if v == False:
                p1,l1,l2,l3,count=display_func()
                return False, p1, l1,l2,l3,count
            else:
                return True, p1, l1,l2,l3,count
        else:
            return False, p1, l1,l2,l3,count

def verif():
    ok='G'
    while ok not in ['Y','N']:
        ok = input('Do you want to play again? (Y or N)')
        if ok not in ['Y','N']:
            print("I don't understand. Please choose Y or N!")
    clear_output()
    if ok=='Y':
        return False
    else:
        print('OK!')
        return True

val=False
p1,l1,l2,l3,count=display_func()
l_x=['X','X','X']
l_o=['O','O','O']

while val==False:
    if p1 == 'Sorry to hear that!':
        print(p1)
        break
    else:
        val, p1,l1,l2,l3, count=game(l1,l2,l3,l_x,l_o,p1,count)
