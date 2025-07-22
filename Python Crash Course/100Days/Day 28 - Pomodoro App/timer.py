


class Pomo:
    def __init__(self):
        self.count = 0

    def start_timer(self):
        from main import count_down
        if self.count < 4:
            count_down(5)
            self.count += 1