#导入模块
import pygame
import random #需要随机的布置地雷
import sys

#属性设置
WIDTH = 400
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
GREEN = (124, 252, 0)
GRID_SIZE = 20 #设置格子的大小
ROWS = HEIGHT // GRID_SIZE #设置行  “//”保证返回一个整数
COLS = WIDTH // GRID_SIZE #设置列 
GRID_NUM = 30 #设置雷的数量
FPS = 30

#初始化
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT)) #创建窗口
pygame.display.set_caption("MineSweeper(扫雷游戏)") #设置标题
screen.fill(WHITE) #设置背景颜色
clock = pygame.time.Clock()

class Grid:
    def __init__(self):
        self.number = 0
        self.show_number = False
        
#初始化 雷区 默认值：0
grid = []
for _ in range(ROWS):
    row = []
    for _ in range(COLS):
        row.append(Grid())
    grid.append(row)
    
#布置地雷 值：-1
for _ in range(GRID_NUM):
    random_row = random.randint(0, ROWS - 1)
    random_col = random.randint(0, COLS - 1)
    grid[random_row][random_col].number = -1

#计算方格 周围的雷的数量
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col].number != -1:
            count = 0 #定义计数变量
            for i in range(-1, 2): #遍历九宫格
                for j in range(-1, 2):
                    if 0 <= row + i < ROWS and 0 <= col + j < COLS: #只需更新位置在界面内的雷
                        if grid[row + i][col + j].number == -1:
                            count += 1 #是雷 计数 + 1
            grid[row][col].number = count 
#=========静态效果============


#刷新界面
pygame.display.update()
#循环使游戏时刻运行
running=True
while running:
    #=========刷新============
    pygame.display.update()
    clock.tick(FPS)
    #监听事件
    for event in pygame.event.get():
        #如果事件类型是退出，while中止游戏结束
        if event.type == pygame.QUIT: 
            pygame.quit
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("鼠标按下",event.pos)
            mouse_x, mouse_y = event.pos
            row = mouse_y // GRID_SIZE
            col = mouse_x // GRID_SIZE
            grid[row][col].show_number = True
            # pygame.draw.circle(screen,(220,250,250),(mouse_x, mouse_y),10)
            pygame.display.update()
                
    #绘制
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, WHITE, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            if grid[row][col].number == -1 and grid[row][col].show_number == True:  # 地雷
                pygame.draw.rect(screen, GRAY, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),1)
                pygame.draw.circle(screen, BLACK, (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2)
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit
                sys.exit()
            elif grid[row][col].number >= 0 and grid[row][col].show_number == True:  # 数字
                pygame.draw.rect(screen, GRAY, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),1)
                font = pygame.font.Font(None, GRID_SIZE)
                text = font.render(str(grid[row][col].number), True, BLACK)
                screen.blit(text, (col * GRID_SIZE + GRID_SIZE // 2 - text.get_width() // 2, row * GRID_SIZE + GRID_SIZE // 2 - text.get_height() // 2))
            elif grid[row][col].show_number == False: #未点击时的展示状态
                pygame.draw.rect(screen, GREEN, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),1)
            else:  # 空白
                pygame.draw.rect(screen, GRAY, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),1)
    