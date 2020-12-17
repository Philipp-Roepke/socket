import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(5)
    print(host)
    print('Waiting for client')

    conn, addr = s.accept()
    print(addr, "Has connected")
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            
    
        

