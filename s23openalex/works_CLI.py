import argparse
from s23openalex.works import Works


def main():
    parser = argparse.ArgumentParser(
        description="Get RIS or BibTeX citation for a given DOI"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ris", action="store_true", help="Request RSI format")
    group.add_argument("--bibtex", action="store_true", help="Request BibTeX format")
    parser.add_argument("doi", help="The DOI to retrieve")

    args = parser.parse_args()

    w = Works(args.doi)

    if args.ris:
        print(w.ris._repr_html_())

    elif args.bibtex:
        print(w.bibtex)


if __name__ == "__main__":
    main()
