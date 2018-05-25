class Fitness():
    def fitness_add(self, show = False):
        self.history_ball_x.append(self.ball_pos.x)
        self.history_ball_y.append(self.ball_pos.y)
        self.history_player1_x.append(self.player1_pos.x)
        self.history_player1_y.append(self.player1_pos.y)
        self.history_player2_x.append(self.player2_pos.x)
        self.history_player2_y.append(self.player2_pos.y)
        before_left = self.left.fitness
        before_right = self.right.fitness
        if self.goal_left_player == True:
            distances = []
            for i in range(len(self.history_ball_x)):
                d_x = self.history_ball_x[i] - self.history_player1_x[i]
                d_y = self.history_ball_y[i] - self.history_player1_y[i]
                distances.append(d_x**2 + d_y**2)
            distances.sort()
            self.left.fitness += 1-(distances[0]**0.5/(self.display.y**2)**0.5)
            self.right.fitness += 0.5
            Fitness.delete_history(self)
        if self.goal_right == True:
            distances = []
            for i in range(len(self.history_ball_x)):
                d_x = self.history_ball_x[i] - self.history_player2_x[i]
                d_y = self.history_ball_y[i] - self.history_player2_y[i]
                distances.append(d_x**2 + d_y**2)
            distances.sort()
            self.right.fitness += 1-(distances[0]**0.5/(self.display.y**2)**0.5)
            self.left.fitness += 0.5
            Fitness.delete_history(self)
        if self.collision_left == True and self.group != True:
            if len(self.history_ball_x) > 1:
                if self.history_ball_x[-1] - self.history_ball_x[-2] < 0:
                    self.left.fitness += 1.5
            else:
                self.left.fitness += 1.5
        if self.collision_right == True and self.group != True:
            if len(self.history_ball_x) > 1:
                if self.history_ball_x[-1] - self.history_ball_x[-2] > 0:
                    self.right.fitness += 1.5
            else:
                self.right.fitness += 1.5
        if show == True:
            dif = self.left.fitness - before_left
            dif_right = self.right.fitness - before_right
            if dif != 0.0 or dif_right != 0.0:
                print("Player1: ", dif)
                print("Player2. ", dif_right)
    def delete_history(self):
        del self.history_ball_x[:]
        del self.history_ball_y[:]
        del self.history_player1_x[:]
        del self.history_player1_y[:]
        del self.history_player2_x[:]
        del self.history_player2_y[:]
