---
tags:
  - planning
description: sprint planner
parent nodes:
child nodes:
start date: 2025-11-04
end date: 2025-11-16
---

## Sprint Scope
```dataview
table description as "Description",
	file.frontmatter["story points"] as "Story Points",
	file.frontmatter["task type"] as "Task Type",
	file.frontmatter["due date"] as "Due Date", 
	file.frontmatter["start date"] as "Start Date",
	file.frontmatter["end date"] as "End Date",
	file.frontmatter["urgency level"] as "Urgency Level", 
	file.frontmatter["importance level"] as "Importance Level",	
	file.frontmatter["status"] as "Status"
from "002 - inbox/raw"
where contains(status, "To Do")
```

#### Story Points
```dataviewjs
// Query To Do tasks
const todoPages = dv.pages('"002 - inbox/raw"').where(p => p.status === "To Do");

let plannedPoints = 0;

for (const page of todoPages) { 
	if (page["story points"]) { 
		plannedPoints += page["story points"]; 
	} 
}

// Render the table
dv.table(
    ["Planned"],
    [
        [plannedPoints],
    ]
);
```
