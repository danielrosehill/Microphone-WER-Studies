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

Published word error rates (WER) by microphone, with microphone type, list price where found, and the source on every row. 95 results from five sources.

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

- Sanna Alander (2025). [Comparing Microphones Used in Medical Dictation Based on Speech Recognition Accuracy and Usability](https://aaltodoc.aalto.fi/handle/123456789/135659). Master's thesis, Aalto University. Limits: Two speakers in stage 1, six in stage 2; stage 2 replayed SpeechOne recordings through a Bose SoundLink Mini; distance not tested. Thesis is CC BY-NC-SA 4.0; only numeric results are cited here.
- Mariah Bradford, Paige Hansen, Ross Beveridge, Nikhil Krishnaswamy, Nathaniel Blanchard (2022). [A deep dive into microphone hardware for recording collaborative group work](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html). Educational Data Mining 2022 (poster). Limits: One ASR engine; differences within one SD; Blue Yeti used in omni mode. Authors' overall pick was the MXL AC-404, for noise robustness and price.
- Brian D. Tran, Di Hu, Seungjun Kim, Yawen Guo, Ramya Mangu, Tera L. Reynolds, Jennifer Elston Lafata, Ming Tai-Seale, Kai Zheng (2026). [Does Recording Hardware Matter for Clinical Speech Recognition? Evaluating ASR Performance Across Consumer Devices](https://pmc.ncbi.nlm.nih.gov/articles/PMC13228836/). Preprint, not peer reviewed. Limits: Two speakers. Across engines, pooled medians ranged 16.7-20.7%.
- Pattara Tipaksorn et al. (2025). [LOTUSDIS: A Thai far-field meeting corpus for robust conversational ASR](https://arxiv.org/abs/2509.18722). arXiv:2509.18722. Limits: Device and distance change together; not a dictation task.
- Daniel Rosehill (2025). [One-Shot Transcription Microphone Eval](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval). Personal benchmark. Limits: One take per condition; one word is 0.32 points, so the 4.13-6.35% spread is about seven words. An anecdotal data point, not a ranking.

## Credit and licence

Measurements belong to the cited authors; cite them. The compilation is CC BY 4.0 and does not relicense the underlying works. Compiled by Daniel Rosehill with Claude. Alander's values were transcribed by eye from table images. `rosehill-2025` is the compiler's own benchmark.
