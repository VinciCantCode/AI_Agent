# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch


def get_profile_url_tavily(name: str):
    """
        Search for a LinkedIn profile URL using Tavily search.
    """
    search = TavilySearch()
    results = search.run(f"site:linkedin.com/in {name}")
    return results
