#creates a connection to the mySQL database
import MySQLdb

class dbhandler():
	connection=None
	dbname='czconnolly'
	dbuser='czconnolly'
	dbpassword='ginger1993'

#if the connection is lost it will reconnect
        def __init__(self):
	        if dbhandler.connection == None:
		        dbhandler.connection = MySQLdb.connect(db=dbhandler.dbname, \
user=dbhandler.dbuser, passwd=dbhandler.dbpassword)

#creates a cursor to use in python. It allows the python code to execute SQL commands in a database session
	def cursor(self):
		return dbhandler.connection.cursor()

#creates the class gene and defines the class variables
class gene():
	gene_symbol=''
	gene_title=''
	geneid=''
	probelist=[]
	exprlist={}
	hexpvalue=''
	dexpvalue=''
	
#initialization method that python calls when you create a new instance of this class
	def __init__(self,geneid): 
		self.geneid=geneid
		db=dbhandler()
		cursor=db.cursor()
		sql='select gene_title,gene_symbol from gene where geneid=%s'
		#executes the sql command
		cursor.execute(sql,(geneid,))
		#query db. get result and populate class fields. 
		results=cursor.fetchone()
		self.gene_title=results[0]
		self.gene_symbol=results[1]		
	
		# fetches the probe names and creates a list of all the results
		probesql='select probe_names from probe where geneid=%s'
		cursor.execute(probesql,(self.geneid,))
		resultlist=cursor.fetchall()
		for result in resultlist:
			self.probelist.append(result[0])

		#fetches all the probe names and expression values for the gene for each experiment. not quite working yet			
		exprsql='select expression,experiment,probe_names from joinedtables where geneid=%s'
		cursor.execute(exprsql,(self.geneid,))
		for result in cursor.fetchall():
			self.exprlist[result[1]]=result[0]
		
	#defines a new method
	def get_expressioncomparison(self,geneid):
	#gets the average gene expression for a gene in healthy samples and the average expression of that gene in disease like samples. 
		self.geneid=geneid
		db=dbhandler()
		cursor=db.cursor()
		hsql='select sum(expression)/count(expression) as average from joinedtables where geneid=%s and disease_state=Healthy'
		cursor.execute(hsql,(self.geneid)) #queries db
		hresult=cursor.fetchone() #fetches the result
		self.hexpvalue=result[0] #populates hexpvalue with the result
		
		dsql='select sum(expression)/count(expression) as average from joinedtables where geneid=%s and disease_state=Alzheimers disease-like'
                cursor.execute(dsql,(self.geneid))
                dresult=cursor.fetchone()
                self.dexpvalue=result[0]
                



