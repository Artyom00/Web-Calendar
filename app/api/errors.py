from . import api


@api.errorhandler(404)
def event_not_found(error):
    return dict(message="The event doesn't exist!"), 404
