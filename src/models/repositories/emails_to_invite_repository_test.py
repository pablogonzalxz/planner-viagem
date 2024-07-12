import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.email_to_invite_repository import EmailToInviteRepository

trip_id = str(uuid.uuid4())
@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    with db_connection_handler as conn:
        emails_to_invite_repository = EmailToInviteRepository(conn)

        email_trips_infos = {
            "id": str(uuid.uuid4()),
            "trip_id": trip_id,
            "email": "olaMundo@email.com"
        }

        emails_to_invite_repository.registry_email(email_trips_infos)
        
@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)

if __name__ == "__main__":
    pytest.main(["-s", "-v", "src/models/repositories/emails_to_invite_repository_test.py"])

