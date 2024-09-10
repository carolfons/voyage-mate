import pytest
import uuid 
from src.models.settings.db_connection_handler import db_connection_handler #gerenciador de conexão com o banco de dados
from .emails_to_invite_repository import EmailsToInviteRepository

#conectando com o banco de dados
db_connection_handler.connect()
trip_id = str(uuid.uuid4())


#função para testar o resgitro de emails no bd
@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    email_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id":trip_id,
        "email":"helloworld@gmail.com"
    }
    
    emails_to_invite_repository.registry_email(email_trips_infos)
    
#função teste para encontrar todos os emails de uma determinada viagem
@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print(emails)