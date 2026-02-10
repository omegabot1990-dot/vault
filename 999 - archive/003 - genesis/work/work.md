---
tags:
  - moc
  - work
description: all things work
parent nodes:
child nodes:
duration: 5
---

```dataviewjs
const workPage = dv.pages('"003 - genesis/work/work.md"');

// Render the table
dv.table(
    ["Hours Planned"],
    [
        workPage["duration"]
    ]
);
```
