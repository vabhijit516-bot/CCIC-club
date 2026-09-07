import os
import re

files = [
    'templates/index.html',
    'templates/events.html',
    'templates/magic_members.html',
    'templates/scope_members.html',
    'templates/register.html',
    'templates/admin.html'
]

ids_per_file = {}
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        ids = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\']', content))
        ids_per_file[f] = ids

all_ids = set()
for f, ids in ids_per_file.items():
    intersect = all_ids.intersection(ids)
    if intersect:
        print(f"Overlapping IDs in {f}: {intersect}")
    all_ids.update(ids)

print("ID check completed.")
