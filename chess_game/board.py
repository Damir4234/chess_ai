class Board:

    def __init__(self):

        self.figures = []

    def add_figure(self, figure):

        for i in self.figures:

            if i.position == figure.position:

                return

        if all(1 <= i <= 8 for i in figure.position):
        
            self.figures.append(figure)

        else:

            print("Такой позиции на доске не существует")
    
    
    def __repr__(self):

        return f"Список: {self.figures}"
