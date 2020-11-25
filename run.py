from app import create_app
import os

configuration_name = os.getenv('FLASK_CONFIG')
app = create_app(configuration_name)


if __name__ == '__main__':
    app.run()
