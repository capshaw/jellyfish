import config
import database

from flask import (request, render_template, session, Blueprint, jsonify, g)
from models import Entry
from util import *
from sqlalchemy import desc

# API for user-specific entry access.
entries_api = Blueprint('entries_api', __name__)

@entries_api.route('/entries/<int:id>', methods=['GET'])
@login_required
def get_entry(id):

    # Make sure the user has access to that entry.
    user_id = session['user_id']
    entry = Entry.query.filter_by(id=id).first()

    if not entry or entry.user_id != user_id:
        return not_authorized

    return jsonify({
        'entry': entry.serialize()
    })

# TODO: is this most RESTful route to use?
@entries_api.route('/entries/page:<int:page>', methods=['GET'])
@login_required
def get_entries_by_page(page):

    if page < 1:
        return bad_request

    user_id = session['user_id']
    base_query = Entry.query.filter_by(user_id=user_id).order_by(desc(Entry.id))

    entries, total_pages = paginate_helper(base_query, page)
    entries = [e.serialize() for e in entries]

    return jsonify({
        'page': page,
        'total_pages': total_pages,
        'entries': entries
    })

@entries_api.route('/entries/<int:id>', methods=['PUT'])
@login_required
def update_entry(id):

    # Make sure the user has access to that entry.
    user_id = session['user_id']
    entry = Entry.query.filter_by(id=id).first()

    if not entry or entry.user_id != user_id:
        return not_authorized

    # Make sure that the request actually has content.
    if 'content' not in request.json:
        return bad_request

    entry.content = request.json['content']
    database.db_session.commit()

    return jsonify({
        'entry': entry.serialize()
    })

@entries_api.route('/entries', methods=['POST'])
@login_required
def post_new_entry():

    # Make sure that the request actually has content.
    if 'content' not in request.json:
        return bad_request

    content = request.json['content']

    # Save to the database and return content for confirmation.
    user_id = session['user_id']
    new_entry = Entry(user_id, content)

    database.db_session.add(new_entry)
    database.db_session.commit()

    return jsonify({
        'entry': new_entry.serialize()
    })

@entries_api.route('/entries/<int:id>', methods=['DELETE'])
@login_required
def delete_entry(id):

    entry = Entry.query.filter_by(id=id).first()

    if not entry:
        return bad_request

    database.db_session.delete(entry)
    database.db_session.commit();

    return empty_response