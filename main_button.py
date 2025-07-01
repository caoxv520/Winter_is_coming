import pygame


class Main_button:
    # 初始化函数，创建一个按钮列表
    def __init__(self,main):
        # 获取窗口尺寸
        size = main.window_size
        # 创建按钮列表
        self.button_string_list= ["开始游戏","存档","设置"]
        # 创建按钮列表
        self.button_list = []
        
        for i in range(len(self.button_string_list)):  
            # 设置文字
            text = pygame.font.SysFont('SimHei',size[0] // 20).render(self.button_string_list[i] , True, ("red"))          
            # 创建rect
            rect = pygame.Rect(size[0] * 37.5 // 100,size[1] * 0.4 + i * (size[1]  / 8) + 5,size[0] / 4,size[1] / 8)
            # 挂载文字
            main.screen.blit(text,rect)
            # 创建按钮
            self.button_list.append(text)
            
