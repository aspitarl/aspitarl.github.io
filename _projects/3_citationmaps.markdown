---
layout: page
title: Building citation maps
description: Using the semantic scholar research corpus citation data to form corpora for NLP
img: /projects/1_nlp/lit-clustering.png
importance: 1
---

<!-- [test](/projects/1_nlp) -->

<!-- https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab -->


<details>
<summary> Here I outline code that builds citation networks from a seed corpus to obtain a full corpus for topic modeling.</summary>
<p>
<br>
* One of the main challenes I've encountered in natural language processing of scientific literature is how to get a representative collection of articles. Searching for articles that have a given term (e.g. carbon nanotube) might miss relevant articles that just don't happen to use that word. To solve this problem I've been experimenting with building citation networks from the semantic scholar open research corpus. 
</p>
</details>

<br>

[See the repository here](https://github.com/aspitarl/NLP-Semantic) for the codes used to generate the plots below and more information about the dataset used. 


# Citation network for "Geographic imaging system"

### Citation growth algorithm

<figure>
<img src="cit_tree_rounds.png"/>
<figcaption style="text-align: center;font-style: italic;">This shows the citation network building through one algorithm. First the initial citation network is formed by searching for "geographic imaging system", then the largest connected graph is kept, and the graph is trimmed to keep the 300 most connected papers. Then, citations in and out for each of these papers are found and the graph is trimmed again. This process (Growth rounds) is repeated with the trimming allowing for more and more overall papers, finishing at 10k papers.</figcaption>
</figure>

### Resulting final literature dataset (~10000 abstracts)

Below is the final dataset of papers with the growth round indicated by the color. 

<div style="text-align:center;">
  <embed type="text/html" src="cit_tree_bokeh.html" style="width:100%; height:100vh" > 
</div>

## Topic modeling on resulting literature dataset

Then on this final collection of papers, topic modeling is performed with a [Correlation Explanation](https://github.com/gregversteeg/corex_topic) topic model with 50 topics.  

### Hot topics

<figure>
<img src="top_slopes_plot.png"/>
<figcaption style="text-align: center;font-style: italic;">This show the top 10 topics as determined by the CorEx topic model, ranked by the slope of the topic probability over the past 5 years (i.e. how 'hot' the topic is)</figcaption>
</figure>

### Interactive topic visualization

Below is an interactive visualization of the topic model. This visualization was developed as part of the MLEF 2021 program and is described further [here](https://mlef-energy-storage.github.io/). 

<div class="row" style="width:100%">
  <embed type="text/html" src="ES_networkplot.html" style="width:100%; height:2000px"> 
</div>

