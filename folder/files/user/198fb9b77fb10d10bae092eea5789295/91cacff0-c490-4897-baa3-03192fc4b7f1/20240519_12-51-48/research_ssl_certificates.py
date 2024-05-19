# filename: research_ssl_certificates.py

from typing import List, Dict

def search_ssl_certificates_articles(scope: str, keywords: List[str], max_results_per_keyword: int = 5) -> Dict[str, List[Dict]]:
    """
    Conducts research on SSL certificates by searching for scholarly articles on arXiv.
    
    Args:
        scope (str): The scope of the research, e.g., "SSL certificates".
        keywords (List[str]): A list of keywords related to the topic.
        max_results_per_keyword (int): The maximum number of results to return per keyword.
        
    Returns:
        Dict[str, List[Dict]]: A dictionary with preliminary research results and results for each keyword.
    """
    from skills import search_arxiv

    # Conduct preliminary research using arXiv
    preliminary_results = search_arxiv(scope, max_results=max_results_per_keyword)

    # Search for scholarly articles and papers using the identified keywords
    keyword_results = {}
    for keyword in keywords:
        keyword_results[keyword] = search_arxiv(keyword, max_results=max_results_per_keyword)

    # Combine the results
    research_results = {
        "preliminary_results": preliminary_results,
        "keyword_results": keyword_results
    }

    return research_results

# This function can be imported and used in another agent to conduct research on SSL certificates.
# Example usage:
# from research_ssl_certificates import search_ssl_certificates_articles
# scope = "SSL certificates"
# keywords = ["encryption", "public key infrastructure", "certificate authority"]
# research_results = search_ssl_certificates_articles(scope, keywords)