import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始值"""
        self.screen = screen  # 屏幕
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/ship.bmp')  # 加载飞船图像
        self.rect = self.image.get_rect()  # 飞船图像处理成矩形元素
        self.screen_rect = screen.get_rect()  # 处理屏幕成为矩形元素

        # rect的属性设置
        self.rect.centerx = self.screen_rect.centerx  # 飞船中心（X坐标）等于屏幕中心位置
        self.rect.bottom = self.screen_rect.bottom  # 飞船底部（Y坐标）等于屏幕底部
        # 在飞船的属性center中储存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 绘制
