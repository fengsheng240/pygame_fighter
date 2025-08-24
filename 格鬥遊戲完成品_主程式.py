import pygame
from pygame.locals import QUIT
import sys
from pygame import mixer
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

mixer.init()
pygame.init()


SCREEN_WIDTH=1000  ####遊戲視窗大小
SCREEN_HEIGHT=600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  ###建立遊戲視窗
pygame.display.set_caption("格鬥遊戲")
clock=pygame.time.Clock()  ###設置偵數
FPS=60
count_font=pygame.font.Font("字型/turok.ttf",80)   ###文字字型
score_font=pygame.font.Font("字型/turok.ttf",30)
sword_fx=pygame.mixer.Sound("音樂與音效/assets_audio_sword.wav")  ###角色攻擊音效
sword_fx.set_volume(0.5)
magic_fx=pygame.mixer.Sound("音樂與音效/assets_audio_magic.wav")
magic_fx.set_volume(0.75)
pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###背景音樂
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0.0,5000)
warrior_sheet=pygame.image.load("圖片和部份圖示/warrior.png").convert_alpha()   ##角色1
wizard_sheet=pygame.image.load("圖片和部份圖示/wizard.png").convert_alpha()   ##角色2

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("字型/font.ttf",size)


k1=pygame.image.load("角色圖示/ok.png").convert_alpha()  ###遊戲說明圖片
k2=pygame.transform.scale(k1,(1000,600))

A1=pygame.image.load("角色圖示/enumy1.png").convert_alpha()    #####角色圖示
bk1=pygame.transform.scale(A1,(65,90))
A2=pygame.image.load("角色圖示/enumy2.png").convert_alpha()
bk2=pygame.transform.scale(A2,(65,90))
A3=pygame.image.load("角色圖示/enumy3.png").convert_alpha()
bk3=pygame.transform.scale(A3,(65,90))
A4=pygame.image.load("角色圖示/enumy4.png").convert_alpha()
bk4=pygame.transform.scale(A4,(65,90))
A5=pygame.image.load("角色圖示/enumy5.png").convert_alpha()
bk5=pygame.transform.scale(A5,(110,100))
A6=pygame.image.load("角色圖示/enumy6.png").convert_alpha()
bk6=pygame.transform.scale(A6,(65,90))
A7=pygame.image.load("角色圖示/enumy7.png").convert_alpha()
bk7=pygame.transform.scale(A7,(65,90))
A8=pygame.image.load("角色圖示/enumy8.png").convert_alpha()
bk8=pygame.transform.scale(A8,(65,90))
A9=pygame.image.load("角色圖示/enumy9.png").convert_alpha()
bk9=pygame.transform.scale(A9,(65,90))


E1=pygame.image.load("角色圖示/enumy11.png").convert_alpha()
bkg1=pygame.transform.scale(E1,(65,90))
E2=pygame.image.load("角色圖示/enumy22.png").convert_alpha()
bkg2=pygame.transform.scale(E2,(65,90))
E3=pygame.image.load("角色圖示/enumy33.png").convert_alpha()
bkg3=pygame.transform.scale(E3,(65,90))
E4=pygame.image.load("角色圖示/enumy44.png").convert_alpha()
bkg4=pygame.transform.scale(E4,(65,90))
E5=pygame.image.load("角色圖示/enumy55.png").convert_alpha()
bkg5=pygame.transform.scale(E5,(110,100))
E6=pygame.image.load("角色圖示/enumy66.png").convert_alpha()
bkg6=pygame.transform.scale(E6,(65,90))
E7=pygame.image.load("角色圖示/enumy77.png").convert_alpha()
bkg7=pygame.transform.scale(E7,(65,90))
E8=pygame.image.load("角色圖示/enumy88.png").convert_alpha()
bkg8=pygame.transform.scale(E8,(65,90))
E9=pygame.image.load("角色圖示/enumy99.png").convert_alpha()
bkg9=pygame.transform.scale(E9,(65,90))






bg_image=pygame.image.load("圖片和部份圖示/background.jpg").convert_alpha()####背景圖片

BG = pygame.image.load("圖片和部份圖示/Background.png").convert_alpha()
scaled_bg=pygame.transform.scale(BG,(1000,600))
screen.blit(scaled_bg,(0,0))

B1=pygame.image.load("背景圖/城堡.jpg").convert_alpha()  ####背景選單圖示
bg1=pygame.transform.scale(B1,(175,105))

