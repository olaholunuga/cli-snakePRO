import curses, traceback, random


class Screen():
    """screen class using curses
    """
    def __init__(self) -> None:
        self.width = 90
        self.height = 30
        sh_y = round(int(self.height / 2))
        sh_x = round(int(self.width / 4))
        self.snakeBody = [(sh_y, sh_x),
                          (sh_y, sh_x - 1),
                          (sh_y, sh_x - 2)]
        self.gameSnake = self.snakeBody
        self.score = 0


if __name__ == "__main__":
    try:
        window = Screen()
        window.main()
        window.createWindow()
        window.closewin()
    except Exception as err:
        window = Screen()
        window.main()
        window.closewin()
        traceback.print_exc()
        print(err)
