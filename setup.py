from setuptools import setup
import subprocess

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='multitaper_toolbox',
   version='1.0.0',
   description = (
    "This repository contains Matlab, Python, and R implementations "
    "of the multitaper spectrogram analysis described in the paper "
    "'Sleep Neurophysiological Dynamics Through the Lens of Multitaper Spectral Analysis' "
    "(https://prerau.bwh.harvard.edu/publications/Physiology_Bethesda_2017_Prerau.pdf). "
    "Multitaper spectral estimation was developed in the early 1980s by David Thomson "
    "and has been shown to have superior statistical properties compared with single-taper "
    "spectral estimates. The multitaper method works by averaging multiple independent spectra "
    "estimated from a single segment of data. Instead of using a single-taper function to compute "
    "the spectrum, it uses multiple taper functions called discrete prolate spheroidal sequences (DPSS). "
    "Because DPSS tapers are uncorrelated, they can be averaged together as if they were independent trials, "
    "producing a spectrum with reduced variance compared to periodogram and single-taper estimation. "
    "Find videos describing the theory of spectral estimation and demonstrations at "
    "http://sleepeeg.org/multitaper on the Prerau Lab website."
   ),
   license="",
   keywords='multitaper_toolbox, neuroscience, electrophysiology',
   package_dir={'multitaper_toolbox': 'python'},
   author='\
           Michael J. Prerau, Ritchie E. Brown, Matt T. Bianchi, Jeffrey M. Ellenbogen, Patrick L. Purdon',
   author_email='',
   maintainer='',
   maintainer_email='',
   url="https://github.com/hengenlab/multitaper_toolbox",
   download_url="https://github.com/hengenlab/multitaper_toolbox",
   packages=['multitaper_toolbox'],
   install_requires=['joblib', 'ipython', 'numpy', 'matplotlib',
                     'seaborn', 'pandas',
                     'scipy'],
   extras_require={
    },
   classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
   scripts=[
           ]
)
