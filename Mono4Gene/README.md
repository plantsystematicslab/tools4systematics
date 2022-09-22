![](https://i.imgur.com/0y2WqLA.png)

### Mono4Gene ver 1.1 beta      
##### Jul 2021
##### A procedure for testing the monophyly of a putative group over a set of gene trees.

###### by Vitor Miranda & Saura Rodrigues Silva
###### [UNESP - São Paulo State University](http://www.fcav.unesp.br/vmiranda), Brazil, campus Jaboticabal 
##### e-mail: vitor.miranda@unesp.br
##

#### Usage:

Firstly, we need to create a folder *gene_trees* in the same folder of this applicative. 
The gene trees to be tested have to be in different files: one file for each tree.
The tree files have to be in *Newick* format, as the example:

>(((A,B),(C,D)),E);

A, B, C, D and E are the terminals.

Copy all tree files to the *gene_trees* folder.

To run the applicative, type the command line:

> python Mono4Gene_v1.1. *tested_group*

##### tested_group
*tested_group* is a text file with the group to be examined in all trees (in the *gene_trees* folder). 
The *tested_group* file have to be in *Newick* format, as the example:

>(A,B);

Using this file, the applicative will search the group (A,B) in all present trees in folder *gene_trees* and chek if the group is *monophyletic* or *polyphyletic*. 

#### Output files

##### report.csv

##### indexed_report.csv



##
If you have any question, contact the authors.

##### Vitor Miranda and Saura Rodrigues Silva
