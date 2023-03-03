import time


def rotate(board, n):
    if n == 0:
        return board
    board_t = board.copy()
    board_t[0] = board[6]
    board_t[1] = board[3]
    board_t[2] = board[0]
    board_t[5] = board[1]
    board_t[6] = board[8]
    board_t[7] = board[5]
    board_t[8] = board[2]
    board_t[3] = board[7]
    if n > 1:
        board_t = rotate(board_t, n - 1)
    return board_t


def remove_rotation_copies(tables):
    output = tables.copy()
    for x in range(len(tables)):
        for z in range(0, 4):
            temp = rotate(tables[x], z)
            for y in (tables[x + 1:len(tables)]):
                if y == temp and x != 4:
                    try:
                        output.remove(tables[x])
                    except:
                        pass
    # for x in output:
    # print(table(x))
    return output
    # compare stable with the change
    # instances of repetition


def iterate(board, turn):
    output = []
    if board.count("_") == -1:
        return None
    else:
        for x in range(len(board)):
            if board[x] == "_":
                similar = board.copy()
                similar[x] = turn
                output.append(similar)
    return output


def game_table(board):
    print("\n", board[0], "|", board[1], "|", board[2], "\n",
          "_________", "\n",
          board[3], "|", board[4], "|", board[5], "\n",
          "_________", "\n",
          board[6], "|", board[7], "|", board[8])


# is used to ask user for input
def gui(current_input, turn):
    output = current_input.copy()
    print(" ___1___2___3___")
    print(" A ", current_input[0], "|", current_input[1], "|", current_input[2], "\n",
          "___________", "\n",
          "B ", current_input[3], "|", current_input[4], "|", current_input[5], "\n",
          "____________", "\n",
          "C ", current_input[6], "|", current_input[7], "|", current_input[8])
    if check_won(current_input) == "X":
        print("X HAS WON!!")
        quit()
    elif check_won(current_input) == "O":
        print("O HAS WON!!")
        quit()
    elif check_won(current_input) == 0:
        print("Its a tie")
        quit()
    try:
        choice_r = input("INPUT THE ROW:").capitalize()
        if choice_r == "A":
            choice_r = 0
        elif choice_r == "B":
            choice_r = 3
        elif choice_r == "C":
            choice_r = 6
        choice_c = int(input("INPUT THE COLUMN:"))
        if output[choice_c - 1 + choice_r] == "_":
            output[choice_c - 1 + choice_r] = turn
        else:
            print("Invalid input!")
            quit()
    except:
        print("Invalid input!")
        quit()
    return output


def check_won(board):
    # this checks rows
    for y in range(0, 7, 3):
        if board[y] == board[y + 1] and board[y + 2] == board[y]:
            return board[y]
    # this checks columns
    for x in range(3):
        if board[x] == board[x + 3] and board[x + 6] == board[x]:
            return board[x]
    # this check diagonals
    if board[0] == board[4] and board[8] == board[0]:
        return board[4]
    elif board[2] == board[4] and board[6] == board[4]:
        return board[2]
    elif board.count("_") == 0:
        return 0
    else:
        return None


# take string of board and turns into a list takes list of board and turns it into string
def convert(board):
    output = ""
    if type(board) == str:
        return board.split(",")
    else:
        for x in board:
            output = output + x + ","
        output = output[0:len(output) - 1]
        return output


