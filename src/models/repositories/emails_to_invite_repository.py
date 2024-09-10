from typing import Dict, Tuple, List
from sqlite3 import Connection #importando a classe connection do módulo sqlite3 para manipular dados relacionados a viagens

#classe projetada para funcionar como um repositório onde ira lidar com as operações do BD
class EmailsToInviteRepository:
    def __init__(self,conn: Connection) -> None: #construtor de classe
        self.__conn = conn #conn -> uma instancia de Connection

    #inserindo dados no banco
    def registry_email(self,email_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(

            '''
                INSERT INTO emails_to_invite 
                    (id, trip_id,email)
                VALUES
                    (?, ?, ?)
            ''', (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"]
            )
        )

        self.__conn.commit()

    def find_emails_from_trip(self,trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM emails_to_invite WHERE trip_id = ?''', (trip_id,)
        )
        trip = cursor.fetchall()
        return trip
    

