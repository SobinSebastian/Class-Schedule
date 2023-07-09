from flask import *
from public import public
from admin import admin
from teacher import teacher

app=Flask(__name__)
app.secret_key="hello"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(teacher,url_prefix='/teacher')
app.run(debug=True,port=5056)
//sobin sebastian