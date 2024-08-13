from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from model_bakery import baker
from conftest import authenticate
from store.models import Collection

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection



@pytest.mark.django_db
class TestCreateCollection:
    # @pytest.mark.skip
    def test_if_user_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    # @pytest.mark.skip
    def test_if_user_not_admin_returns_403(self, create_collection, authenticate):
        authenticate()
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    # @pytest.mark.skip
    def test_if_user_is_admin_returns_201(self, api_client, authenticate):
        authenticate(is_staff=True)
        response = api_client.post('/store/collections/', {'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
    
    # @pytest.mark.skip
    def test_if_data_is_invalid_returns_400(self, api_client, authenticate):
        # api_client.force_authenticate(user=User(is_staff=True))
        authenticate(is_staff=True)
        response = api_client.post('/store/collections/', {'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
    
    # @pytest.mark.skip
    def test_if_data_is_valid_returns_201(self, api_client, authenticate):
        # api_client.force_authenticate(user=User(is_staff=True))
        authenticate(is_staff=True)
        response = api_client.post('/store/collections/', {'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        #Arrange
        collection = baker.make(Collection)
        
        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }

    def test_if_collection_does_not_exist_returns_404(self, api_client):
        #Arrange
        invalid_id = 'abc'  # Invalid ID format
        
        response = api_client.get(f'/store/collections/{invalid_id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND
    
