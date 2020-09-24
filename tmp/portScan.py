import sys
import socket
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main(address):
    socket.setdefaulttimeout(1)
    for p in range(1,9999):
        t = threading.Thread(target=portScanner,args=(address,p))
        threads.append(t)
        t.start()     

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('缺少必要参数.')
        exit(2)
    main(sys.argv[1])