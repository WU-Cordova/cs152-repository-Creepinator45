from projects.project1.game import Game

def main():
    player_name = input("Hello! What's your name? ")
    game = Game(player1_name=player_name)
    game.beginGames()

if __name__ == '__main__':
    main()
    pass
