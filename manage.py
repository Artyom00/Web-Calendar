from flask_migrate import Migrate
from app import create_app, db
from app.models import Events

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
