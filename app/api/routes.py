from .handlers import GetEventForToday, EventHandler, EventHandlerById
from . import api

api.add_url_rule('/event/today',
                 view_func=GetEventForToday.as_view('get_today_events'))
api.add_url_rule('/events', view_func=EventHandler.as_view('event_handler'))
api.add_url_rule('/event/<int:event_id>',
                 view_func=EventHandlerById.as_view('event_handler_by_id'))
