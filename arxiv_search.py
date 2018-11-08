import feedparser
import urllib
import numpy as np
import pandas as pd

""" A Python module for searching arXiv.org using the arXiv API
"""

### sortBy: 'lastUpdatedDate', 'submittedDate'
### sortOrder: 'ascending', 'descending'

def search_query(query, start=0, max_results=10, sortBy='submittedDate', sortOrder='descending'):
    """
    """
    base_url = 'http://export.arxiv.org/api/query?search_query='

    search_url  = base_url
    search_url += query
    search_url += '&start={0}&max_results={1}'.format(start, max_results)

    if sortBy is not None:    search_url += '&sortBy=' + sortBy
    if sortOrder is not None: search_url += '&sortOrder=' + sortOrder

    response = urllib.request.urlopen(search_url).read()
    feed = feedparser.parse(response)
    
    return feed


def get_number_of_results(feed):
    number_of_retrieved_entries = len(feed.entries) 
    total_number_of_results     = int(feed.feed.opensearch_totalresults)
    return number_of_retrieved_entries, total_number_of_results


def stalk_person_on_arxiv(author):
    pass


def plot_histogram(feed, ax):
    # `timestamps` contains the dates when the articles were submitted (first version)
    timestamps = np.array([pd.Timestamp(entry.published) for entry in feed.entries])
    df = pd.DataFrame(data=timestamps, columns=['timestamp'])
    df.groupby(df['timestamp'].dt.year).count().plot(kind='bar', ax=ax, legend=False)

    title = feed.feed.title[:feed.feed.title.find('&')]
    ax.set_title(title)
    ax.set_xlabel('date submitted (year)')
    ax.set_ylabel('# articles matching search criteria')

