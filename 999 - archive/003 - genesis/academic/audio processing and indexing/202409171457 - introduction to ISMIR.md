---
tags:
  - academic
  - api
aliases:
  - assignment one
title: introduction to ISMIR
description: audio processing and indexing - assignment one
parent nodes:
  - "[[audio processing and indexing]]"
child nodes:
---

## What do I want to do?

1. Extract guitar elements from an audio signal
	1. From
		1. Digital signal
		2. Audio recording
	2. Rhythm
	3. Melody
	4. Effect detection 
		1. Delay
		2. Echo
		3. Reverb
		4. Distortion
		5. Modulation
2. Automatic mixing
3. Automatic mastering

## My take on the matter?

One paper I found most interesting is,

[Melody transcription via generative pre-training](https://zenodo.org/records/7316706)
[[melody_transcription_via_generative_pre_training.pdf]]
Published December 4, 2022  
[Chris Donahue](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Chris+Donahue%22), [John Thickstun](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22John+Thickstun%22), [Percy Liang](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Percy+Liang%22)

It was a hard choice; I had to shortlist the most appealing eight out of the many papers I was intrigued with (around 15). 

The top eight that made my list were:

1. Automatic music mixing with deep learning and out-of-domain data
2. Visualisation for AI-Assisted Composing
3. Unveiling the Impact of Musical Factors in Judging a Song on First Listen: Insights From a User Survey
4. Attention-based audio embeddings for query-by-example
5. Generating Coherent Drum Accompaniment with Fills and Improvisations
6. Representation Learning for the Automatic Indexing of Sound Effects Libraries

Having found so many papers that piqued my curiosity, I had to ask myself my objectives and how I plan to prioritise them. I soon realised that my first and foremost goal was extracting harmony and melody from a music score (to be exact, extracting the guitar rhythm and lead from rock and roll music); having made this realisation, I could pin down one paper.

As a guitarist, I’ve always found it challenging and time-consuming to transcribe music. It is a long and tedious process that often takes much trial and error. Extracting notes from an arbitrary audio recording is still quite an open challenge in MIR and one I wish to tackle during the period I undertake this course. I want to be able to implement a practical solution in 6 months. I always wanted to achieve this, and seeing the paper instantly made me realise this was a good starting point.  
One of the first problems I would face on this journey is finding the correct data to do supervised learning, and the paper addresses this by suggesting creating a generative data set. They achieved a 77% improvement over previous baseline metrics, and that too on a broader music classification. This made me wonder how much better I could do by being picky about the pre-training data I use (sticking to rock and roll). By combining older spectrogram-based feature analysis and leveraging beat detection, critical estimation and chord recognition, they were able to create a human-readable lead sheet directly from audio. I wish to do the same but with an output that is not conventional sheet music but guitar tabs, and this paper is a guideline I could follow to achieve this.

## References

1. Sure
	1. [Melody transcription via generative pre-training](https://zenodo.org/records/7316706)
	2. [Automatic music mixing with deep learning and out-of-domain data](https://zenodo.org/records/7316688)
2. Maybe
	1. [Visualization for AI-Assisted Composing](https://zenodo.org/records/7316618)
	2. [Unveiling the Impact of Musical Factors in Judging a Song on First Listen: Insights From a User Survey](https://zenodo.org/records/10265351)
	3. [Attention-based audio embeddings for query-by-example](https://zenodo.org/records/7316592)
	4. [Generating Coherent Drum Accompaniment with Fills and Improvisations](https://zenodo.org/records/7316646)
	5. [Representation Learning for the Automatic Indexing of Sound Effects Libraries](https://zenodo.org/records/7316800)

