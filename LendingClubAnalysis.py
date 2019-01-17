# Lending Club Data Analysis

class main():
    def __init__(self):
        files = ['a', 'b', 'c']
        head = head_node()
        for file in files:
            head.parse_file(file)


class head_node():
    def __init__(self):
        pass

    def parse_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file.readlines():
                pass

class data_node():
    def __init__(self):
        node_title = ""
        node_response = ""
        node_count = 0
        node_sum = 0
