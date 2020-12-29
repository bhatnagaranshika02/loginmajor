from flask import Flask,jsonify,request,render_template
app=Flask('__main__')


class users:
	def __init__ (self,user_id,email,username,password):
		self.id = id
		self.email = email
		self.username = username
		self.password= password


class score:
	def __init__ (self,test_id,user_id,score):
		self.test_id = test_id
		self.user_id = user_id
		self.score = score

	def __lt__ (self,other):
		return self.score<other.score

users_list = dict()
score_list = dict()

@app.route('/login',methods= ['GET','POST'])
def login():
	if request.method == "GET":
		return render_template("login.html")
	username = request.form["username"]
	password = request.form["password"]
	if username in users_list:
		if password == users_list[username].password:
			return jsonify("user valid")
		else:
			return jsonify("password wrong.")
	else:
		return jsonify("user not register")


@app.route('/logout',methods=['GET'])
def logout():
	pass

@app.route('/register',methods=['POST','GET'])
def register():
	if request.method == 'GET':
		return render_template("signup.html")

	email = request.form["email"]
	username = request.form["username"]
	password = request.form["password"]
	user = str(len(users_list)+1)
	if username not in users_list:
		obj = users(1,'bhatnagaranshika02@gmail.com','anshi02','Anshika@123')
		users_list[username] = obj
	else:
		return "<center>User already exist. <a href='login.html'>go back</a></center>"
	return render_template("login.html")


@app.route('/submit_score',methods=['POST'])
def submit_score():
	user_id = request.form["user_id"]
	test_id = request.form["test_id"]
	score = request.form["score"]

	obj2 = score('001','1',4)
	score_list[user_id] = obj2
	return True

@app.route('/forgotpassword',methods=['POST','GET'])
def forgotpassword():
	if request.method == "GET":
		return render_template("forgotpassword.html")
	username = request.form["username"]
	password = request.form["password"]
	confirmpass = request.form["confirmpass"]
	if username in users_list:
		if password == confirmpass:
			users_list[username].password = password
		else:
			return "password not matched."
	else:
		return "username doesnt exist"

	return render_template("login.html")
	
def score_serializer(obj):
	return{ 
		'user_id' : obj.user_id,
		'test_id' : obj.test_id,
		'score' : obj.score
		}

@app.route('/scoreboard',methods=['GET'])
def scoreboard():
	score_list['1']= [score("1","1",5),score("1",'2',3),score('1','6',4)]
	scores = score_list["1"]
	scores.sort()
	scores = list(map(score_serializer,scores))
	return jsonify(scores)

@app.route('/aboutus',methods=['GET','POST'])
def abputus():
	return render_template("aboutus.html")

	

app.run(debug=True)