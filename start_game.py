# 导入需要的模块。
import pygame
import sys
from sound_manager import Sound_manager


class Start_game:
	"""开始游戏类。"""
	def __init__(self, main):
		"""初始化。"""
		self.main = main  # 将传入的main参数赋值给实例变量self.main。
		self.sound_manager = Sound_manager()
		self.sound_manager.play_winter_storm()
		self.set_start_game_bg_img('public/img/game1.png')  # 设置背景图片。

	def game_run(self):
		"""开始游戏"""
		running = True
		while running:
				# 检查鼠标键盘事件。
				running = self.game_check()
				#刷新
				pygame.display.update()

	def game_check(self):
		"""检查鼠标键盘事件"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return False

	def set_start_game_bg_img(self, img_path):
		# 设置背景图片
		self.bg_img = pygame.image.load(img_path)
		# 缩放背景图片到窗口大小
		self.bg_img = pygame.transform.scale(self.bg_img, self.main.window_size)
		# 绘制背景图片
		self.main.screen.blit(self.bg_img, (0, 0))