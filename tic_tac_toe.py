import random as r 
class Node:
    def __init__(self,board,current_level, alpha, beta):
        self.board = board 
        self.current_level = current_level 
        self.ismax_node = True
        self.apha = alpha
        self.beta = beta 


def make_draw(pz,pos,value):
    row = pos//3
    col = pos%3 
    print(row,'row',col,'col')


    if pz[row][col] == -1 :  # Means if Blank space , put the value
        pz[row][col] = value    
        return pz
    
    else:                 # Already filled 
        False
def minimax_alpha_beta(node):
        node.

def choose_best_move(board): # retrurn single move 
    node = Node(board)
    minimax_alpha_beta(node)


def check_solution(pz,value):
    # value is number to be checked of a player assigned (0,1)
    for row in range(3):  # Checking solution in Rows 
        if pz[row][0] == pz[row][1] == pz[row][2] == value :
            print('row',row)
            return True 
        
    for col in range(3): # checking Solution in COLUMNS 
        if pz[0][col] == pz[1][col] == pz[2][col] == value:
            print(col,'col')
            return True 

    if pz[0][0] == pz[1][1] == pz[2][2]:
        return True
    
    elif pz[0][2] == pz[1][1] == pz [2][0]:
       
        return True 
    return False 
def choose_best_move(board): #return the best move(pos where we should draw)
    
    
    pass 


def game():

        #board = [[-1 for i in range(3)]for j in range(3)]  # use the -1 for blank tile
        
        player1 = 'Computer'
        player2 = input('Enter a Name of Second Player:  ')
        
        toss = r.randint(0,1)


        players = []
        
        if toss == 0:
            players.append(player1) # use 0 number for player1 
            players.append(player2) # use 1 number for player2 
        
        if toss == 1:
            players.append(player2)
            players.append(player1)

        attempts = 0 

        while True:
            for plr in range(len(players)):   
                if players[plr] == 'Computer' :   
                    pos = choose_best_move(board)                         # Try unitll specific pladyer draw legal  move 
                    make_draw(board,pos)

                attempts += 1 
                if attempts >= 5:
                    if check_solution(board,plr):
                        print(f'{players[plr]}, Congratulation won the Match')
                        return True 
                     
                if attempts >= 9:
                    print('Match Draw : ')
                    return False 
                    
board = [[-1 for i in range(3)]for j in range(3)]  # use the -1 for blank tile
        
game()