import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

setuptools.setup(
    name = 'memories',
    version = '0.3',
    url = 'https://github.com/veedata/album-manager',
    download_url = 'https://github.com/veedata/album-manager/archive/refs/tags/v0.2-alpha.tar.gz',
    author = 'Viraj Thakkar',
    author_email = 'vdthakkar111@gmail.com',
    description = 'A library for those who want to convert their older images into digitised format (with metadata), and beautify them using borders and other options.',
    long_description=long_desc,
    keywords = ['computer vision', 'image processing', 'opencv', 'album'],
    project_urls={
        "Code": "https://github.com/veedata/album-manager",
        "Issue tracker": "https://github.com/veedata/album-manager/issues",
    },
    install_requires=[
          'piexif',
          'opencv-python',
          'Pillow',
      ],
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "memories"},
    packages=setuptools.find_packages(where="memories"),
    scripts=['bin/range-detector'],
)