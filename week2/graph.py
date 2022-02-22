import csv


class DataGraph:
    def __init__(self, file, de_limit: str):
        '''Makes a wieghted graph from a csv file.
            csv file contains 3 columns.
            columns 1, 2 - node ids
            column 3 - weight of connection between node1 and node2'''
        self.members = {}
        with open(file) as f:
            reader = csv.reader(f, delimiter=de_limit)

            line_count = 0
            for row in reader:
                id1, id2, price = row
                if line_count > 0:
                    node1 = self.members.setdefault(id1, GraphNode(id1))
                    node2 = self.members.setdefault(id2, GraphNode(id2))
                    node1.neighbours[id2] = int(price)
                    node2.neighbours[id1] = int(price)
                line_count += 1

    def distance(self, start_id: str, finish_id: str):
        '''Finding the shortest way using the deicstra algorithm'''
        costs = dict()
        parents = dict()
        costs[start_id] = 0
        parents[start_id] = None

        # making up the tables of node_costs and their parents
        for node_id in self.members.keys():
            if self.members[start_id].neighbours.get(node_id):
                costs[node_id] = self.members[start_id].neighbours[node_id]
                parents[node_id] = start_id
            else:
                costs[node_id] = float('inf')
                parents[node_id] = None

        # making up the list of unused nodes
        unused_nodes = [member for member in costs.keys() if member != start_id]

        while unused_nodes:
            # finding the nearest to start and unused node
            min_dist = float('inf')
            min_id = None
            for node in unused_nodes:
                if costs[node] < min_dist:
                    min_dist = costs[node]
                    min_id = node

            # if finding the shorter way, renewing the parents and costs
            for key, value in self.members[min_id].neighbours.items():
                sum_way = value + min_dist
                if sum_way < costs[key]:
                    costs[key] = sum_way
                    parents[key] = min_id

            # marking the processed node as used
            unused_nodes.remove(min_id)
        return costs.get(finish_id, None)

    def get_neighbours(self, id):
        neighbours = self.members[id].neighbours
        return [neighbour.id for neighbour in neighbours.values()]


class GraphNode:
    def __init__(self, id):
        self.id = id
        self.neighbours = {}

    def __str__(self):
        return self.id


if __name__ == '__main__':
    My_graph1 = DataGraph('graph.csv', ';')
    print(My_graph1.distance('4', '6'))
