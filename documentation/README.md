# WriteRight - Automated Essay Scoring System

<p align="center">
    <img src="../assets/logo.png" alt="Project logo">
</p>

## Introduction & Motivation

The computerized grading of essays by machine learning and natural language processing is known as Automated Essay Scoring (AES). The project's primary goal is to rate an essay from 1 to 10 based on a variety of criteria. The algorithm considers three primary factors: the quality of word and phrase usage (Statistical), the correctness of the grammar (Syntax), and the essay's coherence and depth (Semantics). This makes essay evaluations more interpretable and accurate, while also saving time for educational institutions and tests like the GRE.

## Background & Motivation

Inspired by the need for quick and free essay evaluations during GRE preparation, we developed our AES system. Although not perfect, it's a useful introduction to Natural Language Processing and Machine Learning.

In opting for traditional Machine Learning Techniques with handcrafted features, our goal was to enhance the interpretability of the AES system. Rather than employing more complex neural network architectures like LSTMs or CNNs, which might act as opaque models or black boxes, we deliberately chose model to be transparent. The objective is to empower users by providing a clear understanding of the scoring process, enabling them to identify specific areas for improvement.

## Overview

Taking inspiration from the work of ZhuoyueWang, as outlined in the <a href="https://github.com/ZhuoyueWang/AutomatedEssayScoring">GitHub repository</a>, we propose implementing a similar system. This solution operates in three distinct stages, mirroring the structure laid out by ZhuoyueWang:

* Statistical Analysis Stage:

    This stage involves an examination of the statistical metrics related to words, sentence and POS-Tags usage. By adopting a statistical approach, we aim to quantify language proficiency and evaluate the richness of vocabulary.

* Syntax Analysis:

    This stage primarily focues on finding errors such as spelling error. The goal is to identify and rectify grammatical errors, providing users with specific feedback on grammatical improvements.

* Semantics Analysis:

    The semantics analysis stage assesses the overall coherence and depth of the essay. The core idea behind this stage is to identify how relevant the given essay is to the topic.

## Project Workflow

<p align="center">
    <img src="../assets/flowchart.png" alt="Project logo">
</p>

Our Automated Essay Scoring (AES) system operates on a modular architecture, strategically divided into three distinct modules. Each module is designed to capture specific elements and features of the essay, contributing to a comprehensive and nuanced evaluation. The scoring process is orchestrated by assigning weights to the scores obtained from each module, culminating in the final assessment.

### Module I: Statistical Analysis

Statistical Analysis used Unsupervised Learning, by extracting following statistical features for each essay from the dataset:
* word count
* sentence count
* words per sentence count
* parts of speech tags frequency

```
for essay in essays:
        sentences = sent_tokenize(essay)
        num_sentences += len(sentences)

        words = word_tokenize(essay)
        tags = nltk.pos_tag(words)

        num_words += len(words)

        for tag in tags:
            if tag[1] in norm_pos_freq:
                norm_pos_freq[tag[1]] += 1
            else:
                norm_pos_freq[tag[1]] = 1
```

All these features, once extracted, are normalized by dividing them with total number of essays.

```
    norm_num_words = (int)(num_words / len(essays))
    norm_num_sentences = (int)(num_sentences / len(essays))
    norm_num_words_in_sentences = (int)(norm_num_words / norm_num_sentences)
```

We extract similar features from the user essay and calculate the variance of these features. Essentially, we penalize the essay on the basis on how far it is from normailzed values.

The way this penalty system works is that we assign a weight i.e. importance to each feature. The higher the weight, the more the essay is penalized for each deviation from the norm. In our implementation, we penalize twice for deviating from average number of words in a sentance compared to other features. The intuition behind this is that a user might use lesser words our lesser sentences in an essay, but the words per sentence might remain more consistent. Thus a user might get penalized more for writing shorter sentence or longer sentences, when compared to writing a longer essay. Even for POS-Tags, we penalize the essay more for deviating from the average frequency of certain major POS-Tags. A user might not use rarely used POS Tags 'PDT' or 'SYM', but tags such as 'NN' or 'VB' might be more common.

The formula we use is,

```
penalty_ratio = (num_words_penalty + num_sentences_penalty + 2*num_words_in_sentences_penalty + pos_penalty)/5
penalty_score = (penalty_ratio*10.0)
```