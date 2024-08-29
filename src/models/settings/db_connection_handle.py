import sqlite3 

class DbConnectionHandler:
    def __init__(self)->None:
        self.__connection_string = "storage.db"
        self.__conn = None
    
    def connect(self) -> None:
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)