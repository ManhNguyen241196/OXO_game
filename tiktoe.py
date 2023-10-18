import os
#init params
game_list = [' ']*10
game_over = False
# game_list = ["#","x", "o", "x","o","-", "x","x","x","o"]
game_on = True
player = [1,2]
number_pick = [1,2,3,4,5,6,7,8,9]
number_pick_ed = []

def display_game(game_list):
    os.system('cls')
    print(f'''Here is game board: 
        {game_list[1]} | {game_list[2]} | {game_list[3]}
        {game_list[4]} | {game_list[5]} | {game_list[6]}
        {game_list[7]} | {game_list[8]} | {game_list[9]} ''')
    
    # index = check_input(game_list)
    # replace_posi(game_list, int(index))
    # game_choice()

def check_input(list):
    value = ''
    while not value.isdigit():
        value =  input("Choose number in list: ")
        if(value.isdigit()):
            if (value in number_pick_ed):
                print("Vi tri nay da dk chọn trước đó rồi. Hãy chọn vị trí khác")
            if(int(value) in list and (not value in number_pick_ed)):
                print(value)
                number_pick_ed.append(value)
                return value
            else:
                value = '' 

def chooseXorO():
    player1 = None
    player2 = None
    while player1 != "x" and player1 != "o":
        player1 = input("bạn chọn 'x' hay 'o'? ")
        if(not player1 in ['x','o']):
            print("sai kis tu roi. hay chon 'x'or 'o' ")
        if(player1 == 'x'):
            player2 = 'o'   
        else:
            player2='x'

    return (player1,player2)


def replace_posi(list, index,symbol):
    list[index] = symbol
    # print(f"new list: {list}" )

def game_choice():
    choice = False
    while not choice:
        user_choice = input("ban co muon tiep tuc [y/n]? ")
        if not user_choice in ['y','n']:
            print("xin loi t k hieu hay chon 'y' or 'n'")
            user_choice = input("ban co muon tiep tuc [y/n]? ")
        else:
            if(user_choice == "y"):         
                print("tiep tuc")
                return True
            else:         
                print("ket thuc")
                return False
            
            
def game_func(game_list, game_on):
    
    while game_on:
        global game_over
        #dinh nghia player
        global player
        player = list(chooseXorO())

        for i in range(1,len(game_list)+1):
            
            display_game(game_list)

            def check_win():
                case_win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
                for case_tuple in case_win:
                    if(game_list[case_tuple[0]] != ' ' and game_list[case_tuple[0]] == game_list[case_tuple[1]] and game_list[case_tuple[0]]== game_list[case_tuple[2]]):
                        return True
                return False
            
            def player_turn(name, player):
                global game_over
                print(f'''{name}. Chọn {player}         1 | 2 | 3      
                        4 | 5 | 6       
                        7 | 8 | 9 ''')
                index = check_input(number_pick)
                replace_posi(game_list, int(index), player)
                
                game_over = check_win() 

            if(i < len(game_list) and  not game_over):
                if(i % 2 != 0):
                    player_turn("player1: YOU",player[0])
                      
                else:
                    player_turn("player2",player[1])

            # phản hồi khi game_over dk update
            if(game_over):
                if(i % 2 != 0):
                    display_game(game_list)
                    print("player1: WIN")
                else:
                    display_game(game_list)
                    print("player2: WIN")
                break

        game_on = False
        

        # game_on = game_choice()

# display_game(game_list)
game_func(game_list, game_on)
