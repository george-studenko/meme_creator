import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import Image
from io import BytesIO

from quote_engine.Ingestor import Ingestor
from quote_engine import QuoteModel
from meme_engine.MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for (dir_path, dir_name, file_names) in os.walk(images_path):
        for file in file_names:
            path = f'{dir_path}{file}'
            imgs.append(path)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    json = request.form

    url = json.get('image_url', None)
    body = json.get('body', None)
    author = json.get('author', None)

    quote = QuoteModel(body, author)

    tmp_img = requests.get(url)
    img = Image.open(BytesIO(tmp_img.content))
    tmp_img_path = 'tmp.jpg'
    img.save(tmp_img_path)

    path = meme.make_meme(tmp_img_path, quote.body, quote.author)
    os.remove(tmp_img_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
