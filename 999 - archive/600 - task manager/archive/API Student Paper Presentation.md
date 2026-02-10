---
tags:
  - academic
  - api
description: present the paper in class
due date: 2024-11-12
start date: 2024-11-08
end date: 
status: Archive
importance level: important
urgency level: urgent
task type: execute
story points: 
parent nodes: 
child nodes: 
recurrent:
---

#### References

- https://source-separation.github.io/tutorial/landing.html

[[melody_transcription_via_generative_pre_training.pdf]]

### Slide 1 - Introduction

##### **Importance of Melody in Music:** Discuss the role of melody in music perception and its applications in various fields.

**Why is Melody important?**
Melody is essential to musical composition and often defines a piece's identity in the collective consciousness.

**The key challenge in Melody Transcription?**
A key challenge in melody transcription is developing methods that handle diverse audio with various instruments and styles. Current approaches work well for specific instruments or styles but not universally.

**Applications of automatic Melody Transcription?**
Interaction: Accompaniment Separation for Karaoke Application.
Education: It helps teach music theory, composition, and arrangement by providing real-time notation of the music students play or listen to. This aids in ear training as students identify notes and melodies by ear.
Informatics: Melody transcription enriches music metadata and enhances musicological analysis, helping researchers study styles, structures, and evolution.
Retrieval: It improves music database searchability by allowing users to query by humming or singing tunes.
Separation: It can facilitate more effective source separation by identifying the melodic line that needs to be isolated.
Generation: Useful for musicians' composition and background music in games and media.

**Reliable Melody Transcription still remains an open challenge in MIR.**
Despite the central role of melody in music perception, it remains an open challenge in MIR to reliably detect the notes of the melody in an arbitrary music recording.

### Slide 2 - Abstract Overview

##### **Purpose of the Presentation:** Overview of the advancements in melody transcription using generative pre-training.

- **Summary of Key Points:**
  - The challenge in melody detection across diverse musical styles.
  - Utilisation of the Jukebox model for improved transcription.
  - Creation of a new extensive dataset to enhance performance.

Jukebox: A generative model for wide music audio enhances melody transcription performance by 20% compared to traditional spectrogram features. 
Lack of training data: Create a new dataset with 50 hours of melody transcriptions sourced from community annotations of diverse music. 
By integrating generative pre-training with a new dataset for this task, they achieved a 77% improvement in melody transcription compared to the best existing baseline.
Combining their melody transcription with beat detection, key estimation, and chord recognition, they created Sheet Sage, which transcribes human-readable lead sheets from music audio.

1. **Extract Audio Features**:
    - The Jukebox is a generative model trained on a vast library of songs. It analyzes music and extracts detailed audio features that represent the underlying musical content.
2. **Time Alignment**:
    - Average these extracted features over time to align with the nearest sixteenth note. This uses a tool called `madmom` to accurately detect the timing of beats, helping to standardise the timing across the audio for more precise note detection.
3. **Note Detection**:
    - Train a Transformer model, a type of neural network known for its effectiveness in handling sequences, to identify where notes start (onsets) and whether there are notes at each sixteenth note interval of the music piece.
4. **Output the Transcription**:
    - Convert the detected notes and rhythms into a standard music format like MIDI. This format can be used in various music software or converted into a traditional music score that musicians can read and play.

### Slide 3 - Background and Related Work

- **Definition of Melody and Melody Transcription**
- **Review of Existing Techniques:**
  - Melody extraction vs. melody transcription.
  - Limitations of previous methods.

**Melody Extraction**
Goal: Melody extraction aims to estimate the continuous F0 trajectory from an audio mixture.
Drawback: 
1. While F0 trajectories provide a high-level view of the melody's pitch contour, they do not offer the detailed musical notation that performers and composers rely on.
2. F0 trajectories are not immediately usable in standard music production software that requires discrete note values and timings.

**Melody Transcription**
Goal: To convert audio into a symbolic format where three main attributes define each note:
1. Onset time: When the note begins.
2. Pitch: The musical pitch or note being played.
3. Offset time: When the note ends.
This detailed transcription is more suitable for musicians who rely on scores or MIDI files to learn, perform, or analyse music.

