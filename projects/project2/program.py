from projects.project2.gamecontroller import GameController

def main():
    game = GameController.fromUserInput()
    game.run()

if __name__ == '__main__':
    main()
