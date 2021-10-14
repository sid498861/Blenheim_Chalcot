#######################################################################
#Created By: Siddharth Tiwari
#Create On: 14-Oct-2021
#Description: This script retrieves "Top Stories" from this parliament data RSS feed endpoint: https://www.europarl.europa.eu/rss/doc/top-stories/en.xml
#######################################################################


#Import the required packages and libraries

import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession


def get_source(url):
    """This function returns the source code for the provided URL and
        prints the source code of the URL page

    Args: 
        url (string): URL of the page to parse.

    Returns:
        response (object): HTTP response object from requests_html.
    """
    session = HTMLSession()
    response = session.get(url)
    srcode = requests.get(url, 'html.parser')
    print(srcode.text)
    return response


def get_feed(url):
    """This function returns a Pandas dataframe containing the RSS feed contents and creates .csv file with RS feed data in it.

    Args: 
        url (string): URL of the RSS feed to read.

    Returns:
        df (dataframe): Pandas dataframe containing the RSS feed contents.
    """
    
    response = get_source(url)
    
    df = pd.DataFrame(columns = ['title','link', 'pubDate', 'guid', 'description'])

    with response as r:
        items = r.html.find("item", first=False)

        for item in items:        

            title = item.find('title', first=True).text
            link = item.find('link', first=True).text
            pubDate = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            description = item.find('description', first=True).text

            row = {'title': title, 'link': link, 'pubDate': pubDate, 'guid': guid, 'description': description}
            df = df.append(row, ignore_index=True)

    df.to_csv("RSS_feed_output.csv")
    
url="https://www.europarl.europa.eu/rss/doc/top-stories/en.xml"
df = get_feed(url)
df.head()