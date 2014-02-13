
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

	def __init__(self,geneid): 
		self.gene_id=geneid
		db=dbhandler()
		cursor=db.cursor()
		sql='select gene_title, gene_symbol, geneid from gene where geneid=%s'
		cursor.execute(sql,(geneid,))

		#query db. get result and populate class fields. 

		result= cursor.fetchone()
		self.gene_title = result[0]
		self.gene_symbol = result[1]
		
		probesql='select probe_names from probe where geneid=%s'
		cursor.execute(probesql,(self.gene_id,))
		for result in cursor.fetchall():
			self.probelist.append (result[0])
		return probelist
			

		exprsql='select expression,experiment from joinedtables where geneid=%s'
		cursor.execute(exprsql,(self.gene_id,))
		for result in cursor.fetchall():
			self.exprlist[result[1]]=result[0]
		return exprlist
