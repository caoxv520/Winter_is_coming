import pygame

class Main_button:
    # 初始化函数，创建一个按钮列表
    def __init__(self, main):

        self.main = main
        # 获取窗口尺寸
        size = main.window_size
        # 创建按钮列表
        self.button_string_list = ["开始游戏", "存档", "设置"]
        # 创建按钮列表
        self.button_list = []
        # 创建颜色列表


        
        for i in range(len(self.button_string_list)):  

            font = pygame.font.SysFont('SimHei', size[0] // 20)
            text = font.render(self.button_string_list[i], True, main.button_color_list[i]["color"], main.button_color_list[i]["background_color"])
            # 创建rect
            rect = pygame.Rect(size[0] * 37.5 // 100, size[1] * 0.4 + i * (size[1] / 8) + i * 5, size[0] / 4, size[1] / 8)
            # 挂载文字
            main.screen.blit(text, rect)
            # 创建按钮
            self.button_list.append({
                "rect": rect,
                "text": text
            })

        
    def set_button_color(self):
        # 获取按钮位置
       for i in range(3):
            # 设置按钮颜色
                if self.button_list[i]["rect"].collidepoint(pygame.mouse.get_pos()):
                        self.main.button_color_list[i] = {
                            "color": (200, 200, 200),
                            "background_color": (255, 255, 255)
                        }
                else:
                        self.main.button_color_list[i] = {
                            "color": (255, 255, 255),
                            "background_color": (200, 200, 200)
                        }


   