B2=pygame.image.load("背景圖/惡魔城.jpg").convert_alpha()
bg2=pygame.transform.scale(B2,(175,105))

B3=pygame.image.load("背景圖/城鎮道路.jpg").convert_alpha()
bg3=pygame.transform.scale(B3,(175,105))

B4=pygame.image.load("背景圖/天堂.jpg").convert_alpha()
bg4=pygame.transform.scale(B4,(175,105))

B5=pygame.image.load("背景圖/森林.jpg").convert_alpha()
bg5=pygame.transform.scale(B5,(175,105))





WARRIOR_SIZE=162
WARRIOR_SCALE=4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

WARRIOR_ANIMATION_STEPS=[10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEPS=[8,8,1,8,8,3,7]

x=10
y=10

def play1():
    class Button():
        def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))    ####得到圖片的矩陣大小
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        
        def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                return True
            return False

        def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color) ######文字變數=字體變數.render(文字,平滑值,文字顏色,背景顏色)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)
    while True:
        screen.blit(scaled_bg, (0,0))
        VS_TEXT = get_font(100).render("VS", True, "#b68f40")
        MENU_RECT = VS_TEXT.get_rect(center=(500, 170))
        screen.blit(VS_TEXT, MENU_RECT)

        A123= pygame.mouse.get_pos()#######獲取滑鼠當前的(x,y)座標
        
        PLAY1_BUTTON = Button(bk1, pos=(65, 55), text_input="", font=get_font(50), base_color="#b68f40", hovering_color="White")
        PLAY1_BUTTON.changeColor(A123)
        PLAY2_BUTTON = Button(bk2, pos=(175, 55), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY3_BUTTON = Button(bk3, pos=(285, 55), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY4_BUTTON = Button(bk4, pos=(65, 160), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY5_BUTTON = Button(bk5, pos=(175, 160), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY6_BUTTON = Button(bk6, pos=(285, 160), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY7_BUTTON = Button(bk7, pos=(65, 265), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY8_BUTTON = Button(bk8, pos=(175, 265), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        PLAY9_BUTTON = Button(bk9, pos=(285, 265), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        
        ENUMY1_BUTTON = Button(bkg1, pos=(715, 55), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY2_BUTTON = Button(bkg2, pos=(825, 55), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY3_BUTTON = Button(bkg3, pos=(935, 55), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY4_BUTTON = Button(bkg4, pos=(715, 160), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY5_BUTTON = Button(bkg5, pos=(825, 160), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY6_BUTTON = Button(bkg6, pos=(935, 160), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY7_BUTTON = Button(bkg7, pos=(715, 265), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY8_BUTTON = Button(bkg8, pos=(825, 265), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ENUMY9_BUTTON = Button(bkg9, pos=(935, 265), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        
        OPTIONS_BACK = Button(image=None, pos=(100, 550),text_input="BACK",font=get_font(40),base_color="#b68f40",hovering_color="red")
        OPTIONS_BACK.changeColor(A123)
        NEXT_BUTTON = Button(image=None, pos=(900, 550),text_input="NEXT",font=get_font(40),base_color="#b68f40",hovering_color="red")
        NEXT_BUTTON.changeColor(A123)
        BG1_BUTTON = Button(bg1, pos=(100, 415), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BG2_BUTTON = Button(bg2, pos=(300, 415), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BG3_BUTTON = Button(bg3, pos=(500, 415), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BG4_BUTTON = Button(bg4, pos=(700, 415), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BG5_BUTTON = Button(bg5, pos=(900, 415), text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")



        for button in [PLAY1_BUTTON,PLAY2_BUTTON,PLAY3_BUTTON,PLAY4_BUTTON,PLAY5_BUTTON,PLAY6_BUTTON,PLAY7_BUTTON,PLAY8_BUTTON,PLAY9_BUTTON,ENUMY1_BUTTON,ENUMY2_BUTTON,ENUMY3_BUTTON,ENUMY4_BUTTON,ENUMY5_BUTTON,ENUMY6_BUTTON,ENUMY7_BUTTON,ENUMY8_BUTTON,ENUMY9_BUTTON,OPTIONS_BACK,NEXT_BUTTON,BG1_BUTTON,BG2_BUTTON,BG3_BUTTON,BG4_BUTTON,BG5_BUTTON]:
            button.update(screen)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  ##### MOUSEBUTTONDOWN可以判斷滑鼠是否被按下
                if PLAY1_BUTTON.checkForInput(A123):
                    global warrior_sheet     
                    global WARRIOR_ANIMATION_STEPS
                    global WARRIOR_SIZE
                    global WARRIOR_SCALE
                    global WARRIOR_OFFSET
                    global WARRIOR_DATA
                    global x
                    global sword_fx
                    warrior_sheet=pygame.image.load("圖片和部份圖示/武士.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[8,8,1,6,6,4,6]
                    WARRIOR_SIZE=200
                    WARRIOR_SCALE=3.5
                    WARRIOR_OFFSET=[91,75]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/砍.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY2_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/原住民.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[10,8,1,7,6,3,11]
                    WARRIOR_SIZE=126.1
                    WARRIOR_SCALE=3.2
                    WARRIOR_OFFSET=[50,30]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/assets_audio_sword.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY3_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/warrior.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[10,8,1,7,7,3,7]
                    WARRIOR_SIZE=162
                    WARRIOR_SCALE=4
                    WARRIOR_OFFSET=[72,56]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/assets_audio_sword.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY4_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/wizard.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[8,8,1,8,8,3,7]
                    WARRIOR_SIZE=250
                    WARRIOR_SCALE=3
                    WARRIOR_OFFSET=[112,107]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/assets_audio_magic.wav")
                    sword_fx.set_volume(0.75)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY5_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/魔王.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[6,11,1,15,15,5,18]
                    WARRIOR_SIZE=160
                    WARRIOR_SCALE=3.7
                    WARRIOR_OFFSET=[70,111]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=30
                    sword_fx=pygame.mixer.Sound("音樂與音效/低吼.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/X2Download.app - 【貓咪大戰爭】BGM5 (128 kbps).mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY6_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/馬力歐.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[5,4,7,6,5,3,4]
                    WARRIOR_SIZE=114
                    WARRIOR_SCALE=2.7
                    WARRIOR_OFFSET=[50,17]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/馬力歐.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY7_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/Ninja .png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[9,8,10,6,8,2,5]
                    WARRIOR_SIZE=128
                    WARRIOR_SCALE=2.6
                    WARRIOR_OFFSET=[50,59]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/鞭子(強一點).wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY8_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/abc.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[7,8,11,4,14,3,6]
                    WARRIOR_SIZE=128
                    WARRIOR_SCALE=2.6
                    WARRIOR_OFFSET=[50,59]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/火.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif PLAY9_BUTTON.checkForInput(A123):
                    warrior_sheet=pygame.image.load("圖片和部份圖示/藍毛.png").convert_alpha()
                    WARRIOR_ANIMATION_STEPS=[3,3,3,3,3,5,3]
                    WARRIOR_SIZE=114
                    WARRIOR_SCALE=1.7
                    WARRIOR_OFFSET=[50,-7.5]
                    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
                    x=10
                    sword_fx=pygame.mixer.Sound("音樂與音效/揍人.wav")
                    sword_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY1_BUTTON.checkForInput(A123):
                    global wizard_sheet
                    global WIZARD_ANIMATION_STEPS
                    global WIZARD_SIZE
                    global WIZARD_SCALE
                    global WIZARD_OFFSET
                    global WIZARD_DATA
                    global y
                    global magic_fx
                    wizard_sheet=pygame.image.load("圖片和部份圖示/武士.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[8,8,1,6,6,4,6]
                    WIZARD_SIZE=200
                    WIZARD_SCALE=3.5
                    WIZARD_OFFSET=[75,75]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/砍.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY2_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/原住民.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[10,8,1,7,6,3,11]
                    WIZARD_SIZE=126.1
                    WIZARD_SCALE=3.2
                    WIZARD_OFFSET=[50,30]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/assets_audio_sword.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY3_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/warrior.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[10,8,1,7,7,3,7]
                    WIZARD_SIZE=162
                    WIZARD_SCALE=4
                    WIZARD_OFFSET=[70,56]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/assets_audio_sword.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY4_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/wizard.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[8,8,1,8,8,3,7]
                    WIZARD_SIZE=250
                    WIZARD_SCALE=3
                    WIZARD_OFFSET=[105,107]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/assets_audio_magic.wav")
                    magic_fx.set_volume(0.75)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY5_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/魔王.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[6,11,1,15,15,5,18]
                    WIZARD_SIZE=160
                    WIZARD_SCALE=3.7
                    WIZARD_OFFSET=[61,110]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=30
                    magic_fx=pygame.mixer.Sound("音樂與音效/低吼.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/X2Download.app - 【貓咪大戰爭】BGM5 (128 kbps).mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY6_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/馬力歐.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[5,4,7,6,5,3,4]
                    WIZARD_SIZE=114
                    WIZARD_SCALE=2.7
                    WIZARD_OFFSET=[26,17]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/馬力歐.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY7_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/Ninja .png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[9,8,10,6,8,2,5]
                    WIZARD_SIZE=128
                    WIZARD_SCALE=2.6
                    WIZARD_OFFSET=[37,59]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/鞭子(強一點).wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY8_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/abc.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[7,8,11,4,14,3,6]
                    WIZARD_SIZE=128
                    WIZARD_SCALE=2.6
                    WIZARD_OFFSET=[40,59]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/火.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif ENUMY9_BUTTON.checkForInput(A123):
                    wizard_sheet=pygame.image.load("圖片和部份圖示/藍毛.png").convert_alpha()
                    WIZARD_ANIMATION_STEPS=[3,3,3,3,3,5,3]
                    WIZARD_SIZE=114
                    WIZARD_SCALE=1.7
                    WIZARD_OFFSET=[10,-7.5]
                    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
                    y=10
                    magic_fx=pygame.mixer.Sound("音樂與音效/揍人.wav")
                    magic_fx.set_volume(0.5)
                    pygame.mixer.music.load("音樂與音效/assets_audio_music.mp3")  ###音樂
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,0.0,5000)
                elif BG1_BUTTON.checkForInput(A123):
                    global bg_image
                    bg_image=pygame.image.load("背景圖/城堡.jpg").convert_alpha()   
                elif BG2_BUTTON.checkForInput(A123):
                    bg_image=pygame.image.load("背景圖/惡魔城.jpg").convert_alpha()
                elif BG3_BUTTON.checkForInput(A123):
                    bg_image=pygame.image.load("背景圖/城鎮道路.jpg").convert_alpha()
                elif BG4_BUTTON.checkForInput(A123):
                    bg_image=pygame.image.load("背景圖/天堂.jpg").convert_alpha()
                elif BG5_BUTTON.checkForInput(A123):
                    bg_image=pygame.image.load("背景圖/森林.jpg").convert_alpha()       
                elif  OPTIONS_BACK.checkForInput(A123):
                    main_menu()
                elif NEXT_BUTTON.checkForInput(A123):
                    play2()
            pygame.display.update()




def play2():
    while True:
        red=(255,0,0)
        yellow=(255,255,0)
        white=(255,255,255)

        intro_count=3
        last_count_update=pygame.time.get_ticks()
        score=[0,0]   ###玩家得分
        round_over=False
        ROUND_OVER_COOLDOWN=2000  ####2個回合之間的冷卻時間(2000毫秒相當於2秒)

        victory_img=pygame.image.load("圖片和部份圖示/victory.png").convert_alpha()   ####勝利圖片


        
        back_font=pygame.font.Font("字型/font.ttf",30)      

        
        def text_back():
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            OPTIONS_BACK = Button(image=None, pos=(500,35),text_input="BACK",font=get_font(30),base_color="red",hovering_color="green")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(screen)
        ###繪製文字的函數
        def draw_text(text,font,text_col,x,y):
            img=font.render(text,True,text_col)
            screen.blit(img,(x,y))



        def draw_bg():
            scaled_bg=pygame.transform.scale(bg_image,(1000,600))
            screen.blit(scaled_bg,(0,0))

        def draw_health_bar(health,x,y):
            ratio=health/100
            pygame.draw.rect(screen,white,(x-5,y-5,410,40))
            pygame.draw.rect(screen,red,(x,y,400,30))
            pygame.draw.rect(screen,yellow,(x,y,400*ratio,30))
            
            
            

        class Fighter():
            def __init__(self,player,x,y,flip,data,sprite_sheet,animation_steps,sound):
                self.player=player
                self.size=data[0]
                self.image_scale=data[1]
                self.offset=data[2]
                self.flip=flip    #####翻轉
                self.animation_list=self.load_images(sprite_sheet,animation_steps)
                self.action=0
                self.frame_index=0
                self.image=self.animation_list[self.action][self.frame_index]
                self.update_time=pygame.time.get_ticks()
                self.rect=pygame.Rect((x,y,80,180))
                self.vel_y=0
                self.running=False
                self.jump=False
                self.attacking=False
                self.attack_type=0
                self.attack_cooldown=0
                self.attack_sound=sound
                self.hit=False
                self.health=100
                self.alive=True

            def load_images(self,sprite_sheet,animation_steps):
                animation_list=[]
                for y, animation in enumerate(animation_steps):
                    temp_img_list=[]
                    for x in range(animation):
                      temp_img=sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                      temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.image_scale,self.size*self.image_scale)))
                    animation_list.append(temp_img_list)
                return animation_list

            def move(self,screen_width,screen_height,surface,target,round_over):
                speed=10
                gravity=2.5     ###重力
                dx=0
                dy=0
                self.running=False
                self.attack_type=0
                
                ####得到按鍵
                key=pygame.key.get_pressed()

                if self.attacking==False and self.alive==True: 
                #####以下為玩家1的控制鍵定義
                  if self.player==1:   
                    ###移動
                    if key[pygame.K_a]:   ####定義鍵盤A鍵
                        dx=-speed
                        self.running=True
                    if key[pygame.K_d]:   ####定義鍵盤D鍵
                        dx=speed
                        self.running=True

                    if key[pygame.K_w] and self.jump==False:   ####定義鍵盤W鍵
                        self.vel_y=-25
                        self.jump=True    ####防止玩家連續跳躍
                        
                    if key[pygame.K_r]or key[pygame.K_t]:    #####攻擊
                        self.attack1(target)
                        if key[pygame.K_r]:
                            self.attack_type=1
                        if key[pygame.K_t]:
                            self.attack_type=2

                ####以下為玩家2的控制鍵定義
                  if self.player==2:   
                    ###移動
                    if key[pygame.K_LEFT]:   ####定義鍵盤左鍵為向左
                        dx=-speed
                        self.running=True
                    if key[pygame.K_RIGHT]:   ####定義鍵盤右鍵為向右
                        dx=speed
                        self.running=True

                    if key[pygame.K_UP] and self.jump==False:   ####定義鍵盤向上鍵為跳
                        self.vel_y=-25
                        self.jump=True    ####防止玩家連續跳躍
                        
                    if key[pygame.K_KP1]or key[pygame.K_KP2]:    #####攻擊
                        self.attack2(target)
                        if key[pygame.K_KP1]:
                            self.attack_type=1
                        if key[pygame.K_KP2]:
                            self.attack_type=2
                
                ####重力
                self.vel_y+=gravity
                dy+=self.vel_y
                
                dy+=self.vel_y
                
                if self.rect.left+dx<0:  #####左移動
                    dx=-self.rect.left
                if self.rect.left+dx>1000:####右移動
                    dx=1000-self.rect.right
                if self.rect.bottom+dy>screen_height-110:
                    self.vel_y=0
                    self.jump=False
                    dy=screen_height-110-self.rect.bottom


                if target.rect.centerx>self.rect.centerx:
                    self.flip=False
                else:
                    self.flip=True

                if self.attack_cooldown>0:
                    self.attack_cooldown-=1
                
                ###更新角色的位置
                self.rect.x+=dx
                self.rect.y+=dy

            def update(self): #115行幫助照片不夠時的問題
        #檢查角色使用甚麼甚麼動作
                if self.health <= 0:
                    self.health = 0
                    self.alive = False
                    self.update_action(6)#6 死亡
                elif self.hit == True: 
                    self.update_action(5)#5 遭受攻擊
                elif self.attacking == True:
                    if self.attack_type == 1:
                        self.update_action(3)#3 攻擊一
                    elif self.attack_type == 2:
                        self.update_action(4)#4 攻擊二
                elif self.jump == True:
                    self.update_action(2)#2跳
                elif self.running == True:
                    self.update_action(1)#1移動
                else:
                    self.update_action(0)#0閒置

                animation_cooldown = 50 #50mil sec = 半秒
                #更新照片
                self.image = self.animation_list[self.action][self.frame_index]
                #在動畫更新前確定有足夠時間
                if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                    self.frame_index += 1
                    self.update_time = pygame.time.get_ticks()
                #確定動畫結束
                if self.frame_index >= len(self.animation_list[self.action]):
                    #如果角色死亡則結束動畫
                    if self.alive == False:
                        self.frame_index = len(self.animation_list[self.action]) -1
                    else:
                        self.frame_index = 0 #讓動畫跑完一次後會重複跑
                        #確定攻擊是否執行
                        if self.action == 3 or self.action== 4:
                            self.attacking = False
                            self.attack_cooldown = 20
                        #確定受到攻擊
                        if self.action == 5:
                            self.hit = False #使受到攻擊動畫不再重複
                            #如果有人攻擊時被打,會中斷攻擊
                            self.attacking = False
                            self.attack_cooldown = 20
            

            def attack1(self,target1):
             if self.attack_cooldown==0:
              self.attacking=True                 ###透過判斷自身矩形位置來翻轉角色方向
              self.attack_sound.play()
              attacking_rect=pygame.Rect(self.rect.centerx-(3*self.rect.width*self.flip),self.rect.y, 2.3*self.rect.width,self.rect.height)
              if attacking_rect.colliderect(target1.rect):
                  target1.health-=x
                  target1.hit=True
            def attack2(self,target2):
             if self.attack_cooldown==0:
              self.attacking=True                 ###透過判斷自身矩形位置來翻轉角色方向
              self.attack_sound.play()
              attacking_rect=pygame.Rect(self.rect.centerx-(3*self.rect.width*self.flip),self.rect.y, 2.3*self.rect.width,self.rect.height)
              if attacking_rect.colliderect(target2.rect):
                  target2.health-=y
                  target2.hit=True
              
              
            def update_action(self,new_action):    #####解決每個角色動作偵數不一樣的問題(可能跑步和跳躍的動作數量不一樣)
                if new_action!= self.action:
                    self.action=new_action
                    self.frame_index=0
                    self.update_time=pygame.time.get_ticks()


            def draw(self,surface):
                img=pygame.transform.flip(self.image,self.flip,False)
                surface.blit(img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))
        
        fighter_1=Fighter(1,200,310,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEPS,sword_fx)
        fighter_2=Fighter(2,700,310,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS,magic_fx)
            



        while True:  ##用來建立起遊戲的循環運行
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            OPTIONS_BACK = Button(image=None, pos=(500, 20),text_input="BACK",font=get_font(40),base_color="Black",hovering_color="Green")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(screen)

            clock.tick(FPS)

            draw_bg()

            draw_health_bar(fighter_1.health,20,20)
            draw_health_bar(fighter_2.health,580,20)
            draw_text("P1:"+str(score[0]),score_font,red,20,60)
            draw_text("P2:"+str(score[1]),score_font,red,580,60)
            text_back()


            if intro_count <=0:
                fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2,round_over)
                fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1,round_over)
            else:
                draw_text(str(intro_count),count_font,red,SCREEN_WIDTH/2,SCREEN_HEIGHT/3)
                if (pygame.time.get_ticks()-last_count_update)>=1000:
                    intro_count-=1
                    last_count_update=pygame.time.get_ticks()
                    print(intro_count)



            fighter_1.update()
            fighter_2.update()


            fighter_1.draw(screen)
            fighter_2.draw(screen)

            if round_over==False:
                if fighter_1.alive==False:
                    score[1]+=1
                    round_over=True
                    round_over_time=pygame.time.get_ticks()
                elif fighter_2.alive==False:
                    score[0]+=1
                    round_over=True
                    round_over_time=pygame.time.get_ticks()
            else:
                screen.blit(victory_img,(360,150))
                if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
                    round_over=False
                    intro_count=3
                    fighter_1=Fighter(1,200,310,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEPS,sword_fx)
                    fighter_2=Fighter(2,700,310,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS,magic_fx)
            
                    
                    

            for event in pygame.event.get():  
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        play1()
            pygame.display.update()
def play3():
    while True:
        screen.blit(k2,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_BACK = Button(image=None, pos=(100,550),text_input="BACK",font=get_font(40),base_color="#b68f40",hovering_color="red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()               
        pygame.display.update()
            
        
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 83))

        MENU_BUTTON = Button(image=pygame.image.load("圖片和部份圖示/options Rect.png"), pos=(500, 250), 
                            text_input="MENU", font=get_font(63), base_color="#d7fcd4", hovering_color="#b68f40")
        PLAY2_BUTTON = Button(image=pygame.image.load("圖片和部份圖示/options Rect.png"), pos=(500, 400), 
                            text_input="HOW TO PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load("圖片和部份圖示/Quit Rect.png"), pos=(500, 550), 
                            text_input="QUIT", font=get_font(63), base_color="#d7fcd4", hovering_color="#b68f40")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [MENU_BUTTON, PLAY2_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play1()
                if PLAY2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play3()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()

main_menu()