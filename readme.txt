#docker build
docker build -t rest-api-repository .
#docker run
docker run -dp 5001:5000 -w /app -v "$(pwd):/app" rest-api-repository
#Probar con docker
docker ps -a
docker ps
docker logs -f <CONTAINER ID>
#Probar con curl
curl -X GET http://localhost:5001/products/129
curl -X POST -H "Content-Type: application/json" -d '{"id": 128, "name": "Producto 1", "price": 10.99}' http://localhost:5001/products