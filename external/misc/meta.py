import json
import os
import re

# Load the meta.json file
with open('meta.json', 'r') as f:
    meta_data = json.load(f)

# Extract current patch files from the 'patches/' directory
patch_files = [f for f in os.listdir('patches') if os.path.isfile(os.path.join('patches', f))]

# Define a regex pattern to extract SemVer from filenames (assuming the format contains semver)
semver_pattern = r'(\d+\.\d+\.\d+)(.*)'

# Function to extract the SemVer and the part after it from a patch file name
def extract_semver_and_suffix(filename):
    match = re.search(semver_pattern, filename)
    if match:
        semver = match.group(1)
        suffix = match.group(2).lstrip('-').replace('-', '_').replace('.patch','')  # Remove leading hyphen and replace hyphens with underscores
        return semver, suffix
    return None, None

# Extract SemVer and suffix for all patch files
patch_versions = {extract_semver_and_suffix(patch) for patch in patch_files if extract_semver_and_suffix(patch)[0]}

# Check if the SemVer exists in the meta.json data
def patch_exists_in_meta(semver):
    return any(item['name'] == semver for item in meta_data)

# Add new patches to meta.json if not already present
for semver, suffix in patch_versions:
    if semver and not patch_exists_in_meta(semver):
        # Find all patches with this version
        version_patches = [p for p in patch_files if semver in p]
        for patch in version_patches:
            new_patch_entry = {
                'name': semver,
                'path': f'patches/{patch}',
                'version': suffix  # Use the converted suffix
            }
            meta_data.append(new_patch_entry)
            print(f"Added new patch version {semver}: {patch}")

# Write updated meta.json back to disk
with open('meta.json', 'w') as f:
    json.dump(meta_data, f, indent=2)

print("meta.json has been updated.")