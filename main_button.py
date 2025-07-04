# 导入所需模块。
import pygame


class Main_button:
	"""主按钮类。"""
	def __init__(self, main):
		"""初始化。"""
		self.main = main
		# 获取窗口尺寸。
		self.size = main.window_size
		# 创建按钮字符串列表。
		self.button_string_list = ["开始游戏", "存档", "设置"]
		# 创建按钮列表。
		self.button_list = []
		# 创建按钮颜色列表，初始颜色为白色，背景为黑色。
		self.button_color_list = [{
			"color": (255, 255, 255),
			"background_color": (0, 0, 0),
		} for _ in self.button_string_list]
		self.build_buttons()

	def build_buttons(self):
		"""创建按钮。"""
		# 清空按钮列表。
		self.button_list.clear()
		# 设置按钮的rect和text。
		for i, text_str in enumerate(self.button_string_list):
			font = pygame.font.SysFont('SimHei', self.size[0] // 20)
			text = font.render(text_str, True, self.button_color_list[i]["color"], self.button_color_list[i]["background_color"])
			rect = pygame.Rect(self.size[0] * 37.5 // 100, self.size[1] * 0.4 + i * (self.size[1] / 8) + i * 5, self.size[0] / 4, self.size[1] / 8)
			self.button_list.append({
				"rect": rect,
				"text": text
			})

	def set_button_color(self):
		"""根据鼠标位置设置按钮颜色，并刷新text。"""
		for i in range(len(self.button_string_list)):
			if self.button_list[i]["rect"].collidepoint(pygame.mouse.get_pos()):
				self.button_color_list[i] = {
					"color": (200, 200, 200),
					"background_color": (255, 255, 255)
				}
			else:
				self.button_color_list[i] = {
					"color": (255, 255, 255),
					"background_color": (0, 0, 0)
				}
			# 只更新text
			font = pygame.font.SysFont('SimHei', self.size[0] // 20)
			self.button_list[i]["text"] = font.render(
				self.button_string_list[i],
				True,
				self.button_color_list[i]["color"],
				self.button_color_list[i]["background_color"]
			)

	def draw_buttons(self, screen):
		"""在主循环中调用此方法绘制按钮"""
		for button in self.button_list:
			screen.blit(button["text"], button["rect"])