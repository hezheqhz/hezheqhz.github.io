# -*- coding: utf-8 -*-
"""Generate HugoBlox publication pages for Zhe He's homepage from CV data."""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBS = os.path.join(ROOT, "content", "publications")

# ---------------- demo content cleanup ----------------
for demo in ["conference-paper", "journal-article", "preprint"]:
    p = os.path.join(PUBS, demo)
    if os.path.isdir(p):
        shutil.rmtree(p)
        print("removed demo:", demo)
for section in ["blog", "courses", "events", "slides"]:
    p = os.path.join(ROOT, "content", section)
    if os.path.isdir(p):
        shutil.rmtree(p)
        print("removed demo section:", section)
for proj in ["pandas", "pytorch", "scikit"]:
    p = os.path.join(ROOT, "content", "projects", proj)
    if os.path.isdir(p):
        shutil.rmtree(p)
        print("removed demo project:", proj)

ME = "me"
COVER = {"name": "Cover Article", "level": "featured"}

# fields: slug, title, authors, date, ptype, journal, volume, issue, pages,
#         doi, featured, cover, tags, note(corresponding)
JOURNALS = [
    # ---- 2026 ----
    dict(slug="tong-2026-sciadv", title="Above-twofold quantum super-resolution microscopy enabled by multiple idler passes with entangled biphotons",
         authors=["Xin Tong", ME, "Yi Zhang", "Wentao Liu", "Chao Huang", "Lihong V. Wang"],
         date="2026-07-01", journal="Science Advances", volume="12", issue="30",
         doi="10.1126/sciadv.aea9457", featured=True, tags=["Quantum Imaging"]),
    dict(slug="wang-2026-pnas", title="Single-shot wide-field biochemical imaging at 1 kHz frame rate",
         authors=["Jian Wang", "Nicholas Marshall", "Zhongjiang Han", "Kai Wang", "Randy Sprague", "Zhenhuan Yi", ME, "Alexei V. Sokolov"],
         date="2026-06-01", journal="Proceedings of the National Academy of Sciences", volume="123", issue="27", pages="e2603591123", tags=["Coherent Raman", "Imaging"]),
    dict(slug="li-2026-photonics-research", title="Cryogenic thermometry via nanofilm thermal-strain optomechanics",
         authors=["Guangming Li", "Hao Wu", "Wen Zheng", "Qiuling Cao", ME, "Zhaoyu Cui"],
         date="2026-08-01", journal="Photonics Research", volume="14", issue="8", pages="3318-3325",
         featured=True, cover=True, note="Corresponding author", tags=["Low-Temperature Measurement", "Optomechanics"]),
    dict(slug="li-2026-ichmt", title="Dynamic response and relaxation of vortex line density in superfluid helium under nonlinear oscillating thermal counterflow",
         authors=["Zhiqiang Li", "Wei Shao", ME, "Qiuling Cao", "Zhaoyu Cui", "Liang Cheng"],
         date="2026-05-01", journal="International Communications in Heat and Mass Transfer", volume="175", pages="111107", tags=["Superfluid Helium"]),
    dict(slug="li-2026-prb", title="Suppression of orientation dependent heat transport across Al/α-Al2O3 interfaces by interfacial atomic disorder",
         authors=["Haoyue Li", "Yuan Liu", "Tianli Wang", "Yue Chen", "Jun Lou", ME, "Wen Zheng"],
         date="2026-04-01", journal="Physical Review B", volume="113", issue="16", pages="165304", tags=["Heat Transport"]),
    # ---- 2025 ----
    dict(slug="he-2025-acs-photonics", title="Quantum-resolution imaging with multicenter integration",
         authors=[ME, "Hao Wu", "Guangming Li", "Chenglong Shao", "Wen Zheng", "Qiuling Cao", "Zhaoyu Cui"],
         date="2025-11-01", journal="ACS Photonics", volume="12", issue="11", pages="6530-6534",
         featured=True, cover=True, note="Corresponding author", tags=["Quantum Imaging"]),
    dict(slug="wang-2025-apl", title="Tip-enhanced Raman spectroscopy of cell wall heterogeneity for Aspergillus fumigatus",
         authors=["Jian Wang", "Zhihao Jiang", ME, "Peng Zhang", "Zhenhuan Yi", "Alexei V. Sokolov", "Marlan O. Scully"],
         date="2025-09-01", journal="Applied Physics Letters", volume="127", issue="11", note="Corresponding author", tags=["TERS"]),
    dict(slug="yue-2025-nanophotonics", title="Quantum super-resolution imaging: a review and perspective",
         authors=["Xin Yue", "Hao Wu", "Jian Wang", ME],
         date="2025-04-01", journal="Nanophotonics", volume="14", issue="11", pages="1961-1974",
         featured=True, cover=True, note="Corresponding author", tags=["Quantum Imaging", "Review"]),
    dict(slug="wu-2025-apl", title="Optomechanical thermal effect of nanofilm by time-correlated single-photon counting",
         authors=["Hao Wu", "Guangming Li", ME],
         date="2025-05-01", journal="Applied Physics Letters", volume="126", issue="20", note="Corresponding author", tags=["Optomechanics"]),
    # ---- 2024 ----
    dict(slug="kahraman-2024-njp", title="Quantum mechanical modeling of the multi-stage Stern–Gerlach experiment conducted by Frisch and Segrè",
         authors=["S. Selim Kahraman", "Katherine Titimbo", ME, "Jung-Tsung Shen", "Lihong V. Wang"],
         date="2024-07-01", journal="New Journal of Physics", volume="26", issue="7", pages="073005", tags=["Quantum Dynamics"]),
    dict(slug="he-2024-jap", title="Imaging spatial plasmon mode of nanocavity formed by Au tip and Au nanorod lattice in tip-enhanced Raman spectroscopy",
         authors=[ME, "Jian Wang", "Rui Wang", "Dmitry Kurouski"],
         date="2024-05-01", journal="Journal of Applied Physics", volume="135", issue="19", tags=["TERS", "Plasmonics"]),
    dict(slug="zhang-2024-sciadv", title="Quantum imaging of biological organisms through spatial and polarization entanglement",
         authors=["Yi Zhang", ME, "Xin Tong", "David C. Garrett", "Rui Cao", "Lihong V. Wang"],
         date="2024-03-01", journal="Science Advances", volume="10", issue="10", pages="eadk1495",
         doi="10.1126/sciadv.adk1495", featured=True, tags=["Quantum Imaging"]),
    # ---- 2023 ----
    dict(slug="titimbo-2023-jpb-bloch", title="Numerical modeling of the multi-stage Stern–Gerlach experiment by Frisch and Segrè using co-quantum dynamics via the Bloch equation",
         authors=["Katherine Titimbo", "David C. Garrett", "S. Selim Kahraman", ME, "Lihong V. Wang"],
         date="2023-10-01", journal="Journal of Physics B: Atomic, Molecular and Optical Physics", volume="56", issue="20", pages="205004", tags=["Quantum Dynamics"]),
    dict(slug="he-2023-jpb-schrodinger", title="Numerical modeling of the multi-stage Stern–Gerlach experiment by Frisch and Segrè using co-quantum dynamics via the Schrödinger equation",
         authors=[ME, "Katherine Titimbo", "David C. Garrett", "S. Selim Kahraman", "Lihong V. Wang"],
         date="2023-10-02", journal="Journal of Physics B: Atomic, Molecular and Optical Physics", volume="56", issue="20", pages="205005", tags=["Quantum Dynamics"]),
    dict(slug="wang-2023-nanophotonics", title="Tip-enhanced photoluminescence of monolayer MoS2 increased and spectrally shifted by injection of electrons",
         authors=["Jian Wang", "Zhongjiang Han", ME, "Kai Wang", "Xiaoyan Liu", "Alexei V. Sokolov"],
         date="2023-07-01", journal="Nanophotonics", volume="12", issue="14", pages="2937-2943", note="Corresponding author", tags=["TERS", "2D Materials"]),
    dict(slug="he-2023-natcommun", title="Quantum microscopy of cells at the Heisenberg limit",
         authors=[ME, "Yi Zhang", "Xin Tong", "Lei Li", "Lihong V. Wang"],
         date="2023-04-01", journal="Nature Communications", volume="14", pages="2441",
         featured=True, tags=["Quantum Imaging"]),
    dict(slug="tong-2023-prapplied", title="Experimental full-domain mapping of quantum correlation in Clauser-Horne-Shimony-Holt scenarios",
         authors=["Xin Tong", ME, "Yi Zhang", "Sasha Solomon", "Liang Lin", "Qingqing Song", "Lihong V. Wang"],
         date="2023-03-01", journal="Physical Review Applied", volume="19", issue="3", pages="034049", tags=["Quantum Correlation"]),
    dict(slug="wang-2023-nanoresearch", title="Near-field and photocatalytic properties of mono- and bimetallic nanostructures monitored by nanocavity surface-enhanced Raman scattering",
         authors=["Rui Wang", ME, "Dmitry Kurouski"],
         date="2023-01-01", journal="Nano Research", volume="16", issue="1", pages="1545-1551", tags=["SERS", "Plasmonics"]),
    # ---- 2021 ----
    dict(slug="wang-2021-acs-photonics", title="Femtosecond time-resolved infrared-resonant third-order sum-frequency spectroscopy",
         authors=["Jian Wang", "Kai Wang", "Yong Shen", "Zhongjiang Han", "Feng Li", ME, "Marlan O. Scully"],
         date="2021-04-01", journal="ACS Photonics", volume="8", issue="4", pages="1137-1142", cover=True, tags=["Ultrafast Spectroscopy"]),
    # ---- 2020 ----
    dict(slug="he-2020-acs-photonics-rna", title="Resolving the sequence of RNA strands by tip-enhanced Raman spectroscopy",
         authors=[ME, "Wenjing Qiu", "Megan E. Kizer", "Jian Wang", "Weihong Chen", "Alexei V. Sokolov", "Marlan O. Scully"],
         date="2020-12-01", journal="ACS Photonics", volume="8", issue="2", pages="424-430",
         featured=True, cover=True, tags=["TERS", "Sequencing"]),
    dict(slug="wang-2020-jpcl", title="Gap-mode tip-enhanced Raman scattering on Au nanoplates of varied thickness",
         authors=["Rui Wang", ME, "Alexei V. Sokolov", "Dmitry Kurouski"],
         date="2020-05-01", journal="The Journal of Physical Chemistry Letters", volume="11", issue="10", pages="3815-3820", tags=["TERS", "Plasmonics"]),
    # ---- 2019 ----
    dict(slug="he-2019-sciadv", title="Quantum plasmonic control of trions in a picocavity with monolayer WS2",
         authors=[ME, "Zhongjiang Han", "Jianwei Yuan", "Alexander M. Sinyukov", "Hedi Eleuch", "Chong Niu", "Marlan O. Scully"],
         date="2019-10-01", journal="Science Advances", volume="5", issue="10", pages="eaau8763",
         doi="10.1126/sciadv.aau8763", featured=True, tags=["Plasmonics", "2D Materials"]),
    # ---- 2018 ----
    dict(slug="he-2018-jacs", title="Tip-enhanced Raman imaging of single-stranded DNA with single base resolution",
         authors=[ME, "Zhongjiang Han", "Megan Kizer", "Robert J. Linhardt", "Xing Wang", "Alexander M. Sinyukov", "Marlan O. Scully"],
         date="2018-12-01", journal="Journal of the American Chemical Society", volume="141", issue="2", pages="753-757",
         doi="10.1021/jacs.8b11030", featured=True, tags=["TERS", "Sequencing"]),
    dict(slug="shutov-2018-acs-photonics", title="Giant chemical surface enhancement of coherent Raman scattering on MoS2",
         authors=["Anton D. Shutov", "Zhenhuan Yi", "Jian Wang", "Alexander M. Sinyukov", ME, "Chao Tang", "Marlan O. Scully"],
         date="2018-12-02", journal="ACS Photonics", volume="5", issue="12", pages="4960-4968", tags=["Coherent Raman"]),
    dict(slug="tang-2018-prb", title="Quantum plasmonic hot-electron injection in lateral WSe2/MoSe2 heterostructures",
         authors=["Chao Tang", ME, "Weibing Chen", "Shunfeng Jia", "Jun Lou", "Dmitri V. Voronine"],
         date="2018-07-01", journal="Physical Review B", volume="98", issue="4", pages="041402", tags=["Plasmonics", "2D Materials"]),
    # ---- 2016 ----
    dict(slug="he-2016-jstqe", title="Tip-enhanced Raman scattering on bulk MoS2 substrate",
         authors=[ME, "Dmitri V. Voronine", "Alexander M. Sinyukov", "Zachary N. Liege", "Brett Birmingham", "Alexei V. Sokolov", "Marlan O. Scully"],
         date="2016-03-01", journal="IEEE Journal of Selected Topics in Quantum Electronics", volume="23", issue="2", pages="113-118", tags=["TERS"]),
    # ---- 2015 ----
    dict(slug="cai-2015-jcg", title="Enhanced synthesis of Sn nanowires with aid of Se atom via physical vapor transport",
         authors=["Hua Cai", "Wei Wang", "Peng Liu", "Gang Wang", "An Liu", ME, "Maohui Xia"],
         date="2015-08-01", journal="Journal of Crystal Growth", volume="420", pages="42-46", tags=["Nanomaterials"]),
]

