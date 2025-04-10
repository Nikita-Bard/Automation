import pytest
from CompanyApi import CompanyApi

# "scope" применяется на все ссесию тестирования 1 раз
@pytest.fixture(scope="session")
def client():
    return CompanyApi("https://x-clients-be.onrender.com/")
