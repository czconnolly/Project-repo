#takes the raw data file and creates 4 text files that can each be loaded into a table in mySQL
#!/usr/bin/python

#Reads in the GDS4128 file and assigns the function to open the dataset a variable called fh.
infile='GDS4128'

fh = open(infile)

#Returns a list of lines in the file from the line '!dataset_table_begin'
line= fh.readline()
while line[:20] != '!dataset_table_begin':
    line=fh.readline()


header= fh.readline().strip()

#creates a dictionary for column names
colnames={}

#splits the string into a string array using \t to separate them 
index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#open our output files, one per table.
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')

#defines which columns are to go in each output file. For samples it is the 3rd header until the gene title header and they will be separated by '\t'
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

#creates a new row in the output files under the column names
def buildrow(row, fields):
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"
#creates the rows for the expression file, is slightly different because for each probe and experiment there are several gene expression values.
def build_expression(row, samples):
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
rows=0    
#writes the data to the files 
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))	
	rows=rows+1
    except:
	pass
#closes the created files after the data has been writen to them
genefile.close()
probefile.close()
expressionfile.close()

print '%s rows processed'%rows
    
