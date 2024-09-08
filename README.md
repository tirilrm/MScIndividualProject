# Individual Project - Tiril Ruud Mageli | MSc Computing | Imperial College London

## Project Overview
This repository contains the code and data for **Tiril Ruud Mageli's** Individual Project for the MSc Computing at Imperial College London.

### Introduction
The rapid development of **Small Modular Reactor (SMR)** technology calls for tools to assess the **technological maturity** of organisations in the sector. While empirical data is limited, a wealth of textual data exists, presenting an opportunity for analysis.

### Objective
This study explores the potential of using **Natural Language Processing (NLP)** techniques to construct **Knowledge Graphs (KGs)** from textual news media. The aim is to evaluate the technological maturity of selected SMR organisations by leveraging textual data.

## Methods
A corpus of news articles was collected from four distinct sources. The following NLP techniques were applied:
- **Named Entity Recognition (NER)** for entity extraction.
- **Relation Extraction (RE)** to identify relationships between entities.
- **Triplet construction** to build KGs for 20 SMR organisations.

The resulting KGs were subjected to:
- **Structural and semantic clustering** to identify patterns and gain insights into how the KGs varied across different organisations.

## Key Findings
Five key findings emerged from this study:
1. **Reflection of real-world truths**: The KGs accurately represented real-world relationships, demonstrating the effectiveness of small NLP models in extracting meaningful information.
2. **Clustering insights**: Simple clustering techniques uncovered meaningful patterns, grouping organisations into technological maturity clusters.
3. **Promising semantic clustering**: Semantic clustering yielded encouraging results, though further validation is required.
4. **Value of abundant data**: The wealth of online data underscores the potential of NLP techniques for extracting insights.
5. **Challenges in Relation Extraction (RE)**: Despite promising results, RE remains a challenging task that requires further refinement.

## Limitations
The study identified three main limitations:
1. **Explainability challenges**: Difficulties in interpreting the extracted data.
2. **RE performance constraints**: The performance of RE techniques still has room for improvement.
3. **Data biases**: Sampling and selection biases due to the corpus used.

## Future Work
To build on this research, future work should focus on:
- Expanding data sources and addressing bias mitigation.
- Improving the RE pipeline and optimising the KG creation process.
- Introducing innovative KG analysis methods and integrating temporal factors to assess how technological maturity evolves over time.
- Training models specifically for triplet extraction or leveraging large language models (LLMs) to enhance performance.

---

**Contact Information:**
- **Author**: Tiril Ruud Mageli
- **Institution**: Imperial College London
- **Project**: MSc Computing Individual Project
- **Email** tirilrm@gmail.com