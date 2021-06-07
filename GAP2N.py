import sys
import Bio
from Bio import SeqIO
from Bio.Seq import Seq


############## Apresentação do ShiftGAP ################
print("GAP2N ver 1 beta  Oct 2020")
print("A quick and efficient way to correct the alignment.")
print("by Vitor Miranda")
print("São Paulo State University - Jaboticabal, Brazil")
print("e-mail: vitor.miranda@unesp.br")
print()
########################################################


########## Caso não tenha sido informato o INFILE #######
if len(sys.argv)==1:
       print("Usage:  python INFILE ")
       print("INFILE = file in FASTA")
       print()
       sys.exit()
#########################################################
       

File_In=sys.argv[1]         # Arquivo de entrada FASTA


File_Out=File_In+".out"     # Arquivo de saída FASTA
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
       
print()
print("*** Corrected sequences: ")
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

