---
layout: page
title: Scientific Abstract Topic Modeling
description: Utilizing machine learning to facilitate scientific literature review
img: /projects/1_nlp/lit-clustering.png
importance: 1
---


We are interested in using natural language processing to facilitate literature review. Below are interactive plots visualizing topic modeling on a collection of article abstracts pulled from [Microsoft Academic](https://academic.microsoft.com/home) related to energy storage.   The abstracts were obtained with the search term "Energy Storage", keeping the top 100000 results. Duplicate papers were removed (identified by DOI) and only articles in english were retained, resulting in approximately 40000 abstracts.



# Topic Modeling with Latent Dirichlet Allocation



Topic modeling was performed using Latent Diriclet Allocation (LDA) with [Gensim](https://radimrehurek.com/gensim/). LDA is an unsupervised machine learning technique to determine a set of topics that can represnt the modeled collection of texts (corpus). 

Each document is given a probability of being in each topic, where topics are probability distributions over words. This is a 'soft' clustering technique, in contrast to Kmeans (used previously) which assigns each document to just one cluster. This removes the nuance of papers that lie at the intersection between fields.

# Identifying Research Communities with Louvian Community detection

To understand the high level structure of the corpus I perform topic modeling with 80 topics, and calculate the probability that a given pair of topics are present together in the same paper. This co-occurence matrix defines the edges of a graph where the nodes are each topic. Research communities are then determined through the Louvian communitiy detection algorithm, as described in [Bickel (2019)](https://energsustainsoc.biomedcentral.com/articles/10.1186/s13705-019-0226-z).

The features of the plot indicate the following:

* Louvian communitiy: Marker Color
* Probabiity of the inter-topic co-occurence: Edge Thickness
* Overall probability of the topic: Marker Size
* Probability of the topic over the past 5 years: Opacity 

<div class="row" style="width:100%">
  <embed type="text/html" src="es_network.html" style="width:100%" height=1250> 
</div>



# Per-paper Topic Distribution Visualization with t-SNE

The plot below goes further and visualizes the topic distributions of each individual paper. To be able to visualize the topics, the number of topics is reduced 

Below is a visualization of the topic modeling of the corpus. First, the texts are represented as points on a 2D surface using t-Distributed Stochastic Neighbor Embedding (t-SNE). The topic distribution for each paper is visualized by representing each paper as a pie chart. Each slice represents a topic, and the fractional size (angle) of each slice represents the probability of that topic. Only the top 3 topics for each paper are inclused (resulting in an incomplete pie chart) for the sake of graphics processing. 



![](wedge_example.png)  



The top words for each topic are indicated in the legend (see next visualization to explore the topic words in more detail). The topics in the legend are sorted by the number of papers that have that topic as their most probable topic.

To use the plot, mouse over each item to get information about the paper. Papers can be clicked to open up the articles web page (you will have to allow popups). Use the tools on the right to move around, and note the 'refresh' button to reset the graph. Topics can be hidden by clicking on the topic color in the legend.



<div class="row" style="width:100%">
  <embed type="text/html" src="wedgeplot.html" style="width:100%" height=950> 
</div>

# Topic Visualization with pyLDAvis 


  Below is the visualization of the LDA model using [pyLDAvis](https://github.com/bmabey/pyLDAvis). The graph on the left using Principal Component Analysis to visualize the topics in 2D, similar to TSNE. The dashboard on the right is useful for exploring the words associated with each topic. Slide the relevance metric to about 0.5 to get words more specific to each topic. 


<div class="row" style="width:100%">
<embed type="text/html" src="lda_model.html" style="width:100%" height=900> 
</div>

