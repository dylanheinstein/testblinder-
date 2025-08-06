#!/usr/bin/env python3
import os
import re
import random
import string
import shutil
import zipfile
import csv

def random_code():
    """Generate a random 3-letter uppercase code."""
    return "".join(random.choices(string.ascii_uppercase, k=3))

def blind_copy_and_zip_unblinded(directory="."):
    """
    1. Scans for all .czi files in `directory`.
    2. For each file, extracts the leading ID (e.g. B1, C2) and strips out any 'cKO'/'CTRL'.
    3. Assigns a consistent random 3-letter code per letter group.
    4. Copies the original file to a new blinded filename (leaving the original intact).
    5. Writes blinding_key.csv.
    6. Zips **only the original** .czi files into unblinded_files.zip.
    """
    files = [f for f in os.listdir(directory) if f.lower().endswith(".czi")]
    prefix_map = {}
    mapping = {}

    for fname in files:
        # --- determine blinded name (identical to before) ---
        parts = fname.split("_", 1)
        identifier = parts[0]
        rest = parts[1] if len(parts) > 1 else ""
        subparts = rest.split("_", 1)
        after_label = subparts[1] if subparts[0] in ("cKO", "CTRL") and len(subparts) > 1 else rest
        tail = "_" + after_label if after_label else ""
        m = re.match(r"^([A-Za-z]+)(\d+)$", identifier)
        if m:
            letters, number = m.groups()
        else:
            letters = "".join(filter(str.isalpha, identifier))
            number  = "".join(filter(str.isdigit, identifier))
        if letters not in prefix_map:
            prefix_map[letters] = random_code()
        new_prefix = prefix_map[letters] + number
        blind_name = new_prefix + tail + ".czi"

        # copy original → blinded
        shutil.copy2(os.path.join(directory, fname),
                     os.path.join(directory, blind_name))
        mapping[fname] = blind_name

    # write CSV key
    key_path = os.path.join(directory, "blinding_key.csv")
    with open(key_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Original Filename", "Blinded Filename"])
        for orig, blind in mapping.items():
            writer.writerow([orig, blind])
    print(f"Blinding key written to: {key_path}")

    # zip only the **original** .czi files
    zip_path = os.path.join(directory, "unblinded_files.zip")
    with zipfile.ZipFile(zip_path, "w") as zf:
        for orig in files:
            zf.write(os.path.join(directory, orig), orig)
    print(f"Original (unblinded) files zipped to: {zip_path}")

if __name__ == "__main__":
    blind_copy_and_zip_unblinded(".")
