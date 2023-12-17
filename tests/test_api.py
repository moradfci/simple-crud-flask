import pytest
from app import app  

class TestAPI:
    """test class to test all endpoints."""

    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    
    # data for cretng product
    @pytest.fixture
    def new_product_data(self):
        return {
            'name': 'Product test 1',
            'description': 'any Description',
            'price': 10
        }
    # function that do creating of product so can be used all test functions
    def create_product(self, client, data):
        response = client.post('/products', json=data)
        assert response.status_code == 201
        return response.json['id']
    

    def test_create_product(self, client):
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 20.99
        }
        response = client.post('/products', json=data)
        assert response.status_code == 201


    def test_get_products(self, client,new_product_data):
        #creating anohter product so we can list it 
        product_id = self.create_product(client, new_product_data)
        response = client.get('/products')
        assert len(response.json) == 2
        assert response.status_code == 200

    def test_get_product(self, client):
        response = client.get('/products/1')
        assert response.status_code == 200  

    def test_update_product(self, client):
        data = {
            'name': 'Updated Product Name',
            
        }
        response = client.put('/products/1', json=data)
        assert response.status_code == 200  

    def test_delete_product(self, client):
        response = client.delete('/products/1')
        assert response.status_code == 204 

    
    def test_create__product_with_worng_data_type(self,client):
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': "20.99"
        }
        response = client.post('/products', json=data)
        assert response.json['error'] == 'Invalid price value. Must be a number'
        assert response.status_code == 400


    def test_update_product_with_wrong_data(self, client,new_product_data):
        product_id = self.create_product(client, new_product_data)
        data = {
            'price': '789',
            
        }
        response = client.put(f'/products/{product_id}', json=data)
        assert response.json['error'] == 'Invalid price value. Must be a number'
        assert response.status_code == 400 