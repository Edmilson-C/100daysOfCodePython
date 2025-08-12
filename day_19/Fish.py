import Animal


class Fish(Animal):
    def __init__(self):
        super().__init()

    def breathe(self):
        super().breathe()
        print("Under water")