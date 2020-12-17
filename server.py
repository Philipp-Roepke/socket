import socket

try:
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(5)
    print(host)
    print('Waiting for client')

    conn, addr = s.accept()
    print(addr, "Has connected")
except KeyboardInterrupt:
    pass
