# Microphone-WER-Studies
Public compilation of WER by microphone. `scripts/build.py` is the only place to edit data; README.md and data/ are generated (`uv run scripts/build.py`).
Never merge or rank WER across studies. Every study needs a citation and limits; every price needs a source and `price_basis`. No sale prices.
Alander's tables are images in the PDF (pp. 21, 37, 45); transcribed by eye 2026-11-23.
`data/master.csv` is the master table; GitHub feeds HF dataset danielrosehill/Microphone-WER-Studies. After any data change: `uv run scripts/push_hf.py`, then commit and push. `hf/README.md` is generated from `hf/card_template.md`.
Compare only within `comparison_group`.
Space `danielrosehill/Microphone-WER-Explorer` (static, `space/`) reads the HF dataset live, with a bundled fallback CSV. Redeploy after page edits: `uv run scripts/push_space.py`.
