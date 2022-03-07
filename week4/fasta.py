import pathlib


class Sequence:
    def __init__(self,
                 fasta_id: str,
                 description: str,
                 comments: str,
                 sequence: str):
        self.id = fasta_id
        self.description = description
        self.comments = comments
        self.sequence = sequence


class FastaParser:
    def __init__(self, file_name: str):
        self.sequences = []
        file_path = pathlib.Path(file_name)
        with file_path.open("r") as f:
            for line in f:
                if line[0] == '>':
                    if seq:
                        self.sequences.append(seq)
                    seq = Sequence('', '', '', '')
                    fasta_id, _,  descr = line.partition(' ')
                    seq.id += fasta_id
                    seq.description += descr
                elif line[0] == ';':
                    seq.comments += line
                else:
                    seq.sequence += line
            self.sequences.append(seq)

    def show(self):
        for sequence in self.sequences:
            print(sequence.description)
        return None


my_parse = FastaParser('abcd.fasta')
my_parse.show()
