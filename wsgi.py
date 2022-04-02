from flaskr.main import create_app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['MONGO_URI'] = config['PROD']['DB_URI']

    app.run()