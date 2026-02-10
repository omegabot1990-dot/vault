---
tags:
  - retrospective
description: 
parent nodes: 
child nodes:
start date: <% tp.date.now("YYYY-MM-DD", -7) %>
end date: <% tp.date.now("YYYY-MM-DD") %>
---

## Competed Tasks
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
where contains(status, "Done")
```

## In Review Tasks
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
where contains(status, "In Review")
```

## Spillover Tasks
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
// Query In Review tasks
const inReviewPages = dv.pages('"002 - inbox/raw"').where(p => p.status === "In Review");
// Query Done tasks
const donePages = dv.pages('"002 - inbox/raw"').where(p => p.status === "Done");

let plannedPoints = 0;
let completedPoints = 0;

for (const page of todoPages) { 
	if (page["story points"]) { 
		plannedPoints += page["story points"]; 
	} 
}
for (const page of inReviewPages) { 
	if (page["story points"]) { 
		plannedPoints += page["story points"]; 
	} 
}
for (const page of donePages) { 
	if (page["story points"]) { 
		plannedPoints += page["story points"]; 
		completedPoints += page["story points"]; 
	} 
}

const velocity = completedPoints / plannedPoints * 100;

// Render the table
dv.table(
    ["Planned", "Completed", "Velocity (%)"],
    [
        [plannedPoints, completedPoints, velocity],
    ]
);
```

%%
<%* const today = tp.date.now("DD-MM-YYYY"); const lastWeek = tp.date.now("DD-MM-YYYY", -7); 
const dateString = `Sprint (${lastWeek} to ${today})`;
await tp.file.rename(dateString);
%>
%%