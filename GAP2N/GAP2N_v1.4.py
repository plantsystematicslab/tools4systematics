import sys
import Bio
import warnings

from Bio import SeqIO
from Bio.Seq import Seq

warnings.filterwarnings("ignore") 
  ## warnings will be ignored

############## Apresentação do ShiftGAP ################
print("GAP2N ver 1.4 beta  Sep 2022")
print("A quick and efficient way to correct the alignment.")
print("This tool will shift the terminal false GAPs '-' to 'N'.")
print("by Vitor Miranda & Saura Rodrigues Silva")
print("UNESP - São Paulo State University, campus Jaboticabal, Brazil")
print("e-mail: vitor.miranda@unesp.br")
print()
########################################################

########## Caso não tenha sido informato o INFILE #######
if len(sys.argv)==1:
       print("Usage:  python GAP2N_1.4 infile ")
       print("infile = input file in FASTA")
       print()
       sys.exit()
#########################################################
       

File_In=sys.argv[1]         # Arquivo de entrada FASTA


File_Out=File_In+".out.fas"     # Arquivo de saída FASTA
Extreme_GAP="N"             # Os GAPs de extremidades serão substituidos por essa var

records = list(SeqIO.parse(File_In, "fasta"))

print("*** Reading",len(records),"FASTA sequences: ")
print("*** The sequences have",len(records[0].seq),"base pairs")
print()

############## Percorre sequência por sequência ######
i=0
while (i<len(records)):
      # print(records[i].id,records[i].seq)
       mutable_records = records[i].seq.tomutable()

       ####### Localiza os GAPs falsos da extremidade da ESQUERDA ######
       ####### e substitui por Extreme_GAP ("N") #######################
       j=0
       while (records[i].seq[j]=="-"):
              mutable_records[j]=Extreme_GAP
              j+=1
       records[i].seq=Seq(str(mutable_records))
       #################################################################

       ####### Localiza os GAPs falsos da extremidade da DIREITA #######
       ####### e substitui por Extreme_GAP ("N") #######################
       j=1
       while (records[i].seq[-j]=="-"):
              mutable_records[-j]=Extreme_GAP
              j+=1
       records[i].seq=Seq(str(mutable_records))
       #################################################################
       i+=1
       
#######################################################       
       
print("All initial and terminal GAPs will be replaced by 'N' ")
print()
print("*** Correcting sequences: ")
print()
i=0

while (i<len(records)):
       print(records[i].id,"...   Corrected!")
       i+=1
       
############### Salva seqs corrigidas no output file ##########
fd = open(File_Out, "w")
SeqIO.write(records, fd, "fasta")
fd.close()
###############################################################

print()
print("The", len(records), "corrected sequences were saved in "+ File_Out + ".")

