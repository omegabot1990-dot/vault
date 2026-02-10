---
tags:
  - moc
  - academic
description: all things academic
parent nodes:
child nodes:
duration: 5
---

```dataviewjs
const academicPage = dv.pages('"003 - genesis/academic/academic.md"');

// Render the table
dv.table(
    ["Hours Planned"],
    [
        academicPage["duration"]
    ]
);
```

%% 
(resources:: Resources - 202406040341)
%%
> [!info] 2024-06-04
> > [!example] **Resources:**
> > - https://ocw.mit.edu/search/?d=Mathematics
