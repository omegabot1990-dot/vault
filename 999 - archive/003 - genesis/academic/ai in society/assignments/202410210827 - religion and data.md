---
tags:
  - academic
  - ais
aliases:
  - religion and data
title: religion and data
description: how data affects ai in religious context
parent nodes:
  - "[[ai in society]]"
child nodes: 
annotation-target:
---

## Cues

#### [[unsupervised_by_any_other_name_hidden_layers_of_knowledge_production_in_artificial_intelligence_on_social_media.pdf|Unsupervised by any other name: Hidden layers of knowledge production in artificial intelligence on social media]]

- What is strong AI vs weak AI?

#### [[building_truths_in_ai_making_predictive_algorithms_doable_in_healthcare.pdf|Building truths in AI: Making predictive algorithms doable in healthcare]]

- N/A

## Notes

#### [[unsupervised_by_any_other_name_hidden_layers_of_knowledge_production_in_artificial_intelligence_on_social_media.pdf|Unsupervised by any other name: Hidden layers of knowledge production in artificial intelligence on social media]]

- Data collection is one area in which data classification can occur. What we get reflected back from large-scale studies of these platforms is not society as it is, but a society that is classified immediately into users (of interest, accessible) and non-users (not of interest, inaccessible).
- Another step in which classification work gets done is data cleaning.
- Model training is the third step of classificatory work.
- Classification is a natural part of human reasoning and is important in order to understand the world around us. However, despite such boxes being dynamic, these widely accepted boxes only allow us to see the world from certain cultural and historical standards, often excluding those at the margins and the "residual categories" that do not fit into our system or negations of the standardised classifiers: "deciding what will be visible and invisible in the systems".
- Classes are also ubiquitous and can create "cumulative mess".

#### [[building_truths_in_ai_making_predictive_algorithms_doable_in_healthcare.pdf|Building truths in AI: Making predictive algorithms doable in healthcare]]

- N/A

## Summary

#### [[unsupervised_by_any_other_name_hidden_layers_of_knowledge_production_in_artificial_intelligence_on_social_media.pdf|Unsupervised by any other name: Hidden layers of knowledge production in artificial intelligence on social media]]

The document titled "Unsupervised by any other name: Hidden Layers of Knowledge Production in Artificial Intelligence on Social Media" by Anja Bechmann and Geoffrey C. Bowker discusses the hidden complexities of knowledge production in AI systems used in social media, particularly focusing on classification practices within machine learning (ML) models. Here's a detailed summary:

### Abstract and Introduction

- AI, particularly ML models, are deployed to convert large data sets into actionable knowledge, claiming high autonomy and automation. However, the authors argue for a deeper examination of the classification processes in ML, suggesting that these processes are not fully autonomous as human intervention is often crucial at multiple stages.

### Main Themes and Theoretical Background

- The article challenges the notion that Big Data can function without extensive classification, contesting perspectives from notable figures like Chris Anderson and Bruno Latour. It emphasises the continuous need for classification in knowledge production, seen historically in various sciences.
- The authors explore how social and political factors infiltrate various layers of ML deployment, from data collection and cleaning to model training and deployment, often incorporating biases at each step.

### Classification in Practice

- Detailed examples are provided on how data classification occurs in different stages, such as data cleaning, where anomalous data is often excluded, and model training, where biases in training sets can affect the outcomes.
- They discuss the controversial use of ML by Facebook and the implications seen in the Cambridge Analytica scandal, demonstrating how political micro-targeting can manipulate democratic processes.

### The Role of AI and Machine Learning

- Distinguishing between strong/general AI and weak/narrow AI, the authors describe how both forms incorporate classification, yet they carry potential biases and limitations which must be recognised and addressed.

### Classification Theory

- The authors propose a theoretical framework for analysing classification in ML, emphasising the need to scrutinise how social and cultural biases are embedded in algorithmic decisions. They argue that what seems to be unsupervised learning is often not free from human biases and oversight.

### Case Studies and Empirical Application

