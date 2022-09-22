![](https://i.imgur.com/0y2WqLA.png)

### GenomeToGene ver 1.2 beta    
##### Aug 2022
##### A friendly tool for extracting genes from a GenBank genome.

###### by Vitor Miranda & Saura Rodrigues Silva
###### [UNESP - São Paulo State University](http://www.fcav.unesp.br/vmiranda), Brazil, campus Jaboticabal 
##### e-mail: vitor.miranda@unesp.br
##

#### Usage:

Firstly, we need to edit the script *GenomeToGene_v1.2.py* using any text editor (Notepad++, Komodo, etc.).
Search the "Vars definition" body, at the top of the text, and adjust the variables:

##### Entrez.email = "vitor.miranda@unesp.br"
Include your email to be identified by the NCBI. The email address will be used only to contact developers if NCBI observes any request that violate the policies. For more detailed information, I suggest you to verify: [Entrez Programming Utilities Help [Internet]](https://www.ncbi.nlm.nih.gov/books/NBK25497/).

##### gene_term_ = 'rbcL'
Inform in this variable the gene (rbcL, matK, atp6, etc.) or any sequence (intergenic spacer, intron, etc.) to be searched in retrieved genomes.

##### organism_term_ = 'Lentibulariaceae'
Inform in *organism_term_* the name of the organism or group of organism (taxon). For instance, a name of genus (*Utricularia*), family (*Lentibulariaceae*) or a broader group (*Viridiplantae*) can be informed as a target. 

##### genome_term_ = 'chloroplast'
Type of genome to be search: chloroplast, mithocondrion.

##### Max_hits_NCBI = '100'
Maximum number of hit to be retrieved from NCBI.

With the variables set, it is possible to run using a single command line:

> python GenomeToGene_v1.2.py 

With the variables set as the example, three output files will be resulted:

## *genomes_Lentibulariaceae.gb* (GenBank format)

Store all genomes (limited to *Max_hits_NCBI*) retrieved.  

## *DNA_Lentibulariaceae_rbcL.fas* (FASTA format)

Store all DNA sequences found in genomes retrieved (the search is from the .gb file).

## *CDS_Lentibulariaceae_rbcL.fas* (FASTA format)

Store all CDS sequences found in genomes retrieved (the search is from the .gb file).

##
If you have any question, contact the authors.

##### Vitor Miranda and Saura Rodrigues Silva
