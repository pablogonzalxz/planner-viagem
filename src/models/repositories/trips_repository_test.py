import uuid
import pytest
from datetime import datetime, timedelta
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

@pytest.mark.skip(reason="interacao com o banco")
def test_create_trip():
    with db_connection_handler as conn:
        trips_repository = TripsRepository(conn)

        trip_id = str(uuid.uuid4())
        trips_infos = {
            "id": trip_id,
            "destination": "Osasco",
            "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
            "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
            "owner_name": "Osvaldo",
            "owner_email": "osvaldo@email.com"
        }

        trips_repository.create_trip(trips_infos)

        trip = trips_repository.find_trip_by_id(trip_id)
        print("Before update:", trip)
        assert trip is not None
        assert trip[6] == 0  
        trips_repository.update_trip_status(trip_id)

        updated_trip = trips_repository.find_trip_by_id(trip_id)
        print("After update:", updated_trip)
        assert updated_trip is not None
        assert updated_trip[6] == 1  
if __name__ == "__main__":
    test_create_trip()
    print("Todos os testes passaram!")
