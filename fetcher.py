import requests
import pandas as pd
from typing import List, Dict
from tqdm import tqdm

EMAIL = "your.email@example.com"
API_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str) -> List[str]:
    resp = requests.get(f"{API_BASE}esearch.fcgi", params={
        "db": "pubmed",
        "term": query,
        "retmax": 100,
        "retmode": "json"
    })
    resp.raise_for_status()
    return resp.json()["esearchresult"]["idlist"]

def fetch_details(pmids: List[str]) -> List[Dict]:
    ids = ",".join(pmids)
    resp = requests.get(f"{API_BASE}efetch.fcgi", params={
        "db": "pubmed",
        "id": ids,
        "retmode": "xml",
        "rettype": "abstract"
    })
    resp.raise_for_status()
    from xml.etree import ElementTree as ET
    root = ET.fromstring(resp.content)
    results = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        authors = article.findall(".//Author")
        non_acad_authors = []
        companies = []
        email = ""
        for author in authors:
            aff = author.findtext(".//AffiliationInfo/Affiliation")
            if aff and not any(x in aff.lower() for x in ["university", "college", "school", "institute", "hospital"]):
                lastname = author.findtext("LastName") or ""
                firstname = author.findtext("ForeName") or ""
                non_acad_authors.append(f"{firstname} {lastname}".strip())
                companies.append(aff)
                if "@" in aff:
                    email = aff.split()[-1]
        if non_acad_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email,
            })
    return results
