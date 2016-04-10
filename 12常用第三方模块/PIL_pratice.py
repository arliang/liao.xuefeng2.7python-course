# -*- coding:utf-8 -*-
from PIL import Image,ImageFilter,ImageDraw
#打开图片
tokyo = Image.open('./tokyo.jpg')
#获取图片信息
w,h = tokyo.size
print w,h
#缩放
tokyo.thumbnail((w//2,h//2))
#保存
tokyo.save('./tokyo_handle.bmp','bmp')
#切片、旋转、滤镜、输出文字、调色板
with Image.open('./tokyo.jpg') as im:
	im2 = im.filter(ImageFilter.BLUR)
	im2.save('./blur.jpg','jpeg')





