---
tags:
  - moc
  - music
description: all things music
parent nodes:
child nodes:
duration: 0
---

```dataviewjs
const musicPage = dv.pages('"003 - genesis/music/music.md"');

// Render the table
dv.table(
    ["Hours Planned"],
    [
        musicPage["duration"]
    ]
);
```

