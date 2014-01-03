BNPathologies
=============

Building a Bayesian model of leukemia pathologies.

## Problem

* Genes are responsible for protein synthesis in living cells.
* Genes interact with each other forming complex gene-networks.
* The behaviour of genes in a certain cell can indicate the presence of a certain pathology.
* Discovering interactions among genes which correlate with a pathology can help elucidating its characteristics

## Data

* The expression level (i.e. amount of proteins synthesized in a certain time) of genes can be measured by DNA microarrays.
* Expression level of genes from pathological cells are often measured relative to healthy cells (the control).
* The leukemia dataset consists of expression levels for 5147 genes in 72 patients: 47 affected by acute lymphoblastic leukemia (ALL), 25 by acute myeloid leukemia (AML).

## Task

* Expression levels depend strongly on the gene considered ⇒ need to be normalized
* Use information gain (see decision tree lesson) to choose the best threshold for binarizing each gene (classes are ALL vs AML). Can be iteratively applied to discretize in more than two values.
* Most of the genes will probably be uncorrelated with the pathologies ⇒ uninformative features.
* Perform feature selection on genes according to their information gain, choosing a small subset of the best genes when sorted by infogain (max. 50 genes).
* Once discretized, build a Bayesian network modeling the data.
* Split the dataset into a training and a test set (e.g. 80/20), keeping the same proportion of ALL and AML in both sets.
* Learn structure and parameters of the Bayesian network on the training set
* Evaluate performance of the learned network on the test set.
* Compare different networks:
	1. hugin-lite structure learning (statistical-test based)
	2. b-course structure learning (score based)
	3. naive bayes classifier (simple fixed structure)