- The paper includes case studies using Facebook data to illustrate how classification biases manifest. They apply ML models like text2vec and deep neural networks to demonstrate how these biases can lead to discriminatory outcomes.

### Discussion and Conclusions

- The document stresses the importance of governance in AI deployment, advocating for a framework that incorporates accountability and transparency in the classification processes.
- It calls for more rigorous standards in designing and applying AI systems to prevent discriminatory practices and ensure that AI technologies adhere to democratic and ethical standards.

Overall, Bechmann and Bowker highlight the hidden layers of human intervention in supposedly autonomous AI systems, urging reevaluation of how these systems are designed and governed.

#### [[building_truths_in_ai_making_predictive_algorithms_doable_in_healthcare.pdf|Building truths in AI: Making predictive algorithms doable in healthcare]]

The document "Building Truths in AI: Making Predictive Algorithms Doable in Healthcare", by Anne Henriksen and Anja Bechmann provides an in-depth analysis of how truths are constructed within AI systems, particularly in healthcare applications. Here’s a detailed summary of its contents:

### Abstract and Introduction

- The paper discusses the increasing role of AI algorithms in decision-making within healthcare. It critiques the existing literature for its focus on the biases produced by AI, arguing that more attention needs to be given to how algorithms are designed to embody specific 'truths' that enable systematic decision-making.

### Main Themes and Methodology

- The authors conducted an ethnographic study in a Scandinavian AI company to explore how developers translate complex patient conditions into operational algorithms. The study examines the iterative practices of defining, adjusting, and validating these truths in algorithm design.

### Truth and Knowledge Production in AI

- The paper explores the concept of 'ground truth' in AI, which is essential for training models to predict and make decisions. The authors delve into the nuances of selecting data and defining targets that reflect a particular interpretation of patient conditions, which are often subjective and variable.

### AI Predictive Modelling and Practices

- The discussion extends to the practices of AI modelling, highlighting the balance between using expert knowledge and statistical models to shape decision-making in healthcare. This involves ongoing negotiations and recalibrations to align AI outputs with practical healthcare outcomes.

### Ethnographic Insights from AI Development

- The ethnographic study reveals five main practices through which truth is constructed in AI:
    1. **Negotiation between data signals, human classification, and data selection:** Developers continuously adjust data inputs and model parameters to refine AI performance.
    2. **Validation according to experts and objective metrics:** External experts and standardised metrics play crucial roles in validating the AI’s decisions.
    3. **Balancing contextualisation and generalisation:** Developers must consider the specific healthcare context while designing algorithms that perform reliably across different situations.
    4. **Elimination of errors:** The pursuit of minimising errors in AI predictions to surpass human accuracy.
    5. **Reorganisation of healthcare practice:** AI development is not just about technology but also involves rethinking and reshaping healthcare practices to integrate new AI tools effectively.

### Conclusion

- The study concludes that the construction of truth in AI for healthcare is a complex, multimodal process that involves various stakeholders, including engineers, medical experts, and data scientists. The findings emphasise the need to critically examine how truths are built into AI systems and the implications for healthcare practices.

This document underscores the intricate interplay between technology and healthcare, highlighting the importance of transparent and accountable AI development practices to ensure that these systems serve the intended purposes without unintended consequences.

---

## Q and A

Q: Can you establish what data AI systems of your interest (in your domain) rely on? What concerns regarding biases would you have, considering what we have discussed in class and what you know about your domain?  (Approx. 200 words)
A: The data for a religious AI system would predominantly be sourced from scriptures. The first obvious challenge is related to translation; even gender-neutral languages like Hungarian used today, when translated into English, exhibit gender bias in machine translation. When translated, an old and not natively spoken language could carry an enormous implicit bias.  
The second challenge is data collection. The religious ideologies prevalent today may be based on the scriptures and arise from cultures throughout history that interact with the text and within themselves to create something new and novel. But would all these be recorded? The implicit rules, tacit knowledge, and social cues could be lost over time.
The third aspect is data curation. Since every religion has a select human intermediary who facilitates the curation process before a machine consumes the information as part of the training, anomalies are likely to be weeded out before they are even spotted. Selection bias in such cases is inevitable, and we will notice that the data selected aligns more with the dominant cultural narratives or institutionalised goals. The data on marginalised or alternative religions may not even be considered in these cases. 
Finally, AI may influence religious beliefs and practices and cause homogenisation. As AI begins to influence religious discussions or provide "answers" to theological questions, it may alter the fabric of religious belief systems. This influence could challenge traditional religious authorities and doctrines, leading to community tensions and conflicts.

