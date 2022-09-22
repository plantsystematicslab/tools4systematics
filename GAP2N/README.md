![](https://i.imgur.com/0y2WqLA.png)

### GAP2N ver 1.4 beta  
##### Sep 2022
##### A quick and efficient way to correct the alignment.
###### This tool will shift the terminal false GAPs '-' to 'N'.

###### by Vitor Miranda & Saura Rodrigues Silva
###### [UNESP - São Paulo State University](http://www.fcav.unesp.br/vmiranda), Brazil, campus Jaboticabal 
##### e-mail: vitor.miranda@unesp.br
##

##### Usage:

> python GAP2N_1.4 infile 

infile = input file in FASTA
##

Two files are available in the repository for tests:
rbcl10seqs.fas
rbcl1266seqs.fas

Both files contains sequences of (10 and 1266 sequences) rbcL chloroplast gene from GenBank.

Thus, you can run the tool using as described:

> python GAP2N_1.4 rbcL10seqs.fas

In this case, the file *rbcL10seqs.fas.out.fas* will be created with the 10 corrected sequences.

And using the 1266-sequences file:

> python GAP2N_1.4 rbcL10seqs.fas

In this case, the file *rbcL1266seqs.fas.out.fas* will be created with the 1,266 corrected sequences.

##
If you have any question, contact the authors.

##### Vitor Miranda and Saura Rodrigues Silva
