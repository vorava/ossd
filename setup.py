import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='ossd',  
     version='1.0.3',
     py_modules=['ossd'],
     author="Vojtech Orava",
     author_email="vojtech.orava@gmail.com",
     description="OpenSubtitles subtitles downloader",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/vorava/osd",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )