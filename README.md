# Microphone WER Studies

Which microphone gives the lowest word error rate (WER) in speech recognition? This is a credited compilation of studies that measured WER by microphone, with microphone type and list price.

**Short answer:** none of the studies here identifies one lowest-WER microphone for every situation. In quiet, decent microphones mostly cluster together. Distance, noise, airflow and the choice of speech engine often matter more.

> **Compare within a table, not between tables.** Texts, engines, rooms, distances and statistics differ by study. This is not an exhaustive literature review.

## Observations

- **Alander 2025:** eight of eleven mics averaged 3.96-4.65%. With the strongest fan, results ran from 4.87% to 99.17%.
- **Bradford 2022:** script reading spanned 10.7-12.0%, within one SD. The authors found no clear relationship between price and ASR performance.
- **Tran 2026:** on Azure Whisper, five devices spanned 17.6-17.9%. Engine medians spanned 16.7-20.7%.
- **LOTUSDIS 2025:** untuned Whisper got much worse on the distant devices.

## Results

### Sanna Alander (2025): Comparing Microphones Used in Medical Dictation Based on Speech Recognition Accuracy and Usability

Sanna Alander. *Master's thesis, Aalto University*. [Source](https://aaltodoc.aalto.fi/handle/123456789/135659)

- **Engine:** Dragon Medical One
- **Statistic:** mean WER, average of stages 1 and 2 (Table 9)
- **Setup:** Close-up dictation in quiet; 60 cm laptop, 6.5 cm handhelds, 3 cm headsets in playback tests
- **Limits:** Two speakers in stage 1, six in stage 2; stage 2 replayed SpeechOne recordings through a Bose SoundLink Mini; distance not tested. Thesis is CC BY-NC-SA 4.0; only numeric results are cited here.

