"""Single source of the results: writes data/results.csv, data/studies.json and the README tables."""
import csv, json, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
TODAY = "2026-11-23"
PH = "https://www.dictation.philips.com/us/products/desktop-dictation/"
EDM = "https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.65/index.html"
OWN = "https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval"
studies = {
 "alander-2025": dict(authors="Sanna Alander", year=2025, title="Comparing Microphones Used in Medical Dictation Based on Speech Recognition Accuracy and Usability", venue="Master's thesis, Aalto University", url="https://aaltodoc.aalto.fi/handle/123456789/135659", engine="Dragon Medical One", statistic="mean WER, average of stages 1 and 2 (Table 9)", setup="Close-up dictation in quiet; 60 cm laptop, 6.5 cm handhelds, 3 cm headsets in playback tests", limits="Two speakers in stage 1, six in stage 2; stage 2 replayed SpeechOne recordings through a Bose SoundLink Mini; distance not tested. Thesis is CC BY-NC-SA 4.0; only numeric results are cited here."),
 "bradford-2022": dict(authors="Mariah Bradford, Paige Hansen, Ross Beveridge, Nikhil Krishnaswamy, Nathaniel Blanchard", year=2022, title="A deep dive into microphone hardware for recording collaborative group work", venue="Educational Data Mining 2022 (poster)", url=EDM, engine="Google Cloud ASR", statistic="mean WER", setup="33 people in 11 groups, simultaneous recording, mics 5 ft away", limits="One ASR engine; differences within one SD; Blue Yeti used in omni mode. Authors' overall pick was the MXL AC-404, for noise robustness and price."),
 "tran-2026": dict(authors="Brian D. Tran, Di Hu, Seungjun Kim, Yawen Guo, Ramya Mangu, Tera L. Reynolds, Jennifer Elston Lafata, Ming Tai-Seale, Kai Zheng", year=2026, title="Does Recording Hardware Matter for Clinical Speech Recognition? Evaluating ASR Performance Across Consumer Devices", venue="Preprint, not peer reviewed", url="https://pmc.ncbi.nlm.nih.gov/articles/PMC13228836/", engine="Azure Whisper (one of six engines tested)", statistic="median WER", setup="35 re-enacted clinical conversations, simultaneous recording, about 1.5 ft; clip-on worn by one speaker; quiet", limits="Two speakers. Across engines, pooled medians ranged 16.7-20.7%."),
 "tipaksorn-2025": dict(authors="Pattara Tipaksorn et al.", year=2025, title="LOTUSDIS: A Thai far-field meeting corpus for robust conversational ASR", venue="arXiv:2509.18722", url="https://arxiv.org/abs/2509.18722", engine="Whisper large-v3, zero-shot", statistic="WER", setup="Spontaneous three-person Thai meetings with overlapping speech", limits="Device and distance change together; not a dictation task."),
 "rosehill-2025": dict(authors="Daniel Rosehill", year=2025, title="One-Shot Transcription Microphone Eval", venue="Personal benchmark", url=OWN, engine="OpenAI whisper-1", statistic="WER, single take", setup="One speaker, one 315-word passage, mostly a quiet home office", limits="One take per condition; one word is 0.32 points, so the 4.13-6.35% spread is about seven words. An anecdotal data point, not a ranking."),
}
rows = []
def a(s, mic, typ, cond, wer, rrp="", basis="", src="", note=""):
    rows.append(dict(study=s, microphone=mic, type=typ, condition=cond, wer_pct=wer, price=rrp, price_basis=basis, price_source=src, note=note))
HH="Handheld dictation"; S="alander-2025"; q="quiet"
MAN="manufacturer list"; PAP="price in study"; RES="reseller-stated list"; OAP="author's approximate price"
a(S,"Poly Blackwire C5210T","Headset, wired USB boom",q,3.96,"EUR 121.34",RES,"https://www.huntoffice.ie/headsets~connection_type=usb-c","Price is for the current Blackwire 5210 USB-C; equivalence to the tested unit assumed")
a(S,"Philips SpeechOne PSM6500 series","Headset, wireless dictation",q,3.99,"USD 618.00",RES,"https://www.tvps.com/wireless-dictation-headsets/","PSM6500")
a(S,"Olympus RecMic DR-2200",HH+", wired",q,4.00)
a(S,"Philips SpeechMike Premium Touch SMP3700/3800",HH+", wired USB",q,4.19,"USD 423.00 (from)",MAN,PH)
a(S,"Philips SpeechMike wireless",HH+", wireless",q,4.26,"USD 497.00 (from)",MAN,PH,"Thesis prints 'SMP400'; SMP4000 assumed")
a(S,"Olympus RM-4100S",HH+", wired",q,4.40)
a(S,"iPhone 11","Phone, built-in",q,4.51)
a(S,"Logitech H340","Headset, wired USB boom",q,4.65,"USD 24.99",MAN,"https://www.logitech.com/en-us/shop/p/h340-usb-pc-noise-cancelling-mic")
a(S,"JBL Tune 520BT","Headphones, Bluetooth, built-in mic",q,7.48,"USD 59.95",MAN,"https://www.jbl.com/TUNE520BT.html","Regular price; another variant on the page is 69.95")
a(S,"HP 255 G8 laptop mic","Laptop, built-in",q,11.63)
a(S,"Logitech USB headset (older, unnamed)","Headset, wired USB",q,13.70,note="Very inconsistent results")
for m,t,f,n in [("Philips SpeechOne PSM6500 series","Headset, wireless dictation",52.87,12.25),("Olympus RecMic DR-2200",HH+", wired",19.32,8.44),("Poly Blackwire C5210T","Headset, wired USB boom",99.17,4.96),("Philips SpeechMike Premium Touch SMP3700/3800",HH+", wired USB",4.87,9.52)]:
    a(S,m,t,"strongest fan airflow (phase 3)",f); a(S,m,t,"loudest background noise (phase 3)",n)
for m,t,w,g,p,b,u in [("Saramonic SmartMic","Compact plug-in phone mic",10.7,58.1,"USD 25.00",PAP,EDM),("Audio-Technica U891Rb","Boundary, cardioid condenser",11.2,52.7,"USD 349.00",MAN,"https://www.audio-technica.com/en-us/u891rb"),("Audio-Technica U891RbO","Boundary, omni condenser",11.2,53.0,"USD 319.00",PAP,EDM),("Audio-Technica ATR2100x-USB","Handheld dynamic, cardioid USB/XLR",11.5,57.7,"USD 99.00",PAP,EDM),("Blue Yeti","Desktop USB condenser (omni mode)",11.7,61.3,"USD 139.99",MAN,"https://www.logitechg.com/en-us/shop/p/yeti-premium-usb-microphone"),("MXL AC-404","Boundary USB, 3-capsule, 180 degrees",12.0,60.2,"USD 99.95",PAP,EDM)]:
    n="Type is general knowledge; paper says only that it used an AUX port" if m.startswith("Sara") else ("Discontinued" if "ATR21" in m else "")
    a("bradford-2022",m,t,"script reading, 5 ft",w,p,b,u,n); a("bradford-2022",m,t,"group task, overlapping speech, 5 ft",g)
for m,t,w in [("Blue Yeti","Desktop USB condenser",17.6),("MacBook Pro 2017","Laptop, built-in",17.6),("Samsung Galaxy S7","Phone, built-in",17.7),("Sony ICD-UX533","Portable voice recorder",17.9),("Aputure A.lav","Lavalier / clip-on",17.9)]:
    y=m=="Blue Yeti"
    a("tran-2026",m,t,"two-person conversation, quiet",w,"USD 139.99" if y else "",MAN if y else "","https://www.logitechg.com/en-us/shop/p/yeti-premium-usb-microphone" if y else "")
for m,t,c,w in [("Table condensers","Desktop condenser","12-15 cm",48.37),("Lavaliers","Lavalier / clip-on","12-15 cm",51.95),("JBL speaker device","Tabletop speaker mic","2 m",59.90),("Bluetooth speakerphone (3 m)","Speakerphone, Bluetooth","3 m",117.03),("Bluetooth speakerphone (10 m)","Speakerphone, Bluetooth","10 m",125.52)]:
    a("tipaksorn-2025",m,t,c,w)
for m,t,c,w,p in [("OnePlus Nord 3 5G","Phone, built-in","quiet",4.13,""),("UGreen CM564","Gooseneck USB","30 cm",4.44,18),("Audio-Technica ATR4697","Boundary","80 cm",4.76,45),("EMEET conference speakerphone","Speakerphone","quiet",5.08,40),("Samson Q2U","Handheld dynamic, cardioid USB/XLR","30 cm",5.40,70),("OnePlus Nord 3 5G","Phone, built-in","Voicenotes MP3",5.40,""),("Audio-Technica ATR4697","Boundary","30 cm",5.40,45),("Jabra Speak 510","Speakerphone","quiet",5.40,110),("Logitech C925e","Webcam, built-in","30 cm",5.40,75),("Maono Elf","Lavalier / clip-on","quiet",5.40,25),("Logitech H390","Headset, wired USB boom","quiet",5.71,30),("OnePlus Nord 3 5G","Phone, built-in","ASR HQ recording",5.71,""),("Yealink BH72","Headset, wireless","vendor dongle",6.03,160),("Yealink BH72","Headset, wireless","generic Bluetooth adapter",6.03,160),("OnePlus Nord 3 5G","Phone, built-in","noisy market",6.03,""),("Sony ICD-UX570","Portable voice recorder","MP3",6.03,100),("Audio-Technica ATR4750-USB","Gooseneck USB, omni","quiet",6.35,55)]:
    a("rosehill-2025",m,t,c,w,f"~USD {p}" if p else "",OAP if p else "",OWN if p else "")
