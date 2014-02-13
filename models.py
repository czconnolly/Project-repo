
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
		sql='select gene_title, gene_symbol from gene where geneid=%s'
			 #execute the sql command
		self.gene_id=geneid
		cursor.execute(sql,(gene_id,))
			#query db. get result and populate class fields. 
		result=cursor.fetchone()
		for answer in result:
				self.gene_title=answer[0]
				self.gene_symbol=answer[1]
			#now print fetched result
		return result


		#print 'self.gene_title=%s,self.gene_symbol=%s'\
		#			(gene_title,gene_symbol)
		#except: 
			#print 'Error fetching data' 










		#probesql='select probe_names from probe where geneid=%s'
		#cursor.execute(probesql,(self.gene_id,))
		#for result in cursor.fetchall():
		#	self.probelist.append (result[0])
		#return result
			
		#exprsql='select expression,experiment,probe_names from joinedtables where geneid=%s'
		#cursor.execute(exprsql,(self.gene_id,))
		#for result in cursor.fetchall():
		#	self.exprlist[result[1]]=result[0]
		#return result
