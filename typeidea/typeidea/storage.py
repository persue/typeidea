# -*- coding: utf-8 -*-
from io import BytesIO

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image, ImageDraw, ImageFont

class WatermarkStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if 'image' in content.content_type:
            image = self.watermark_with_text(content, 'SCS.com', 'red')
            content = self.convert_image_to_file(image, name)
        
        return super().save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = BytesIO()
        image.save(temp, format='PNG')
        file_size = temp.tell()

        return InMemoryUploadedFile(temp, None, name, 'image/png', file_size,None)

    def watermark_with_text(self, file_obj, text, color, fontfamily=None):
        image = Image.open(file_obj).convert('RGBA')
        draw = ImageDraw.Draw(image)
        width, height = image.size
        margin = 10
        if fontfamily:
            font = ImageFont.truetype(fontfamily, int(height/20))
        else:
            font = None
        
        textWidth, textHeight = draw.textsize(text, font)
        x = (width - textWidth -margin) /2
        y = height - textHeight - margin
        draw.text((x,y), text, color, font)

        return image