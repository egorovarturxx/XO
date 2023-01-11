board=['_','_','_',
       '_','_','_',
       '_','_','_',]

def display():
   print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
   print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
   print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')

def check(board):
   p1='x'
   p2='o'
   if board[0]==board[1]==board[2]==p1 or board[0]==board[1]==board[2]==p2:
      return True
   elif board[3]==board[4]==board[5]==p1 or board[3]==board[4]==board[5]==p2:
      return True
   elif board[6]==board[7]==board[8]==p1 or board[6]==board[7]==board[8]==p2:
      return True
   elif board[3]==board[0]==board[6]==p1 or board[3]==board[0]==board[6]==p2:
      return True
   elif board[1]==board[4]==board[7]==p1 or board[1]==board[4]==board[7]==p2:
      return True
   elif board[2]==board[5]==board[8]==p1 or board[2]==board[5]==board[8]==p2:
      return True
   elif board[0]==board[4]==board[8]==p1 or board[0]==board[4]==board[8]==p2:
      return True
   elif board[2]==board[4]==board[6]==p1 or board[2]==board[4]==board[6]==p2:
      return True
   else:
      return False

display()
def inp(board):
   x = int(input("Выберите позицию от 1-9: "))
   if board[x-1]!='_':
      print("Позиция была уже выбрана, укажите другую позицию")
      return inp(board)
   else:
      return x


for i in range (9):
   if i%2==0:
      x=inp(board)
      board[x-1]='x'
      display()
      if check(board):
         print('Игрок 1 победил')
         break
   else:
      x=inp(board)
      board[x-1] = 'o'
      display()
      if check(board):
         print('Игрок 2 победил')
         break
print('Игра окончена')
