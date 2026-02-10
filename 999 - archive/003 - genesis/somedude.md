---
tags:
  - moc
description: who am I
parent nodes: 
child nodes:
  - "[[academic]]"
  - "[[music]]"
  - "[[personal]]"
  - "[[work]]"
  - "[[somedude - time.canvas|somedude - time]]"
---

```dataviewjs
const academicPage = dv.pages('"003 - genesis/academic/academic.md"');
const musicPage = dv.pages('"003 - genesis/music/music.md"');
const workPage = dv.pages('"003 - genesis/work/work.md"');
const personalPage = dv.pages('"003 - genesis/personal/personal.md"');

const totalPlanned = academicPage["duration"].values[0] + musicPage["duration"].values[0] + workPage["duration"].values[0] + personalPage["duration"].values[0];

const academicPlanned = academicPage["duration"].values[0] / totalPlanned * 100;
const musicPlanned = musicPage["duration"].values[0] / totalPlanned * 100;
const workPlanned = workPage["duration"].values[0] / totalPlanned * 100;
const personalPlanned = personalPage["duration"].values[0] / totalPlanned * 100;

// Render the table
dv.table(
    ["Total Hours Planned", "Academic Planned (%)", "Music Planned (%)", "Work Planned (%)", "Personal Planned (%)"], 
    [ 
	    [totalPlanned, academicPlanned.toFixed(2), musicPlanned.toFixed(2), workPlanned.toFixed(2), personalPlanned.toFixed(2)] 
	]
);
```