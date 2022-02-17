import csv


class ParentNotFound(Exception):
    pass


class ChildAlreadyExists(Exception):
    pass


class DataTree:
    def __init__(self, file, de_limit, building_type='upstairs'):
        self.members = {}
        with open(file) as f:
            reader = csv.reader(f, delimiter=de_limit)

            line_count = 0
            for row in reader:
                id, type_id = row
                if line_count > 0 and type_id != '':
                    val1 = id if building_type == 'upstairs' else type_id
                    val2 = type_id if building_type == 'upstairs' else id
                    child = self.members.setdefault(val1, TreeNode(val1))
                    parent = self.members.setdefault(val2, TreeNode(val2))
                    child.parent = parent
                    parent.children.append(child)
                line_count += 1
            del line_count

    def get_parent(self, id):
        parent = self.members[id].parent
        return parent

    def get_children(self, id):
        children = self.members[id].children
        return [child.id for child in children] if children else None

    def add_a_child(self, parent_id: str, child_id: str):
        if not self.members.get(child_id, None):
            try:
                self.members[child_id] = TreeNode(child_id)
                child = self.members[child_id]
                self.members[parent_id].children.append(child)
            except KeyError:
                raise ParentNotFound('There is no such id in a tree(parent_id). Please, check the order of args.')
        else:
            raise ChildAlreadyExists('The child is already in a tree. Please, check the order of args.')


class TreeNode:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parent = None

    def __str__(self):
        return self.id


if __name__ == '__main__':
    My_tree1 = DataTree('tree1.csv', ';', building_type='downstairs')
    print(My_tree1.get_parent('4'))
    print(My_tree1.get_children('0'))

    My_tree2 = DataTree('tree2.csv', ';', building_type='downstairs')
    print(My_tree2.get_parent('4'))
    My_tree2.add_a_child('0', '10')
    print(My_tree2.get_children('0'))
