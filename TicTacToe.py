board=[' ' for x in range(10)]

def printboard(board):
    print('  |   |  ')
    print(board[1],'|',board[2],'|',board[3])
    print('----------')
    print(board[4],'|',board[5],'|',board[6])
    print('  |   |  ')
    print('----------')
    print('  |   |  ')
    print(board[7],'|',board[8],'|',board[9])

def correctchoice(move):
    return board[move]==' '

def playertwo(move):
    board[move]='O'
    printboard(board)


def isfull(bo):
    for i in range(1,len(bo)):
        if bo[i]!=' ':
            f=True
        else:
            f=False
            break
    return f
    

def playerone(move):
    board[move]='X'
    printboard(board)


def winner(bo,le):
    return (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le)or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)

def main():
    while True:
        if isfull(board):
            print('Match is tied')
            break
        i=int(input('enter the 1st player move'))
        if correctchoice(i):
            playerone(i)
        else:
            i=int(input('please enter the correct no'))
            if correctchoice(i):
                playerone(i)
        if winner(board,'X'):
            print("Player 1 is win")
            break

        if isfull(board):
            print('Match is tied')
            break
        
        j=int(input('enter the 2st player move'))
        if correctchoice(j):
            playertwo(j)
        else:
            j=int(input('please enter the correct no'))
            if correctchoice(j):
                playertwo(j)

        if winner(board,'O'):
            print('Player 2 is win')
            break

        if isfull(board):
            print('Match is tied')
            break

main()





