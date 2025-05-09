'''client code - Muhammad Maheri - 402725094'''
import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            # just decode and show the message
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
            else:
                break
        except:
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to this address and port, we have to change this address when running these codes in VMs as described in my report
    client.connect(("127.0.0.1", 5555))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    print("Enter 'my data' to request all of your data\nEnter 'owner' and enter ids (type 'end' to end prompt) to show their owner\ntype 'finish' to end connection:")
    while True:
        command = input()
        client.send(command.encode("utf-8"))
        if command.lower() == "finish":
            break
        if command.lower() == "owner":
            # doing this to show "id:" at each line so the user know we are in id query mode
            while True:
                command = input("id:")
                client.send(command.encode("utf-8"))
                if command == "end":
                    break

    client.close()


if __name__ == "__main__":
    main()
