
import MySQLdb

class dbhandler():
	connection=None
	dbname='czconnolly'
	dbuser='czconnolly'
	dbpassword='ginger1993'

        def __init__(self):
	        if dbhandler.connection == None:
		        dbhandler.connection = MySQLdb.connect(db=dbhandler.dbname, \
user=dbhandler.dbuser, passwd=dbhandler.dbpassword)

	def cursor(self):
		return dbhandler.connection.cursor()

class gene():
	gene_symbol=''
	gene_title=''
	geneid=''
	probelist=[]
	exprlist={}
	hexpvalue=''
	dexpvalue=''
	

	def __init__(self,geneid): 
		self.geneid=geneid
		db=dbhandler()
		cursor=db.cursor()
		sql='select gene_title,gene_symbol from gene where geneid=%s'
			 #execute the sql command
		cursor.execute(sql,(geneid,))
			#query db. get result and populate class fields. 
		results=cursor.fetchone()
		self.gene_title=results[0]
		self.gene_symbol=results[1]		
	
		#print 'self.gene_title=%s,self.gene_symbol=%s'\
		#	(self.gene_title,self.gene_symbol)

		probesql='select probe_names from probe where geneid=%s'
		cursor.execute(probesql,(self.geneid,))
		resultlist=cursor.fetchall()
		for result in resultlist:
			self.probelist.append(result[0])
		
			
		exprsql='select expression,experiment,probe_names from joinedtables where geneid=%s'
		cursor.execute(exprsql,(self.geneid,))
		for result in cursor.fetchall():
			self.exprlist[result[1]]=result[0]
		

	def get_expressioncomparison(self,geneid):
	#gets the average gene expression for a gene in healthy samples and the average expression of that gene in disease like samples. 
		self.geneid=geneid
		db=dbhandler()
		cursor=db.cursor()
		hsql='select sum(expression)/count(expression) as average from joinedtables where geneid=%s and disease_state=Healthy'
		cursor.execute(hsql,(geneid))
		hresult=cursor.fetchone()
		self.hexpvalue=result[0]
		
		dsql='select sum(expression)/count(expression) as average from joinedtables where geneid=%s and disease_state=Alzheimers disease-like'
                cursor.execute(dsql,(geneid))
                dresult=cursor.fetchone()
                self.dexpvalue=result[0]
                


		#for result in expvalue:
		#	self.averageexp.append(result[0])
		#return expvalue


