import mysqldb

class dbhandler():
	connection=none
	dbname='mydbase'
	dbuser='dbusername'
	dbpassword='dbpassword'

def_init_(self):
	if dbhandler.connection == none:
		dbhandler.connection = mysqldb.connect(db=dbhamdler.dbname, \
user=dbhandler.dbuser, passwd=dbhandler.dbpassword)

	def cursor(self):
	return dbhandler.connection.cursor()

class gene():
	gene_symbol=''
	gene_title=''
	geneid=''
	probelist=[]

	def_init_(self,geneid): #or gene symbol#
		self.gene_id=geneid
		db=dbhandler()
		cursor=db.cursor()
		sql='select gene_title, gene_symbol, geneid, from gene where gene_id=$s'
		cursor.execute(sql,(geneid,))

		#query db. get result and populate class fields. 

		result= cursor.fetchone()
		self.gene_title = result[0]
		self.gene_symbol = result[1]




#now fetch probes... probesql='select probeid from probe where gene id=$s

def get_probe(self,probe_names) :
                self.gene_names = probeID
                db=dbhandler()
                cursor=db.cursor()
                sql='select probe_names, from probe where gene_id=$s'
                cursor.execute(sql,(probe_names,))



#fill in blank!!!#

for result in cursor.fetchall():
self.probelist.append (result[0])

def get_expression(self,experiment):
                db=dbhandler()
                cursor=db.cursor()
                sql='select expression, from gene_expression where probe_names=$s'
                cursor.execute(sql,(expression,))

