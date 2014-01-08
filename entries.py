import config
import database

from flask import (request, render_template, session, Blueprint, jsonify, g)
from models import Entry
from util import *

entries_api = Blueprint('entries_api', __name__)

@entries_api.route('/entries', methods=['GET'])
@login_required
def get_entries():

    # Get all entries that the currently logged-in user has posted.
    user = session['user']
    entries = Entry.query.filter_by(user_id=user.id).all()

    return jsonify({ 'entries': [e.serialize() for e in entries]})

@entries_api.route('/entries', methods=['POST'])
@login_required
def post_new_entry():

    # Make sure that the request actually has content.
    if 'content' not in request.json:
        return bad_request

    content = request.json['content']

    # Save to the database and return content for confirmation.
    user = session['user']
    new_entry = Entry(user.id, content)

    database.db_session.add(new_entry)
    database.db_session.commit()

    return jsonify({ 'entry': new_entry.serialize() })


@entries_api.route('/entries/<id>', methods=['DELETE'])
@login_required
def delete_entry(id):

    entry = Entry.query.filter_by(id=id).first()

    if not entry:
        return bad_request

    database.db_session.delete(entry)
    database.db_session.commit();

    return empty_response