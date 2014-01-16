import config
import database

from flask import (request, render_template, session, Blueprint, jsonify, g)
from sqlalchemy import desc
from models import Entry
from util import *
from lib.cors import crossdomain

# The public feed API. In generally, a robust GET API that allows access to 
# users' entries.
feed_api = Blueprint('feed_api', __name__)

@feed_api.route('/feed/<int:user_id>/<int:page>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', 
             methods=['GET', 'OPTIONS'], 
             headers=['X-Requested-With', 'Content-Type', 'Origin'])
def get_feed(user_id, page):

    if page < 1:
        return bad_request

    # Lets us obtain the total count of all entries in this feed.
    # TODO: eventually only get PUBLIC entries
    base_query = Entry.query.filter_by(user_id=user_id).order_by(desc(Entry.id))

    entries, total_pages = paginate_helper(base_query, page)
    entries = [e.serialize() for e in entries]

    return jsonify({
        'page': page,
        'total_pages': total_pages,
        'feed': entries
    })