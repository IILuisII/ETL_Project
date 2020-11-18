# ETL_Project

## Overview

The purpose of this project is to Extract information from three main news websites, Transform the scraped
data into a structured data frame (with categorizations), and Load this data frame into a SQL data base, to be able to
retrieve the latest news from our tree main websites on one single table.

<img src="DB%20Strucute.PNG" width="300">

## Extract:

We primarily used Jupyter Notebook’s, Splinter and Beautiful Soup to extract the latest news headlines, URLs and
dates from three sources. For this project, we pulled news from CNN, NPR and CNBC. We choose these websites as
they are more reliable news sources, have neaty laid-out websites for ease of data scraping and are constantly being
updated.

Additionally, we chose these websites as their pages are laid out in a similar fashion (although NPR differed slightly).
For the sake of simplicity, we chose to scrape the article headers, dates and URLs for each news story. This limited
the amount of null information in our database.
When we initially set out on this project, we had hoped to pull a subheader/teaser for each story; however,
not all sources provided this information (with the exception of NPR).

## Transform:

We input our scraped data into uniform data frames to ensure that this data could be loaded into our SQL database
properly. As mentioned above, this meant removing columns we had initially hoped to have in our dataset.
However, there were issues with site layouts and information provided by each data source that limited our ability
to do so. Furthermore, we needed to ensure that all the data frames had the same headers as the database so that
all scraped data could be accurately pushed into the SQL database. This required sanity checks querying the data base to make sure it was correctly pushed.

Additionally, we had to apply appropriate tags to each article. This required creating a formula to search each
headline for keywords that related to each tag (see below):

## Load:

We utilized the Google Cloud to house our SQL database. Our database consists of four different tables, connected
by ID keys.
Our “News” table is the only dynamic table, meaning the information will constantly be updating as it
contains all the articles headers, URL’s, date published, and tag/site ID’s.
Our “Site Tag” table is static and is a reference point to each news site used (contains the Site ID, Main URL
and Site Name.
Our “Tag” table is static and contains the Tag ID and Tag.
The “Keyword” table is a static table housing all the keywords to categorize the articles in reference to the
appropriate tag. All tables have a “Last Updated” column indicating the last time a row was updated:
