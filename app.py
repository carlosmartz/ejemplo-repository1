from flask import Flask, jsonify, request

app = Flask(__name__)

class AbstractAllProductsRepository:
    def add(self, product):
        pass

    def get(self, product_id):
        pass
    def deleteProducto(self, product_id):
        pass

# Implementación concreta del repositorio de productos
class AllProductsRepository(AbstractAllProductsRepository):
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product['id']] = product

    def get(self, product_id):
        return self.products.get(product_id)
   
    def deleteProducto(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False

# Instanciar el repositorio de productos
all_products_repo = AllProductsRepository()

# Datos de ejemplo
all_products_repo.add({
    'id': 123,
    'name': 'Producto 1',
    'price': 10.99
})
all_products_repo.add({
    'id': 456,
    'name': 'Producto 2',
    'price': 19.99
})
all_products_repo.add({
    'id': 999,
    'name': 'Producto 999',
    'price': 99.99
})

# Ruta para agregar un nuevo producto (POST)
@app.route('/products', methods=['POST'])
def add_product():
    product = request.get_json()
    all_products_repo.add(product)
    return jsonify({'message': 'Product added successfully'})

# Ruta para obtener un producto por su ID (solo método GET)
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = all_products_repo.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'})
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted = all_products_repo.deleteProducto(product_id)
    if deleted:
        return jsonify({'message': 'Product deleted successfully'})
    else:
        return jsonify({'message': 'Product not found'})

if __name__ == '__main__':
    app.run()