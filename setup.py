from setuptools import setup, find_packages
import codecs
import os

# Setting up
setup(
    name='cell-count',
    version='0.0.2',
    author='nemo256 (Amine Neggazi)',
    author_email='<neggazimedlamine@gmail.com>',
    description='Count blood cells',
    long_description='Count red, white blood cells to detect various diseases such as blood cancer (leukemia), lower red blood cells (anemia)...',
    packages=find_packages(),
    install_requires=['opencv-python', 'tensorflow', 'numpy'],
    keywords=['python', 'artificial intelligence', 'deep learning', 'blood cells', 'image segmentation', 'unet'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
    extras_require={
        'testing': ['pytest'],
    }
)