THESIS = [
    dict(slug="he-2020-phd-thesis", title="Advances in Tip-Enhanced Raman and Photoluminescence Spectroscopy",
         authors=[ME], date="2020-05-01", journal="PhD dissertation, Texas A&M University", tags=["TERS"]),
]

CONFERENCES = [
    dict(slug="tong-2024-spie", title="Super-resolution quantum microscopy at the Heisenberg limit",
         authors=["Xin Tong", ME, "Yi Zhang", "Lei Li", "Lihong V. Wang"],
         date="2024-03-01", journal="Quantum Sensing, Imaging, and Precision Metrology II, SPIE", pages="PC1291226", tags=["Quantum Imaging"]),
    dict(slug="titimbo-2024-spie", title="Numerical modeling of the multi-stage Stern–Gerlach experiment by Frisch and Segrè using co-quantum dynamics via the Bloch equation",
         authors=["Katherine Titimbo", "David C. Garrett", "S. Selim Kahraman", ME, "Lihong V. Wang"],
         date="2024-03-02", journal="Quantum Sensing, Imaging, and Precision Metrology II, SPIE", pages="PC129122F", tags=["Quantum Dynamics"]),
    dict(slug="hu-2022-spie", title="Resolving the sequence of DNA and RNA strands by tip-enhanced Raman spectroscopy",
         authors=["Jiajun Hu", ME, "Alexei V. Sokolov", "Xing Wang", "Marlan O. Scully"],
         date="2022-03-01", journal="Smart Photonic and Optoelectronic Integrated Circuits 2022, SPIE", pages="PC1200503", tags=["TERS", "Sequencing"]),
    dict(slug="he-2021-cleo", title="Gap mode tip-enhanced Raman and AFM imaging of RNA strands",
         authors=[ME, "Wenjing Qiu", "Megan E. Kizer", "Jian Wang", "Alexei V. Sokolov", "Xing Wang", "Marlan O. Scully"],
         date="2021-05-01", journal="CLEO: Applications and Technology, Optica", pages="AM1R-3", tags=["TERS"]),
    dict(slug="wang-2021-cleo", title="Femtosecond time-resolved infrared-resonant third-order sum-frequency spectroscopy towards label-free imaging",
         authors=["Jian Wang", "Kai Wang", "Yong Shen", "Zhongjiang Han", "Feng Li", ME, "Marlan O. Scully"],
         date="2021-05-02", journal="CLEO: QELS Fundamental Science, Optica", pages="JTh3A-71", tags=["Ultrafast Spectroscopy"]),
    dict(slug="shutov-2018-aps", title="Chemical surface-enhanced coherent Raman scattering by semiconductor nanoparticles",
         authors=["Anton D. Shutov", "Zhenhuan Yi", "Jian Wang", "Alexander M. Sinyukov", ME, "Chao Tang", "Marlan O. Scully"],
         date="2018-03-01", journal="Bulletin of the American Physical Society", volume="63", tags=["Coherent Raman"]),
    dict(slug="shutov-2018-ls", title="Coherent anti-Stokes Raman scattering enhanced by MoS2 nanoparticles",
         authors=["Anton D. Shutov", "Zhenhuan Yi", "Jian Wang", "Alexander M. Sinyukov", ME, "Chao Tang", "Marlan O. Scully"],
         date="2018-09-01", journal="Laser Science, Optica", pages="JW3A-40", tags=["Coherent Raman"]),
    dict(slug="tang-2017-aps", title="Nano-optical imaging of 2D materials",
         authors=["Chao Tang", ME, "Dmitri V. Voronine"],
         date="2017-03-01", journal="Bulletin of the American Physical Society", volume="62", tags=["TERS", "2D Materials"]),
    dict(slug="he-2015-aps", title="Chemical mapping of CuPc on MoS2 using tip-enhanced Raman scattering",
         authors=[ME, "Dmitri V. Voronine", "Alexander M. Sinyukov", "Zachary N. Liege", "Brett Birmingham", "Kevin Moore", "Marlan O. Scully"],
         date="2015-03-01", journal="Bulletin of the American Physical Society", volume="60", tags=["TERS"]),
]

