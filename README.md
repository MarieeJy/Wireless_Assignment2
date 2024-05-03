Example: IPC using sockets in Python between a container that is running the server code and a client script running on the host.
1. To build the image, run:  
docker run --rm -p 9898:9898 my_ipc_server
2. Open other terminal, run the client by:  
python ipc_clinet.py
You will see ‘Hello, world. IPC success!’ on the client terminal