# different naming mechanic you also need a depth hit problem solve
# BE careful it produces a hash map with keyboard and value a list with the node and a dictionary
# with all the children IN WHICH EACH KEY VALUE MAPS
# When traversing through the data structure I made it will require u to change it and then rotate
# need a way of ending
# SOMETHING IS UP WITH THE RECURSION
def step(nd, turn):
    final_tree = {}
    lowest_highest = []
    iterations = remove_rotation_copies(iterate(nd.game, turn))
    final_tree[nd.identifier] = [nd, {}]
    if turn == "X":
        high = -2
    else:
        high = 2
    for x in iterations:
        current_node_win = check_won(x)
        quantitative_value = None
        if current_node_win == "X":
            quantitative_value = 1
        elif current_node_win == "O":
            quantitative_value = -1
        elif current_node_win == None:
            quantitative_value = None
        elif current_node_win == "_":
            quantitative_value = None
        new_node = Node(quantitative_value, nd.identifier, convert(x), x)
        # worthless?
        if quantitative_value != None:
            # something here is wrong
            final_tree[nd.identifier][1][new_node.identifier] = [new_node, {}]
            lowest_highest.append(quantitative_value)
        # this is the problem
        else:
            if turn == "X":
                part = step(new_node, "O")
                final_tree[nd.identifier][1][new_node.identifier] = list(part.values())[0]
                lowest_highest.append((list(part.values())[0])[0].data)
            else:
                part = step(new_node, "X")
                final_tree[nd.identifier][1][new_node.identifier] = list(part.values())[0]
                lowest_highest.append((list(part.values())[0])[0].data)
    if len(lowest_highest) == 0:
        current_node_win = check_won(nd.game)
        quantitative_value = None
        if current_node_win == "X":
            quantitative_value = 1
        elif current_node_win == "O":
            quantitative_value = -1
        elif current_node_win == None:
            quantitative_value = None
        elif current_node_win == "_":
            quantitative_value = None
        elif current_node_win == 0:
            quantitative_value = 0
        new_node = Node(quantitative_value, nd.identifier, convert(nd.game), nd)
        final_tree[nd.identifier][0].data = new_node.data
    elif len(lowest_highest) == 1:
        final_tree[nd.identifier][0].data = lowest_highest[0]
    else:
        lowest_highest.sort()
        if turn == "X":
            high = lowest_highest[len(lowest_highest) - 1]
        elif turn == "O":
            high = lowest_highest[0]
        final_tree[nd.identifier][0].data = high
    return final_tree


# We pray to whatever god exists
# partitions goal take a node and a turn and return a dictionary list mix of every single iteration

# this should work it's a function that returns a node that is best
def response(dic, turn, position):
    if turn == "X":
        goal = 1
    else:
        goal = -1
    responses = (dic[position][1].values())
    output_node = None
    for x in responses:
        if (goal >= x[0].data) and turn == "X":
            goal = x[0].data
            output_node = x[0]
        elif goal < x[0].data and turn == "O":
            goal = x[0].data
            output_node = x[0]
        else:
            pass
    if output_node == None:
        print("ITS A TIE!")
        quit()
    return output_node


def find_offset(dic, position):
    for x in range(0, 6):
        try:
            test = (dic[convert(rotate(position, x))])
            offset = x
            return x
        except:
            pass


class Node:
    def __init__(self, data, parent, identifier, game):
        self.parent = parent
        self.data = data
        self.identifier = identifier
        self.game = game

    def __str__(self):
        return f"{self.data}|{self.parent}|{self.identifier}|{self.game}"


board_end = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
# experiment
# already_made_node=Node(None,None,convert(board_end),board_end)
# LETS OPEN THE FLOOD GATES SHALL WE?
# already_made_node=Node(None,None,convert(first_board),first_board)
already_made_node = Node(None, None, convert(board_end), board_end)
st = time.time()  # function used to time the function
key_space = step(already_made_node, "X")
et = time.time()
elapsed_time = et - st
# print("PRINTING TEMP:",temp)
print("Flag 1 passed", ' Execution time:', elapsed_time, 'seconds')
team = input("PICK TEAM O or X:\n").replace(" ", "").capitalize()
if team == "O":
    current_branch = key_space
    computer = response(current_branch, "O", convert(board_end))
    current_branch = current_branch[convert(already_made_node.game)][1]
    current_branch = current_branch[convert(computer.game)][1]
    user = gui(computer.game, "O")
    offset = find_offset(current_branch, user)
    while True:
        computer = response(current_branch, "O", convert(rotate(user, offset)))
        current_branch = current_branch[convert(rotate(user, offset))][1]
        current_branch = current_branch[convert(computer.game)][1]
        user = gui(rotate(computer.game, 4 - offset), "O")
elif team == "X":
    user = gui(already_made_node.game, "X")
    current_branch = key_space[convert(already_made_node.game)][1]
    offset = find_offset(current_branch, user)
    computer = response(current_branch, "X", convert(rotate(user, offset)))
    offset = find_offset(current_branch, user)
    current_branch = current_branch[convert(rotate(user, offset))][1]
    current_branch = current_branch[convert(computer.game)][1]
    while True:
        user = gui((rotate(computer.game, 4 - offset)), "X")
        computer = response(current_branch, "X", convert(rotate(user, offset)))
        current_branch = current_branch[convert(rotate(user, offset))][1]
        current_branch = current_branch[convert(computer.game)][1]
else:
    print("INVALID INPUT TEAM")
    quit()
