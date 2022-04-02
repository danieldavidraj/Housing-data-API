from flaskr import app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app.config['MONGO_URI'] = config['PROD']['DB_URI']

    app.run()