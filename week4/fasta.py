import pathlib
from dataclasses import dataclass


@dataclass
class Sequence:
    id: str
    description: str
    comments: str
    sequence: str


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
