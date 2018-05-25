class Collisions():
    def goal_left_bounce(self):
        if self.ball_pos.x - self.ball_size < 0:
            self.ball_pos.x = self.ball_size
            self.ball_vel.x = (-1)*self.ball_vel.x
            return True
        else:
            return False
    def goal_right_bounce(self):
        if self.ball_pos.x + self.ball_size > self.display.x:
            self.ball_pos.x = self.display.x - self.ball_size
            self.ball_vel.x = (-1)*self.ball_vel.x
            return True
        else:
            return False
    def collision_ball_player_left(self):
        if self.ball_pos.x + self.ball_size > self.player1_pos.x and self.ball_pos.x - self.ball_size < self.player1_pos.x + self.player_size.x:
            if self.ball_pos.y + self.ball_size > self.player1_pos.y and self.ball_pos.y - self.ball_size < self.player1_pos.y + self.player_size.y:
                self.ball_pos.x = self.player1_pos.x + self.player_size.x + self.ball_size
                self.ball_vel.x = abs(self.ball_vel.x)
                self.ball_vel.x += self.player1_vel.x
                return True
    def collision_ball_player_right(self):
        if self.ball_pos.x + self.ball_size > self.player2_pos.x and self.ball_pos.x - self.ball_size < self.player2_pos.x + self.player_size.x:
            if self.ball_pos.y + self.ball_size > self.player2_pos.y and self.ball_pos.y - self.ball_size < self.player2_pos.y + self.player_size.y:
                self.ball_pos.x = self.player2_pos.x - self.ball_size
                self.ball_vel.x = (-1)*abs(self.ball_vel.x)
                self.ball_vel.x += self.player2_vel.x
                return True
    def display_collision(self):
        if self.player1_pos.x + self.player_size.x > self.display.x:
            self.player1_pos.x = self.display.x - self.player_size.x
            self.player1_vel.x = 0
        if self.player1_pos.x < 0:
            self.player1_pos.x = 0
            self.player1_vel.x = 0
        if self.player1_pos.y + self.player_size.y > self.display.y:
            self.player1_pos.y = self.display.y - self.player_size.y
            self.player1_vel.y = 0
        if self.player1_pos.y < 0:
            self.player1_pos.y = 0
            self.player1_vel.y = 0
        if self.player2_pos.x + self.player_size.x > self.display.x:
            self.player2_pos.x =self.display.x - self.player_size.x
            self.player2_vel.x = 0
        if self.player2_pos.x < 0:
            self.player2_pos.x = 0
            self.player2_vel.x = 0
        if self.player2_pos.y + self.player_size.y > self.display.y:
            self.player2_pos.y = self.display.y - self.player_size.y
            self.player2_vel.y = 0
        if self.player2_pos.y < 0:
            self.player2_pos.y = 0
            self.player2_vel.y = 0
        if self.ball_pos.y < self.ball_size:
            self.ball_pos.y = self.ball_size
            self.ball_vel.y *= -1
        if self.ball_pos.y > self.display.y - self.ball_size:
            self.ball_pos.y = self.display.y - self.ball_size
            self.ball_vel.y *= -1
