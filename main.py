import random
import sys


class StartEasyUser:
    def __init__(self):
        self.board = {(x, y): " " for y in range(3, 0, -1)
                      for x in range(1, 4)}
        self.available_co = list(self.board.keys())
        self.moves = {"X": 0, "O": 0, " ": 0}
        self.user = User("user")
        self.comp = Computer("comp")
        self.game_on = True
        self.whos_turn = self.user  # can change in future
        self.winner = ""
        self.easy_user()

    def easy_user(self):
        while self.game_on:
            StartEasyUser.draw_board(self.board)
            if self.whos_turn.p_name == "comp":
                move, m_char = self.user.check_commit(self.available_co)
                self.available_co.remove(move)
                self.board[move] = m_char
                self.moves[m_char] += 1
                self.whos_turn = self.user
            else:
                move, m_char = self.comp.make_move(self.available_co)
                self.available_co.remove(move)
                self.board[move] = m_char
                self.moves[m_char] += 1
                self.whos_turn = self.comp
            self.winner = self.declare_winner()
            if self.winner != "":
                self.game_on = False
                self.draw_board(self.board)
                print(self.winner)

    @staticmethod
    def draw_board(the_board):
        print("-" * len(the_board))
        for y in range(3, 0, -1):
            print("| ", end="")
            for x in range(1, 4):
                print(f"{the_board[(x, y)]} ", end="")
            print("|")
        print("-" * len(the_board))

    @staticmethod
    def checker(the_list):
        for item in the_list:
            if item[0] != item[1] or item[0] == " ":
                continue
            else:
                if item[1] == item[2]:
                    return True, item[2]
                else:
                    continue
        return False, ""

    def declare_winner(self):
        all_rows, self.winner = self.checker([[self.board[x, y]
                                               for x in range(1, 4)]
                                              for y in range(1, 4)])
        if all_rows:
            return f"{self.winner} wins"
        all_columns, self.winner = self.checker([[self.board[x, y]
                                                  for y in range(1, 4)]
                                                 for x in range(1, 4)])
        if all_columns:
            return f"{self.winner} wins"
        main_diagonal = [self.board[x, y] for x, y in zip(range(1, 4),
                                                          range(3, 0, -1))]
        side_diagonal = [self.board[x, x] for x in range(1, 4)]
        diagonals, self.winner = self.checker([main_diagonal, side_diagonal])
        if diagonals:
            return f"{self.winner} wins"
        moves_counter = sum([value_ for move, value_ in self.moves.items()
                             if move != " "])
        if moves_counter == 9:
            return "Draw"
        return ""


class Player:
    def __init__(self, player_name, which_char):
        self.p_name = player_name
        self.play_char = which_char


class User(Player):
    def __init__(self, name, p_char="O"):
        super().__init__(name, p_char)
        self.move = ""

    def check_commit(self, av_co):
        self.move = input("Enter the coordinates: ").split()
        while True:
            if not all(list(map(self.elementary, self.move))):
                print("You should enter numbers!")
                self.move = input("Enter the coordinates: ").split()
            else:
                if not self.is_in_range(self.move):
                    print("Coordinates should be from 1 to 3!")
                    self.move = input("Enter the coordinates: ").split()
                    continue
                if self.is_occupied(self.move, av_co):
                    print("This cell is occupied! Choose another one!")
                    self.move = input("Enter the coordinates: ").split()
                    continue
                break
        return tuple([int(point) for point in self.move]), self.play_char

    @staticmethod
    def elementary(the_str):
        return the_str.isdigit()

    @staticmethod
    def is_occupied(coordinate, av_co):
        return tuple([int(point) for point in coordinate]) not in av_co

    @staticmethod
    def is_in_range(coordinate):
        temp_list = list(map(int, coordinate))
        return all([True if 1 <= point <= 3 else False for point in temp_list])


class Computer(Player):
    def __init__(self, name, level="easy", p_char="X"):
        super().__init__(name, p_char)
        self.play_char = p_char
        self.level = level

    def make_move(self, av_co):
        print(f'Making move level "{self.level}"')
        return random.choice(av_co), self.play_char


class StartUserUser:
    def __init__(self):
        self.board = {(x, y): " " for y in range(3, 0, -1)
                      for x in range(1, 4)}
        self.available_co = list(self.board.keys())
        self.moves = {"X": 0, "O": 0, " ": 0}
        self.user = User("user")
        self.user2 = User2("user2")
        self.game_on = True
        self.whos_turn = self.user  # can change in future
        self.winner = ""
        self.user_user()

    def user_user(self):
        while self.game_on:
            StartUserUser.draw_board(self.board)
            if self.whos_turn.p_name == "user":
                move, m_char = self.user2.check_commit2(self.available_co)
                self.available_co.remove(move)
                self.board[move] = m_char
                self.moves[m_char] += 1
                self.whos_turn = self.user2
            else:
                move, m_char = self.user.check_commit(self.available_co)
                self.available_co.remove(move)
                self.board[move] = m_char
                self.moves[m_char] += 1
                self.whos_turn = self.user
            self.winner = self.declare_winner()
            if self.winner != "":
                self.game_on = False
                self.draw_board(self.board)
                print(self.winner)

    @staticmethod
    def draw_board(the_board):
        print("-" * len(the_board))
        for y in range(3, 0, -1):
            print("| ", end="")
            for x in range(1, 4):
                print(f"{the_board[(x, y)]} ", end="")
            print("|")
        print("-" * len(the_board))

    @staticmethod
    def checker(the_list):
        for item in the_list:
            if item[0] != item[1] or item[0] == " ":
                continue
            else:
                if item[1] == item[2]:
                    return True, item[2]
                else:
                    continue
        return False, ""

    def declare_winner(self):
        all_rows, self.winner = self.checker([[self.board[x, y]
                                               for x in range(1, 4)]
                                              for y in range(1, 4)])
        if all_rows:
            return f"{self.winner} wins"
        all_columns, self.winner = self.checker([[self.board[x, y]
                                                  for y in range(1, 4)]
                                                 for x in range(1, 4)])
        if all_columns:
            return f"{self.winner} wins"
        main_diagonal = [self.board[x, y] for x, y in zip(range(1, 4),
                                                          range(3, 0, -1))]
        side_diagonal = [self.board[x, x] for x in range(1, 4)]
        diagonals, self.winner = self.checker([main_diagonal, side_diagonal])
        if diagonals:
            return f"{self.winner} wins"
        moves_counter = sum([value_ for move, value_ in self.moves.items()
                             if move != " "])
        if moves_counter == 9:
            return "Draw"
        return ""


