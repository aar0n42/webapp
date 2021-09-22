from flask import Flask
import pymongo
import os
import socket
from pymongo import MongoClient

client = MongoClient('mongodb://172.17.0.3:27017')

app = Flask(__name__)

@app.route("/")
def hello():
    db = client.company
    people = db.people
    people_data = {
        'name' : 'Erika',
        'lastname' : 'Mustermann'
    }

    result = people.insert_one(people_data)

    inserted_id = result.inserted_id
    
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Data BS inserted ID:</b> {inserted_id} "
           
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), inserted_id=inserted_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
