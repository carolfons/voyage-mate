#Testes utilizando o pytest
import pytest
import uuid 
from datetime import datetime, timedelta
from .trips_repository import TripsRepository  #importando o repositório de viagens
from src.models.settings.db_connection_handler import db_connection_handler #gerenciador de conexão com o banco de dados


db_connection_handler.connect() #estabelecendo conexão inicial com banco de dados
trip_id = str(uuid.uuid4()) #gerando um UUID único para ser usado com o ID da viagem

#função teste para criar uma nova viagem no banco de dados
@pytest.mark.skip(reason="interacao com o banco")
def test_create_trip():
    #conectando com o banco de dados
    conn = db_connection_handler.get_connection()
    #criando uma instancia do repositório de viagens usando a conexão
    trips_repository = TripsRepository(conn)

    # Definindo as informações da viagem, com um ID gerado anteriormente (trip_id)
    trips_infos = {
        "id":trip_id,
        "destination":"Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name":"Osvaldo",
        "owner_email":"osvaldo@gmail.com"
    }

    #inserindo a viagem no BD
    trips_repository.create_trip(trips_infos)

#Função teste para buscar uma viagem pelo ID no Banco de Dados
@pytest.mark.skip(reason="interacao com o banco")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection() #conectando com o bd
    trips_repository = TripsRepository(conn) #criando uma instancia do repo de viagens
    trip = trips_repository.find_trip_by_id(trip_id)
  
    print(trip)
    
@pytest.mark.skip(reason="interacao com o banco")    
def test_update_trip_status():
    conn = db_connection_handler.get_connection() #conectando com o bd
    trips_repository = TripsRepository(conn) #criando uma instancia do repo de viagens
    trips_repository.update_trip_status(trip_id) # Buscando a viagem no banco de dados pelo ID previamente gerado