Q: Drawing on insights from Bechmann and Bowker (2019) and Henriksen and Bechmann (2020), explain how the choices and interpretations made by developers (and the institutions they represent) shape the construction of "truth" in AI systems. Relate these insights to your domain. (Approx. 300 words) 
A: The papers focus on how even so-called highly automated and autonomous models possess underlying hidden complexities regarding knowledge production. They also highlight developers' agency in embodying certain truths within AI systems and how special attention should be given to the design of these algorithms.
The former article examines how classification is an innate property of even unsupervised models, delving deeper into how these biases become visible in certain machine-learning steps. Data collection is one of the foremost areas where this may occur, resulting in an immediate separation into users of interest and non-users of no interest. Still, the collected data is used to represent the entirety of society. When placed in a religious context, we can see that this could lead to further marginalisation of smaller sects, which are underrepresented. This is a very evident example of representation bias. Unless a framework incorporates transparency and accountability in the classification process, this could result in widespread homogenisation of religious experience and understanding that discounts less dominant voices. In this instance, institutions have unregulated power to determine the outcomes of the models, and unless this is regulated, it could incite mass unrest.
The next stage is data cleaning. Here, it is observed that removing anomalous data from the training set can skew the output, distorting the situation's reality. This scenario becomes increasingly relevant when creating tools that help interpret religious texts; if the developer opts not to include certain texts based on inherent biases, it could alter how the model represents the ground truth, much like the case of the Cambridge Analytica scandal, which demonstrated how AI could be used for political micro-targeting. If not conducted under appropriate standards, such practices could lead to religious micro-targeting and become the next big scandal.
Interpretive bias could also exist because of how the ground truths are encoded into the model via the training data and the developer's understanding of the generalisations versus the contextualisation; as we can see, religious tools are very volatile when inspected through this lens, and we need the right governing agencies to regulate them.


Q: Why, according to Roger A. Søraa (2022), intersectional approach to AI development is essential? How would you see that relevant in your domain? (Approx. 300 words)
A: According to Roger A. Søraa, AI systems will have inherent biases encoded into their workings that could inadvertently reproduce and propagate existing social inequalities unless a conscious and deliberate design philosophy is implemented to encompass inclusivity and equality. The author tries to focus on how an intersectional perspective adopted by AI developers, designers, producers and makers can make it easier and more effective to identify and mitigate biases that arise because of the multi-faceted characteristics of each user, which means through a systematic analysis considering class, gender, age, sexuality, disability, ethnicity, culture and religion that could contribute to a person's identity we can hope to reduce bias to a large extent.
An intersectional approach to AI development is essential as it addresses multiple, overlapping social identities and complex power structures that affect how technology is developed and used, especially in domains like religion where there already exists inherent gender, class, sexuality, etc. biases based on the subjective interpretation of theological doctrines. Religious beliefs and practices are closely connected to cultural, racial, and gender identities, all of which can shape an individual's spiritual experiences and needs. For example, AI-driven platforms might personalise religious content or foster community interactions while being attuned to the diverse backgrounds of their users.
Furthermore, intersectionality is the key to building AI-based tools that respect and preserve how the vast and diverse cultures, sects, and subcultures express their faith; this could help increase tolerance between various communities and religious groups. Also, considering the global nature of religion, AI systems designed based on intersectional awareness can provide a better hyper-localised experience that caters to the local cultures in which they operate rather than a generalised experience. This kind of adaptation is crucial for the inclusion of marginalised groups. This can strengthen technology's role in facilitating religious education, interfaith dialogue, and community services, making sure these innovations foster inclusion instead of worsening existing disparities.
