from src.main import create_app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

print("name")
print(__name__)
if __name__ == "run":
    print("init")
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['LOCAL']['DB_URI']

    app.run()