

class NodeCounter:

    def __init__(self):
        self.counter = 0     # counts the amount of nodes
        self.counter_with_2_or_more = 0     # counts the amount of nodes with 2 or more targets
        self.counter_with_3_or_more = 0     # counts the amount of nodes with 3 or more targets
        self.counter_with_4_or_more = 0     # counts the amount of nodes with 4 or more targets
        self.counter_all_targets = 0     # counts all targets
        self.counter_all_unique_targets = 0     # counts all unique targets
        self.amount_of_targets = -1     # counts the amount of targets assigned to node
        self.targets_list = []     # initializing list of all targets
        self.nodes_list = []     # initializing list of all nodes
        self.counter_unique_targets_that_are_nodes = 0     # counts the amount of unique targets that are also nodes
        self.targets_set = {}     # initializing set of unique targets

    def filter_by_target_amount(self):     # counts only nodes with x amount targets
        if self.amount_of_targets >= 2:
            self.counter_with_2_or_more += 1

        if self.amount_of_targets >= 3:
            self.counter_with_3_or_more += 1

        if self.amount_of_targets >= 4:
            self.counter_with_4_or_more += 1

    def node_file_parsing(self):     # reads the data file and calls some methods
        with open("data.yaml") as nodes_data:
            for row in nodes_data:
                row = row.replace("\n", "")
                if row[0] != " ":
                    self.nodes_list.append(row[:5])
                    self.filter_by_target_amount()

                    self.amount_of_targets = -1
                    self.counter += 1

                else:
                    self.counter_all_targets += 1
                    self.targets_list.append(row[2:7])

                self.amount_of_targets += 1

            self.filter_by_target_amount()

        self.results()

    def filter_unique_targets_that_are_also_nodes(self):     # filters all the unique targets that are also nodes
        for i in self.targets_set:
            if i in self.nodes_list:
                self.counter_unique_targets_that_are_nodes += 1

    def results(self):     # handles all the prints and calls task 7 filtering method

        print("Amount of nodes:", self.counter)     # Task 2
        print("Amount of nodes with 2 or more targets:", self.counter_with_2_or_more)     # Task 3
        print("Amount of nodes with 3 or more targets:", self.counter_with_3_or_more)     # Task 4
        print("Amount of nodes with 4 or more targets:", self.counter_with_4_or_more)     # Task 5
        print("Amount of all targets:", self.counter_all_targets)     # Task 6
        self.targets_set = set(self.targets_list)
        print("Amount of unique targets:", len(self.targets_set))     # Task 6
        self.filter_unique_targets_that_are_also_nodes()
        print("Amount of unique targets that are also nodes:", self.counter_unique_targets_that_are_nodes)     # Task 7


n_counter = NodeCounter()
n_counter.node_file_parsing()
