from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='242ad85a3af04231993e7e51ae1269d9')

newsapi = NewsApiClient(api_key='242ad85a3af04231993e7e51ae1269d9')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2026-02-12',
                                      to='2026-02-15',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()