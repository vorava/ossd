# OpenSubtitles Subtitles Downloader - OSSD
This package allows you to download subtitles as text from [www.opensubtitles.com](https://www.opensubtitles.com). All you need to have is [**Selenium**](https://selenium-python.readthedocs.io) with Chrome driver, **requests** package (*pip install requests*) and this **OSSD** package.
## Instalation
```
pip install ossd
```
PyPi page - [https://pypi.org/project/ossd/](https://pypi.org/project/ossd/)
## Usage
    import ossd
    ossd.get_subtitles(driver, movie_name)

* driver -- [Chrome Driver (Selenium)](https://chromedriver.chromium.org)
* movie_name -- Name of movie which subtitles you want to download

## Methods
**get_subtitles** -- returns most downloaded subtitles text, if error occurs then returns " " (whitespace) and prints error code
**parse_subtitles** -- parses script lines from default format into one line only text format, skips ads on the script start

## Example
     import ossd
     from selenium import webdriver  
     driver = webdriver.Chrome(executable_path=driverPath)
     text = ossd.get_subtitles(driver, "Star Wars: A New Hope")

#### Output (in variable text)
Same as [here](https://www.opensubtitles.org/en/subtitles/3182984/star-wars-episode-iv-a-new-hope-en).
> 0 \
> 00:02:40,680 --> 00:02:42,557 \
> Did you hear that? \
> 
> 1 \ 
> 00:02:42,680 --> 00:02:45,319 \
> They shut down the main reactor. \ 
> We'll be destroyed for sure. \
> 
> 2 \
> 00:02:45,440 --> 00:02:46,873 \
> This is madness. \
> 
> 3 \
> 00:02:56,560 --> 00:02:57,913 \
> We're doomed. \
> ....
---
	one_text = ossd.parse_subtitles(text)
#### Output (in variable one_text)
> Did you hear that? They shut down the main reactor. We'll be destroyed for sure. This is madness. We're doomed. ...
## Licence - MIT
Free for use, editing, selling, just mention author

## Development

+ Clean ununsed: `rm -rf build/ dist/ *egg* **.pyc __pycache__`
+ Build package: `python setup.py sdist bdist_wheel`
+ deploy package: `python -m twine upload dist/*`