# -*- coding: utf-8 -*-
"""
创建视频封面图片（简单版本）
"""

from PIL import Image, ImageDraw
from pathlib import Path

output_path = Path(r'C:\Users\komal\Desktop\laser-marking-website\(最终)kvlasermarking.com\video-poster.jpg')

# 创建 1280x720 的图片
img = Image.new('RGB', (1280, 720), color=(30, 30, 50))
draw = ImageDraw.Draw(img)

# 添加标题文字
try:
    from PIL import ImageFont
    font = ImageFont.truetype("arial.ttf", 48)
    small_font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()
    small_font = font

# 主标题
main_text = "KINGVAN"
draw.text((640, 280), main_text, fill=(255, 255, 255), font=font, anchor="mm")

# 副标题
sub_text = "Laser Marking Machine"
draw.text((640, 340), sub_text, fill=(200, 200, 200), font=small_font, anchor="mm")

# 绘制播放按钮背景圆形
play_center_x = 640
play_center_y = 420
circle_radius = 60

# 绘制半透明圆形背景
draw.ellipse([
    play_center_x - circle_radius,
    play_center_y - circle_radius,
    play_center_x + circle_radius,
    play_center_y + circle_radius
], fill=(255, 0, 0, 180), outline=(255, 255, 255, 200), width=3)

# 绘制三角形播放图标
triangle_points = [
    (play_center_x - 25, play_center_y - 35),
    (play_center_x - 25, play_center_y + 35),
    (play_center_x + 45, play_center_y)
]
draw.polygon(triangle_points, fill=(255, 255, 255))

# 保存
img.save(output_path, 'JPEG', quality=90)
print(f"✅ 视频封面已生成：{output_path}")
print(f"   尺寸：1280x720")
print(f"   位置：{output_path}")
