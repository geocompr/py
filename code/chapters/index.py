# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Introduction
#
# This site contains ideas, code and an outline of a yet-to-be written book on *Geocomputation with Python*.
#
# ## Motivations
#
# *Geocomputation with Python*, is motivated by the need for an introductory yet rigorous and maintained resource on working with geographic data in Python.
# A unique feature of the book is that it that demonstrates code for working with *both vector and raster* geographic data types.
# <!-- , and how to use them together. -->
# There are many resources on Python packages for geographic research and various applications but, to the best of our knowledge, no other resource brings together the following features into a single home:
#
# 1. Small introductory textbook focuses on doing basic operations well
# 2. Integration of vector and raster datasets in the same book, and within each section
# 3. Clear explanation of the code and exercises to maximize learning for newcomers
# 4. Provision of lucid example datasets and meaningful operations to illustrate the applied nature of geographic research
#
# The book aims to supplement other resources in the ecosystem, as highlighted by comparison with the book's scope with existing and in-progress works:
#
# - [Learning Geospatial Analysis with Python](https://www.packtpub.com/product/learning-geospatial-analysis-with-python/9781783281138) and [Geoprocessing with Python](https://www.manning.com/books/geoprocessing-with-python) focuses on processing spatial data using low-level Python interfaces for GDAL, such as the `gdal`, `gdalnumeric`, and `ogr` [packages](https://gdal.org/api/python.html) from `osgeo`. 
# This approach is more complex, [less "Pythonic"](https://rasterio.readthedocs.io/en/latest/intro.html#philosophy), and perhaps outdated in light of development of packages such as `geopandas` and `rasterio` covered here
# - [pythongis.org](https://pythongis.org/) (at an early stage of development) seeks to provide a general introduction to 'GIS in Python', with parts focusing on Python essentials, using Python with GIS, and case studies. 
# Compared with pythongis.org, geocompy has a relatively narrow scope (1) and a greater focus on raster-vector interoperability
# - [geographicdata.science](https://geographicdata.science/book/intro.html) is an ambitious project with chapters dedicated to advanced topics, with Chapter 4 on [Spatial Weights](https://geographicdata.science/book/notebooks/04_spatial_weights.html) getting into complex topics relatively early, for example.
# Geocompy would be shorter, simpler and more introductory, and cover raster and vector data with equal importance (1 to 4)
#
# Geocompy is a sister project of [Geocomputation with R](https://geocompr.robinlovelace.net/) -- a book on geographic data analysis, visualization, and modeling using the R programming language.
#
# ## Reproducing this book
#
# An important aspect of scientific research and 'citizen science' that is participatory is reproducibility of results.
#
# To reproduce this book you can simply click on the link below to see the code running in your web browser (see details of how this works at [mybinder.org](https://mybinder.org/)):
#
# [![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/geocompr/py/main?urlpath=lab/tree/ipynb)
#
# To run the code locally, recommended for using the material on real data, you need to have a reasonable computer, e.g. with 8 GB RAM.
# You'll need administrative rights to install the requirements, which include:
#
# - A suitable integrated development environment (IDE) such as VS Code, RStudio or Jupyter Notebook
# - Quarto, if you want to reproduce the book's open access website
# - Either an Anaconda-like environment (we recommend `miniconda3`) or Docker to get systems dependencies
#
# See the project's README for details on getting set-up.
# After you have installed the necessary dependencies and cloned or [unzipped](https://github.com/geocompr/py/archive/refs/heads/main.zip) the book's source code, you should be able to reproduce the code in its entirety with the following command:
#
# ```bash
# quarto preview
# ```
#
# If you see output like that below (with the IDE and browser arranged to see live updates after editing the source code), congratulations, it has worked!
#
# ![](https://user-images.githubusercontent.com/1825120/161321382-ac36aeab-5628-4bef-b3dd-7b2becdd4860.png)
#
