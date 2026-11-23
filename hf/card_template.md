---
license: cc-by-4.0
language: [en]
pretty_name: Microphone WER Studies
size_categories: [n<1K]
tags: [speech-recognition, asr, word-error-rate, microphones, dictation]
configs:
- config_name: default
  data_files: master.csv
---

# Microphone WER Studies

Published word error rates (WER) by microphone, with microphone type, list price where found, and the source on every row. {{N}} results from five sources.

**Explore:** [Microphone WER Explorer](https://huggingface.co/spaces/danielrosehill/Microphone-WER-Explorer)

Generated from [github.com/danielrosehill/Microphone-WER-Studies](https://github.com/danielrosehill/Microphone-WER-Studies). Please send corrections there.

## Do not rank across the whole table

Only compare rows with the same `comparison_group`. Texts, engines, rooms and statistics differ between studies. In the `rosehill-2025` and `tipaksorn-2025` groups, distance or conditions also vary by row, so check `condition`.

## Key columns

| Column | Meaning |
|---|---|
| `comparison_group` | Same study, engine and task |
| `mic_category`, `mic_type` | Normalised category, then detail (assigned by the compiler) |
| `distance_cm` | Nominal; blank where not stated per row. 12-15 cm is stored as 13.5 |
| `wer_pct` | As reported; see `statistic` for mean, median or single take |
| `wer_gap_to_group_best_pts` | Derived: points above the lowest WER in the group |
| `price_amount`, `price_currency`, `price_basis` | Not all are manufacturer prices; check the basis. Blank means not found or not listed for that row |
| `source_*` | Full citation and known limits |

## Sources

{{STUDIES}}

## Credit and licence

Measurements belong to the cited authors; cite them. The compilation is CC BY 4.0 and does not relicense the underlying works. Compiled by Daniel Rosehill with Claude. Alander's values were transcribed by eye from table images. `rosehill-2025` is the compiler's own benchmark.
