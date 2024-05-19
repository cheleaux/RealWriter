# filename: find_ssl_cert_papers.py
from skills import search_arxiv

def main():
    query = "SSL certificates"
    max_results = 5  # You can adjust the number of results as needed
    papers = search_arxiv(query, max_results)

    if papers:
        print(f"Found {len(papers)} papers related to '{query}':\n")
        for i, paper in enumerate(papers, start=1):
            print(f"Paper {i}:")
            print(f"Title: {paper['title']}")
            print(f"Authors: {', '.join(paper['authors'])}")
            print(f"Summary: {paper['summary']}\n")
            print(f"PDF URL: {paper['pdf_url']}\n")
    else:
        print(f"No papers found for the query '{query}'.")

if __name__ == "__main__":
    main()