from includes import database
from includes import pgp
from socket import *
from threading import Thread

class ThreadPool(dict):
    def next_thread(self):
        return len(self) + 1

    def append(self, item):
        self[self.next_thread()] = item
        return True

    def remove_at(self,index):
        self.pop(index)
        return self

class MultiThread(Thread):
    def __init__(self, thread_pool):
        self.thread_pool = thread_pool
        self.thread_number = self.thread_pool.next_thread()
        self.thread_pool.append(self)
        Thread.__init__(self)

    def free(self):
        self.thread_pool.remove_at(self.thread_number)

    def run(self):
        pass

    def get_thread_number(self):
        return self.thread_number



class RequestHandler(MultiThread):
    def __init__(self, ip, thread_pool):
        self.ip = ip
        MultiThread.__init__(self,thread_pool)

    def run(self):
        print("Got Request from", self.ip)
        self.free()
        


thread_pool = ThreadPool()

class Server():
    def __init__(self, thread_pool, host,port=5103):
        self.thread_pool = thread_pool
        self.addr = (host, port)
    
    def start(self):
        sh = socket(AF_INET, SOCK_DGRAM)
        sh.bind(self.addr)
        while 1:
            data, ip = sh.recvfrom(1024)
            rq = RequestHandler(ip,thread_pool)
            cli = database.get_clients()
            resp = "["
            for i in cli:
                resp += i[0]
            resp += "]"
            sh.sendto(bytes(resp, "utf-8"), ip)
            database.add_client(str(ip[0]),1)
            rq.start()
            

server = Server(thread_pool,"127.0.0.1")
server.start()
