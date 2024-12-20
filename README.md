# Basic gRPC server implementation

This is the most basic gRPC server implementation

# Basic event flow -
![gRPC server setup](./img/image.png)

The client requets the server with id, which the server in turn fetches the mysql DB to get the details, and sends back to the user. 

### Few setup details :
I ran all the setup in docker
- My MySQL server was running in Docker container which mapped localhost:8101 to mysql:3306 
- I ran my installation on a virtuanenv, so that my system libraries do not get messed up



