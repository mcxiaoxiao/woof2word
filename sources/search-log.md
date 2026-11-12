# Search log · 检索记录

Survey: *The Canine Rosetta Stone: How Far Are We from Translating What Dogs Say?*
Method: narrative, evidence-bounded review (not PRISMA). Search window: **2026-11-09 → 2026-11-12**.
Tooling: structured web search + secondary-index citation verification.
Commercial accuracies are logged **as vendor claims**, not verified results.

## Queries executed (date · query · purpose)

| Date | Query (abridged) | Purpose |
|---|---|---|
| 2026-11-09 | AI translate dog barks emotion Traini Petpuls accuracy 2026 | product landscape |
| 2026-11-09 | Earth Species Project / CETI whale decoding 2026 | cross-species projects |
| 2026-11-09 | sperm whale phonetic alphabet Nature Communications 2024 Sharma | CETI structure result |
| 2026-11-09 | Google DolphinGemma Wild Dolphin Project parameters SoundStream | DolphinGemma specs |
| 2026-11-09 | dog bark acoustic Pongracz Farago Molnar humans classify barks | ELTE psychophysics |
| 2026-11-09 | dog soundboard buttons Rossano Scientific Reports Bunny | AIC button studies |
| 2026-11-09 | DogFACS Waller 2013 dog facial expression | facial coding |
| 2026-11-09 | Chaser 1022 words Pilley Reid 2011 / Rico Kaminski 2004 Science | receptive vocabulary |
| 2026-11-09 | Earth Species Project AVES NatureLM-audio BEANS benchmark | bioacoustic foundation models |
| 2026-11-10 | Bastos Rossano 2024 soundboard dogs PLoS ONE / Sci Rep title | verify button-study DOIs |
| 2026-11-10 | Sharma 2024 contextual combinatorial sperm whale Nat Commun | verify CETI DOI |


## Corpus accounting (reproducible)

`sources/corpus_stats.py` reads `paper/sections/12_bibliography.tex` and derives
every corpus number printed in the paper. Run:

    python3 sources/corpus_stats.py --csv sources/corpus_stats.csv

Current output (2026-11-12):

- **256** `ibitem` entries, all cited, zero orphans, zero dangling keys.
- Year of an entry = the latest four-digit year stated in it; **23** entries
  predate 2001, **177** (70%) fall in 2016 onward, **89** in 2020–2023.
- Thematic groups, assigned by bibliography block (the unlabelled front block
  is assigned entry by entry in `KEY_GROUP`): canine communication, cognition
  & products **48**; speech/audio/codecs **39**; transfer, evaluation & ML
  methods **38**; machine translation & the Transformer **36**; cross-species
  decoding & bioacoustics **33**; LLMs & multimodality **32**; enrichment,
  ethics & population statistics **27**.
- The script asserts that the group totals sum to the entry count, so a new
  bibliography block without a mapping fails loudly instead of silently.
- `corpus_stats.csv` is the per-entry audit trail (key, year, block, group).

## Provenance of the protocol section (Section 9)

The benchmark specification was assembled from methodological sources already in
the bibliography (datasheets, model cards, stochastic-parrots, the button-array
combination analysis, the object-choice literature) plus three canonical
measurement references added on 2026-11-12 for the parts the corpus did not
cover: calibration reporting, a transferred speaker-verification baseline, and
an experimental design that removes the human observer. Their bibliographic
details were checked against the primary record:

- Guo, Pleiss, Sun & Weinberger, *On calibration of modern neural networks*,
  ICML 2017 — arXiv **1706.04599**.
- Snyder, Garcia-Romero, Sell, Povey & Khudanpur, *X-vectors: robust DNN
  embeddings for speaker recognition*, Proc. ICASSP 2018, pp. 5329–5333
  (author list and pagination corrected after checking citing records; the
  DOI was left out because it could not be confirmed directly).
- Proops, McComb & Reby, *Cross-modal individual recognition in domestic
  horses*, PNAS 106(4):947–951 (2009) — DOI **10.1073/pnas.0809127105**; and
  Proops & McComb, *... extends to familiar humans*, Proc. R. Soc. B
  279:3131–3138 (2012) — DOI **10.1098/rspb.2012.0626**.
  An initial draft cited a 2018 Biology Letters horse paper that checking
  against citing records failed to confirm; it was replaced by the two studies
  above rather than left in the manuscript.

No new product or vendor claims entered the paper in this revision.

## Citations verified to venue/year/DOI (via secondary indexes)

- Sharma et al. 2024, *Nat. Commun.* 15:3617 — DOI **10.1038/s41467-024-47221-8**
  (authors: Sharma, Gero, Payne, Gruber, Rus, Torralba, Andreas).
- Bastos et al. 2024, *PLoS ONE* 19:e0307189 — DOI **10.1371/journal.pone.0307189**
  (word comprehension; ~30 + 29 dogs, two experiments).
- Bastos et al. 2024, *Sci. Rep.* 14:28771 — DOI **10.1038/s41598-024-79517-6**
  (non-accidental, non-random, non-imitative two-button combinations).
- Bastos & Rossano 2023, *Interaction Studies* 24:311–334 — DOI **10.1075/is.22050.pin**.
- ICASSP 2018 "What is my dog trying to tell me?" — DOI **10.1109/ICASSP.2018.8461757**.
- NatureLM-audio — **arXiv:2411.07186** (Robinson, Miron, Hagiwara, Pietquin).
- OpenBEATs — **arXiv:2507.14129**; translative whale model — **arXiv:2512.02206**.
- DogFACS facial-expression papers — DOIs 10.1038/s41598-022-27079-w,
  -023-30442-0, -024-61110-6, -025-15741-y, -025-07040-3.
- Kaminski et al. 2004, *Science* 304:1682–1683 (Rico, fast mapping).
- Pilley & Reid 2011, *Behav. Processes* 86:184–195 (Chaser, 1,022 objects).

## Reported as claims / not peer-reviewed (flagged in paper)

- Traini PetGPT/PEBI: 81.5%, ~12 emotions, ~120 breeds (vendor).
- "Meng Xiao Yi": 94.6% (vendor, via Chinese tech press).
- WhAM (CETI, 2025), ZF-AIM finch model (ESP/McGill, 2026): project reports.
- DolphinGemma: Google DeepMind project report, 2025-04-14 (~400M params).

## Limitations

- Web-ranked results and excerpts cannot establish exhaustive coverage.
- Several fast-moving items rest on reports/journalism, not peer review.
- Some citations confirmed via secondary indexes, not full-text retrieval;
  a production version should verify each against the primary record.
- Single-reviewer screening; no independent second eligibility decision.