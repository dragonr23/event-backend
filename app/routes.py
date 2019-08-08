from app import app, db
from flask import request, jsonify
from app.models import Event



# set index route to return nothing, just so no error occurs


@app.route('/')
def index():
    return ''

@app.route('/api/save', methods=['POST'])
def save():

    try:

        title = request.headers.get('title')
        day = request.headers.get('day')
        month = request.headers.get('month')
        year = request.headers.get('year')
        notes = request.headers.get('notes')

        #if any event is missing give back an error for a jsonify message


        if not day or not title or not month or not year or not notes:
            return jsonify({ 'error': 'Error #001: Invalid Parameters'})

        #all info is included, save the event

        event = Event(title=title, day=day, month=month, year=year, notes=notes)

        db.session.add(event)
        db.session.commit()

        return jsonify({ 'success': 'Saved Event'})
    except:
        return jsonify({ 'error': 'Error #002: Could not save event'})

@app.route('/api/retrieve', methods=['GET'])
def retrieve():
    try:
        day = request.headers.get('day')
        month = request.headers.get('month')
        year = request.headers.get('year')

        #year is required, day cannot be paired with year, otherwise return errors

        if not year:
            return jsonify({ 'error': 'Error #003: Year Parameter is Required'})
        elif day and not month:
            return jsonify({ 'error': 'Error #004: Month is reqired with day'})
        elif year and not month and not day:
            #get events for the entire Year

            results = Event.query.filter_by(year=year).all()


        elif year and month and not day:
            #get events for the month passed

            results = Event.query.filter_by(year=year, month=month).all()
        else:
            results = Event.query.filter_by(year=year, month=month, day=day).all()

        #if results is empty then there are no events
        if results == []:
            return jsonfiy({'success' : 'No events scheduled'})

        # loop over results because it is an instance of an event. Save information into new list and return

        parties = []

        for result in results:
            party = {
                'title': result.title,
                'day': result.day,
                'month': result.month,
                'year': result.year,
                'notes': result.notes,
                'event_id': result.event_id

            }

            parties.append(party)

        return jsonify({
            'success': 'Retrieved Events',
            'events': parties
            })
    except:
        return jsonify({ 'error':'Something went wrong!'})


@app.route('/api/delete', methods=['DELETE'])
def delete():
    try:
        event_id = request.headers.get('event_id')

        event = Event.query.filter_by(event_id=event_id).first()

        if not event:
            return jsonify({ 'error':'Event #005: Event does not exist'})


        title = event.title

        db.session.delete(event)
        db.session.commit()

        return jsonify({ 'success': f'Event "{title}" deleted.'})
    except:
        return jsonify({ 'error': 'Event #006:Invalid Parameters'})
