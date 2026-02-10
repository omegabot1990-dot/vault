---
tags:
  - planning
description: 
parent nodes: 
child nodes: 
start date: 2025-01-19
end date: <% tp.date.now("YYYY-MM-DD", 7) %>
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


%%
<%* const today = tp.date.now("DD-MM-YYYY"); const nextWeek = tp.date.now("DD-MM-YYYY", 7); 
const dateString = `Sprint (${today} to ${nextWeek})`;
await tp.file.rename(dateString);
%>
%%