### Slide 4 - Task Definition and Evaluation

### Slide 5 - Dataset Overview

**Title: Overcoming Data Limitations in Melody Transcription**

1. **Existing Data Sources**
    - RWC Music Database: 8.7 hours of usable audio
    - Laaksonen Dataset: 1.5 hours
2. **HookTheory Dataset Creation**
    - 50 hours from 22,000 segments of 13,000 unique recordings
    - Diverse genres: Pop, Rock, EDM, Jazz, Classical
    - Data split: 80% training, 10% validation, 10% testing
3. **Data Format and Conversion**
    - Original annotations in functional format (scale degrees, roman numerals)
    - Converted to an absolute format (JSON) for MIR compatibility

- **Introduction to Data Sources**
    - Begin by highlighting the limitations in existing datasets for melody transcription, particularly noting the small size and inconsistent annotations in datasets like RWC and Laaksonen, which restrict the development of effective transcription models.
- **Introducing the HookTheory Dataset**
    - Explain the creation of a new, larger dataset using crowdsourced annotations from HookTheory, a platform where users annotate YouTube music videos. Emphasize the volume and diversity of the data, which covers a broad range of musical genres and a significant number of recordings, providing a robust foundation for training transcription models.
- **Challenges in Data Annotation**
    - Discuss the original format of HookTheory annotations, which uses musical terms like scale degrees that are less useful for straightforward machine learning applications. Mention the process of converting these annotations into a more usable, absolute note format while noting the challenge of the relative octave system which remains unaligned with a concrete ground truth.
- **Significance for MIR Research**
    - Conclude by highlighting how this dataset not only supports melody transcription but also enhances other areas of MIR research such as chord recognition and harmonisation. The adaptation from a functional to an absolute annotation format makes it more suitable for diverse MIR tasks, potentially setting a new standard for dataset creation in this field.

### Slide 6 - Methods

- **Adapting State-of-the-Art Methods**
    - Use of Transformer models for transcription.
    - Leveraging pre-trained model features (Jukebox and MT3).
- **Unique Methodological Adjustments**
    - **Pre-trained Representations:** Jukebox (fk ≈ 345 Hz) and MT3 (fk = 125 Hz) for nuanced audio feature extraction.
    - **Refined Alignments:** Utilising beat detection to improve alignment accuracy for transcription.
- **Training Strategy Under Approximate Alignments**
    - **Beat-wise Resampling:** Normalising feature timing to enhance model training accuracy.
    - **Modelling Approach:** Sequence-to-sequence modelling to predict note onsets from resampled audio features.

- **Introduction to Methodology**
    - Begin by explaining the foundation of using Transformer models in melody transcription, inspired by their success in polyphonic transcription tasks.
    - Highlight the adaptation of using deep layers of Jukebox for feature extraction, chosen for its effectiveness in various MIR tasks, and MT3 known for transcription capabilities albeit in different domains.
- **Detailed Explanation of Adjustments**
    - Discuss the significance of choosing pre-trained models over traditional spectrogram features, emphasising the broader audio coverage and the need for detailed feature extraction to handle complex audio scenarios.
    - Explain the refined alignment process using `madmom` for beat detection, which compensates for the approximate nature of the dataset’s annotations and improves the transcription's reliability.
- **Training Strategy**
    - Describe the beat-wise resampling strategy that aligns audio features with musical beats more precisely, mitigating issues with raw alignment and enhancing transcription accuracy.
    - Detail the sequence-to-sequence modelling approach used to predict note onsets and how it's adapted to work with these refined alignments and resampled features.
    - Mention the challenge of the relative octave information in the dataset and how the model is designed to be octave-tolerant, ensuring the system's practical applicability across various musical keys and styles.
- **Conclusion**
    - Summarise the innovative aspects of the methodology that address specific challenges in melody transcription, particularly the use of advanced AI models and sophisticated data preprocessing techniques to achieve high accuracy in note prediction.
    - Encourage questions about how these techniques can be applied in other areas of music information retrieval or adapted for other complex audio processing tasks.

