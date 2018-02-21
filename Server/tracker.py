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

class MultiThread(Thread):
    def __init__(self, thread_pool):
        self.thread_pool = thread_pool
        self.thread_number = self.thread_pool.next_thread()
        self.thread_pool.append(self)
        Thread.__init__(self)

    def run(self):
        pass

    def get_thread_number(self):
        return self.thread_number



class Server(MultiThread):
    def run(self):
        print("TEST")
        print(self.thread_pool)

thread_pool = ThreadPool()
server = []

for con in range(0, 20) :
    server.append(Server(thread_pool))
    server[con].start()