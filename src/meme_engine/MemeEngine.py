"""This module is in charge of the image processing to generate memes."""
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
import uuid


class MemeEngine:
    """MemeEngine is in charge of the image processing to generate memes."""

    def __init__(self, output_dir):
        """Initialize the MemeEngine."""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme, by writing the text on top of an images.

        Returns the path to the generated image.
        """
        try:
            meme_file = str(uuid.uuid4()) + '.jpg'
            img = Image.open(img_path)
            height, img = self.resize_image(img, width)
            x, y = self.get_random_coordinates(height)

            self.draw_text(author, height, img, text, x, y)

            meme_full_path = self.save_meme(img, meme_file)
            return meme_full_path
        except Exception as exception:
            raise exception('An error occurred when trying to create the meme')

    def save_meme(self, img, meme_file):
        """Save the meme to disk."""
        meme_full_path = f'{self.output_dir}/{meme_file}'
        img.save(meme_full_path)
        return meme_full_path

    def draw_text(self, author, height, img, text, x, y):
        """Write the meme text on top of the image."""
        font_size = 24
        font = ImageFont.truetype('meme_engine/impact.ttf', font_size)
        wrapped_text = textwrap.wrap(f'{text}', width=40)
        wrapped_text.append(f'       - {author}')
        wrapped_text_str = '\n'.join(wrapped_text)
        ImageDraw.Draw(img).text(
            (x, y),  # Coordinates
            wrapped_text_str,  # Text
            (0, 0, 0),  # Color
            font=font
        )
        ImageDraw.Draw(img).text(
            (x - 2, y - 3),  # Coordinates
            wrapped_text_str,  # Text
            (255, 255, 255),  # Color
            font=font
        )

    def get_random_coordinates(self, height):
        """Get random coordinates to position the text on top of the image."""
        x = random.randint(20, 100)
        y = random.randint(height - 200, height - 60)
        return x, y

    def resize_image(self, img, width):
        """Resize the original image to create the meme."""
        original_width, original_height = img.size
        height = width * original_height // original_width
        img = img.resize((width, height), Image.ANTIALIAS)
        return height, img