### Slide 7 - Experiments

- **Purpose of Experiments**
    - Evaluate the effectiveness of pre-trained models vs. handcrafted spectrogram features.
    - Benchmark against other melody transcription baselines.
- **Model Configuration**
    - Encoder-only Transformers with 4 layers (reduced from 6 for GPU compatibility).
- **Training Details**
    - Input: Random slices of up to 96 beats or 24 seconds.
    - Optimisation: Early stopping based on maximum F1 score.
- **Computational Details**
    - Training convergence: Within 15,000 steps (~1 day) on a K40 GPU.

- **Introduction**
    - Begin by explaining the dual objectives of the experiments: to test whether pre-trained model features outperform traditional spectrogram features and how our models stack up against existing baselines in melody transcription.
- **Model Setup**
    - Detail the use of encoder-only Transformer models, adapted for training on available GPU resources by reducing the number of layers. This modification ensures that the models are both efficient and effective within the computational limits.
- **Training Process**
    - Discuss the selection process for training data, emphasising the randomness and the limitation to either 96 beats or 24 seconds, whichever is shorter, to maintain uniformity and manageability.
    - Explain the loss function and the use of early stopping based on the validation set's maximum F1 score, which helps in preventing overfitting and ensures that the models generalise well on unseen data.
- **Computational Efficiency**
    - Highlight the efficiency of the training process, noting that all models converge within approximately one day on a single K40 GPU, demonstrating the practical feasibility of the training regimen for academic and small-scale professional settings.
- **Conclusion**
    - Summarise the expected outcomes of these experiments, focusing on the implications for advancing the field of Music Information Retrieval through improved melody transcription techniques.
    - Encourage questions about the model configurations, training strategies, or results anticipated from this experimental setup.

### Slide 8 - Results

**Title: Comparative Analysis of Feature Representations in Melody Transcription**

1. **Feature Types Tested**
    - Jukebox (pre-trained on 1M songs)
    - MT3 (encoder-decoder model pre-trained on diverse tasks)
    - Handcrafted Spectrogram Features (log-amplitude Mel spectrograms)
2. **Combinatorial Approach**
    - Experimentation with all possible combinations of these features.
    - Utilisation of beat-wise resampling for feature integration.
3. **Performance Metrics**
    - Evaluation based on F1 scores from the HookTheory test set.
    - Best performance achieved by Jukebox, followed by combined features, and then MT3.
4. **Practical Considerations**
    - Despite some benefits, combining features has practical downsides such as increased computational requirements.

1. **Introduction to Feature Types**
    - Start by explaining the different types of features evaluated: pre-trained models like Jukebox and MT3 versus traditional handcrafted spectrogram features.
    - Mention the significance of each feature type, with Jukebox being notable for its broad pre-training and MT3 for its task-specific pre-training.
2. **Methodology of Feature Combination**
    - Discuss the beat-wise resampling strategy that allows for the easy combination of features with different sampling rates, enhancing the richness of the input data for the models.
3. **Key Findings on Performance**
    - Highlight the main finding that Jukebox provided the strongest individual performance in terms of F1 score, indicating fewer transcription errors and better rhythm detection.
    - Note that while combining features did improve performance slightly, Jukebox alone was almost as effective.
4. **Discussion on Practical Implications**
    - Discuss the practical trade-offs of combining features, such as increased computational load and software compatibility issues, which can be significant drawbacks in real-world applications.
    - Conclude with the decision to focus on single-feature models for further development due to these practical considerations.
5. **Conclusion**
    - Summarise by affirming the value of pre-trained models in improving the accuracy of melody transcription and the practical decision to use them individually to optimize both performance and computational efficiency.
    - Encourage questions about how these findings might influence future transcription model development or application.

1. **Study Design**
    - Tested on 10 songs from RWC-MDB.
    - Comparison includes early DSP-based methods and recent advanced models.
