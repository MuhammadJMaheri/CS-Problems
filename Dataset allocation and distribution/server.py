'''server side distributer - Muhammad Maheri - 402725094'''
import threading
import socket
import random
import csv

clients = {}
id_allocation = {}
CLIENT_COUNT = 0
ACTIVE_CLIENTS = 0
active_client_ids = []
data_set = []

def handle_client(client_socket, client_id):
    '''main thread for handling each client'''
    global clients, ACTIVE_CLIENTS, active_client_ids

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                if message.lower() == "finish":
                    client_socket.send("Chat ended. You can exit now.".encode("utf-8"))
                    break
                if message.lower() == "my data":
                    client_data(client_socket, client_id)

                if message.lower() == "owner":
                    req_ids = []
                    while True:
                        # get all requested ids
                        message = client_socket.recv(1024).decode("utf-8")
                        if message.lower() == "end":
                            break
                        if message.lower() == "all":
                            req_ids = id_allocation.keys()
                            break
                        req_ids.append("'" + message + "'")
                    for id in req_ids:
                        # send id : owner pair for requested ids
                        mess = id + ": client " + str(id_allocation[id]) + "\n"
                        client_socket.send(mess.encode("utf-8"))

            else:
                client_socket.send("Request not understood.".encode("utf-8"))
        except:
            break

    client_socket.close()
    del clients[client_id]
    ACTIVE_CLIENTS -= 1  # Decrease active client count
    active_client_ids.remove(client_id)
    id_alloc_copy = id_allocation.items()
    for item in id_alloc_copy:
        if item[1] == client_id:
            # choose a random active client and give this ids to it
            r = random.randrange(0, len(active_client_ids))
            id_allocation[item[0]] = active_client_ids[r]

    print(f"Client[{client_id}] disconnected. Active clients: {ACTIVE_CLIENTS}")

    # Check if there are no active clients left
    if ACTIVE_CLIENTS == 0:
        print("No active clients left. Closing server.")
        shutdown_server()


def client_data(client_socket, client_id):
    '''for sending clients data'''
    global id_allocation
    ids =[]
    # get all ids fo this client
    for item in id_allocation.items():
        if item[1] == client_id:
            ids.append(item[0])
    # print all data fo those ids
    for item in data_set:
        if item[0] in ids:
            client_socket.send(str(item).encode("utf-8"))


def shutdown_server():
    '''for closing all sockets'''
    for client_socket in clients.values():
        client_socket.close()
    print("Server socket closed.")
    exit(0)  # Exit the server application

def main():
    '''main function'''
    global CLIENT_COUNT, ACTIVE_CLIENTS, data_set, id_allocation, active_client_ids 

    # open the CSV file
    with open('RandomData.csv', mode='r') as file:
        # create a CSV reader object
        csv_reader = csv.reader(file)

        # extract rows as list of tuples
        data_set = [tuple(row) for row in csv_reader]

    # remove header
    data_set.pop(0)

    # it should be noted that there are some ways to make good queries of this data set in linear time, like using sqlite, better data structures and ...
    # but it doesn't seem to be the purpose of this assignment, so basically i made a vector consisting all the dataset using the csv module.

    # initially set all allocation status for all IDs free
    for item in data_set:
        id_allocation[item[0]] = "free"
    # make a TCP socket, bind and listen for clients
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen()
    print("Server listening on port 5555")

    while True:
        # block and wait for clients establishing connection
        client_socket, addr = server.accept()

        CLIENT_COUNT += 1
        # give a client id for each(this) client, client ids won't be reused
        client_id = CLIENT_COUNT
        clients[client_id] = client_socket
        ACTIVE_CLIENTS += 1  # Increase active client count
        active_client_ids.append(client_id)
        # using a random number between 0 and allocation dictionary, determine how many ids are going to be allocated
        num = random.randrange(0, len(id_allocation))
        # make a copy of allocation dictionary to iterate over
        id_allocation_copy = id_allocation.items()
        i = 0
        # in this loop id allocation will happen, i should note that the num variable is always between 0 and total number of ids, regardless of how many ids are already allocated.
        # it makes sense, because if the random number was between zero and the number of remaining ids, there would be a very low probability for a reasonable number of 
        # clients(like 4 or 5 clinets) to take all IDs, meaning there would be almost always some IDs unallocated.
        # but with this approach the chance of allocating all the remaining IDs increases with each client making a connection to the server.
        # also this loop obviously stops when it iterates over all IDs, so there are no worries for the random number being more than the remaining IDs.
        for item in id_allocation_copy:
            
            if item[1] == 'free':
                # if this id is 'free', then allocate it to this client in the original dictionary
                id_allocation[item[0]] = client_id
            else:
                # skip if this id is already allocated, don't increment the counter
                continue
            i += 1
            if i == num:
                # enough for this client
                break

        print(f"Accepted connection from {addr}, assigned client ID: {client_id}")
        # make a thread and start it for this client, next we are waiting for new clients in this while loop
        thread = threading.Thread(target=handle_client, args=(client_socket, client_id))
        thread.start()


if __name__ == "__main__":
    main()
