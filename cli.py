import argparse
from pubmed.fetcher import search_pubmed, fetch_details
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech authors.")
    parser.add_argument("query", type=str, help="PubMed query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()
    if args.debug:
        print(f"Searching PubMed for query: {args.query}")
    ids = search_pubmed(args.query)
    if args.debug:
        print(f"Found {len(ids)} paper IDs.")
    papers = fetch_details(ids)
    df = pd.DataFrame(papers)
    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Saved results to {args.file}")
    else:
        print(df)
