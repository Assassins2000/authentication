import yaml
import os
import sys

class DataBaseConfig:
    _host: str = None
    _port: int = None
    _db: str = None
    _user: str = None
    _password: str = None
    _engine: str = 'django.db.backends.postgresql'

    def __init__(self, dbSettings):
        self._host = dbSettings['host']
        self._port = dbSettings['port']
        self._db = dbSettings['port']
        self._user = dbSettings['user']
        self._password = dbSettings['password']



    def getObjectSettings(self):
        return {
            "ENGINE": self._engine,
            "NAME": self.db,
            "USER": self._user,
            "PASSWORD": self._password,
            "HOST": self._host,
            "PORT": self._port 
        }

class SettingsParser:
    _read_data = {}

    def __init__(self) -> None:
        print(os.listdir())
        with open('config.yaml') as config:
           self._read_data = yaml.load(config, Loader=yaml.FullLoader)

    def getData(self):
        return {
            "db": DataBaseConfig(self._read_data["config"]["database"]),
            "secretKey": self._read_data["config"]["secretKey"]
        }