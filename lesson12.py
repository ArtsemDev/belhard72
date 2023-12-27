# from threading import *
# from queue import PriorityQueue
# from time import sleep
#
#
# # print_lock = Lock()
# #
# #
# # def foo():
# #     for _ in range(10):
# #         print_lock.acquire()
# #         print(current_thread().name)
# #         print_lock.release()
# #         sleep(1)
# #
# #
# # flag = 5
# # flag_lock = Lock()
# #
# #
# # def bar():
# #     global flag
# #     with flag_lock:
# #         if flag == 5:
# #             sleep(2)
# #             print(flag * 2)
# #
# #
# # def baz():
# #     global flag
# #     with flag_lock:
# #         sleep(1)
# #         flag = 4
# #
# #
# # # if __name__ == '__main__':
# # #     threads = [Thread(target=foo) for _ in range(10)]
# # #     for thread in threads:
# # #         thread.start()
# #
# # if __name__ == '__main__':
# #     thread1 = Thread(target=bar)
# #     thread2 = Thread(target=baz)
# #     thread1.start()
# #     thread2.start()
#
# semaphore = Semaphore(value=5)
# barrier = Barrier(parties=3)
#
#
# print_lock = Lock()
#
#
# def foo():
#     barrier.wait(timeout=3)
#     for _ in range(10):
#         with print_lock:
#             print(current_thread().name)
#         sleep(1)
#
#
# # if __name__ == '__main__':
# #     threads = [Thread(target=foo) for _ in range(10)]
# #     for thread in threads:
# #         thread.start()
#
#
# # event1 = Event()
# # l = local()
# #
# #
# # def func():
# #     print(l.a)
# #     l.a = 4
# #
# #
# # def bar():
# #     l.a = 5
# #     func()
# #     baz()
# #
# #
# # def baz():
# #     print(l.a)
# #
# #
# # if __name__ == '__main__':
# #     thread1 = Thread(target=bar)
# #     # thread2 = Thread(target=baz)
# #     thread1.start()
# #     # thread2.start()
# from random import randint
# q = PriorityQueue(maxsize=10)
#
#
# def bar():
#     for _ in range(10):
#         q.put((randint(1, 10), randint(1, 10)))
#
#
# def baz():
#     while not q.full():
#         pass
#     for _ in range(10):
#         print(q.get())
#
#
# if __name__ == '__main__':
#     thread1 = Thread(target=bar)
#     thread2 = Thread(target=baz)
#     thread1.start()
#     thread2.start()


from multiprocessing import *


def foo():
    for _ in range(10):
        print(current_process().name)


if __name__ == "__main__":
    process = Process(target=foo)
    process.start()
