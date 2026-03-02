from PIL import Image, ImageDraw, ImageFont

# 创建画布
img = Image.new('RGB', (600, 800), 'white')
draw = ImageDraw.Draw(img)

# 尝试加载字体
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
except:
    font_title = font_text = font_small = font_bold = ImageFont.load_default()

# 颜色
color_dark = '#333333'
color_blue = '#4A90E2'
color_blue_light = '#87CEEB'
color_blue_top = '#5BA0F3'
color_gray = '#666666'
color_line = '#999999'

# 缩放和偏移
scale = 8
offset_x = 300
offset_y = 100

# 参数
head_d, head_h = 10, 10
neck_d, neck_h = 8, 2
shank_d, shank_h = 3, 20
tip_h = 4

# 绘制标题
draw.text((300, 40), '小钉子设计图（修正版）', fill=color_dark, font=font_title, anchor='mm')
draw.text((300, 65), '尺寸单位：mm | 建议层高0.15mm打印', fill=color_gray, font=font_text, anchor='mm')

# 中心虚线
for y in range(100, 650, 10):
    draw.line([(offset_x, y), (offset_x, y+5)], fill='#dddddd', width=1)

# 从下到上绘制，确保所有部分都严格以 offset_x 为中心

# 尖头（最底部）
tip_w = shank_d * scale
tip_l = offset_x - tip_w//2
tip_r = tip_l + tip_w
tip_bottom = 600
tip_top = tip_bottom - tip_h * scale
points = [(offset_x, tip_bottom), (tip_l, tip_top), (tip_r, tip_top)]
draw.polygon(points, fill=color_blue_light, outline=color_dark, width=2)
draw.text((tip_r + 15, tip_top + tip_h*scale//2), f'尖头 {tip_h}mm', fill=color_dark, font=font_text)

# 钉体（圆柱）
shank_w = shank_d * scale
shank_l = offset_x - shank_w//2
shank_r = shank_l + shank_w
shank_bottom = tip_top
shank_top = shank_bottom - shank_h * scale
draw.rectangle([shank_l, shank_top, shank_r, shank_bottom], fill=color_blue, outline=color_dark, width=2)
draw.text((shank_r + 15, shank_top + shank_h*scale//2), f'钉体 Ø{shank_d}mm × {shank_h}mm', fill=color_dark, font=font_text)

# 环槽（收腰）
neck_w = neck_d * scale
neck_l = offset_x - neck_w//2
neck_r = neck_l + neck_w
neck_bottom = shank_top
neck_top = neck_bottom - neck_h * scale
draw.rectangle([neck_l, neck_top, neck_r, neck_bottom], fill=color_blue_light, outline=color_dark, width=2)

# 钉头（顶部，严格居中）
head_w = head_d * scale
head_l = offset_x - head_w//2
head_r = head_l + head_w
head_bottom = neck_top
head_top = head_bottom - head_h * scale
draw.rectangle([head_l, head_top, head_r, head_bottom], fill=color_blue, outline=color_dark, width=2)
draw.ellipse([head_l, head_top-5, head_r, head_top+5], fill=color_blue_top, outline=color_dark, width=2)
draw.text((head_r + 15, head_top + head_h*scale//2), f'钉头 Ø{head_d}mm × {head_h}mm', fill=color_dark, font=font_text)

# 总高标注线
label_x = 390
draw.line([(label_x, head_top), (label_x, tip_bottom)], fill=color_dark, width=1)
draw.line([(label_x-5, head_top), (label_x+5, head_top)], fill=color_dark, width=1)
draw.line([(label_x-5, tip_bottom), (label_x+5, tip_bottom)], fill=color_dark, width=1)
draw.text((label_x + 10, (head_top + tip_bottom)//2 - 8), f'总高 {head_h+neck_h+shank_h+tip_h}mm', fill=color_dark, font=font_text)

# 左侧尺寸标注
left_x = 210
# 钉头高度
draw.line([(left_x, head_top), (left_x, head_bottom)], fill=color_line, width=1)
draw.line([(left_x-5, head_top), (left_x+5, head_top)], fill=color_line, width=1)
draw.line([(left_x-5, head_bottom), (left_x+5, head_bottom)], fill=color_line, width=1)
draw.text((left_x - 50, (head_top + head_bottom)//2 - 6), f'{head_h}mm', fill=color_gray, font=font_small)

# 环槽高度
draw.line([(left_x, neck_top), (left_x, neck_bottom)], fill=color_line, width=1)
draw.line([(left_x-5, neck_bottom), (left_x+5, neck_bottom)], fill=color_line, width=1)
draw.text((left_x - 40, (neck_top + neck_bottom)//2 - 6), f'{neck_h}mm', fill=color_gray, font=font_small)

# 钉体长度
draw.line([(left_x, shank_top), (left_x, shank_bottom)], fill=color_line, width=1)
draw.line([(left_x-5, shank_bottom), (left_x+5, shank_bottom)], fill=color_line, width=1)
draw.text((left_x - 50, (shank_top + shank_bottom)//2 - 6), f'{shank_h}mm', fill=color_gray, font=font_small)

# 尖头高度
draw.line([(left_x, tip_top), (left_x, tip_bottom)], fill=color_line, width=1)
draw.line([(left_x-5, tip_bottom), (left_x+5, tip_bottom)], fill=color_line, width=1)
draw.text((left_x - 40, (tip_top + tip_bottom)//2 - 6), f'{tip_h}mm', fill=color_gray, font=font_small)

# 打印建议
draw.text((50, 680), '打印建议：', fill=color_dark, font=font_bold)
draw.text((50, 705), '• 材料：PLA / PETG', fill=color_gray, font=font_text)
draw.text((50, 725), '• 层高：0.15mm（保证细钉强度）', fill=color_gray, font=font_text)
draw.text((50, 745), '• 墙厚：3-4层 或 填充100%', fill=color_gray, font=font_text)
draw.text((50, 765), '• 方向：尖头朝上打印，减少支撑', fill=color_gray, font=font_text)

# 保存
img.save('/root/.openclaw/workspace/小钉子示意图_修正.png')
print('PNG示意图已生成：小钉子示意图_修正.png')