def yaml_str(s):
    return '"' + s.replace('"', '\\"') + '"'

def render(p, ptype):
    lines = ["---"]
    lines.append("title: " + yaml_str(p["title"]))
    lines.append("authors:")
    for a in p["authors"]:
        lines.append("- " + a)
    if p.get("note"):
        notes = []
        for a in p["authors"]:
            notes.append(yaml_str(p["note"]) if a == ME and "Corresponding" in p["note"] else '""')
        # corresponding marker: attach note to Zhe He
        lines.append("author_notes:")
        for a in p["authors"]:
            if a == ME:
                lines.append("- " + yaml_str(p["note"]))
            else:
                lines.append('- ""')
    lines.append('date: "%sT00:00:00Z"' % p["date"])
    lines.append("publication_types: [%s]" % yaml_str(ptype))
    lines.append("publication:")
    lines.append("  name: " + yaml_str(p["journal"]))
    if p.get("volume"):
        lines.append("  volume: %s" % p["volume"])
    if p.get("issue"):
        lines.append("  issue: %s" % p["issue"])
    if p.get("pages"):
        lines.append("  pages: " + yaml_str(str(p["pages"])))
    lines.append("peer_reviewed: true")
    if p.get("cover"):
        lines.append("awards:")
        lines.append('  - name: "Cover Article"')
        lines.append('    level: featured')
    if p.get("doi"):
        lines.append("doi: " + yaml_str(p["doi"]))
        lines.append("links:")
        lines.append("  - type: publisher")
        lines.append("    url: https://doi.org/" + p["doi"])
    lines.append("tags:")
    for t in p.get("tags", []):
        lines.append("- " + t)
    lines.append("featured: %s" % ("true" if p.get("featured") else "false"))
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

count = 0
for p in JOURNALS:
    d = os.path.join(PUBS, p["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
        f.write(render(p, "article-journal"))
    count += 1
for p in THESIS:
    d = os.path.join(PUBS, p["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
        f.write(render(p, "thesis"))
    count += 1
for p in CONFERENCES:
    d = os.path.join(PUBS, p["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
        f.write(render(p, "paper-conference"))
    count += 1

print("generated %d publication pages" % count)
