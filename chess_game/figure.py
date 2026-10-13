class Figure:


    def __init__(self, color, position):

        self.color = color
        self.position = position


    def move(self): pass


class Pawn(Figure):


    def __init__(self, color, position):
        
        super().__init__(color, position)
        self.was_move = False

    
    def move(self, future_position): # получает позицию на которую хотят перместить 

        if self.color == "white":

            possible_moves = [] # список всех возможных позиций исходя от настоящей 

            new_position = self.position.copy()
            new_position[1] += 1
            possible_moves.append(new_position)

            hit_position_1 = self.position.copy()
            hit_position_1[0] -= 1
            hit_position_1[1] += 1
            possible_moves.append(hit_position_1)

            hit_position_2 = self.position.copy()
            hit_position_2[0] += 1
            hit_position_2[1] += 1
            possible_moves.append(hit_position_2)


            if self.was_move == False: # проверяем был ли уже ранее сделан ход у пешки, так как первый ход за игру может быть на 2 клетки вперед 
                
                new_position = self.position.copy()
                new_position[1] += 2
                possible_moves.append(new_position)           

            
            return future_position in possible_moves

        elif self.color == "black":
            
            possible_moves = [] # список всех возможных позиций исходя от настоящей 
            
            new_position = self.position.copy()
            new_position[1] -= 1
            possible_moves.append(new_position)

            hit_position_1 = self.position.copy()
            hit_position_1[0] -= 1
            hit_position_1[1] -= 1
            possible_moves.append(hit_position_1)

            hit_position_2 = self.position.copy()
            hit_position_2[0] += 1
            hit_position_2[1] -= 1
            possible_moves.append(hit_position_2)

            if self.was_move == False: # проверяем был ли уже ранее сделан ход у пешки, так как первый ход за игру может быть на 2 клетки вперед 
                
                new_position = self.position.copy()
                new_position[1] -= 2
                possible_moves.append(new_position)           

            
            return future_position in possible_moves

    def __repr__(self):

        return f"(Пешка {self.color}, позиция: {self.position})"

