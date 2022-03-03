import pathlib


class Sequence:
    def __init__(self, description, comments, sequence):
        self.description = description
        self.comments = comments
        self.sequence = sequence


class FastaParser:
    def __init__(self, file_name):
        self.sequences = []
        data_storage = []
        file_path = pathlib.Path(file_name)
        with file_path.open("r") as f:
            for line in f:
                if line[0] == '>':
                    data_storage.append(['', '', ''])
                    data_storage[-1][0] += line
                elif line[0] == ';':
                    data_storage[-1][1] += line
                else:
                    data_storage[-1][2] += line
        for data in data_storage:
            self.sequences.append(Sequence(*data))

    def show(self):
        for sequence in self.sequences:
            print(sequence.description)


my_parse = FastaParser('abcd.fasta')
my_parse.show()
