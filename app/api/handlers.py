from datetime import date

from flask import request
from flask.views import MethodView
from marshmallow import ValidationError

from .. import db
from ..models import Events
from ..schema import EventSchema


class GetEventForToday(MethodView):
    def get(self):
        events_for_today = Events.query.filter_by(date=date.today()).all()

        if not events_for_today:
            return dict(message='There are no events for today!'), 404

        return dict(events=EventSchema(many=True).dump(events_for_today))


class EventHandler(MethodView):
    def get(self):
        if not request.args:
            return dict(events=EventSchema(many=True).dump(Events.query.all()))

        if all([request.args.get('start_time'), request.args.get('end_time')]):
            events = Events.query.filter(Events.date.between(
                request.args['start_time'], request.args['end_time'])).all()

            if not events:
                return dict(
                    message='There are no events matching the range!'), 404

            return dict(events=EventSchema(many=True).dump(events))

        return dict(message='You must specify both start_time and end_time' 
            ' parameters to select a range.'), 400

    def post(self):
        try:
            event_obj = EventSchema().load(request.form)
        except ValidationError as err:
            return err.messages, 400

        db.session.add(event_obj)
        db.session.commit()

        return dict(
            message="The event has been added!",
            event=request.form['event'],
            date=request.form['date']
        ), 201


class EventHandlerById(MethodView):
    def get(self, event_id: int):
        event = Events.query.get_or_404(event_id)
        return dict(event=EventSchema().dump(event))

    def delete(self, event_id: int):
        event = Events.query.get_or_404(event_id)

        db.session.delete(event)
        db.session.commit()

        return dict(message='The event has been deleted!')

    def put(self, event_id: int):
        try:
            updated_event = EventSchema().load(request.form,
                                               session=db.session,
                                               instance=Events.query.get(
                                                   event_id),
                                               partial=True)
        except ValidationError as err:
            return err.messages, 400

        db.session.add(updated_event)
        db.session.commit()

        return dict(message='The event has been updated successfully!')
