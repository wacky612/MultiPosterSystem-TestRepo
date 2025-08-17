#!/usr/bin/env python

import json
from pathlib import Path

data = []

for group_id in sorted(list(Path('posters').rglob('*/group_id'))):
    data.append(group_id.read_text().strip())

Path('build/group_id.json').write_text(json.dumps(data, ensure_ascii=False))

i = 0

Path(f'working/{i:05}.png').unlink(missing_ok=True)
Path(f'working/{i:05}.png').symlink_to(Path('blank.png').absolute())

i = i + 1
    
for png in sorted(list(Path('posters').rglob('*/poster.png'))):
    Path(f'working/{i:05}.png').unlink(missing_ok=True)
    Path(f'working/{i:05}.png').symlink_to(png.absolute())
    i = i + 1

Path(f'working/{i:05}.png').unlink(missing_ok=True)
Path(f'working/{i:05}.png').symlink_to(Path('blank.png').absolute())
