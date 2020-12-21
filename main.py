from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/cs446"
mongo = PyMongo(app)

@app.route('/populate', methods=['POST'])
def populate():
    js = request.get_json()
    index = js["Index"]
    year = js["Year"]

    age = js["Age"]
    name = js["Name"]
    movie = js["Movie"]

    if index and year and age and name and movie and request.method == 'POST':
        id = mongo.db.oscars.insert({"Index": index, "Year": year, "Age": age, "Name": name, "Movie": movie})
        resp = jsonify('Data inserted succesfully into the database "cs446"...')
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/index', methods=['GET'])
def Index():
    requestedindex = request.json['Index']
    if requestedindex and request.method == 'GET':
        db = mongo.db.oscars.find()
        for i in db:
            for key,val in i.items():
                if key == "Index" or key == ' "Index"':
                    if requestedindex in val:
                        Index = key
                        requestedindex = val

        mv = mongo.db.oscars.find_one({Index : (requestedindex)})
        resp = dumps(mv)
        return resp

@app.route('/year', methods=['GET'])
def FindByYear():
    requestedyear = request.json['Year']
    if requestedyear and request.method == 'GET':
        db = mongo.db.oscars.find()
        for i in db:
            for key,val in i.items():
                if key == "Year" or key == ' "Year"':
                    if requestedyear in val:
                        Year = key
                        requestedyear = val

        mv = mongo.db.oscars.find_one({Year : (requestedyear)})
        resp = dumps(mv)
        return resp

@app.route('/age', methods=['GET'])
def FindByAge():
    requestedage = request.json['Age']
    if requestedage and request.method == 'GET':
        db = mongo.db.oscars.find()
        for i in db:
            for key,val in i.items():
                if key == "Age" or key == ' "Age"':
                    if requestedage in val:
                        Age = key
                        requestedage = val

        mv = mongo.db.oscars.find_one({Age : (requestedage)})
        resp = dumps(mv)
        return resp

@app.route('/name', methods=['GET'])
def FindByName():
    nameRequested = request.json['Name']
    if nameRequested and request.method == 'GET':
        nam = mongo.db.oscars.find()
        for i in nam:
            for key,val in i.items():
                if key == "Name" or key == ' "Name"':
                    if nameRequested in val:
                        Name = key
                        nameRequested = val

        nm = mongo.db.oscars.find_one({Name : (nameRequested)})
        resp = dumps(nm)
        return resp


@app.route('/movie', methods=['GET'])
def FindByMovie():
    movieRequested = request.json['Movie']
    if movieRequested and request.method == 'GET':
        mov = mongo.db.oscars.find()
        for i in mov:
            for key,val in i.items():
                if key == "Movie" or key == ' "Movie"':
                    if movieRequested in val:
                        Movie = key
                        movieRequested = val

        mv = mongo.db.oscars.find_one({Movie : (movieRequested)})
        resp = dumps(mv)
        return resp


@app.route('/movie/<requestedmovie>', methods=['GET'])
def movie(requestedmovie):
    mov = mongo.db.oscars.find()
    for i in mov:
        for key,val in i.items():
            if key == "Movie" or key == ' "Movie"':
                if requestedmovie in val:
                    Movie = key
                    requestedmovie = val

    movvie = mongo.db.oscars.find_one({Movie : (requestedmovie)})
    resp = dumps(movvie)
    return resp



if __name__ == '__main__':
    app.run(debug = True)
