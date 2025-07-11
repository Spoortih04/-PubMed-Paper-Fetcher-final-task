# PubMed Paper Fetcher

This is a simple Python tool that helps you search for research papers from PubMed. It finds papers where at least one author is from a pharmaceutical or biotech company.

---

## Features

- Search papers from PubMed using any query.
- Filters out academic authors (like universities or hospitals).
- Shows company-affiliated authors and their details.
- Save results as a CSV file or print to the screen.
- Easy-to-use command-line interface.
- Built with Python and Poetry.

---

## Installation

### Requirements

- Python 3.9 or above
- Poetry (for installing dependencies)

### Steps

1. Clone the project:
```bash
git clone https://github.com/Spoortih04/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

2. Install dependencies:
```bash
poetry install
```

---

## How to Use

Run this command with your search:

```bash
poetry run get-papers-list "your pubmed search here"
```

To save to a CSV file and show debug info:

```bash
poetry run get-papers-list "cancer immunotherapy" --file results.csv --debug
```

---

## Output

The result includes:

- PubMed ID
- Title
- Publication date
- Author names (from companies)
- Company affiliations
- Contact email (if available)

---


