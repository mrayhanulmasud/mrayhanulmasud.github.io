import argparse, re, json, sys, html
from pathlib import Path

def safe(v): return (v or "").strip()

def is_first_author(author_line, last_name_hint="Masud"):
    # crude check: first author contains 'Masud' (customize with --first-author)
    parts = [a.strip() for a in author_line.split(" and ") if a.strip()]
    return len(parts) > 0 and last_name_hint.lower() in parts[0].lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scholar-id", required=True)
    ap.add_argument("--out", default="_data/publications.yml")
    ap.add_argument("--first-author", default="Masud")
    args = ap.parse_args()

    try:
        from scholarly import scholarly
        import bibtexparser
    except Exception as e:
        print("Please install dependencies first: pip install scholarly bibtexparser", file=sys.stderr)
        sys.exit(2)

    author = scholarly.search_author_id(args.scholar_id)
    author = scholarly.fill(author, sections=["publications"])
    pubs = []
    for p in author.get("publications", []):
        bib = scholarly.fill(p).get("bib", {})
        title = safe(bib.get("title"))
        authors = safe(bib.get("author", "").replace(",", " and"))
        venue = safe(bib.get("venue") or bib.get("journal") or bib.get("booktitle"))
        year = safe(bib.get("pub_year") or bib.get("year"))
        url = safe(p.get("eprint_url") or p.get("pub_url") or p.get("pub_url"))
        entry = {
            "title": title,
            "authors": authors.replace(" and ", ", "),
            "venue": venue,
            "year": int(year) if year.isdigit() else year,
            "type": "Conference" if venue and venue.isupper() else "",
            "first_author": is_first_author(authors, args.first_author),
            "paper_url": url,
            "tool_url": "",
            "code_url": "",
            "poster_url": "",
            "abstract": ""
        }
        pubs.append(entry)

    # sort by year desc
    pubs = sorted(pubs, key=lambda x: x.get("year", 0) or 0, reverse=True)

    # write YAML
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for p in pubs:
            f.write("- " + "
  ".join(f"{k}: {json.dumps(v)}" for k, v in p.items()) + "
")

    print(f"Wrote {len(pubs)} entries to {out}")

if __name__ == "__main__":
    main()