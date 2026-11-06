import os
import subprocess
import json

base = r"C:\Users\ketro\Downloads\clone\audiobook"

# Check sample files from each book
test_samples = [
    os.path.join(base, "The Dead and the Frost", "Track_01_The_Snowshoe_Trail.mp3"),
    os.path.join(base, "The Dead and the Dustbowl", "Chapter_001_Story_One__The_Black_Blizzard_Chapter_One__The_Wall_of_Dirt.mp3"),
    os.path.join(base, "The Dead and the Signal", "Chapter_001_Story_1__The_Traffic_Chopper_Chapter_1__Pre-Flight_Check.mp3"),
    os.path.join(base, "No Treaty With The Dead", "Chapter_001_Story_One__The_Ironworkers_Chapter_One__The_High_Steel.mp3"),
    os.path.join(base, "Static and Sinew", "Chapter_01_Chapter_1__The_Cosplay_of_the_Dead.mp3"),
    os.path.join(base, "The_Unspoken_Series", "Book_01_Unspoken", "Track_01_Scene_0__The_Forests_Breath.mp3"),
    os.path.join(base, "The_Unspoken_Series", "Book_07_Unspoken_VII", "Track_01_Scene_1__The_Frost_Settles.mp3")
]

results = []
for s in test_samples:
    if os.path.exists(s):
        cmd = ["ffprobe", "-v", "error", "-show_entries", "stream=sample_rate,bit_rate,channels:format_tags=title,artist,album", "-of", "json", s]
        res = subprocess.run(cmd, capture_output=True, text=True)
        try:
            d = json.loads(res.stdout)
            st = d["streams"][0]
            tg = d.get("format", {}).get("tags", {})
            results.append({
                "book": os.path.basename(os.path.dirname(s)),
                "track": os.path.basename(s),
                "sample_rate": st.get("sample_rate"),
                "bit_rate": st.get("bit_rate"),
                "artist": tg.get("artist"),
                "album": tg.get("album")
            })
        except Exception as e:
            results.append({"error": str(e), "file": s})

for r in results:
    print(f"VERIFIED: {r['album']} | SR: {r['sample_rate']} Hz | Bitrate: {int(r['bit_rate'])//1000}k | Artist: {r['artist']}")
