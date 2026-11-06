import os
import subprocess
import shutil
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"C:\Users\ketro\Downloads\clone\audiobook"

# 1. Collect all mp3 files
mp3_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.lower().endswith(".mp3"):
            mp3_files.append(os.path.join(root, f))

print(f"Total audio tracks found in library: {len(mp3_files)}", flush=True)

temp_dir = tempfile.gettempdir()

def process_track(item):
    idx, file_path = item
    # Generate unique temp file
    pid = os.getpid()
    t_id = int(time.time() * 1000) % 1000000
    tmp_out = os.path.join(temp_dir, f"upg44k_{idx}_{pid}_{t_id}.mp3")

    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-i", file_path,
        "-ar", "44100",
        "-b:a", "128k",
        "-c:a", "libmp3lame",
        "-id3v2_version", "3",
        tmp_out
    ]
    try:
        subprocess.run(cmd, check=True)
        if os.path.exists(tmp_out) and os.path.getsize(tmp_out) > 1000:
            # Overwrite original
            shutil.move(tmp_out, file_path)
            return True, file_path
        else:
            return False, file_path
    except Exception as e:
        if os.path.exists(tmp_out):
            try:
                os.remove(tmp_out)
            except Exception:
                pass
        return False, f"{file_path} (Error: {e})"

start_time = time.time()
print(f"Beginning 44.1 kHz upgrade across 8 worker threads...", flush=True)

success_count = 0
failed_count = 0
total = len(mp3_files)

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(process_track, (i, f)) for i, f in enumerate(mp3_files)]
    for fut in as_completed(futures):
        success, path = fut.result()
        if success:
            success_count += 1
        else:
            failed_count += 1
            print(f"Failed: {path}", flush=True)

        if (success_count + failed_count) % 50 == 0 or (success_count + failed_count) == total:
            elapsed = time.time() - start_time
            rate = (success_count + failed_count) / max(elapsed, 0.001)
            print(f"Progress: [{success_count + failed_count}/{total}] completed ({success_count} success, {failed_count} fail) - {rate:.1f} tracks/sec", flush=True)

total_elapsed = time.time() - start_time
print(f"\nUPGRADE COMPLETE in {total_elapsed:.1f} seconds!", flush=True)
print(f"Total Success: {success_count} / {total}", flush=True)
print(f"Total Failed: {failed_count} / {total}", flush=True)
