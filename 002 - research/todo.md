---
tags:
  - moc
  - root
description: research todos
parent nodes:
  - "[[research.base]]"
child nodes:
---

- [ ] Paper to read
	- [ ] [Sebastian Raschka 2025 - List 1](https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one)
	- [ ] [Sebastian Raschka 2025 - List 2](https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2)
	- [ ] [Ilya Sutskever's Top 30](https://aman.ai/primers/ai/top-30-papers/)


```dataview 
task
from "003 - genesis/research"
where !completed
group by file.link
sort file.mtime desc
```
