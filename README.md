# Introduction to Web Scraping

This repository contains the notebook, slides, sample data, and code for the introduction to web scraping tutorial given on Friday, March 31, 2017.

The primary goal for this tutorial is to introduce scraping at a high level for analysts. We will discuss how to leverage HTTP methods to fetch data from the internet, then parse that data into a usable form. We will explore the use of APIs, scraping raw HTML, and building towards crawlers. The primary content is as follows:

- [Web Scraping Notebook](scraping.ipynb) contains the demos and content presented to the course by the instructor.
- [Web Scraping Slides](slides/scraping.pdf) contains a presentation version of the content for review purposes.
- [Anansi](anansi/) is a sample Twitter search scraper that uses the Twitter API.

## Getting Started

Step one is to clone or [download](https://github.com/DistrictDataLabs/brookings/archive/master.zip) the repository, unzip it and then cd into the project directory.

Note, this code requires [Python 3](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads) to run, as well as several third party libraries. Make sure that you have [Jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html) installed, and if you're using Python that you have [pip](https://pip.pypa.io/en/stable/installing/) installed.  One you do, you can install the required third party dependencies as follows:

```
$ pip install -r requirements.txt
```

or

```
$ conda install --yes --file requirements.txt
```

Once done, you can run the notebook as follows:

```
$ jupyter notebook scraping.ipynb
```

The notebook may already have cells executed or it may not, you can clear all output and start from a fresh slate, running each cell in turn -- or you can simply read through the content. 
