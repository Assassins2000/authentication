import yaml
import os
import sys

from dataclasses import dataclass 

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
        self._db = dbSettings['db']
        self._user = dbSettings['user']
        self._password = dbSettings['password']



    def getObjectSettings(self):
        return {
            "ENGINE": self._engine,
            "NAME": self._db,
            "USER": self._user,
            "PASSWORD": self._password,
            "HOST": self._host,
            "PORT": self._port 
        }

class BaseSettingsException(Exception):
    def __init__(self, key, *args) -> None:
        super().__init__(*args)
        self.key = key

    def __str__(self):
        return f"Поле {self.key}. обязательное"

@dataclass
class Config:
    db: DataBaseConfig
    secret_key: str

class SettingsParser:
    _settings = {}

    def __init__(self) -> None:
        print(os.listdir())
        with open('config.yaml') as config:
           self._settings = yaml.load(config, Loader=yaml.FullLoader)

    def getData(self) -> Config:
        secret_key = self._settings.get('secret_key', None)
        if secret_key is None:
            raise BaseSettingsException('secret_key');
        return Config(db = DataBaseConfig(self._settings["database"]), secret_key = self._settings["secret_key"])
