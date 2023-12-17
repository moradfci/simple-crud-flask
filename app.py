from flask import Flask, jsonify, request

app = Flask(__name__)

# Constant ID that will be automaticlly increase each time product is added 
ID = 1
# In-memory data structure (dictionary to store products)
products = {}


# Define Product model
class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def validate_fields(cls, data):
        required_fields = ['name', 'description', 'price']

        if not all(field in data for field in required_fields):
            return False, 'Missing required fields'

        if not isinstance(data.get('price'),(float,int)):
            return False, 'Invalid price value. Must be a number'
        
        return True , data

# validate request data for update operation
def validate_request_data(data):
    allowed_fields = ['name', 'description', 'price']
   
    if not all(field in allowed_fields for field in data):
        return False, "Invalid key provided"
    if data.get('price') and not isinstance(data.get('price'),(float,int)) :
         return False, 'Invalid price value. Must be a number'
    
    return True ,data
# the following is the CURD operation.

# Routes for Read product
@app.route('/products', methods=['GET'])
def get_products():
    response = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price
        }
        for product in products.values()
    ]
    return jsonify(response)

# Routes for Read Single product 
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(vars(product))
    else:
        return jsonify({'error': 'Product does not exicst '}), 404

# Routes for Post product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    is_valid, error_message = Product.validate_fields(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    new_product = Product(
        id=ID+1 if products else ID ,
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    products[new_product.id] = new_product
    return jsonify(vars(new_product)), 201

# Routes for Update (put) product
@app.route('/products/<int:product_id>', methods=['PUT','PATCH'])
def update_product(product_id):
    product = products.get(product_id)
    if product:
        data = request.get_json()
        is_valid , error_message = validate_request_data(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        # Update fields if new value is sent in the request body; otherwise, keep the old value
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        return jsonify(vars(product))
    else:
        return jsonify({'error': 'Product not found'}), 404

# Routes for delete product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return '', 204
    else:
        return jsonify({'error': 'Product not found'}), 404


# Run the app
if __name__ == '__main__':
    app.run(debug=True)