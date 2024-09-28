from sqlite3 import Connection
from typing import  Dict,List,Tuple

class ActivitiesRepository:
    def __init__(self,conn: Connection) -> None: #construtor de classe
        self.__conn = conn #conn -> uma instancia de Connection
        

    def registry_activity(self, activity_infos: Dict) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO activities
                (id, trip_id, title, occurs_at)
            VALUES
                (?,?,?,?)
            ''',(
                activity_infos["id"],
                activity_infos["trip_id"],
                activity_infos["title"],
                activity_infos["occurs_at"],
            )
        )
        
        self.__conn.commit()
        
    def find_activities_from_trip(self, trip_id:str)->List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            #relacionando a tabela de emails_to_invite com a tabela de participantes
            '''
                SELECT * FROM activities WHERE trip_id = ?
                
            ''',(trip_id,)
        )
        
        activities = cursor.fetchall()
        return activities