![](https://i.imgur.com/0y2WqLA.png)

### GenomeToGene ver 1.2 beta    
##### Aug 2022
##### A friendly tool for extracting genes from a GenBank genome.

###### by Vitor Miranda & Saura Rodrigues Silva
###### [UNESP - São Paulo State University](http://www.fcav.unesp.br/vmiranda), Brazil, campus Jaboticabal 
##### e-mail: vitor.miranda@unesp.br
##

##### Usage:

Firstly, we need to edit the script *GenomeToGene_v1.2.py* using any text editor (Notepad++, Komodo, etc.).
Search the "Vars definition" body, at the top of the text, and adjust the variables:

### Entrez.email = "vitor.miranda@unesp.br"
Include your email to be identified by the NCBI. The email address will be used only to contact developers if NCBI observes any request that violate the policies. For more detailed information, I suggest you to verify: [Entrez Programming Utilities Help [Internet]](https://www.ncbi.nlm.nih.gov/books/NBK25497/).

### gene_term_ = 'rbcL'

### organism_term_ = 'Lentibulariaceae'


### genome_term_ = 'chloroplast'

### Max_hits_NCBI = '100'




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
