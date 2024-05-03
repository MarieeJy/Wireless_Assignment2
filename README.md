Example: IPC using sockets in Python between a container that is running the server code and a client script running on the host.
1. To build the image, run:  
`docker run --rm -p 9898:9898 my_ipc_server`
2. Open other terminal, run the client by:  
`python ipc_clinet.py`  

You will see ‘Hello, world. IPC success!’ on the client terminal  

Example2: deploy the client Python script inside another container and demonstrate IPC between containers.  
1. To build the image
   In the server file, run:  
   `docker build -t my_ipc_server .`  
   In the client file, run:  
   `docker build -t my_ipc_client .`
2. Define bridged network in Docker for containers to be able to communicate via sockets, run:  
   `docker network create my_socket_ipc_network`
3. running both containers:  
   `docker run -rm --network=my_socket_ipc_network --name ipc_server_dns_name my_ipc_server`  
   `docker run -rm --network=my_socket_ipc_network my_ipc_client`
