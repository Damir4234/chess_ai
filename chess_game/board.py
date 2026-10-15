from figure import Pawn


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

            figure_on_final_coordinates = next((i for i in self.figures if i.position == final_coordinates), None)

            for i in self.figures:

                if i.position == initial_coordinates:

                    if isinstance(i, Pawn):

                        if i.move(final_coordinates):

                            if i.position[0] == final_coordinates[0]:

                                if figure_on_final_coordinates != None:

                                    print("Это поле занято")

                                elif self.is_path_clear(initial_coordinates, final_coordinates):

                                    i.position = final_coordinates

                                else:

                                    print("На пути преграда")
                            
                            elif figure_on_final_coordinates != None:

                                if i.color != figure_on_final_coordinates.color:

                                    i.position = final_coordinates
                                    print("Взятие фигуры")

                                else:

                                    print("Ход невозможен")



    def is_path_clear(self, initial, final):

        x = initial[0]
        y = initial[1]

        step = 1 if final[1] > initial[1] else -1

        for current_y in range(initial[1] + step, final[1], step):

            position = [x, current_y]

            for i in self.figures:

                if i.position == position:

                    return False

        return True

              


    def __repr__(self):


        return f"Список: {self.figures}"
