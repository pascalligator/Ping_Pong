import pygame
pygame.font.init()
import pickle
import P_Vec2
class Display():
    def __init__(self):
        self.display = P_Vec2.Vec2(800, 600)
        self.screen = pygame.display.set_mode((self.display.x, self.display.y))
        pygame.display.set_caption("Pong")
    def handle_events(self, nets):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        file = []
                        file.append(nets)
                        pickle.dump(file, open("save.p", "wb"))
                    elif event.key == pygame.QUIT:
                        return False
                    elif event.key == pygame.K_w and self.index_left < len(nets) - 1:
                        self.index_left += 1
                    elif event.key == pygame.K_s and self.index_left > 0:
                        self.index_left -= 1
                    elif event.key == pygame.K_UP and self.index_right < len(nets) - 1:
                        self.index_right += 1
                    elif event.key == pygame.K_DOWN and self.index_right > 0:
                        self.index_right -= 1
    def show_everything(me, self):
        me.screen.fill((190, 190, 190))
        me.player1(self)
        me.player2(self)
        me.ball(self)
        me.show_score(self.scoore.x, self.scoore.y)
        me.show_individual_left(self.index_left)
        me.show_individual_right(self.index_right)
        me.explanation()
        pygame.display.update()
    def player1(me, self):
        pygame.draw.rect(me.screen, (235, 97, 6), (self.player1_pos.x, self.player1_pos.y, int(self.player_size.x), self.player_size.y), 0)
    def player2(me, self):
        pygame.draw.rect(me.screen, (235, 97, 6), (self.player2_pos.x, self.player2_pos.y, int(self.player_size.x), self.player_size.y), 0)
    def ball(me, self):
        pygame.draw.circle(me.screen, (235, 97, 6), (round(self.ball_pos.x), round(self.ball_pos.y)), int(self.ball_size), 0)
    def show_score(me, s1, s2):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(s1)+":"+str(s2), 1, (0,0,0))
        me.screen.blit(label, (me.display.x*0.5, 30))
    def show_text(me, text):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(text, 1, (0,0,0))
        me.screen.blit(label, (x, y))
    def show_individual_left(me, index):
        text = "Individual number: " + str(index)
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(text, 1, (0,0,0))
        me.screen.blit(label, (int(me.display.x*0.05), int(me.display.y*0.1)))
    def show_individual_right(me, index):
        text = "Individual number: " + str(index)
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(text, 1, (0,0,0))
        me.screen.blit(label, (int(me.display.x*0.7), int(me.display.y*0.1)))
    def explanation(me):
        text = "save: 'Esc' / change left network: 'w' and 's' / change right network: 'UP' and 'Down'"
        myfont = pygame.font.SysFont("monospace", 15)
        label  = myfont.render(text, 1, (0,0,0))
        me.screen.blit(label, (0, 0))