from sqlite3 import Connection
from typing import  Dict,List,Tuple

class ParticipantsRepository:
    def __init__(self,conn: Connection) -> None: #construtor de classe
        self.__conn = conn #conn -> uma instancia de Connection
    
    def registry_participants(self, participant_infos: Dict) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO participants
                (id, trip_id, emails_to_invite_id, name)
            VALUES
                (?,?,?,?)
            ''',(
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"],
            )
        )
        
        self.__conn.commit()
        
    
    def find_participants_from_trip(self, trip_id:str)->List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            #relacionando a tabela de emails_to_invite com a tabela de participantes
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                FROM participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id 
                WHERE p.trip_id =?
                
            ''',(trip_id,)
        )
        
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, participant_id:str) ->None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                    SET is_confirmed = 1
                WHERE id = ?
            '''
        )
        self.__conn.commit()

#criar os arquivos de teste para cada função