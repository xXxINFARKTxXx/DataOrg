from constants import *
from record import Record
from serial_file import SerialFile
from sequential_file import SequentialFile

filename = "/home/vladimir/MyProjects/3Semester/0_DataOrg(python_java)/seminars/python_05-08/perezdachi/solution /data/sample.dat"
if __name__ == '__main__':
    record = Record(attributes=ATTRIBUTES, format=FMT, coding=CODING)
    serial_file = SerialFile(filename=filename, record=record, blocking_factor=F)
    sequential_file = SequentialFile(filename=filename, record=record, blocking_factor=F)

    # sequential_file.add_record({"id": 4322, "name": "huesos", "q": 65.5})
    sequential_file.delete_by_id(0)
    sequential_file.print_file()





    # for i in range(12):
    #     serial_file.add_record({"id": i*10, "123": "gandon"+str(i), "q": 10000+i})
    # serial_file.print_file()
    # print(serial_file.add_record({"id": 123, "name": "gandon", "q": 10000}))
        # serial_file.delete_record(i)
    # serial_file.init_file()
    # serial_file.print_file()
