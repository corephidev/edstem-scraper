# edstem-scraper

An extremely basic Python script I made out of interest, to collect data about who's posted the most on a given EdStem forum.

## Requirements
Make sure you have Chrome installed and driveable with Selenium, and you'll need the following packages installed (see the headers of `render.py` and `scraper.py`):
```
selenium
webdriver_manager
bs4
matplotlib
```

## Usage
First run `scraper.py`. Just enter the EdStem course URL (something like `https://edstem.org/au/courses/COURSEID/discussion/`), your login username and password, and (after a fair while) the filename you want to save the collection of names under.

Then run `render.py` and enter the filename, and it should just work (tm) :)
