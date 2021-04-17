# Meme Generator

The meme generator is capable of generating random memes given a collection of images and a collection of quotes, the
quotes can be stored in different formats such as csv, pdf, txt or docx.

## Setup

To run the project install the requirements with pip from inside the src folder:  
```pip install -r requirements.txt```

Another requirement is pdftotext to install it run:  
``` sudo apt-get xpdf```

## Running the project
### Web Interface
To run the web interface execute:  
```python app.py```  

Then open the following url ```http://127.0.0.1:5000/``` using a web browser.

### CLI
To generate a meme from the command line run:  
```python meme.py```

The CLI will accept the following optional arguments:
```
optional arguments:
  -h, --help       show this help message and exit
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image
  --path PATH      path to an image file
```

If no arguments are provided the CLI will generate a random meme.

## Project modules
### Quote engine

Contains the code that will read the quotes from the different text files, the quote engine contains ingestors capable
of reading files in the following formats:

* csv
* pdf
* text
* docx

### Meme engine

This module is the one in charge of doing image manipulation, it will load the images, write the quotes on top of the
image, save it to disk and return the path to the meme image.