# TexasLaborStatisticsAPICall
A script I wrote that automate the download of Texas Labor Statistics Supply Reports. 
The example API request in ex.py downloads the reports for all Technical Schools/Universities in Texas. 
Downloads of other data will require looking at API requests through something like the XHR tab in a browser's DevToolssection.

## Setup
First, clone this repository (or optionally download the zip and extract the files), and then open the repository's root directory:
```shell
git clone https://github.com/aptitudepi/TexasLaborStatisticsAPICall.git
cd TexasLaborStatisticsAPICall/
```
Install prerequisites:
```shell
./install.sh
```
And execute the script!
```shell
./scraper.py
```
You should see the downloaded Excel files in ```out/```
