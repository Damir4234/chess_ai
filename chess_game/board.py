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
    
    
    def move_on_board(self, initial_coordinates, final_coordinates):


        if all(1 <= i <= 8 for i in initial_coordinates) and all(1 <= i <= 8 for i in final_coordinates):

            for i in self.figures:

                if i.position == initial_coordinates:

                    if i.move(final_coordinates):

                        i.position = final_coordinates
                        print("Позиция измененна")

                    else:

                        print("Перемещение не допустимо")

                # else:

                #     print("Эта позиция пустая")

        else:

            print("Таких координат не существует")



    def __repr__(self):


        return f"Список: {self.figures}"