| Microphone | Type | Condition | WER | List price |
|---|---|---|---|---|
| Poly Blackwire C5210T | Headset, wired USB boom | quiet | 3.96% | [EUR 121.34](https://www.huntoffice.ie/headsets~connection_type=usb-c) (reseller-stated list) |
| Philips SpeechOne PSM6500 series | Headset, wireless dictation | quiet | 3.99% | [USD 618.00](https://www.tvps.com/wireless-dictation-headsets/) (reseller-stated list) |
| Olympus RecMic DR-2200 | Handheld dictation, wired | quiet | 4.00% | n/a |
| Philips SpeechMike Premium Touch SMP3700/3800 | Handheld dictation, wired USB | quiet | 4.19% | [USD 423.00 (from)](https://www.dictation.philips.com/us/products/desktop-dictation/) (manufacturer list) |
| Philips SpeechMike wireless | Handheld dictation, wireless | quiet | 4.26% | [USD 497.00 (from)](https://www.dictation.philips.com/us/products/desktop-dictation/) (manufacturer list) |
| Olympus RM-4100S | Handheld dictation, wired | quiet | 4.40% | n/a |
| iPhone 11 | Phone, built-in | quiet | 4.51% | n/a |
| Logitech H340 | Headset, wired USB boom | quiet | 4.65% | [USD 24.99](https://www.logitech.com/en-us/shop/p/h340-usb-pc-noise-cancelling-mic) (manufacturer list) |
| JBL Tune 520BT | Headphones, Bluetooth, built-in mic | quiet | 7.48% | [USD 59.95](https://www.jbl.com/TUNE520BT.html) (manufacturer list) |
| HP 255 G8 laptop mic | Laptop, built-in | quiet | 11.63% | n/a |
| Logitech USB headset (older, unnamed) | Headset, wired USB | quiet | 13.70% | n/a |
| Philips SpeechOne PSM6500 series | Headset, wireless dictation | strongest fan airflow (phase 3) | 52.87% | n/a |
| Philips SpeechOne PSM6500 series | Headset, wireless dictation | loudest background noise (phase 3) | 12.25% | n/a |
| Olympus RecMic DR-2200 | Handheld dictation, wired | strongest fan airflow (phase 3) | 19.32% | n/a |
| Olympus RecMic DR-2200 | Handheld dictation, wired | loudest background noise (phase 3) | 8.44% | n/a |
| Poly Blackwire C5210T | Headset, wired USB boom | strongest fan airflow (phase 3) | 99.17% | n/a |
| Poly Blackwire C5210T | Headset, wired USB boom | loudest background noise (phase 3) | 4.96% | n/a |
| Philips SpeechMike Premium Touch SMP3700/3800 | Handheld dictation, wired USB | strongest fan airflow (phase 3) | 4.87% | n/a |
| Philips SpeechMike Premium Touch SMP3700/3800 | Handheld dictation, wired USB | loudest background noise (phase 3) | 9.52% | n/a |

### Mariah Bradford (2022): A deep dive into microphone hardware for recording collaborative group work

Mariah Bradford, Paige Hansen, Ross Beveridge, Nikhil Krishnaswamy, Nathaniel Blanchard. *Educational Data Mining 2022 (poster)*. [Source](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html)

- **Engine:** Google Cloud ASR
- **Statistic:** mean WER
- **Setup:** 33 people in 11 groups, simultaneous recording, mics 5 ft away
- **Limits:** One ASR engine; differences within one SD; Blue Yeti used in omni mode. Authors' overall pick was the MXL AC-404, for noise robustness and price.

| Microphone | Type | Condition | WER | List price |
|---|---|---|---|---|
| Saramonic SmartMic | Compact plug-in phone mic | script reading, 5 ft | 10.70% | [USD 25.00](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html) (price in study) |
| Saramonic SmartMic | Compact plug-in phone mic | group task, overlapping speech, 5 ft | 58.10% | n/a |
| Audio-Technica U891Rb | Boundary, cardioid condenser | script reading, 5 ft | 11.20% | [USD 349.00](https://www.audio-technica.com/en-us/u891rb) (manufacturer list) |
| Audio-Technica U891Rb | Boundary, cardioid condenser | group task, overlapping speech, 5 ft | 52.70% | n/a |
| Audio-Technica U891RbO | Boundary, omni condenser | script reading, 5 ft | 11.20% | [USD 319.00](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html) (price in study) |
| Audio-Technica U891RbO | Boundary, omni condenser | group task, overlapping speech, 5 ft | 53.00% | n/a |
| Audio-Technica ATR2100x-USB | Handheld dynamic, cardioid USB/XLR | script reading, 5 ft | 11.50% | [USD 99.00](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html) (price in study) |
| Audio-Technica ATR2100x-USB | Handheld dynamic, cardioid USB/XLR | group task, overlapping speech, 5 ft | 57.70% | n/a |
| Blue Yeti | Desktop USB condenser (omni mode) | script reading, 5 ft | 11.70% | [USD 139.99](https://www.logitechg.com/en-us/shop/p/yeti-premium-usb-microphone) (manufacturer list) |
| Blue Yeti | Desktop USB condenser (omni mode) | group task, overlapping speech, 5 ft | 61.30% | n/a |
| MXL AC-404 | Boundary USB, 3-capsule, 180 degrees | script reading, 5 ft | 12.00% | [USD 99.95](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html) (price in study) |
| MXL AC-404 | Boundary USB, 3-capsule, 180 degrees | group task, overlapping speech, 5 ft | 60.20% | n/a |

### Brian D. Tran (2026): Does Recording Hardware Matter for Clinical Speech Recognition? Evaluating ASR Performance Across Consumer Devices

Brian D. Tran, Di Hu, Seungjun Kim, Yawen Guo, Ramya Mangu, Tera L. Reynolds, Jennifer Elston Lafata, Ming Tai-Seale, Kai Zheng. *Preprint, not peer reviewed*. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC13228836/)

- **Engine:** Azure Whisper (one of six engines tested)
- **Statistic:** median WER
- **Setup:** 35 re-enacted clinical conversations, simultaneous recording, about 1.5 ft; clip-on worn by one speaker; quiet
- **Limits:** Two speakers. Across engines, pooled medians ranged 16.7-20.7%.

| Microphone | Type | Condition | WER | List price |
|---|---|---|---|---|
| Blue Yeti | Desktop USB condenser | two-person conversation, quiet | 17.60% | [USD 139.99](https://www.logitechg.com/en-us/shop/p/yeti-premium-usb-microphone) (manufacturer list) |
| MacBook Pro 2017 | Laptop, built-in | two-person conversation, quiet | 17.60% | n/a |
| Samsung Galaxy S7 | Phone, built-in | two-person conversation, quiet | 17.70% | n/a |
| Sony ICD-UX533 | Portable voice recorder | two-person conversation, quiet | 17.90% | n/a |
| Aputure A.lav | Lavalier / clip-on | two-person conversation, quiet | 17.90% | n/a |

### Pattara Tipaksorn (2025): LOTUSDIS: A Thai far-field meeting corpus for robust conversational ASR

Pattara Tipaksorn et al.. *arXiv:2509.18722*. [Source](https://arxiv.org/abs/2509.18722)

- **Engine:** Whisper large-v3, zero-shot
- **Statistic:** WER
- **Setup:** Spontaneous three-person Thai meetings with overlapping speech
- **Limits:** Device and distance change together; not a dictation task.

| Microphone | Type | Condition | WER | List price |
|---|---|---|---|---|
| Table condensers | Desktop condenser | 12-15 cm | 48.37% | n/a |
| Lavaliers | Lavalier / clip-on | 12-15 cm | 51.95% | n/a |
| JBL speaker device | Tabletop speaker mic | 2 m | 59.90% | n/a |
| Bluetooth speakerphone (3 m) | Speakerphone, Bluetooth | 3 m | 117.03% | n/a |
| Bluetooth speakerphone (10 m) | Speakerphone, Bluetooth | 10 m | 125.52% | n/a |

### Daniel Rosehill (2025): One-Shot Transcription Microphone Eval

Daniel Rosehill. *Personal benchmark*. [Source](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval)

- **Engine:** OpenAI whisper-1
- **Statistic:** WER, single take
- **Setup:** One speaker, one 315-word passage, mostly a quiet home office
- **Limits:** One take per condition; one word is 0.32 points, so the 4.13-6.35% spread is about seven words. An anecdotal data point, not a ranking.

| Microphone | Type | Condition | WER | List price |
|---|---|---|---|---|
| OnePlus Nord 3 5G | Phone, built-in | quiet | 4.13% | n/a |
| UGreen CM564 | Gooseneck USB | 30 cm | 4.44% | [~USD 18](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Audio-Technica ATR4697 | Boundary | 80 cm | 4.76% | [~USD 45](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| EMEET conference speakerphone | Speakerphone | quiet | 5.08% | [~USD 40](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Samson Q2U | Handheld dynamic, cardioid USB/XLR | 30 cm | 5.40% | [~USD 70](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| OnePlus Nord 3 5G | Phone, built-in | Voicenotes MP3 | 5.40% | n/a |
| Audio-Technica ATR4697 | Boundary | 30 cm | 5.40% | [~USD 45](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Jabra Speak 510 | Speakerphone | quiet | 5.40% | [~USD 110](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Logitech C925e | Webcam, built-in | 30 cm | 5.40% | [~USD 75](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Maono Elf | Lavalier / clip-on | quiet | 5.40% | [~USD 25](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Logitech H390 | Headset, wired USB boom | quiet | 5.71% | [~USD 30](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| OnePlus Nord 3 5G | Phone, built-in | ASR HQ recording | 5.71% | n/a |
| Yealink BH72 | Headset, wireless | vendor dongle | 6.03% | [~USD 160](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Yealink BH72 | Headset, wireless | generic Bluetooth adapter | 6.03% | [~USD 160](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| OnePlus Nord 3 5G | Phone, built-in | noisy market | 6.03% | n/a |
| Sony ICD-UX570 | Portable voice recorder | MP3 | 6.03% | [~USD 100](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |
| Audio-Technica ATR4750-USB | Gooseneck USB, omni | quiet | 6.35% | [~USD 55](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) (author's approximate price) |

## Related work (abstract or excerpt read only; not in the dataset)

- Brady et al. (2014), [microphones and placement for classroom ASR](https://pubs.aip.org/jasa/article/136/4_Supplement/2215/708554/Evaluating-microphones-and-microphone-placement): preliminary results favoured the Crown PZM-30 boundary mic.
- [Microphone Array Processing for Distant Speech Recognition](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Microphone20Array20Processing20for20Distant20Speech20Recognition20-20Towards20Real-World20Deployment.pdf): one channel of a 64-channel array 14.3%, full system 5.3%, lapel 4.2%.
- [Idiap RR 05-47 (2005)](https://publications.idiap.ch/attachments/reports/2005/rr-05-47.pdf): unadapted headset 42.5%, array 64.2%, lapel 67.0%.
- [Alapetite (2006)](https://alexandre.alapetite.fr/phd-risoe/publications/Alapetite-2006-IJMI.pdf): headset 83.2% recognition vs 73.9% for a Philips SpeechMike; reports recognition rate, not WER.

## Prices

Checked 2026-11-23. `price_basis` says what each figure is: `manufacturer list`, `reseller-stated list`, `price in study`, or `author's approximate price`. Only the first is a confirmed manufacturer price. Sale prices are excluded. `n/a` means no list price was found or none applies.

## Data

- [`data/results.csv`](data/results.csv): one row per study, microphone and condition.
- [`data/studies.json`](data/studies.json): citations, methods and limits.
- [`scripts/build.py`](scripts/build.py): edit this, then run `uv run scripts/build.py` to regenerate both files and this README.

Corrections and more studies are welcome by issue or pull request. Please include a source that reports WER by microphone.

## Credit and licence

The measurements belong to the cited authors; please cite them. This compilation is [CC BY 4.0](LICENSE), which does not relicense the underlying works. Compiled by Daniel Rosehill with Claude. The last table is the compiler's own benchmark.
