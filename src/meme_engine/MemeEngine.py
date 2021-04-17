import os
from PIL import Image, ImageDraw, ImageFont
import uuid


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Creates a meme, by writing the text on top of an images, returns the path to the generated image.
        """
        try:
            meme_file = str(uuid.uuid4())+'.jpg'
            img = Image.open(img_path)
            original_width, original_height = img.size

            height = width * original_height // original_width
            img = img.resize((width, height), Image.ANTIALIAS)
            font_size = 24
            font = ImageFont.truetype('meme_engine/impact.ttf',font_size)

            ImageDraw.Draw(img).text(
                (20, height - 40),  # Coordinates
                f'{text} - {author}',  # Text
                (0, 0, 0),  # Color
                font=font
            )

            ImageDraw.Draw(img).text(
                (18, height - 42),  # Coordinates
                f'{text} - {author}',  # Text
                (255, 255, 255),  # Color
                font=font
            )
            meme_full_path = f'{self.output_dir}/{meme_file}'
            img.save(meme_full_path)
            return meme_full_path
        except Exception as exception:
            raise exception
