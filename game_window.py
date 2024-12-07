import random
import pygame
import cv2
import math

#这个是目前已经可以正常运行的，但是缺乏1，攻击特效声音。2，如何清空上一句残留下的内存

pygame.init()


WITH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WITH, HEIGHT))


pygame.display.set_caption("Flight Simulator")
#背景图片的导入

cap=cv2.VideoCapture("/Users/liujiu/python/flight simulator/material/bg.mov")
fps=int(cap.get(cv2.CAP_PROP_FPS))
width=int(cap.get(WITH))
height=int(cap.get(HEIGHT))

#背景音乐的导入
pygame.mixer.music.load("/Users/liujiu/python/flight simulator/material/bg01.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

clock = pygame.time.Clock()

#背景音乐的暂停
button_bg = pygame.Rect(600,5,40,15)
font = pygame.font.Font(None, 15)
button_text = font.render("stop", True, (255,255,255)) 

#飞机的图形导入

feiji_bg= pygame.image.load("/Users/liujiu/python/flight simulator/material/player.png")
feiji_x= 300
feiji_y= 400
feiji_speed= 0
current_plane_image = feiji_bg
#第二级别的飞机形状
feiji_bg_new= pygame.image.load("/Users/liujiu/python/flight simulator/material/feiji_up.png")



#创建敌人
class enemy_1:
    def __init__(self):
        self.img=pygame.image.load("/Users/liujiu/python/flight simulator/material/enemy.png")
        self.x=random.randint(50,590)
        self.y=random.randint(300,480)
        self.speed=random.randint(1,2)
    def move(self):
        self.y +=self.speed
        if self.y >480 :
            self.reset_position()

    def reset_position(self): 
        self.x=random.randint(0,600)
        self.y=random.randint(20,50)

class enemy_2:
    def __init__(self):
        self.img=pygame.image.load("/Users/liujiu/python/flight simulator/material/guaiwu.png")
        self.x=random.randint(50,590)
        self.y=random.randint(300,480)
        self.speed=random.randint(1,2)
    def move(self):
        self.y +=self.speed
        if self.y >480 :
            self.reset_position()

    def reset_position(self):
        self.x=random.randint(0,600)
        self.y=random.randint(20,50)

enemies=[enemy_1() for _ in range(2)] + [enemy_2() for _ in range(2)]

def show_enmies():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.move()
        
        if e.y <0:
            game_over()
        
#子弹类
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("/Users/liujiu/python/flight simulator/material/bullet.png")
        self.speed = 10
        
    def move(self):
        self.y -= self.speed
    def is_off_screen(self):
        return self.y < 0

bullets = []
#发射子弹的
def fire_bullet():
    bullet=Bullet(feiji_x+feiji_bg.get_width()//3, feiji_y)
    bullets.append(bullet)
    
def show_bullets():
    for bullet in bullets:
        screen.blit(bullet.img, (bullet.x, bullet.y))
        bullet.move()
        if bullet.is_off_screen():
            bullets.remove(bullet)
                
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

score = 0

def check_collision():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if distance(bullet.x, bullet.y, enemy.x, enemy.y) < 30:
                enemy.reset_position()
                bullets.remove(bullet)
                score += 1                
                

def game_over():
    print("game over")
    global running
    running = False
    

def show_score():
    score_text = font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(score_text, (10,10))

def update_plat():
    global feiji_bg
    if score == 10:
        feiji_bg = feiji_bg_new


running = True
while running:
    screen.fill((0,0,0))
    ret,frame=cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret,frame=cap.read()
    if ret:
        frame = cv2.flip(frame,-1)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface =pygame.surfarray.make_surface(frame_rgb)
        frame_surface = pygame.transform.rotate(frame_surface, 90)
        screen.blit(frame_surface, (0, 0))
    pygame.draw.rect(screen, (200,0,0), button_bg)  
    
    screen.blit(button_text, (button_bg.x+10, button_bg.y+5))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                feiji_speed = -10
            if event.key == pygame.K_RIGHT:
                feiji_speed = 10
            if event.key == pygame.K_SPACE:
                fire_bullet()
        #如果没有了这一行代码，意味着如果不松手，则一直往左或往右移动-5或5。只有松开了按键才能停止移动        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                feiji_speed = 0
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_bg.collidepoint(event.pos):
                pygame.mixer.music.stop()
                print("music stop")
                running = False

    feiji_x += feiji_speed
    if feiji_x < 0:
        feiji_x = 0
    if feiji_x > 580:
        feiji_x = 580

    update_plat()
    screen.blit(feiji_bg, (feiji_x, feiji_y))




    show_enmies()
    show_bullets()
    check_collision()
    show_score()
    
    
    pygame.display.update()
    clock.tick(fps)

cap.release()
pygame.quit()