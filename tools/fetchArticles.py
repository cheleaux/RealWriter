import requests
from feedparser import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def arxiv_search( query :str , max_results :int = 10 ) -> list:
  """
  This function searches for arXiv papers based on a query and attempts to locate the PDF link for each result.

  Args:
      query (str): The search query/scope for arXiv papers.
      max_results (int, optional): The maximum number of results to return (defaults to 10).

  Returns:
      list: A list of dictionaries containing paper information and the found PDF link (if available).
  """
  base_url = "http://export.arxiv.org/api/query?"
  search_query = f"search_query=all:{query}"
  start = 0
  max_results = f"max_results={max_results}"
  url = f"{base_url}{search_query}&start={start}&{max_results}"

  response = requests.get(url)
  feed = parse(response.content)
  papers_with_pdf = []

  for entry in feed.entries:
    paper_info = {"title": entry.title, "link": entry.link}
    pdf_link = find_pdf_link(entry.link)
    paper_info["pdf_link"] = f"https://arxiv.org/{pdf_link}" if pdf_link and pdf_link.startswith('/pdf/') else None
    papers_with_pdf.append(paper_info)

  return papers_with_pdf

def find_pdf_link( url :str ) -> str:
  """
  This function attempts to find the anchor tag with the text "view pdf" on the given URL.

  Args:
      url (str): The URL of the webpage to search.

  Returns:
      str: The href attribute of the anchor tag with the text "view pdf" or None if not found.
  """
  try:
    response = urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    
    # Search for anchor tags with text "view pdf" (case-insensitive)
    anchors = soup.find_all('a', string=lambda text: text and text.lower() == "view pdf")
    
    if anchors:
      # Assuming there's only one relevant anchor tag, return its href attribute
      return anchors[0]['href']
    else:
      return None
  except Exception as e:
    print(f"An error occurred finding PDF link for {url}: {e}")
    return None


# for paper in results: 
#   print(f"Title: {paper['title']}")
#   print(f"Link: {paper['link']}")
#   if "pdf_link" in paper:
#     print(f"PDF Link: {paper['pdf_link']}")
#   else:
#     print("PDF link not found on the webpage.")
#   print("-" * 50)

