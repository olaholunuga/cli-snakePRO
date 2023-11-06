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

    def main(self):
        """initialization
        """
        self.screen = curses.initscr()
        curses.cbreak
        curses.noecho
        self.screen.border()
        self.screen.nodelay(True)
        self.screen.keypad(True)
        curses.curs_set(0)

    def createWindow(self):
        """_summary_
        """
        self.screen.clear()
        self.gameWindow = curses.newwin(self.height + 1,
                                        self.width + 1, 0, 0)
        self.gameWindow.border()
        self.gameWindow.keypad(True)
        self.gameWindow.timeout(100)
        self.gameWindow.addstr(5, 5, "To Start the game PRESS 'c'")
        self.gameWindow.refresh()

        # definition of direction - d
        d = curses.KEY_RIGHT
        snk = self.gameSnake
        sh = self.height
        sw = self.width
        food = (int(sh / 2), int(sw / 2))
        self.power(d, snk, sh, sw, food)

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
