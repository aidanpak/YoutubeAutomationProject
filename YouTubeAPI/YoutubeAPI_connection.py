from googleapiclient.discovery import build

api_key = 'AIzaSyBw1R3xD_LlKNZ8DMQTzIzFklq-ZA1CT_U'

class APIConnection:
    Youtube = build('youtube', 'v3', developerKey=api_key)
    #Youtube.close()


# YouTubeWatchLaterAutomation
An Application that automates a WatchLater Youtube Playlist. Using the Youtube Data API, webscraping, and browser automation.


Outline of Project
- will need directories and python files...
  - youtube api --> to get subscriber list
    - connection to api
    - getting subscriber list
  - automation (every chrome login) --> every time login to website will run the script
  - webscraping --> to return all videos on page
    - locators
    - pages
    - parsers

- Libraries needed
  - libraries to use Google API
    - google-api-python-client
  - chrome driver stuff for automation
  - webscraping
    - beautiful soup
    - requests


Notes:
- make sure to not publish with my api_key.. lol
