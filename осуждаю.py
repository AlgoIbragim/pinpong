import pygame

pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('pinpong')
back = (255, 136, 255)
window.fill(back)
#clock = pygame.time.Clock()
FPS = 60
game = True
clllock = pygame.time.Clock()
finish = False
pygame.font.init()
font3 = pygame.font.SysFont(None, 100)




class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (75, 49))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (72, 95))
    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        if keys_pressed[pygame.K_s] and self.rect.y < 410:
            self.rect.y += self.speed
class Player2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (72, 95))
    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        if keys_pressed[pygame.K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, ball_image, ball_x, ball_y, ball_speed_x, ball_speed_y):
        super().__init__(ball_image, ball_x, ball_y, 0)
        self.image = pygame.transform.scale(pygame.image.load(ball_image), (95, 95))
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y
        self.final=False

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.bottom >= 500 or self.rect.top <= 0:
            self.speed_y *= -1
        
        if pygame.sprite.collide_rect(self, rocket) or pygame.sprite.collide_rect(self, rocket2):
            self.speed_x *= -1
        
    def final1(self):
        if self.rect.x > 700:
            text_superwin = font3.render('PLAYER2 LOSE', 1, (255, 0, 0))
            window.blit(text_superwin, (95, 225))
            self.finish = True
            return False
        if self.rect.x < -100:
            text_superwin = font3.render('PLAYER1 LOSE', 1, (255, 0, 0))
            window.blit(text_superwin, (95, 225))
            self.finish = True
            return False
        else:
            return True
            



rocket = Player('platform.png', -23, 250, 5)
rocket2 = Player2('platform2.png', 650, 250, 5)
ball = Ball('ball.png', 350, 250, 3, 5)

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False


    if ball.final1():
        window.fill(back)
        rocket.update()
        rocket.reset()
        rocket2.update()
        rocket2.reset()
        ball.update()
        ball.reset()
        ball.final1()


        



    pygame.display.update()
    clllock.tick(FPS)
