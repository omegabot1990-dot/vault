---
tags:
  - academic
  - cc
aliases:
  - cc discussion
title: explore an enactive model for creativity for computational collaboration and co-creation
description: analyse the paper based on bad poets society
parent nodes:
  - "[[computational creativity]]"
child nodes: 
annotation-target:
---

Task: Read the suggested paper below on co-creativity and post to the forum an analysis of either one of the generative systems you’ve created or experimented with as part of this course.

Literature: [[davis_et_al_2015_an_enactive_model_of_creativity_for_computational_collaboration_and_cocreation.pdf]]

## Analysis

Working on the Bad Poets Society assignment, I experimented with Llama and Google T5-small. Working with Llama was easy, mainly because it was a pre-trained model with 3 billion parameters, compared to T5-small, a much smaller model with just 60 million parameters. Learning more about the Enactive Model of Creativity, I could see how, when interacting with Llama as an active process, cognition emerged as I kept interacting with the generative system through prompts. I could sense a certain form of creativity emerge when the autonomous agent interacted with its environment (me as the user); the dynamic interaction seemed to produce better results, but I could see that the memory state was not that great because the autonomous agent (Llama) kept forgetting the history of the prompts, one solution I found was the pass the whole chat history as the input every time, and this significant improved the outputs with noticeable novelty. 
With T5, though, I struggled to generate the desired outputs. I had to train the model on a set of select haikus, and by increasing the number of epochs and experimenting with hyperparameters, I got some okay results. However, with this model, I noticed that the chat history approach was not working out, and the system just gave me the same output as I added more of the history. I had to finally implement a test framework based on templates to get a good result.
The degree to which an agent is autonomous affects how helpful it can be while working as a co-creator. With Llama, I often found I was being helped, and we could work on finding solutions together, but with T5, it seemed more of a hassle; loose intentions that guide interactions but are flexible and evolve based on ongoing engagement with the creative process did not work out.

## Summary

The document "An Enactive Model of Creativity for Computational Collaboration and Co-creation" provides a comprehensive examination of how creativity can be understood and fostered within computational systems, particularly through the lens of the enactive approach to cognition. Here's a summary of the key points covered in the document:

### 1. **Introduction to Enactive Creativity**:
   - The document begins by critiquing the traditional models where humans command computers, suggesting a shift towards creative computers that can act as collaborators with humans.
   - It introduces the theory of enaction from cognitive science, which posits that cognition and creativity emerge through real-time, improvised interactions with the environment rather than through the internal manipulation of symbols.

### 2. **Computational Creativity**:
   - **Creativity Support Tools (CSTs)**: These tools enhance human creativity and help users explore creative domains. Examples include software like Adobe’s Photoshop and various design tools.
   - **Generative Systems**: These are autonomous systems that create art or poetry, for instance, based on algorithms and data they have learned from.
   - **Computer Colleagues**: Advanced systems designed to collaborate on creative tasks with humans, learning and improvising in real-time.

### 3. **Enactive Model of Creativity**:
   - **Perception and Action**: The enactive model views perception as an active process where cognition emerges from continuous interaction with the environment.
   - **Participatory Sensemaking**: Creativity is seen as a process of continuous negotiation and interaction, where new goals and solutions emerge organically from the dynamic between the cognitive agent and the environment.
   - **Goals and Directives**: Unlike traditional goal-based AI systems, the enactive approach focuses on 'directives'—loose intentions that guide interactions but are flexible and evolve based on ongoing engagement with the creative process.

### 4. **Application of the Enactive Model**:
   - **Sketching and Design**: The document discusses how sketching acts as a cognitive tool, allowing creators to externalise thoughts and engage with them perceptually, which helps in refining creative ideas.
   - **Musical Performance and Visual Arts**: Examples of how musicians and artists use perceptual feedback from their environments to adjust and refine their performances and artworks.

### 5. **Building Co-creative Agents**:
   - The document outlines how the enactive model can guide the development of computational agents that can act as creative collaborators, capable of adapting their behaviour based on the interaction dynamics with human users.

### 6. **Conclusions**:
   - The potential of computational creativity is emphasised, advocating for a cognitive theory that can adequately describe the enactive nature of creativity and support systems that truly collaborate with humans in creative processes.

This document offers a robust framework for understanding and developing computational systems that can participate in creative activities as genuine collaborators, using principles derived from the enactive approach to cognition.