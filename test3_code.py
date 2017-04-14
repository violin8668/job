import sys,os
import fcntl
import random, threading


test_files = ['a', 'b', 'c', 'd', 'e']
write_flag = [0]*5
read_flag = [0]*5
write_content ={}
file_lock = [threading.Lock() for i in xrange(5)]

def write_file():
    file_list = [ i for i in xrange(5) if write_flag[i] < 2 ]
    while len(file_list):
        index = file_list[random.randint(0, len(file_list)-1)]
        content = str(random.randint(0,100))
        file_lock[index].acquire()
        if write_flag[index] < 2:
            write_flag[index] += 1
            fd = open(test_files[index], 'w')
            fd.write(str(content))
            write_content[index] = content
            fd.close()
        file_list = [ i for i in xrange(5) if write_flag[i] < 2 ]
        file_lock[index].release()

def read_file():
    file_list = [ i for i in xrange(5) if read_flag[i] < 2 ]
    while len(file_list):
        index = file_list[random.randint(0, len(file_list)-1)]
        file_lock[index].acquire()
        fd = open(test_files[index], 'r')
        content = fd.readline()
        if read_flag[index] < 2:
            read_flag[index] += 1
            result = "File Name: " + test_files[index]
            result += "\nExpected Content: " + write_content[index]
            result += "\nActual Content: " + content
            if write_content[index] != content:
                result += "\nTest Result: Fail"
            else:
                result += "\nTest Result: Pass"
            fd.close()
            print result
        file_list = [ i for i in xrange(5) if read_flag[i] < 2 ]
        file_lock[index].release()

def write_case():
    write_thread_list = []
    for i in xrange(10):
        t = threading.Thread(target=write_file)
        write_thread_list.append(t)

    return write_thread_list

def read_case():
    read_thread_list = []
    for i in xrange(2):
        t = threading.Thread(target=read_file)
        read_thread_list.append(t)

    return read_thread_list

if __name__ == "__main__":
    write_thread_list = write_case()
    read_thread_list = read_case()
    for i in xrange(10):
        write_thread_list[i].start()

    for i in xrange(2):
        read_thread_list[i].start()