2. **Baseline Comparisons**
    - DSP-based method from previous studies.
    - Note segmentation heuristic combined with a melody extraction algorithm.
    - MT3 model evaluated in a zero-shot fashion.
    - Tony software for monophonic transcription on vocals isolated by Spleeter.
3. **Performance Metrics**
    - Evaluation based on correctness of pitch and rhythmic consistency.
    - Our method outperforms all baselines, especially in vocal transcription.
4. **Statistical Significance**
    - Results show significant improvement (p < 0.01).

1. **Background and Selection of Dataset**
    - Begin by introducing the RWC-MDB dataset, specifically chosen due to its inclusion of melody transcription labels and its use in prior seminal DSP-based studies. Explain that the dataset's historical use provides a robust foundation for comparative analysis.
2. **Description of Baselines**
    - Detail each baseline method used for comparison:
        - **Early DSP-based approaches**: Mention the historical context and the lack of available code, highlighting the challenge of replicating these methods.
        - **Note segmentation and melody extraction**: Explain this method's relevance to the study, focusing on its traditional application in melody transcription.
        - **MT3 zero-shot application**: Clarify that MT3 was not specifically trained for melody transcription, providing context on its inclusion as a modern comparative baseline.
        - **Tony software**: Discuss its application to vocals, important since vocals often carry the melody in popular music, and the use of Spleeter for vocal isolation to enhance transcription accuracy.
3. **Performance Overview**
    - Highlight the superior performance of your method, particularly emphasizing its effectiveness in handling both general and vocal-specific transcription tasks.
    - Discuss the quantitative measures used, such as pitch accuracy and rhythmic consistency, and the statistical methods confirming the significance of the results.
4. **Conclusion and Implications**
    - Summarise the implications of these findings for the field of Music Information Retrieval, emphasising how your method's performance could influence future transcription technologies.
    - Encourage questions about methodological choices, potential applications, and possible future enhancements based on the study's findings.

## Outline

### Presentation Title: Advancements in Melody Transcription through Generative Pre-training

---

#### Slide 1: Introduction
- **Importance of Melody in Music:** Discuss the role of melody in music perception and its applications in various fields.
- **Purpose of the Presentation:** Overview of the advancements in melody transcription using generative pre-training.

---

#### Slide 2: Abstract Overview
- **Summary of Key Points:**
  - The challenge in melody detection across diverse musical styles.
  - Utilisation of the Jukebox model for improved transcription.
  - Creation of a new extensive dataset to enhance performance.

---

#### Slide 3: Background and Related Work
- **Definition of Melody and Melody Transcription**
- **Review of Existing Techniques:**
  - Melody extraction vs. melody transcription.
  - Limitations of previous methods.
  
---

#### Slide 4: Problem Statement
- **Challenges in Melody Transcription:**
  - Handling broad audio containing diverse ensembles and styles.
  - Lack of sufficient training data for complex models.

---

#### Slide 5: Innovations in Dataset Creation
- **New Dataset Introduction:**
  - Description of the 50-hour melody transcription dataset.
  - Sources and composition of the dataset (genres, annotations).

---

#### Slide 6: Methodology
- **Feature Extraction Techniques:**
  - Use of generative models (Jukebox and MT3) for feature extraction.
- **Transformer Models for Transcription:**
  - How Transformers are trained on the new dataset to predict notes.

---

#### Slide 7: Experimental Results
- **Setup and Protocols:**
  - Description of test sets and baseline models.
- **Performance Comparisons:**
  - Statistical results show improvements over traditional methods.

---

#### Slide 8: Sheet Sage - A Practical Application
- **Overview of Sheet Sage:**
  - System capable of converting audio into lead sheets.
- **Components and Workflow:**
  - Integration of melody transcription, beat detection, chord recognition, and key estimation.

---

#### Slide 9: Ethical Considerations
- **Cultural and Ethical Impacts:**
  - Discussion on the Western-centric approach and its implications.
- **Potential Risks:**
  - Plagiarism and labor displacement concerns in the use of AI in music.

---

#### Slide 10: Conclusion
- **Summary of Contributions:**
  - Recap of the improvements introduced by the new methods and dataset.