class Player2:
    def __init__(self, player_name, which_char):
        self.p_name = player_name
        self.play_char2 = which_char


class User2(Player2):
    def __init__(self, name, p_char="X"):
        super().__init__(name, p_char)
        self.move = ""

    def check_commit2(self, av_co):
        self.move = input("Enter the coordinates: ").split()
        while True:
            if not all(list(map(self.elementary, self.move))):
                print("You should enter numbers!")
                self.move = input("Enter the coordinates: ").split()
            else:
                if not self.is_in_range(self.move):
                    print("Coordinates should be from 1 to 3!")
                    self.move = input("Enter the coordinates: ").split()
                    continue
                if self.is_occupied(self.move, av_co):
                    print("This cell is occupied! Choose another one!")
                    self.move = input("Enter the coordinates: ").split()
                    continue
                break
        return tuple([int(point) for point in self.move]), self.play_char2

    @staticmethod
    def elementary(the_str):
        return the_str.isdigit()

    @staticmethod
    def is_occupied(coordinate, av_co):
        return tuple([int(point) for point in coordinate]) not in av_co

    @staticmethod
    def is_in_range(coordinate):
        temp_list = list(map(int, coordinate))
        return all([True if 1 <= point <= 3 else False for point in temp_list])


class StartEasyEasy:
    def __init__(self):
        self.board = {(x, y): " " for y in range(3, 0, -1)
                      for x in range(1, 4)}
        self.available_co = list(self.board.keys())
        self.moves = {"X": 0, "O": 0, " ": 0}
        self.comp1 = Computer("comp1")
        self.comp2 = Computer2("comp2")
        self.game_on = True
        self.whos_turn = self.comp2  # can change in future
        self.winner = ""
        self.easy_easy()

    def easy_easy(self):
        while self.game_on:
            StartEasyEasy.draw_board(self.board)
            if self.whos_turn.p_name == "comp1":
                move, m_char = self.comp2.make_move2(self.available_co)
                self.available_co.remove(move)
                self.board[move] = m_char
                self.moves[m_char] += 1
                self.whos_turn = self.comp2
            else:
                move, m_char = self.comp1.make_move(self.available_co)
                self.available_co.remove(move)
                self.board[move] = m_char
                self.moves[m_char] += 1
                self.whos_turn = self.comp1
            self.winner = self.declare_winner()
            if self.winner != "":
                self.game_on = False
                self.draw_board(self.board)
                print(self.winner)

    @staticmethod
    def draw_board(the_board):
        print("-" * len(the_board))
        for y in range(3, 0, -1):
            print("| ", end="")
            for x in range(1, 4):
                print(f"{the_board[(x, y)]} ", end="")
            print("|")
        print("-" * len(the_board))

    @staticmethod
    def checker(the_list):
        for item in the_list:
            if item[0] != item[1] or item[0] == " ":
                continue
            else:
                if item[1] == item[2]:
                    return True, item[2]
                else:
                    continue
        return False, ""

    def declare_winner(self):
        all_rows, self.winner = self.checker([[self.board[x, y]
                                               for x in range(1, 4)]
                                              for y in range(1, 4)])
        if all_rows:
            return f"{self.winner} wins"
        all_columns, self.winner = self.checker([[self.board[x, y]
                                                  for y in range(1, 4)]
                                                 for x in range(1, 4)])
        if all_columns:
            return f"{self.winner} wins"
        main_diagonal = [self.board[x, y] for x, y in zip(range(1, 4),
                                                          range(3, 0, -1))]
        side_diagonal = [self.board[x, x] for x in range(1, 4)]
        diagonals, self.winner = self.checker([main_diagonal, side_diagonal])
        if diagonals:
            return f"{self.winner} wins"
        moves_counter = sum([value_ for move, value_ in self.moves.items()
                             if move != " "])
        if moves_counter == 9:
            return "Draw"
        return ""


class Computer2(Player):
    def __init__(self, name, level="easy", p_char="O"):
        super().__init__(name, p_char)
        self.play_char = p_char
        self.level = level

    def make_move2(self, av_co):
        print(f'Making move level "{self.level}"')
        return random.choice(av_co), self.play_char


while True:
    print('Input command: > ("start easy user or start user easy", "start user user", "start easy easy"')
    start = input()
    if start == 'start user easy' or start == 'start easy user':
        StartEasyUser()
    elif start == 'start user user':
        StartUserUser()
    elif start == 'start easy easy':
        StartEasyEasy()
    elif start == 'exit':
        sys.exit()
    else:
        print('Bad parameters!')
