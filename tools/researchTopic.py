import sys  
from autogen import search_arxiv  
  
def safe_print(content):  
    """ 
    Function to safely print Unicode text to the console.  
    Handles UnicodeEncodeError by encoding the content before printing.  
      
    Args:  
        content (str): The content to print.  
    """  
    try:  
        print(content)  
    except UnicodeEncodeError:  
        print(content.encode('utf-8').decode(sys.stdout.encoding, errors='replace'))  
  
def conduct_research(scope, objectives, keywords, max_results_per_keyword=5):  
    """  
    Conducts research on a given scope with specified objectives and keywords.  
    Searches for scholarly articles and papers using arXiv.  
  
    Args:  
        scope (str): The research scope or main topic.  
        objectives (list): A list of objectives for the research.  
        keywords (list): A list of keywords related to the research topic.  
        max_results_per_keyword (int): Maximum number of results to fetch per keyword.  
  
    Returns:  
        None  
    """  
    # Conduct preliminary research using arXiv  
    preliminary_results = search_arxiv(scope, max_results=max_results_per_keyword)  
  
    # Search for scholarly articles and papers using the identified keywords  
    scholarly_articles = []  
    for keyword in keywords:  
        scholarly_articles.extend(search_arxiv(keyword, max_results=max_results_per_keyword))  
  
    # Output the preliminary research results  
    safe_print("Preliminary research results:")  
    for result in preliminary_results:  
        safe_print(f"Title: {result['title']}")  
        safe_print(f"Authors: {', '.join(result['authors'])}")  
        safe_print(f"Summary: {result['summary']}\n")  
  
    # Output the scholarly articles found  
    safe_print("Scholarly articles found:")  
    for article in scholarly_articles:  
        safe_print(f"Title: {article['title']}")  
        safe_print(f"Authors: {', '.join(article['authors'])}")  
        safe_print(f"Summary: {article['summary']}\n")  
  
# Example usage:  
# scope = "SSL certificates"  
# objectives = ["educate readers", "provide a how-to guide", "analyze current trends"]  
# keywords = ["encryption", "public key infrastructure", "certificate authority"]  
# conduct_research(scope, objectives, keywords)  