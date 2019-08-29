class X():
   
   from definition_file import Y
   read_file_pass=Y.read_file_pass

   import glob
   print(print(read_file_pass))
   data1=glob.glob(r'{}/*.txt'.format(read_file_pass))
   data2=glob.glob(r'{}/*.fasta'.format(read_file_pass))

   result_file_pass=Y.result_file_pass

   print("txt file: "+str(len(data1)))
   print("fasta file:"+str(len(data2)))
   print("========START========")

#definition_file.py
   from definition_file import Y

#input_data_storage_file.py
   from input_data_storage_file import Data_Storage
   input_name=Data_Storage.input_name
   input_element=Data_Storage.input_element


# Run finding primary element,for example:Alu elements(AluSc,AluJb and so on)     
   p=0
   r=0
   v=0
   for p in range(len(data1)):
      f1=open(data1[p],"r")
      name=f1.readline()
      sequence=f1.read()
      print(data1[p])
      print(name)
      print(str(len(sequence))+"bp")
      print(sequence[0:35])
      print("-----------------")
      sequence=sequence.replace("N", "").replace(" ", "") 
      print("\n")

      print("=================START=================")

      class_Main=Y()
      class_Main.mkfile(name[5:40],sequence)
      class_Main.Input_find(sequence)
      print("===============continue==============")
      p=p+1
   else:
      pass
      
      



   q=0  
   u=0
   w=0
   for q in range(len(data2)):
      f2=open(data2[q],"r")
      name=f2.readline()
      sequence=f2.read()
      print(data2[q])
      print(name)
      print(str(len(sequence))+"bp")
      print(sequence[0:35])
      print("-----------------")
      sequence=sequence.replace("N", "").replace(" ", "").replace("\n", "") 
      print("\n")

      print("=================START=================")

      class_Main=Y()
      class_Main.mkfile(name[1:40],sequence)
      class_Main.Input_find(sequence)
      print("===============continue==============")
      q=q+1
   else:
      pass




  
   print("========END========")
