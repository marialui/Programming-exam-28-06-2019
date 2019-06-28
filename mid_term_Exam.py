file = 'gff3_insulin.gff'
#build a dictionary in which the keys are the uniprot IDS and
#values are the glycosilation site lists
dizionario = {}
with open(file) as source:
    for i in source:
        if 'Glycosylation' not in i: continue
        i = i.split() #if Glycosylation is in line, split it and take the corrispondent value
        values = [x for x in i[3:7] if not x.startswith(".")]
#        print i[0],values
        if dizionario.get(i[0]) == None:
            dizionario[i[0]] = values
        else:
            dizionario[i[0]] += values
for i in dizionario:
    dizionario[i] = list(set(dizionario[i]))
    print (i,dizionario[i])



#put in a list all the protein that have the signal peptide
signal_peptide = []
with open(file) as source:
    for i in source:
        if 'Signal peptide' not in i: continue
        i = i.split()
        signal_peptide.append(i[0])
print ('the Uniprot IDs of the proteins with the  signal peptide are: %s' %signal_peptide)



# write in a file (named secondary_structure.tab) the information related to secondary structure (Helix, Beta strand, Turn) and their starting position
with open("secondary_structure.tab", "w") as output:
    with open(file) as source:
        for i in source:
            if 'Helix' in i:
                i = i.split()
                string = str(i[0]+"\t"+i[2]+"\t"+i[3]+"\n")
                output.write(string)
            if "Beta strand" in i:
                i = i.split()
                string = str(i[0]+"\t"+i[2]+" "+i[3]+"\t"+i[4]+"\n")
                output.write(string)