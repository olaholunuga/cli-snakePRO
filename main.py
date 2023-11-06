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

    def power(self, d, snk, sh, sw, food):
        while True:
            key = self.gameWindow.getch()
            if key == ord("c"):
                #self.gameWindow.addch(food[0], food[1], "O")
                while True:
                    nhead = None
                    if snk[0][0] in (0, sh) or snk[0][1] in (0, sw) or snk[0] in snk[1:]:
                        # We crashed
                        curses.endwin()
                        print("GAME OVER")
                        quit()
                    key = self.gameWindow.getch()
                    if key == ord("d"):
                        curses.endwin()
                        print("GAME OVER")
                        quit()
                    food, det = self.shake(snk, sh, sw, food)
                    if key == -1:
                        d = d
                    else:
                        d = key
                    oldhead = snk[0]
                    if d == curses.KEY_RIGHT or d == 454:
                        nhead = (oldhead[0], oldhead[1] + 1)
                    if d == curses.KEY_LEFT or d == 452:
                        nhead = (oldhead[0], oldhead[1] - 1)
                    if d == curses.KEY_UP or d == 450:
                        nhead = (oldhead[0] - 1, oldhead[1])
                    if d == curses.KEY_DOWN or d == 456:
                        nhead = (oldhead[0] + 1, oldhead[1])
                    self.gameSnake.insert(0, nhead)
                    if det == 1:
                        snakeTail = self.gameSnake.pop()
                        tail_y, tail_x = snakeTail
                        self.render(sw, food, det, tail_y, tail_x)
                    else:
                        tail_y, tail_x = 0, 0
                        self.render(sw, food, det, tail_y, tail_x)

    def render(self, sw, food, det, tail_y=0, tail_x=0):
        if det == -1:
            self.gameWindow.addch(tail_y, tail_x, " ")
        self.gameWindow.clear()
        self.gameWindow.border()
        self.gameWindow.addch(food[0], food[1], "x")
        self.gameWindow.addstr(0, round(sw * 0.8), F"SCORE: {self.score}")
        for x in self.gameSnake:
            self.gameWindow.addch(x[0], x[1], curses.ACS_BLOCK)
        self.gameWindow.refresh()
        
    def shake(self, snk, sh, sw, food):
        if snk[0] == food:
            food = None
            self.score += 1
            while food is None:
                new_food = (random.randint(1, sh - 1), random.randint(1, sw - 1))
                if new_food in snk:
                    new_food = None
                else:
                    food = new_food
            det = -1
        else:
            det = 1
        return food, det

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
