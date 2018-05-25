import pygame
import random
import pickle
import P_Vec2
import P_Functions
import P_Collisions
import P_Position_Control
import P_Input_Output
import P_Fitness
import P_Display
class Training():
    def __init__(self):
        self.ball_maxVel = 3
        self.ball_size = 10
        self.player_size = P_Vec2.Vec2(8, 60)
        self.display = P_Vec2.Vec2(800, 600)
        P_Position_Control.Position_Control.reset_initial(self, 0)
        self.history_ball_x = []
        self.history_ball_y = []
        self.history_player1_x = []
        self.history_player1_y = []
        self.history_player2_x = []
        self.history_player2_y = []
    def play(self, left, right, starts_each):
        self.left = left
        self.right = right
        #self.deviation = []
        #self.fitness_before = self.left.fitness
        for i in range(2):
            if i == 1:
                self.ball_vel.x = self.ball_maxVel
            current_start = 0
            while current_start < starts_each:
                P_Input_Output.InputOutput.ask_net_left(self)
                P_Input_Output.InputOutput.ask_net_right(self)
                P_Position_Control.Position_Control.only_oldschool(self) #nur bewegung auf y-Achse
                P_Position_Control.Position_Control.update(self)
                self.goal_left_player = P_Collisions.Collisions.goal_left_bounce(self)
                self.goal_right = P_Collisions.Collisions.goal_right_bounce(self)
                P_Position_Control.Position_Control.ball_decelleration(self)
                P_Collisions.Collisions.display_collision(self)
                self.collision_left = P_Collisions.Collisions.collision_ball_player_left(self)
                self.collision_right = P_Collisions.Collisions.collision_ball_player_right(self)
                P_Position_Control.Position_Control.scramble(self)
                self.group = P_Position_Control.Position_Control.group(self)
                P_Fitness.Fitness.fitness_add(self)
                if self.goal_left_player == True or self.goal_right == True:
                    #self.deviation.append(self.left.fitness - self.fitness_before)
                    #self.fitness_before = self.left.fitness
                    P_Position_Control.Position_Control.reset(self, starts_each, current_start, i)
                    current_start += 1
        #self.deviation.sort()
        #print(self.deviation[-1])
    def show(self, nets):
        self.window = P_Display.Display()
        self.index_left = 0
        self.index_right = 1
        self.scoore = P_Vec2.Vec2(0, 0)
        clock = pygame.time.Clock()
        counter = 0
        running = True
        while not running == False:
            running = P_Display.Display.handle_events(self, nets)
            self.left = nets[self.index_left]
            self.right = nets[self.index_right]
            P_Input_Output.InputOutput.ask_net_left(self)
            P_Input_Output.InputOutput.ask_net_right(self)
            P_Position_Control.Position_Control.only_oldschool(self) #nur bewegung auf y-Achse
            P_Position_Control.Position_Control.update(self)
            self.goal_left_player = P_Collisions.Collisions.goal_left_bounce(self)
            self.goal_right = P_Collisions.Collisions.goal_right_bounce(self)
            P_Position_Control.Position_Control.ball_decelleration(self)
            P_Collisions.Collisions.display_collision(self)
            self.collision_left = P_Collisions.Collisions.collision_ball_player_left(self)
            self.collision_right = P_Collisions.Collisions.collision_ball_player_right(self)
            P_Position_Control.Position_Control.scramble(self)
            self.group = P_Position_Control.Position_Control.group(self)
            P_Fitness.Fitness.fitness_add(self, True)
            if self.collision_right == True:
                print("collision right")
            if self.collision_left == True:
                print("collision left")
            if self.goal_left_player == True:
                self.scoore.y += 1
                P_Position_Control.Position_Control.reset_random(self)                
                counter += 1
            if self.goal_right == True:
                self.scoore.x += 1
                P_Position_Control.Position_Control.reset_random(self)
                counter += 1
            self.window.show_everything(self)
            #P_Functions.player1(self.player1_pos.x, self.player1_pos.y, self.player_size, gameDisplay)
            #P_Functions.player2(self.player2_pos.x, self.player2_pos.y, self.player_size, gameDisplay)
            #P_Functions.ball(self.ball_pos.x, self.ball_pos.y, self.ball_size, gameDisplay)
            #P_Functions.show_score(self.scoore.x, self.scoore.y, gameDisplay, self.display)
            #P_Functions.show_text("Individual number: "+str(self.index_left), int(self.display.x*0.05), int(self.display.y*0.1), gameDisplay)
            #P_Functions.show_text("Individual number: "+str(self.index_right), int(self.display.x*0.7), int(self.display.y*0.1), gameDisplay)
            #P_Functions.explanation(gameDisplay)
            #pygame.display.update()
            clock.tick(50)