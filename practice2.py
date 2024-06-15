# -*- coding: utf-8 -*-
import zipfile
import os
from random import randint


class File:

    def __init__(self, filename, dirname=None):
        self.filename = filename
        self.dirname, self.filepath = self.__get_full_path(filename, dirname)
        self.filesize = self.__get_filesize(self.filepath)

    def __repr__(self):
        return self.filename

    def __eq__(self, other):
        return self.filepath == other.filepath and self.filesize == other.filesize

    @staticmethod
    def __get_filesize(filepath):
        return os.path.getsize(filepath)

    @staticmethod
    def __get_full_path(filename, dirname=None):
        if dirname is None:
            dirname = os.path.dirname(__file__)
        dirname = os.path.normpath(dirname)
        return dirname, os.path.join(dirname, filename)


class Chatterer:
    analyze_count = 4

    def __init__(self):
        self.filenames = []
        self.__stats = {}
        self.totals = {}
        self.__stats_for_gen = {}
        self.files_collected = []

    def __len__(self):
        return len(self.__stats)

    @staticmethod
    def __get_full_path(filename, dirname=None):
        if dirname is None:
            dirname = os.path.dirname(__file__)
        dirname = os.path.normpath(dirname)
        return os.path.join(dirname, filename)

    def __unzip(self, zip_filename, zip_dirname=None):
        if '\\' not in zip_filename and '/' not in zip_filename:
            zip_filename = self.__get_full_path(zip_filename, zip_dirname)

        zfile = zipfile.ZipFile(zip_filename)
        files_unzipped = []
        for filename in zfile.namelist():
            if zfile.extract(filename):
                new_file = File(filename, zip_dirname)
                files_unzipped.append(filename)
                if new_file not in self.filenames:
                    self.filenames.append(new_file)
        return files_unzipped

    @staticmethod
    def __exceptions_check(exceptions, filename):
        for item in exceptions:
            if item in filename:
                return True
        return False

    def seek(self, key_word='', exceptions=None, dirname=None):
        if not dirname:
            dirname = os.path.dirname(__file__)
        if exceptions and not isinstance(exceptions, list):
            exceptions = [exceptions]

        files_found = []
        for root, dirs, files in os.walk(dirname):
            for filename in files:
                if filename.endswith('.txt') and key_word in filename:
                    if exceptions and self.__exceptions_check(exceptions, filename):
                        continue
                    new_file = File(filename, root)
                    files_found.append(filename)
                    if new_file not in self.filenames:
                        self.filenames.append(new_file)
        return files_found

    def collect(self, filenames=None, dirname=None):
        if not filenames:
            if self.filenames:
                filenames = self.filenames
                filenames_manual = False
            else:
                print('Нет файлов для сбора данных')
                return
        else:
            filenames_manual = True
            if not isinstance(filenames, list):
                filenames = [filenames]

            unzipped = []
            for i in range(len(filenames)-1, -1, -1):
                if filenames[i].endswith('.zip'):
                    unzipped += self.__unzip(filenames[i], dirname)
                    filenames.pop(i)

            for filename in unzipped:
                if filename not in filenames:
                    filenames.append(filename)

        collection_changed = False
        char_seq = ' ' * self.analyze_count
        for filename in filenames:
            if filenames_manual:
                filename = File(filename, dirname)

            if filename not in self.files_collected:
                with open(filename.filepath, mode='r', encoding='cp1251') as file_in:
                    for line in file_in:
                        line = line[:-1]
                        for char in line:
                            if char_seq in self.__stats:
                                if char in self.__stats[char_seq]:
                                    self.__stats[char_seq][char] += 1
                                else:
                                    self.__stats[char_seq][char] = 1
                            else:
                                self.__stats[char_seq] = {char: 1}
                            char_seq = char_seq[1:] + char
                    self.files_collected.append(filename)
                    collection_changed = True

        if collection_changed:
            self.totals = {}
            self.__stats_for_gen = {}
            self.__prepare()

    def __prepare(self):
        for char_seq, char_stats in self.__stats.items():
            self.totals[char_seq] = 0
            self.__stats_for_gen[char_seq] = []
            for char, count in char_stats.items():
                self.totals[char_seq] += count
                self.__stats_for_gen[char_seq].append([count, char])
            self.__stats_for_gen[char_seq].sort(reverse=True)

    def chat(self, n=10000, out_filename=None):
        if not self.__stats_for_gen:
            print('Нет данных для генерации')
            return
        chat_n = n
        printed = 0
        if out_filename is not None:
            file_out = open(out_filename, mode='w', encoding='utf8')
            file_out.write('# -*- coding: utf-8 -*-\n')
            file_out.write(f'Текст сгенерирован на основе словаря, содержащего {len(self)} записей.\n\n')
        else:
            file_out = None

        char_seq = ' ' * self.analyze_count
        spaces_printed = 0
        while printed < chat_n:
            char_stats = self.__stats_for_gen[char_seq]
            total = self.totals[char_seq]
            dice = randint(1, total)
            count = 0
            char = ''
            for count_, char_ in char_stats:
                count += count_
                if dice <= count:
                    char = char_
                    break
            if file_out:
                file_out.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    if file_out:
                        file_out.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            char_seq = char_seq[1:] + char
        if file_out:
            file_out.close()
        else:
            print()


if __name__ == '__main__':
    chatter = Chatterer()
    files_txt = chatter.seek(key_word='voyna-i-mir')
    chatter.collect()
    chatter.collect(files_txt)
    chatter.collect('voyna-i-mir-tom-2.txt')
    chatter.collect('voyna-i-mir.zip')
    # print(len(chatter))

    chatter.seek(exceptions='out')
    chatter.collect()
    # print(len(chatter))

    chatter.chat(n=5000, out_filename='out.txt')
    # print(chatter.totals)
