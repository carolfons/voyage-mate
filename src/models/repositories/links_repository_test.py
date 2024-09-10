import pytest
import uuid 
from src.models.settings.db_connection_handler import db_connection_handler #gerenciador de conexão com o banco de dados
from .links_repository import LinksRepository


#conectando com o banco de dados
db_connection_handler.connect()
trip_id = str(uuid.uuid4())

#função para testar o resgitro de links no bd
#@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links_infos = {
            "id": str(uuid.uuid4()),
            "trip_id":trip_id,
            "link":"link test",
            "title":"link title"
    }
    
    links_repository.registry_links(links_infos)
    
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links = links_repository.find_links_from_trip(trip_id)
    print(links)