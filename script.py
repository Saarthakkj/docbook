#!/usr/bin/env python3
import argparse
import arxiv

def main():
    parser = argparse.ArgumentParser(description="Search arXiv from the command line")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("--max_results", type=int, default=5, help="Maximum number of results to fetch")
    parser.add_argument("--sort", type=str, default="submittedDate", choices=["relevance", "lastUpdatedDate", "submittedDate"], help="Sort criterion")
    parser.add_argument("--pdf", action="store_true", help="Print PDF links instead of abstract URLs")

    args = parser.parse_args()

    # Map string sort to enum
    sort_map = {
        "relevance": arxiv.SortCriterion.Relevance,
        "lastUpdatedDate": arxiv.SortCriterion.LastUpdatedDate,
        "submittedDate": arxiv.SortCriterion.SubmittedDate,
    }

    search = arxiv.Search(
        query=args.query,
        max_results=args.max_results,
        sort_by=sort_map[args.sort],
    )

    for result in search.results():
        print("Title:", result.title)
        print("Authors:", ", ".join(a.name for a in result.authors))
        print("Published:", result.published.date())
        print("Link:", result.pdf_url if args.pdf else result.entry_id)
        print("Summary:", result.summary[:250].replace("\n", " "), "...\n")

if __name__ == "__main__":
    main()

