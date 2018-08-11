from flask import Flask
from flask_pymongo import PyMongo
app=Flask(__name__)
app.config['MONGO_DBNAME']='miti'
app.config['MONGO_URI']='mongodb://shayan:shayan123@ds111072.mlab.com:11072/miti'

mongo= PyMongo(app)
@app.route('/add')
def add():
    u=mongo.db.mycollection
    u.insert({'name':'shayan','language':'Python'})
    u.insert({'name':'hamza', 'language':'Ruby'})
    u.insert({'name':'sherry', 'language':'C++'})
    u.insert({'name':'faris', 'language':'php'})
    return 'Add Sucessfully'
@app.route('/find')
def find():
    u=mongo.db.mycollection
    shayan=u.find_one({'name':'shayan'})
    return 'You Found'+shayan['name']+'favorite language'+shayan['language']
@app.route('/update')
def update():
    u = mongo.db.mycollection
    Ali= u.find_one({'name': 'Ali'})
    Ali['language']='JavaScript'
    u.save()
    return 'Update Sucessfully'
@app.route('/delete')
def delete():
    u=mongo.db.mycollection
    faris =u.find_one({'name':'faris'})
    u.remove(faris)
    return 'Remove sucessfully'
if __name__=='__main__':
    app.run(debug=True,port=4040)