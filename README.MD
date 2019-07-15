# Readme.md

## Authors:

* [Daniel de la Osa](mailto:d.osa@estudiantes.matcom.uh.cu) C411
* [Rafael Martinez](mailto:r.martinez@estudiantes.matcom.uh.cu) C412
* [Jose Luis Alvarez](mailto:j.alvarez@estudiantes.matcom.uh.cu) C412

## Description

**OilNews** is a news extractor and a keywords filtering tool for oil related news. 

## Requirements

* news-please
* python 3.7
* **Elasticsearch** 7.2.0
* **Kibana** (Recommended) 7.2.0

## Install

The news-please library was updated to use the latest **Elasticsearch** distribution. Also a keyword-filter was added.

In order to install run the following lines in your terminal

```bash
$ git clone https://github.com/maxblu/news-please.git
$ cd news-please
$ python setup.py install
```

There is also required a server of **Elasticsearch**. We recommend you to download the binary from [this](http://elastic.co/start) site

You can get **Kibana** from the same place.

## Configuration

On `config/sitelist.hjson` there is a list in *json* format containing the *url* that will be scrapped every day.

The `config/config.cfg` file contains the values of a lots of necessary variables, including the location of the **Elasticsearch** server. One of them is the list of keywords for filtering news called `keywords`.

## Use

```bash
$ python main.py
```
