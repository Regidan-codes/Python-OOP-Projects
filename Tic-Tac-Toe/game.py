from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("*************************")
        print(" Welcome to Tic-Tac-Toe ")
        print("*************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        # Ask user would they like to play another round
        while True:  # Game

            # Get move, check tie, check game over
            while True:  # Round

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_tie():
                    print("It's a tie! 👍 Try again.")
                    break
                elif board.check_game_is_over(player, player_move):
                    print("Awesome, You won the game! 🎉")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_game_is_over(computer, computer_move):
                        print("Oops!... ☹️ The computer won. Try again.")
                        break

            play_again = input("Would to like to play the game again? Enter X for yes, or O for no: ").upper()

            if play_again == "O":
                print("Bye! Come back soon.👋")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was invalid. But I assume you want to play again.💡")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("*********************")
        print("Starting a new round")
        print("*********************")
        board.reset_board()
        board.print_board()


game = TicTacToeGame()
game.start()
