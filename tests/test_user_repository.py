from src.infra.database.repositories.user_repository import UserRepository
from src.infra.database.models.user import User
def test_create_user(db_session):
    repo = UserRepository(db_session)

    user = User(
        email="test@email.com",
        username="teste",
        password="123",
        cellphone="123456789",
        birth_date="2000-01-01"
        )

    result = repo.create(user)

    assert result.id is not None
    assert result.email == "test@email.com"