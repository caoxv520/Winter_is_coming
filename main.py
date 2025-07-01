# 引入需要的包
import pygame
from main_button import Main_button

class Main:
    # 初始化pygame
    def __init__(self):
        # 初始化pygame
        pygame.init()
        #获取屏幕尺寸
        self.get_screen_size()
        # 获取窗口尺寸
        self.get_window_size()
        # 设置窗口宽高
        self.screen = pygame.display.set_mode(self.window_size)
        # 设置窗口标题
        pygame.display.set_caption("凌冬已至游戏窗口")
        # 设置背景图片
        self.set_bg_img("public/img/bg.png")
        # 设置背景音乐
        self.set_main_bgm("public/music/main_bgm.mp3")
        # 创建按钮列表
        self.button = Main_button(self)



    # 主循环
    def run(self):
        while True:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # 更新屏幕
            pygame.display.update()

    def get_screen_size(self):
        # 获取屏幕尺寸
        info = pygame.display.Info()
        # 获取屏幕宽度和高度
        width, height = info.current_w, info.current_h
        # 返回屏幕宽度和高度
        self.screen_size = (width, height)
        
    def get_window_size(self):
        # 获取窗口尺寸
        width = self.screen_size[0] // 2
        height = self.screen_size[1] // 2
        # 返回窗口宽度和高度
        self.window_size = (width, height)

    def set_bg_img(self, img_path):
        # 设置背景图片
        self.bg_img = pygame.image.load(img_path)
        # 缩放背景图片到窗口大小
        self.bg_img = pygame.transform.scale(self.bg_img, self.window_size)
        # 绘制背景图片
        self.screen.blit(self.bg_img, (0, 0))

    def set_main_bgm(self, bgm_path):
        # 设置背景音乐
        pygame.mixer.music.load(bgm_path)
        # 播放背景音乐
        pygame.mixer.music.play(-1)

# 主函数
main = Main()
# 启动主循环
main.run()