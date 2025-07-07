# 导入所需模块。
import pygame

class Sound_manager:
	"""声音管理类，负责加载播放游戏中的音效。"""
	def __init__(self):
		"""初始化声音管理器。"""
		self.new_email = pygame.mixer.Sound("public/SoundEffect/new-notification-010-352755.mp3")
		self.winter_storm = pygame.mixer.Sound("public/SoundEffect/howling-winter-storm-ambient-sounds-6756.mp3")

	def play_winter_storm(self):
		"""播放暴风雪背景声音"""
		self.winter_storm.play()