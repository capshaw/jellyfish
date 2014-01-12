import config
import database

from flask import (request, render_template, session, Blueprint, jsonify, g)
from sqlalchemy import desc
from models import Entry
from util import *
from math import ceil
from lib.cors import crossdomain

# The public feed API. In generally, a robust GET API that allows access to 
# users' entries.
feed_api = Blueprint('feed_api', __name__)

ENTRIES_PER_PAGE = 10

@feed_api.route('/feed/<int:user_id>/<int:page>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', 
             methods=['GET', 'OPTIONS'], 
             headers=['X-Requested-With', 'Content-Type', 'Origin'])
def get_feed(user_id, page):

    if page < 1:
        return bad_request

    # Lets us obtain the total count of all entries in this feed.
    base_query = Entry.query.filter_by(user_id=user_id).order_by(desc(Entry.id))

    # The programmatic offset is one less than the user-friendly page number.
    page -= 1

    entries = base_query.limit(ENTRIES_PER_PAGE).offset(page * ENTRIES_PER_PAGE)
    entries = [e.serialize() for e in entries]
    total_pages = ceil(base_query.count() / (1.0 * ENTRIES_PER_PAGE))

    return jsonify({
        'page': page + 1,
        'total_pages': total_pages,
        'feed': entries
    })