from flask import Flask, request
app = Flask(__name__)  

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='history'
mysql= MySQL(app)




@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/2010") 
def name():         
	return "The winner in 2010 was Germany"
@app.route("/2011") 
def 2011(): 
 return "The winner in 2011 was Azerbaijan" 
@app.route("/2012") 
def 2012(): 
 return "The winner in 2012 was Sweden"
if __name__ == "__main__":     
	app.run()