import os
import json

audiobook_root = r"C:\Users\ketro\Downloads\clone\audiobook"
pub_root = r"C:\Users\ketro\Downloads\Publication_Packages"

catalog = [
    {
        "id": "the_dead_and_the_siege",
        "title": "The Dead and the Siege",
        "subtitle": "Behind the Redoubt",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Horror / Post-Apocalyptic / Military",
        "blurb": "From the initial terminal outbreak at JFK Airport to flooded Midtown Manhattan vaults, a convoy of survivors fights down the Atlantic seaboard to make a final stand behind the 16 million bricks of Fort Jefferson.",
        "folder": os.path.join(audiobook_root, "The Dead and the Siege"),
        "cover": os.path.join(audiobook_root, "The Dead and the Siege", "cover_spotify_3000x3000.jpg"),
    },
    {
        "id": "the_dead_and_the_dustbowl",
        "title": "The Dead and the Dustbowl",
        "subtitle": "The Complete Chronicles",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Horror / Post-Apocalyptic / Western",
        "blurb": "Across the scorched, choking expanse of the High Plains, drought and reanimation scour the remnants of human civilization. A gritty saga of mechanical grit, steel iron doors, and the unyielding will to survive.",
        "folder": os.path.join(audiobook_root, "The Dead and the Dustbowl"),
        "cover": os.path.join(audiobook_root, "The Dead and the Dustbowl", "cover_spotify_3000x3000.jpg"),
    },
    {
        "id": "the_dead_and_the_signal",
        "title": "The Dead and the Signal",
        "subtitle": "The Audio Transmission Archives",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Science Fiction / Apocalyptic",
        "blurb": "When regional broadcast relays collapse under electromagnetic pulses and swarming hosts, radio operators, radar engineers, and naval detachments trace phantom radio carrier frequencies across dead frequencies.",
        "folder": os.path.join(audiobook_root, "The Dead and the Signal"),
        "cover": os.path.join(audiobook_root, "The Dead and the Signal", "cover_spotify_3000x3000.jpg"),
    },
    {
        "id": "no_treaty_with_the_dead",
        "title": "No Treaty With The Dead",
        "subtitle": "The Borderland Engagements",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Military / Post-Apocalyptic",
        "blurb": "There are no terms. There are no truces. In the militarized corridors and frontier outposts, surviving garrisons hold perimeter redoubts with iron discipline against unrelenting tides.",
        "folder": os.path.join(audiobook_root, "No Treaty With The Dead"),
        "cover": os.path.join(audiobook_root, "No Treaty With The Dead", "cover_spotify_3000x3000.jpg"),
    },
    {
        "id": "the_dead_and_the_frost",
        "title": "The Dead and the Frost",
        "subtitle": "Winter at the Perimeter",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Horror / Survival",
        "blurb": "Sub-zero temperatures freeze flesh and engine blocks alike. In the deep snowdrifts of the North, cold is both the greatest enemy and the only barrier slowing down the dead.",
        "folder": os.path.join(audiobook_root, "The Dead and the Frost"),
        "cover": os.path.join(audiobook_root, "The Dead and the Frost", "cover_spotify_3000x3000.jpg"),
    },
    {
        "id": "static_and_sinew",
        "title": "Static and Sinew",
        "subtitle": "A Post-Collapse Odyssey",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Horror / Dystopian",
        "blurb": "Where biology meets electrical decay. A relentless narrative following survivors patching torn relay networks and defending precarious generator stations against relentless host swarms.",
        "folder": os.path.join(audiobook_root, "Static and Sinew"),
        "cover": os.path.join(audiobook_root, "Static and Sinew", "cover_spotify_3000x3000.jpg"),
    }
]

# Add Unspoken 1-7
unspoken_dir = os.path.join(audiobook_root, "The_Unspoken_Series")
for i in range(1, 8):
    roman = ["I", "II", "III", "IV", "V", "VI", "VII"][i-1]
    name = f"Book_{i:02d}_Unspoken" if i == 1 else f"Book_{i:02d}_Unspoken_{roman}"
    bpath = os.path.join(unspoken_dir, name)
    catalog.append({
        "id": f"unspoken_book_{i}",
        "title": f"Unspoken: Book {roman}",
        "subtitle": f"The Unspoken Chronicles - Volume {roman}",
        "author": "Gabriel Simon",
        "narrator": "Gabriel Simon",
        "genre": "Fiction / Psychological / Dark Suspense",
        "blurb": f"Volume {roman} of the critically acclaimed Unspoken series by Gabriel Simon. An intense, atmospheric exploration of survival, isolation, and inner reckoning.",
        "folder": bpath,
        "cover": os.path.join(bpath, "cover_spotify_3000x3000.jpg")
    })

# Verify file counts
manifest_path = os.path.join(audiobook_root, "MASTER_DISTRIBUTION_MANIFEST.json")
for item in catalog:
    fpath = item["folder"]
    if os.path.exists(fpath):
        tracks = [f for f in os.listdir(fpath) if f.endswith(".mp3")]
        item["track_count"] = len(tracks)
        item["has_cover"] = os.path.exists(item["cover"])
    else:
        item["track_count"] = 0
        item["has_cover"] = False

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2)

print("Saved Master Distribution Manifest to:", manifest_path)
for item in catalog:
    print(f"- {item['title']}: {item['track_count']} tracks | Cover: {item['has_cover']}")
