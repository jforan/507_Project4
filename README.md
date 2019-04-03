# Project Option 1: Scraping and Parsing NPS site

# Jen Foran (jlforan)

# Functionality

This programs scraps data from https://www.nps.gov/index.htm, parsing through each of the states and territories to collect the names, types, locations, and descriptions of each of the parks in each of the states/territories. It the organizes this and writes it to a csv called nps_export.csv.


# Requirements

* SCRAPING_SI507_project4
* CSV
* requests, json
* bs4
* advanced_expiry_caching

note: all library and package requirements can be found acquired by running the requirements.txt file.


# How to Run

type 'python SI507_project4.py' into the command terminal


# Misc. Items

* SCRAPING_SI507_project4.py scrapes the data and is NECESSARY in order to compelte this exercise
* advanced_expiry_caching.py required to cache the data properly
* SAMPLE_nps_export.csv is an example of what the CSV output will look like