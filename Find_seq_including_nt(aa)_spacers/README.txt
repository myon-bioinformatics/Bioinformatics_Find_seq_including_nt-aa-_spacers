"The three py file(definition_file, input_data_storage_file,main_file) must exist in the same directory"


//definition_file.py
"You don't need to append or rewrite this code source."
This file is the definition file for making a decision of the region including spacer sequences.
This file makes a decision for CORDENCE, DISCORDENCE et...    #CORDENCE(front,back) or DISCORDENCE(front, expected back; expected front,back)
the every result(CORDENCE,DISCORDENCE) is saved at xlsx file.



----------------EXAMPLE(Anaconda prompt)---------------------------
=================START=================
in AGGTTG turn for AluS_family-ERE
element is AGGTTG/nnn/TGAGCC


in AGGCTG turn for AluJb-ERE
element is AGGCTG/nnn/TGAGCC
-------------------------------------------
--------------EXAMPLE(/Anaconda prompt)----------------------------


//input_data_storage_file.py
"You must append the data about the region including spacer sequences."
Example data1; front1:AGGTTG, back1:TGAGCC, spacer number1:3, name:AluS family-ERE
Example data2; front2:AGCCTG, back2:TGAGCC, spacer number2:3, name:AluJb-ERE
-------------input_data_storage_file.py-----------------------------------------
input_element=[["AGGTTG,"TGAGCC"],[,]]     #[[front1, back1],[front2, back2]]
input_spacer_number=[3,3]
input_name=["AluS family-ERE","AluJb-ERE"]  #name1,name2
count_name=["polyA(10bp)","GC(n repeats)"]
count_elements=["AAAAAAAAAA","GCGCGCGCGCGCGC"]
------------------/input_data_storage_file.py-----------------------------------------------------------------



//main_file.py
"You must excecute this file."
You must input the file pass twice.
#"Input the file pass including the read sequence .txt or .fasta files>"  #read_file_pass
#"Input the file pass for saving result .xlsx files>"  #result_file_pass
example:C:\User\spSeq    NG:"C:\User\spSeq"(=without " ",' ')

Every txt or fasta file in read file_pass is read, and get name ,sequence.
--------------EXAMPLE(Anaconda prompt)--------------
C:\Users\YOSHUN MYOMOTO\Desktop\read Nucleotide Sequence\NC_000002.12 chromosome 2 primary assembly.fasta
>NC_000002.12 Homo sapiens chromosome 2, GRCh38.p12 Primary Assembly

244008146bp
-----------------EXAMPLE(/Anaconda prompt)--------------------------------






