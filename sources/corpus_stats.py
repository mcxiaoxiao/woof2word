#!/usr/bin/env python3
"""Regenerate the corpus statistics behind Figure 5 (and the Method section).

Reads paper/sections/12_bibliography.tex, splits it into the thematic blocks
marked by comment headers, and derives every number printed by this script
directly from the \bibitem entries. No count is hardcoded.

Usage:  python3 sources/corpus_stats.py [--csv sources/corpus_stats.csv]
"""

import argparse
import collections
import os
import re
import sys

BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir,
                   "paper", "sections", "12_bibliography.tex")

# Each bibliography block header is folded into one of seven reporting groups.
# The mapping is by header name, so re-running the script after adding entries
# re-derives the group sizes instead of trusting a stale number.
# The unlabelled front block of the bibliography mixes three kinds of source,
# so its entries are assigned by key. Every other block is assigned by header.
CANINE_FRONT = {
    "pongracz2005barks", "pongracz2006acoustic", "molnar2006discriminate",
    "farago2017growls", "icassp2018dogbark", "waller2013dogfacs",
    "kaminski2017attention", "kaminski2004rico", "pilley2011chaser",
    "bastos2024plos", "bastos2024scirep", "bastos2023interact",
    "animalcog2025review", "quaranta2007tail", "andics2014voice",
    "kassis2026skills", "sci2024domestication", "sci2022explainable",
    "sci2023cnnewoa", "sci2025automated", "sci2025landmarks",
}
CROSS_FRONT = {
    "sharma2024whale", "andreas2022ceti", "google2025dolphingemma",
    "wham2025", "arxiv2025whaletrans", "hagiwara2023aves",
    "robinson2024naturelm", "ghani2023perch", "hagiwara2023beans",
    "openbeats2025", "esp2026finch", "yovel2025critique",
}
PRODUCT_FRONT = {
    "traini2024", "bowlingual2002", "meowtalk2020", "mengxiaoyi2026",
    "petpuls2021",
}
KEY_GROUP = {}
for _key in CANINE_FRONT:
    KEY_GROUP[_key] = "Canine communication, cognition & products"
for _key in CROSS_FRONT:
    KEY_GROUP[_key] = "Cross-species decoding & bioacoustics"
for _key in PRODUCT_FRONT:
    KEY_GROUP[_key] = "Canine communication, cognition & products"

GROUP_OF_HEADER = {
    "FRONT": "Canine communication, cognition & products",
    "Bioacoustics & animal communication": "Cross-species decoding & bioacoustics",
    "Canine cognition (additional)": "Canine communication, cognition & products",
    "Human MT & the Transformer genealogy": "Machine translation & the Transformer",
    "Speech SSL, ASR, speech translation": "Speech, audio self-supervision & neural codecs",
    "Neural audio codecs & generative audio":
        "Speech, audio self-supervision & neural codecs",
    "Pretraining, LLMs, multimodality": "Large language models & multimodality",
    "Transfer, evaluation, grounding": "Transfer, evaluation & ML methods",
    "ML methods & foundations": "Transfer, evaluation & ML methods",
    "Ethics & governance": "Enrichment, ethics & population statistics",
    "Population & ownership statistics": "Enrichment, ethics & population statistics",
    "Developmental closed-loop route (Section 9)":
        "Canine communication, cognition & products",
    "Enrichment: MT stack, audio, dog cognition, ethics":
        "Enrichment, ethics & population statistics",
}

GROUP_ORDER = [
    "Canine communication, cognition & products",
    "Cross-species decoding & bioacoustics",
    "Speech, audio self-supervision & neural codecs",
    "Transfer, evaluation & ML methods",
    "Machine translation & the Transformer",
    "Large language models & multimodality",
    "Enrichment, ethics & population statistics",
]

BIBITEM = re.compile(r"\\bibitem(\[[^\]]*\])?\{([^}]+)\}")
HEADER = re.compile(r"^%\s*(?:=+|-+)\s*(.*?)\s*(?:=+|-+)\s*$")


def entries(path):
    """Yield (header, key, text) for every \bibitem in the bibliography."""
    with open(path, encoding="utf-8") as handle:
        body = handle.read().split(r"\begin{thebibliography}")[1]
        body = body.split(r"\end{thebibliography}")[0]
    header, key, buf = "FRONT", None, []
    out = []
    for line in body.split("\n"):
        marked = HEADER.match(line)
        if marked:
            if key is not None:
                out.append((header, key, "\n".join(buf)))
            header, key, buf = marked.group(1), None, []
            continue
        found = BIBITEM.match(line)
        if found:
            if key is not None:
                out.append((header, key, "\n".join(buf)))
            key, buf = found.group(2), [line]
        elif key is not None:
            buf.append(line)
    if key is not None:
        out.append((header, key, "\n".join(buf)))
    return out


def year_of(text):
    """Latest four-digit year in the entry, i.e. the year of the cited work."""
    years = [int(y) for y in re.findall(r"\b(1[89]\d\d|20\d\d)\b", text)]
    return max(years) if years else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None, help="write a per-entry CSV here")
    args = ap.parse_args()

    rows = entries(BIB)
    per_year = collections.Counter()
    per_header = collections.Counter()
    per_group = collections.Counter()
    undated = []
    for header, key, text in rows:
        per_header[header] += 1
        group = KEY_GROUP.get(key) or GROUP_OF_HEADER.get(header)
        if group is None:
            sys.exit(f"unmapped bibliography entry: {key!r} in block {header!r}")
        per_group[group] += 1
        year = year_of(text)
        if year is None:
            undated.append(key)
            per_year["pre-1800 or undated"] += 1
        else:
            per_year[year] += 1

    total = len(rows)
    pre2001 = sum(v for k, v in per_year.items() if isinstance(k, int) and k < 2001)
    print(f"bibliography entries: {total}")
    print(f"entries dated before 2001: {pre2001}")
    if undated:
        print(f"undated entries: {len(undated)} -> {', '.join(undated)}")

    print("\nper-entry-count by year (from 2001)")
    running = pre2001
    for year in sorted(k for k in per_year if isinstance(k, int) and k >= 2001):
        running += per_year[year]
        print(f"{year}\t{per_year[year]}\t{running}")

    print("\nper-group totals (sum = %d)" % total)
    for group in GROUP_ORDER:
        print(f"{per_group[group]}\t{group}")
    print("\nper-header totals (audit trail)")
    for header, count in per_header.items():
        print(f"{count}\t{header}")

    assert sum(per_group.values()) == total, "group mapping lost entries"
    print("\ncheck: groups sum to the entry count, %d == %d" % (sum(per_group.values()), total))

    if args.csv:
        import csv
        with open(args.csv, "w", newline="", encoding="utf-8") as handle:
            w = csv.writer(handle)
            w.writerow(["key", "year", "bibliography_block", "reporting_group"])
            for header, key, text in rows:
                w.writerow([key, year_of(text) or "", header, KEY_GROUP.get(key) or GROUP_OF_HEADER.get(header, "UNMAPPED")])
        print(f"wrote {args.csv}")


if __name__ == "__main__":
    main()
