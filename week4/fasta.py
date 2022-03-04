import pathlib


class Sequence:
    def __init__(self, fasta_id, description, comments, sequence):
        self.id = fasta_id
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
                    data_storage.append(['', '', '', ''])
                    fasta_id, _,  descr = line.partition(' ')
                    data_storage[-1][0] += fasta_id
                    data_storage[-1][1] += descr
                elif line[0] == ';':
                    data_storage[-1][2] += line
                else:
                    data_storage[-1][3] += line
        for data in data_storage:
            self.sequences.append(Sequence(*data))

    def show(self):
        for sequence in self.sequences:
            print(sequence.description)


my_parse = FastaParser('abcd.fasta')
my_parse.show()
