# -*- coding: utf-8 -*-

from Bio import SeqIO
import os

from Bio import Entrez
from Bio import SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline 
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import time

##########################################
########### Vars definition ##############
Entrez.email = "vitor.miranda@unesp.br"
                                                    #### É importante sempre informar ao NCBI qm vc é

gene_term_ = 'rbcL'
                                                    #### gene alvo buscado em cada genoma
organism_term_ = 'Lentibulariaceae'
                                                    #### target organism 
                                          
genome_term_ = 'chloroplast'
                                                    #### target genome 

Max_hits_NCBI = '100'
                                                    #### max hits retrived from NCBI
##########################################                                                   
term_ = organism_term_ + "[Orgn] AND " + genome_term_ + " AND complete genome AND " + gene_term_+"[Gene]"
                                                    #### termo para busca de seqs no genbank, incluindo o gene alvo

File_Out = "genomes_"+ organism_term_ +".gb"
                                                    #### arquivo de saida gb dos hits do genbank

file_term = organism_term_ +'_'+ gene_term_
                                                    #### additional (putative) term to be included in the output files - use for your organization

output_file_name = "CDS_" + file_term + ".fas"
                                                    #### arquivo de saida do CDS encontrados no arquivo gb 
########### Vars definition ##############
##########################################

start_time = time.time()
            ##### register starting time 

############## Presentation ################
print("GenomeToGene ver 1.2 beta  Aug 2022")
print("A tool for extracting genes from a GenBank genome.") 
print("by Vitor Miranda & Saura Rodrigues Silva")
print("UNESP - São Paulo State University - Jaboticabal, Brazil")
print("e-mail: vitor.miranda@unesp.br\n\n")
############################################


#########################################################################
################## Busca as seqs no genbank #############################

handle = Entrez.esearch(db="nucleotide", term=term_, idtype="acc", retmax=Max_hits_NCBI)
record = Entrez.read(handle)

################## Busca as seqs no genbank #############################
#########################################################################

##########################################################################
#################### salva as seqs encontradas em arquivo gb #############
fd = open(File_Out, "w")

i_genomes_found = 0
print('Searching for the term: ' + term_ + ' in GenBank...\n')
print('Max hits: ' + Max_hits_NCBI,'\n')

with Entrez.efetch(
    db="nucleotide", rettype="gb", retmode="text", id=record["IdList"]
) as handle:
    for seq_record in SeqIO.parse(handle, "gb"):
        print("%s %s..." % (seq_record.id, seq_record.description[:85]))
        SeqIO.write(seq_record, fd, "gb")
        i_genomes_found += 1

fd.close()

print('Found ', i_genomes_found, ' genomes.\n')

#################### salva as seqs encontradas em arquivo gb #############
##########################################################################

#########################################################################################
####################### Localiza CDS nos genomas em formato gb ##########################

input_file = File_Out

i_CDS_found = 0

if not os.path.exists(output_file_name):
    for rec in SeqIO.parse(input_file, "gb"):
        acc = rec.annotations['accessions'][0] #Defines your accession numbers
        organism = rec.annotations['organism'] #defines your organism ID
        for feature in rec.features:
            for key, val in feature.qualifiers.items():
                if gene_term_ in val:
                    with open(output_file_name, "a") as ofile:
                        if 'translation' in feature.qualifiers:
                            record_ = ">" + acc +"|"+ organism +"|"+ str(feature.qualifiers['gene'][0])+"\n"+ str(feature.qualifiers['translation'][0])+"\n\n"
                            ofile.write(record_)
                            i_CDS_found += 1
else:
    print ("The output file already exists in the current working directory {0}. Please change the name of the output file.\n\n".format(os.getcwd()))                    

####################### Localiza CDS nos genomas em formato gb ##########################
#########################################################################################


###########################################################################################
############### Localiza genes nos genomas em formato gb e salva em FASTA##################

File_Out_FASTA = "DNA_" + file_term + ".fas"

i_DNA_found = 0

with open(File_Out_FASTA, 'w') as nfh:
    for rec in SeqIO.parse(File_Out, "genbank"):
            if rec.features:
                    for feature in rec.features:
                         for key, val in feature.qualifiers.items():
                            if gene_term_ in val:
                                if feature.type == "CDS":
                                        organism = rec.annotations['organism'] #defines your organism ID
                                        nfh.write(">%s|%s|%s from %s\n%s\n\n" % (
                                            organism,
                                              feature.qualifiers['gene'][0],
                                              feature.qualifiers['product'][0],
                                              rec.name,
                                              feature.location.extract(rec).seq))
                                        i_DNA_found += 1

############### Localiza genes nos genomas em formato gb e salva em FASTA##################
###########################################################################################


##########################################################
################### Summary results ######################

print('---------------------------------------------------------------------------\nSummary resuts\n---------------------------------------------------------------------------')
print (i_genomes_found, ' genomes found and exported to the file ', File_Out)
print (i_CDS_found, ' Aminoacid sequences (CDS) found and exported to the file ', output_file_name)
print (i_DNA_found, ' DNA sequences found and exported to file ', File_Out_FASTA)
print('Max hits limited to ' + Max_hits_NCBI,'\n')
end_time = time.time()
print("\nElapsed time: {0} sec".format(end_time - start_time))

################### Summary results ######################
##########################################################


# New versions:
#
# 1.1. 30/08/2021
# - ajustados os nomes dos arquivos de saida para incluirem file_term
#
# 1.2. 22/08/2022
# - realizados ajustes para tornar o aplicativo público
#
