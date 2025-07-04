# 引入需要的包
import pygame
import sys
from start_game import Start_game
from main_button import Main_button


class Main:
	"""主类，负责游戏的初始化和主循环。"""
	def __init__(self):
		"""初始化。"""
		pygame.init()
		#获取屏幕尺寸
		self.get_screen_size()
		# 获取窗口尺寸
		self.window_size = self.get_window_size()
		# 设置窗口宽高
		self.screen = pygame.display.set_mode(self.window_size)
		# 设置窗口标题
		pygame.display.set_caption("凛冬已至")
		# 创建时钟对象。
		self.clock = pygame.time.Clock()
		# 设置背景图片
		self.set_bg_img("public/img/bg.png")
		# 设置背景音乐
		self.set_main_bgm("public/music/main_bgm.mp3")
		# 创建按钮实力。
		self.button = Main_button(self)


	def run(self):
		"""游戏主循环。"""
		while True:
			# 设置游戏fps为30。
			self.clock.tick(30)
			# 检查鼠标和键盘事件。
			self.check_event()
			# 绘制背景图片。
			self.screen.blit(self.bg_img, (0, 0))
			# 设置按钮颜色。
			self.button.set_button_color()
			# 绘制按钮。
			self.button.draw_buttons(self.screen)
			#  更新屏幕显示内容。
			pygame.display.update()

	def check_event(self):
		"""检查鼠标和键盘事件。"""
		for event in pygame.event.get():
			# 如果点击关闭按钮，退出游戏。
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# 检测键盘按下事件。
			elif event.type == pygame.KEYDOWN:
				# 按下esc退出游戏。
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			# 如果鼠标按下，判断是否点击了按钮。
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# 如果点击了第一个按钮，开始游戏。
				if self.button.button_list[0]["rect"].collidepoint(event.pos):
					start_game = Start_game(self)
					start_game.game_run()

	def get_screen_size(self):
		"""获取屏幕尺寸。"""
		info = pygame.display.Info()
		# 获取屏幕宽度和高度
		width, height = info.current_w, info.current_h
		# 返回屏幕宽度和高度
		self.screen_size = (width, height)

	def get_window_size(self):
		"""获取窗口尺寸。"""
		width = self.screen_size[0] // 2
		height = self.screen_size[1] // 2
		return (width, height)

	def set_bg_img(self, img_path):
		"""设置背景图片。"""
		self.bg_img = pygame.image.load(img_path)
		# 缩放背景图片到窗口大小
		self.bg_img = pygame.transform.scale(self.bg_img, self.window_size)
		# 绘制背景图片
		self.screen.blit(self.bg_img, (0, 0))

	def set_main_bgm(self, bgm_path):
		"""设置背景音乐。"""
		pygame.mixer.music.load(bgm_path)
		# 播放背景音乐
		pygame.mixer.music.play(-1)


main = Main()
main.run()