with (R/"data/results.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,rows[0].keys(),lineterminator="\n"); w.writeheader(); w.writerows(rows)
(R/"data/studies.json").write_text(json.dumps(studies,indent=2,ensure_ascii=False)+"\n")
def table(k, cond=None):
    o=["| Microphone | Type | Condition | WER | List price |","|---|---|---|---|---|"]
    for r in rows:
        if r["study"]!=k: continue
        p=f"[{r['price']}]({r['price_source']}) ({r['price_basis']})" if r["price"] else "n/a"
        o.append(f"| {r['microphone']} | {r['type']} | {r['condition']} | {r['wer_pct']:.2f}% | {p} |")
    return "\n".join(o)
out=["""# Microphone WER Studies

Which microphone gives the lowest word error rate (WER) in speech recognition? This is a credited compilation of studies that measured WER by microphone, with microphone type and list price.

**Short answer:** none of the studies here identifies one lowest-WER microphone for every situation. In quiet, decent microphones mostly cluster together. Distance, noise, airflow and the choice of speech engine often matter more.

> **Compare within a table, not between tables.** Texts, engines, rooms, distances and statistics differ by study. This is not an exhaustive literature review.

## Observations

- **Alander 2025:** eight of eleven mics averaged 3.96-4.65%. With the strongest fan, results ran from 4.87% to 99.17%.
- **Bradford 2022:** script reading spanned 10.7-12.0%, within one SD. The authors found no clear relationship between price and ASR performance.
- **Tran 2026:** on Azure Whisper, five devices spanned 17.6-17.9%. Engine medians spanned 16.7-20.7%.
- **LOTUSDIS 2025:** untuned Whisper got much worse on the distant devices.

## Results
"""]
for k,s in studies.items():
    out.append(f"### {s['authors'].split(',')[0].replace(' et al.','')} ({s['year']}): {s['title']}\n\n{s['authors']}. *{s['venue']}*. [Source]({s['url']})\n\n- **Engine:** {s['engine']}\n- **Statistic:** {s['statistic']}\n- **Setup:** {s['setup']}\n- **Limits:** {s['limits']}\n\n{table(k)}\n")
out.append(f"""## Related work (abstract or excerpt read only; not in the dataset)

- Brady et al. (2014), [microphones and placement for classroom ASR](https://pubs.aip.org/jasa/article/136/4_Supplement/2215/708554/Evaluating-microphones-and-microphone-placement): preliminary results favoured the Crown PZM-30 boundary mic.
- [Microphone Array Processing for Distant Speech Recognition](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Microphone20Array20Processing20for20Distant20Speech20Recognition20-20Towards20Real-World20Deployment.pdf): one channel of a 64-channel array 14.3%, full system 5.3%, lapel 4.2%.
- [Idiap RR 05-47 (2005)](https://publications.idiap.ch/attachments/reports/2005/rr-05-47.pdf): unadapted headset 42.5%, array 64.2%, lapel 67.0%.
- [Alapetite (2006)](https://alexandre.alapetite.fr/phd-risoe/publications/Alapetite-2006-IJMI.pdf): headset 83.2% recognition vs 73.9% for a Philips SpeechMike; reports recognition rate, not WER.

## Prices

Checked {TODAY}. `price_basis` says what each figure is: `manufacturer list`, `reseller-stated list`, `price in study`, or `author's approximate price`. Only the first is a confirmed manufacturer price. Sale prices are excluded. `n/a` means no list price was found or none applies; repeat conditions are left blank.

## Data

- [`data/results.csv`](data/results.csv): one row per study, microphone and condition.
- [`data/studies.json`](data/studies.json): citations, methods and limits.
- [`scripts/build.py`](scripts/build.py): edit this, then run `uv run scripts/build.py` to regenerate both files and this README.

Corrections and more studies are welcome by issue or pull request. Please include a source that reports WER by microphone.

## Credit and licence

The measurements belong to the cited authors; please cite them. This compilation is [CC BY 4.0](LICENSE), which does not relicense the underlying works. Compiled by Daniel Rosehill with Claude. The last table is the compiler's own benchmark.
""")
(R/"README.md").write_text("\n".join(out))
