import P_Vec2
import random
class Position_Control():
    def scramble(self):
        if self.collision_left == True and self.collision_right == True:
            self.reset()
    def group(self):
        if abs(self.player1_pos.x - self.player2_pos.x) < self.display.x/10 and abs(self.player1_pos.y - self.player2_pos.y) < self.player_size.y:
            return True
    def reset(self, starts_each, current_start, i):
        self.player1_pos = P_Vec2.Vec2(self.display.x * 0.05, self.display.y*0.5)
        self.player2_pos = P_Vec2.Vec2(self.display.x * 0.95, self.display.y*0.5)
        self.player1_vel = P_Vec2.Vec2(0, 0)
        self.player2_vel = P_Vec2.Vec2(0, 0)
        self.ball_pos = P_Vec2.Vec2(self.display.x * 0.5, self.display.y *0.5)
        y = (current_start + 1) * 4.5 / (starts_each - 1) - 2.25
        self.ball_vel = P_Vec2.Vec2((2 * i * self.ball_maxVel) - self.ball_maxVel, y)
    def reset_initial(self, i):
        self.player1_pos = P_Vec2.Vec2(self.display.x * 0.05, self.display.y*0.5)
        self.player2_pos = P_Vec2.Vec2(self.display.x * 0.95, self.display.y*0.5)
        self.player1_vel = P_Vec2.Vec2(0, 0)
        self.player2_vel = P_Vec2.Vec2(0, 0)
        self.ball_pos = P_Vec2.Vec2(self.display.x * 0.5, self.display.y *0.5)
        self.ball_vel = P_Vec2.Vec2((i*self.ball_maxVel) - self.ball_maxVel, -2.25)
    def reset_random(self):
        self.player1_pos = P_Vec2.Vec2(self.display.x * 0.05, self.display.y*0.5)
        self.player2_pos = P_Vec2.Vec2(self.display.x * 0.95, self.display.y*0.5)
        self.player1_vel = P_Vec2.Vec2(0, 0)
        self.player2_vel = P_Vec2.Vec2(0, 0)
        self.ball_pos = P_Vec2.Vec2(self.display.x * 0.5, self.display.y *0.5)
        self.ball_vel = P_Vec2.Vec2(random.choice([-3, 3]), random.uniform(-2.25, 2.25))
    def update(self):
        self.ball_pos.x += self.ball_vel.x
        self.ball_pos.y += self.ball_vel.y
        self.player1_pos.x += self.player1_vel.x
        self.player1_pos.y += self.player1_vel.y
        self.player2_pos.x += self.player2_vel.x
        self.player2_pos.y += self.player2_vel.y
    def ball_decelleration(self):
        if abs(self.ball_vel.x) > self.ball_maxVel:
            self.ball_vel.x = self.ball_vel.x*0.975
        if abs(self.ball_vel.x) < self.ball_maxVel/1.025:
            self.ball_vel.x *= 1.025
    def only_oldschool(self):
        self.player1_vel.x = 0
        self.player2_vel.x = 0