class InputOutput():
    def ask_net_left(self):
        inputs = []
        inputs.append((self.player1_pos.x/self.display.x)*2-1)
        inputs.append((self.player1_pos.y/self.display.y)*2-1)
        inputs.append((self.player2_pos.x/self.display.x)*2-1)
        inputs.append((self.player2_pos.y/self.display.y)*2-1)
        inputs.append((self.ball_pos.x/self.display.x)*2-1)
        inputs.append((self.ball_pos.y/self.display.y)*2-1)
        inputs.append((self.ball_vel.x/3))
        inputs.append((self.ball_vel.y/1))
        changes = self.left.net(inputs)
        if changes[0] > 0 and changes[1] > 0 or changes[0] < 0 and changes[1] < 0:
            self.player1_vel.x = 0
        if changes[0] > 0 and changes[1] < 0:
            self.player1_vel.x = -5
        if changes[0] < 0 and changes[1] > 0:
            self.player1_vel.x = 5
        if changes[2] > 0 and changes[3] > 0 or changes[2] < 0 and changes[3] < 0:
            self.player1_vel.y = 0
        if changes[2] > 0 and changes[3] < 0:
            self.player1_vel.y = -5
        if changes[2] < 0 and changes[3] > 0:
            self.player1_vel.y = 5
    def ask_net_right(self):
        inputs = []
        inputs.append((self.player2_pos.x/self.display.x)*2-1)
        inputs.append((self.player2_pos.y/self.display.y)*2-1)
        inputs.append((self.player1_pos.x/self.display.x)*2-1)
        inputs.append((self.player1_pos.y/self.display.y)*2-1)
        inputs.append((self.ball_pos.x/self.display.x)*2-1)
        inputs.append((self.ball_pos.y/self.display.y)*2-1)
        inputs.append((self.ball_vel.x/3))
        inputs.append((self.ball_vel.y/1))
        for i in range(len(inputs)):
            inputs[i] *= -1
        changes = self.right.net(inputs)
        if changes[0] > 0 and changes[1] > 0 or changes[0] < 0 and changes[1] < 0:
            self.player2_vel.x = 0
        if changes[0] > 0 and changes[1] < 0:
            self.player2_vel.x = -5
        if changes[0] < 0 and changes[1] > 0:
            self.player2_vel.x = 5
        if changes[2] > 0 and changes[3] > 0 or changes[2] < 0 and changes[3] < 0:
            self.player2_vel.y = 0
        if changes[2] > 0 and changes[3] < 0:
            self.player2_vel.y = -5
        if changes[2] < 0 and changes[3] > 0:
            self.player2_vel.y = 5
        self.player2_vel.x *= -1
        self.player2_vel.y *= -1
