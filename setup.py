from distutils.core import setup

setup(
    name = 'memories',
    packages = ['memories'],
    version = '0.1',
    description = 'A library that will seperate images from an input containing multiple images and simply the process of addition of metadata to images.',
    author = 'Viraj Thakkar',
    author_email = 'vdthakkar111@gmail.com',
    url = 'https://github.com/veedata/album-manager',
    download_url = 'https://github.com/jrosebr1/imutils/tarball/0.1',
    keywords = ['computer vision', 'image processing', 'opencv'],
    install_requires=[
          'piexif',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
    ],
    scripts=['bin/range-detector'],
)