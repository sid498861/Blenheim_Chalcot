# Blenheim_Chalcot
Assignment for Blenheim Chalcot hiring process

Created By- Siddharth Tiwari

Create On- 14-Oct-2021

Description- This is a readme document explaning how to use the script RSS_feed.py

**What script does!!!!!**

***Step1:***
This script uses three Python packages: Requests, Requests-HTML, and Pandas. Requests is one of the most popular Python libraries and is used for making HTTP requests to servers to fetch data. Requests-HTML is a web scraping library that combines Requests with the Beautiful Soup parsing package, while Pandas is used for data storage and manipulation.

*If the above packages are not installed use below commands to install the packages-*

!pip3 install requests_html

!pip3 install pandas

!pip3 install requests

***Step 2:***
Two functions have been created as part of the script-

get_source(url) : This function reads the RSS feed in Python to fetch the source of the feed itself. We do this using the HTMLSession() feature of requests_html. This creates a session, then fetches the URL, and returns the source code of the page in its response object. Also it prints the Source code of the URL as part of the requirement

get_feed(url): This function takes the URL of the RSS feed and passes it to the get_source() function we created above, returning the raw XML code of the feed itself in an element called response. We then create a Pandas dataframe in which to store the parsed data, then loop through each item element found within the response. When each item is detected, we then use the find() function to look for the element names, i.e. title, pubDate, link, and description, and we extract the text from within by appending the .text argument.
Finally, we add the contents of each item to a dictionary called row which maps the data to our dataframe, and then uses the Pandas append() function to add the row of data to the dataframe, without adding an index. At the end, we return a dataframe containing all the feed contents we’ve scraped, also we export this dataframe to a .csv file.


**How to run the script!!!!!**

This script could be run as follows -

1. Open a command-line and type the word python followed by the path to your script file, like this:
python RSS_feed.py

2. Open a jupyter notebook and paste the contents of the file in a cell and run that cell



