from pymongo import MongoClient
import json,csv

class Tokenizer:

	config = None
	db = None
	out_file = file("output.csv",'wt')
	csv_w = csv.writer(out_file)
	punc_list = ['.',',',':','(',')','&','|','-','@','#']

	def __init__(self,config,db):
		self.config = config
		self.db = db
		self.printResult(self.tokenize())

	def tokenize(self):
		tokens = dict()
		for tweet in db.tweets.find():
			for token in self.stripPunc(tweet["text"]).split(' '):
				token = token.lower()
				if self.checkIgnore(token): continue
				if tweet["handle"] in config["mute"]: continue 
				if(not tokens.has_key(token)):
					tokens[token] = 1
				else :
					tokens[token] = tokens[token] + 1
		return tokens

	def stripPunc(self,txt):
		for i in self.punc_list:
			txt = txt.replace(i,"")
		return txt

	def checkIgnore(self,txt):
		if len(txt) is 1 : return True
		if txt is " " : return True
		return False

	def printResult(self,tokens):
		csv = None
		valid_pr = db.tweets.count()*1/100
		print(("Total results collected for "+unicode(config['project-name'])+" = "+str(db.tweets.count())))
		self.csv_w.writerow(('Total',str(db.tweets.count())))
		print("Passing Tolerence = "+str(valid_pr))
		self.csv_w.writerow(('Tolerence',str(valid_pr)))
		self.csv_w.writerow(('Token','Occurrence'))
		for t in sorted(tokens, key=tokens.get, reverse = True):
			if tokens[t] > valid_pr:
				print(unicode(t) + "\t\t==>\t"+ unicode(tokens[t]))
				try:
					self.csv_w.writerow((unicode(t) ,unicode(tokens[t])))
				except:
					pass
		self.out_file.close()


if __name__ == '__main__':
    config = None
    client = None
    try:
        config = json.loads(open("config.json").read())
    except:
        print("Config loading/parsing failed")
        exit()
    try:
        client = MongoClient()
    except:
        print("database connection error")
        exit()

    db = client[config["project-name"]]
    tk = Tokenizer(config,db)
