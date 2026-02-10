---
tags:
  - academic
  - mgaa
description: first mgaa assignment
due date: 2025-02-27
start date:
end date: ""
status: Archive
importance level: important
urgency level: not urgent
task type: execute
story points: 13
parent nodes:
child nodes:
recurrent:
---

[[modern_game_ai_algorithms_minecraft.pdf]]

## Notes

> Set Build Area
```
/setbuildarea 0 64 0 99 128 99
```

- x-axis
	- 0 - 99
- y-axis
	- 64 - 128
- z-axis
	- 0 - 99
- Total Area: 100 x 100 blocks


## Report

>  self-contained scientific pdf report with figures, references, etc. The page count we expect of you might vary depending on your layout (4-8 pages would be reasonable). 
>  This report contains: 
	An explanation of the techniques you applied, e.g. ∗ How do you find an area to place your building? Include plots that visualize your terrain evaluation ∗ What is variable / random in the building process? 
	How you addressed believablity.
	Multiple example figures showing the variation as well as adaptability to different environments. – Overall conclusions

#### Introduction

This assignment focuses on utilising Procedural Content Generation to design a house in the well-loved game Minecraft, employing the GDPC API available in Python. We will leverage this package to develop code that constructs a modern-style house, characterised by its simplicity yet functional appeal. The fundamental shape resembles a cuboid, but its minimalistic design is truly commendable. 

This house presents a harmonious fusion of traditional and contemporary design features, resulting in a cozy yet elegant look that captures immediate attention. The exterior highlights sharp lines and a well-proportioned arrangement of windows, while delicate decorative elements—like timber accents or an inviting front porch—enhance its welcoming ambiance. From the muted color scheme to the thoughtful use of natural materials, every aspect is designed to be both practical and aesthetically pleasing. The open, airy layout promotes abundant natural light, enhancing a feeling of comfort and spaciousness. In my Minecraft creation, I’ve drawn from these inspirations to replicate the house’s inviting atmosphere and harmonious proportions in a block-style format.

This project investigates Procedural Content Generation for designing a house in the popular game Minecraft, utilising the GDPC API in Python. The final structure is inspired by modern architecture, featuring both simplicity and functional appeal, and takes on a refined cuboid shape. This design seamlessly incorporates traditional and contemporary elements, resulting in a cozy yet sophisticated appearance that captivates attention. The façade presents clean lines and a well-proportioned arrangement of windows, while subtle touches—like timber accents or a welcoming front porch—enhance its approachable ambiance. Featuring a muted colour scheme and carefully selected natural materials, the house is both visually striking and practical, offering an open layout that maximises natural light to create a sense of comfort and spaciousness.

I first came across the original house, shown in \textbf{subfigure~\ref{fig:subfig1}}, on the 
\href{https://www.elledecor.com/design-decorate/g8674077/modern-houses/}{Elle Decor website} 
and was immediately impressed. Notably, it was rebuilt after the original was destroyed by a hurricane. In my Minecraft adaptation, I’ve aimed to replicate the house’s inviting atmosphere and balanced proportions, while also addressing local concerns in Kerala, where recurring monsoon floods have become common since 2018. Many houses in my neighborhood face flooded ground floors during heavy rains, causing significant disruptions. To counter this, I incorporated an open staircase design that remains accessible even when the lower levels are submerged. I also added solar-powered lighting blocks that absorb sunlight by day and emit light at night, as depicted in \textbf{subfigure~\ref{fig:subfig2}}.

I aimed to design a minimalist structure with a narrow, stable base, utilising two different materials to enhance resistance to water and other damages. The structure stands a few meters tall, with a solar-powered light source positioned right in the middle, as monsoons often disrupt energy supply. Leaving one side open ensures that, in case of rising water levels, access to the stairs remains possible from any height. For example, you could access the structure from any height by boat.

The upper level is an open-format house that has windows on all sides, which means there is an abundance of sunlight that can come in. I also decided to keep the garden inside, as the idea of protection from the monsoon makes an outdoor garden impractical. Thus, the house has an indoor garden that produces oxygen and keeps the interior fresh. There are four light sources placed at the four corners of the house, made from the same solar-powered material as in the staircase. The interior is then furnished with beds, furnaces, and other items.

To incorporate randomness into the design, I focused on the arrangement of the interior. Various materials were utilised to create unique furniture, and the placement of different elements was altered as well.

#### Methodology

I utilised the standard deviation to pinpoint the sub-area within a 100 by 100 build zone that exhibits the lowest deviation. This technique helps me identify a location with minimal terrain disruption, making it suitable for construction. By using this method, I can effectively adapt to the terrain and build a functional house. The house's base measures 5 by 5, and the platform is 10 units wide on top. With a height of 10, the house is elevated and positioned at a different level, aligning with the design pattern referenced in the introduction.

Regarding the viability of the land, I conduct a check to determine the ground level, ensuring it's not one of the following: "water, " "lava, " "leaves, " "ice, " "seagrass, " "kelp, " "magma, " or "soul_sand. " This ensures I find suitable ground that can serve as a stable base for construction. Along with the standard deviation, this approach forms a strong strategy that can address most challenges. I have added an example heat map to find the area suitable for the process. 

Regarding variability, since I have adhered to a minimalistic design pattern, I decided to modify the layout of the house's interior. I work with different objects to create the layout, and various colours have been utilised as well. The placement of the objects is also randomised, as can be observed in the layout of the carpets shown in the images displayed in the figures.

As for believability, I have adhered to a minimalistic design that has been developed to construct an actual house, as mentioned in the introduction. This design has been tried and tested in the real world. One aspect I have sought to incorporate is flood resistance functionality. I believe that if the right materials are used, we can create a platform light enough to be supported by the pillars.

While the project meets its objectives, it has a few limitations: \ begin {itemize} \ item The reliance on standard deviation for terrain selection is effective in flat areas but often overlooks natural terrain features that could benefit construction. \ item The procedural generation of furniture adopts a randomized approach but lacks a thorough room segmentation system that could further enhance variety. \ item The design's effectiveness against extreme environmental factors, such as heavy storms, landslides, or elevated flood levels, remains theoretical within the Minecraft simulation. \ end {itemize}

This project effectively illustrates the capabilities of Procedural Content Generation in crafting both functional and visually pleasing structures in Minecraft. Using the GDPC API, an automated building system was developed to adapt to landscape constraints, integrate randomised design features, and tackle real-world challenges like flood resistance. A systematic approach to choosing the best build site guarantees that the house is located in the most stable and practical area of the defined terrain. The introduction of randomised interior components enhances replayability and ensures unique experiences with each build, while the flood-resistant architecture realistically reflects modern design solutions.
Future enhancements might revolve around improving the realism of room divisions, fine-tuning terrain adaptation methods, and introducing more sophisticated furniture placement options. Expanding the procedural generation framework to accommodate various house styles and layouts could further enhance the overall experience. In conclusion, this study underscores the promise of PCG in Minecraft for constructing dynamic and adaptable structures that resonate with real-world architectural concepts.