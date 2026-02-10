## All Action Items
```dataview 
task
from "003 - genesis"
where !completed and action-items 
group by file.link
sort file.mtime desc
```

## Raw Action Items

```dataview 
task
from "002 - inbox"
where !completed and action-items 
group by file.link
sort file.mtime desc
```