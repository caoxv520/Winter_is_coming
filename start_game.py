import pygame


class Start_game:

    def __init__(self, main):
        # 初始化函数，用于创建类的实例
        self.main = main  # 将传入的main参数赋值给实例变量self.main
        # 设置背景图片
        self.set_start_game_bg_img('public/img/game1.png')
     

    def game_run():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                #刷新
                pygame.display.update()

    def set_start_game_bg_img(self, img_path):
        # 设置背景图片
        self.bg_img = pygame.image.load(img_path)
        # 缩放背景图片到窗口大小
        self.bg_img = pygame.transform.scale(self.bg_img, self.main.window_size)
        # 绘制背景图片
        self.main.screen.blit(self.bg_img, (0, 0))
                
                

