from typing import Dict, Tuple, List
from sqlite3 import Connection #importando a classe connection do módulo sqlite3 para manipular dados relacionados a viagens


#classe projetada para funcionar como um repositório onde ira lidar com as operações do BD
class LinksRepository:
    def __init__(self,conn: Connection) -> None: #construtor de classe
        self.__conn = conn #conn -> uma instancia de Connection


#inserindo dados no banco
    def registry_links(self,links: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(

            '''
                INSERT INTO links 
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                links["id"],
                links["trip_id"],
                links["link"],
                links["title"]
            )
        )

        self.__conn.commit()
        
    def find_links_from_trip(self,trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,)
        )
        trip = cursor.fetchall()
        return trip