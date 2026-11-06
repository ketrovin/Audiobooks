# 🎧 Gabriel Simon Audiobooks & Master Publications
### Official Audio Ingestion & Digital Distribution Repository

This repository contains the publication packages, distribution manifests, metadata profiles, and production tooling for **Gabriel Simon's** catalog of post-apocalyptic, military, and dark speculative fiction.

---

## 📋 Audio Engineering & Ingestion Standards

All audio tracks across all volumes in this catalog strictly conform to the unified industry ingestion standard for **Findaway Voices / Spotify for Authors**, **ACX (Audible / Amazon / iTunes)**, and **Draft2Digital**:

* **Sample Rate**: `44,100 Hz (44.1 kHz)` (Converted and verified across all masters)
* **Bitrate & Channel Mode**: `128 kbps Constant Bitrate (CBR) MP3`, Mono
* **Metadata Tags (ID3v2)**:
  * `Title`: Sequential chapter name (e.g. `CHAPTER 1: THE DEPARTURE GATE`)
  * `Artist`: `Gabriel Simon`
  * `Album`: Official Volume Title
  * `Genre`: `Audiobook`
* **Cover Master**: `3000 × 3000 px` square, 24-bit RGB JPEG, min 300 DPI, no borders

---

## 📚 Master Catalog Volumes

| Volume | Format | Chapter Count | Status |
| :--- | :--- | :---: | :---: |
| **The Dead and the Siege** | Novel (32 Ch) + Audio + Print | 32 Tracks | 100% Mastered |
| **The Dead and the Dustbowl** | Full Novel Collection | 300 Tracks | 100% Mastered |
| **The Dead and the Signal** | Complete Novel Archive | 300 Tracks | 100% Mastered |
| **No Treaty With The Dead** | Borderland Series Collection | 120 Tracks | 100% Mastered |
| **The Dead and the Frost** | Winter Perimeter Novel | 30 Tracks | 100% Mastered |
| **Static and Sinew** | Post-Collapse Odyssey | 31 Tracks | 100% Mastered |
| **The Unspoken Series (Books I – VII)** | 7-Volume Psychological Series | 74 Tracks | 100% Mastered |

**Total Production Volume**: **887 Audio Tracks** across **13 Unabridged Titles**.

---

## 📦 Directory Structure

```
Audiobooks/
├── README.md
├── MASTER_DISTRIBUTION_MANIFEST.json
├── packages/
│   ├── the_dead_and_the_siege/
│   │   ├── The_Dead_and_the_Siege.docx    <-- D2D eBook & Paperback Master
│   │   ├── The_Dead_and_the_Siege.epub    <-- Standalone ePub 3
│   │   ├── The_Dead_and_the_Siege_Cover.jpg (1600x2400)
│   │   ├── cover_spotify_3000x3000.jpg
│   │   ├── manuscript.md
│   │   └── metadata.json
├── tools/
│   ├── verify_audio_44k.py                <-- Automated 44.1 kHz compliance scanner
│   └── export_d2d_docx.py                 <-- Word Heading 1 formatter
```

---

## ⚖️ License & Intellectual Property
All manuscript texts, audio recordings, character designs, and cover artwork are Copyright © 2026 Gabriel Simon. All rights reserved.