- **Future Directions:**
  - Potential areas for further research and improvement in melody transcription technologies.

---

#### Slide 11: Acknowledgements and References
- **Acknowledging Contributions:**
  - Mention colleagues, advisors, and reviewers.
- **Key References:**
  - Highlight important references that underpin the research.

---

#### Slide 12: Questions and Discussion
- **Open Floor for Questions:**
  - Invite questions from the audience to clarify or expand on specific points.

---


# Melody Transcription Process Overview

## Definition
Melody transcription involves converting a music recording into a sequence of notes that represent its dominant melody.

## Process Steps

### Step 1: Understanding the Audio Input
- **Input**: A music waveform $a$ of length $T$ seconds.
- **Output**: A sequence of $N$ notes $y = [y_1, \ldots, y_N]$ that represent the melody.
- **Notation**: Each note $y_i$ is defined by an onset time $t_i$ and a discrete musical pitch $n_i$.
  
### Step 2: Featurizing the Audio
- **Purpose**: To convert raw audio into a format that's easier for algorithms to process.
- **Method**: Use a function `Featurize` to transform the audio waveform $a$ into a matrix $X$ of d-dimensional features.
- **Details**:
  - $X = \text{Featurize}(a)$ results in a matrix where features are sampled at a rate $f_k$ much less than the sampling rate $f_s$ of the original audio.
  - Commonly, $X$ could be a spectrogram, capturing the frequency content over time.

### Step 3: Transcribing Audio Features into Notes
- **Task**: Map the featurized audio $X$ to the sequence of notes $y$.
- **Function**: $\text{Transcribe}(X) \rightarrow y$
- **Focus on Onsets**:
  - Only the onset time $t_i$ and the pitch $n_i$ are considered for each note.
  - Offsets are omitted because they are less crucial for the perceived accuracy of the transcription and often match a preset pattern.

## Note Representation
- **Format**: Each note is a pair $(t_i, n_i)$ where:
  - $t_i$ is the onset time within the audio length $[0, T)$.
  - $n_i$ is the pitch, selected from a set of pitches $V = \{A0, \ldots, C8\}$.
- **Sequence Order**: The sequence is ordered so that $t_i < t_j$ if $i < j$, ensuring notes are listed in the order they occur.

## Additional Details
- The method disregards note offsets because they do not significantly impact the perceived quality of transcription and are often predictable based on the onset of subsequent notes.


# Evaluating Melody Transcription Methods

## Overview
To assess the accuracy of a melody transcription method, we use a specialized evaluation metric adapted for this task.

## Evaluation Metric: Onset-only Note-wise F-measure

### Description
- **Metric Used**: Onset-only note-wise F-measure, a common standard in polyphonic music transcription.
- **Procedure**:
  - Compare the note onsets of the transcribed output $\text{Transcribe}(X)$ to a reference note sequence $y$ with a tolerance of 50ms.
  - Compute the F1 score, where a transcribed note is considered correct if its pitch matches the reference note's pitch, accounting for the onset alignment.

### Significance
- **Correlation with Perception**: This metric correlates strongly with human perception of transcription quality, more so than other metrics like frame-based measures.
- **Source**: Demonstrated by Ycart et al. 

## Modifications for Melody Transcription

### Octave Invariance
- **Adjustment for Practical Use**: The metric is modified to accommodate octave shifts, recognising that transcriptions might be adjusted in practice for readability or performance across different vocal ranges.
- **Calculation**:
  - $$ \max_{\sigma \in \mathbb{Z}} F1(\text{OctaveShift}(\text{Transcribe}(X), \sigma), y) $$
  - This allows the transcription to be evaluated in a way that is invariant to octave shifts, enhancing its utility in real-world applications.

### New Term
- **Octave-Invariant F1 Score**: Hereafter, we refer to this modified, octave-invariant metric as the F1 score.

This evaluation method ensures that the melody transcription not only accurately captures the notes from audio but also does so in a manner that aligns with how musicians and listeners perceive and use music transcriptions.
