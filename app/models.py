from . import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Events> {self.event}'
