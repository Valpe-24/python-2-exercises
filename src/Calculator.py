class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = 0

    def add(self):
        self.result = self.x + self.y

    def sub(self):
        self.result = self.x - self.y

    def mul(self):
        self.result = self.x * self.y

    def div(self):
        self.result = self.x / self.y

    @property
    def get_result(self):
        return self.result



