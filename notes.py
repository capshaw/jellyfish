from flask import (redirect, session, Blueprint, render_template, request)
import pymongo
import datetime

from configuration import *
from util import *

notes_api = Blueprint('notes_api', __name__)

# POSTs a new note to the server.
# TODO: authentication
@notes_api.route('/notes/', methods=['POST'])
def post_note():
    try:
        content = request.json['content']
        title = request.json['title']
    except ValueError:
        return jsonify({}) # TODO: invalid access exception

    table = pymongo.MongoClient()[DB_NAME][NOTES_TABLE_NAME]
    note = {
        "content": content,
        "title": title,
        "date": datetime.datetime.now()
    }
    table.insert(note)
    return jsonify({})

# DELETE a note by id
# TODO: Authentication
@notes_api.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
    table = pymongo.MongoClient()[DB_NAME][NOTES_TABLE_NAME]
    table.remove({
        "_id": ObjectId(id)
    })
    return jsonify({})

# GETs all notes on the server. Not efficient, but hey.
@notes_api.route('/notes/', methods=['GET'])
def get_notes():
    table = pymongo.MongoClient()[DB_NAME][NOTES_TABLE_NAME]
    notes = {
        "notes" : []
    }
    for note in table.find().sort('date', pymongo.DESCENDING):
        notes["notes"].append(note)
    return jsonify(notes)
