import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, mode='r') as file:
        line = ' '
        while line:
            line = file.readline()
            all_data.append(line)


if __name__ == '__main__':
    files = []
    for index in range(1, 5):
        files.append(f'./files/file {index}.txt')

    # линейный вызов
    start = datetime.datetime.now()
    for filename in files:
        read_info(filename)
    end = datetime.datetime.now()
    print(end - start)

    # многопроцессорный подход
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.datetime.now()
    print(end - start)
