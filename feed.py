import config
import database

from flask import (request, render_template, session, Blueprint, jsonify, g)
from sqlalchemy import desc
from models import Entry
from util import *
from math import ceil

feed_api = Blueprint('feed_api', __name__)

entries_per_page = 2

@feed_api.route('/feed/<int:user_id>', defaults={'page': 1}, methods=['GET'])
@feed_api.route('/feed/<int:user_id>/<int:page>', methods=['GET'])
def get_feed(user_id, page):

    if page < 1:
        return bad_request

    # Start with zero as offset.
    page -= 1

    query = Entry.query.filter_by(user_id=user_id).order_by(desc(Entry.id))
    total_pages = ceil(query.count() / (1.0 * entries_per_page))

    entries = query.limit(entries_per_page).offset(page * entries_per_page)
    entries = [e.serialize() for e in entries]
    entries.reverse()

    return jsonify({
        'page': page + 1,
        'total_pages': total_pages,
        'feed': entries
    })
