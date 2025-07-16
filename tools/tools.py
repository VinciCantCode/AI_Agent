# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch


def get_profile_url_tavily(query: str):
    """
        Search for anything using Tavily search.
    """
    search = TavilySearch()
    results = search.run(f"{query}")
    return results
