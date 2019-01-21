# Lending Club Data Analysis
import re
class main():
    def __init__(self, fields):
        #file = "C:\\Users\\M113455\\Desktop\\LoanStats_2018Q3.csv"
        files = ["C:\\Users\\manlo\\Desktop\\LendingClubData\\LoanStats_2018Q1.csv"]
        fields = fields
        self.head_node = data_node("head", level = 0)
        self.retrieve_header(files[0])
        self.retrieve_fields(fields)
        for file in files:
            self.parse_file(file)

    def parse_file(self, file_path):
        with open(file_path, 'r', errors='ignore') as file_in:
            next(file_in)
            for j, line in enumerate(file_in.readlines()):
                line = line.strip().split('","')
                line[0] = ""
                if line[16] == 'Current':
                    continue
                records = [line[i] for i in self.field_inds]
                if line[16] == 'Fully Paid':
                    value = 1
                else:
                    value = 0
                self.fill_tree(records, value)

    def fill_tree(self, records, value):
        current_node = self.head_node

        for record, field in zip(records, self.fields):
            if not len(current_node.branches):
                branch = data_node(field, level = current_node.lvl + 1)
                current_node.branches.append(branch)
                current_node = branch
                current_node.node_response = record
                current_node.node_count += 1
                current_node.node_sum += value
            else:
                match = 0
                for branch in current_node.branches:
                    if branch.node_title == field and branch.node_response == record:
                        current_node = branch
                        current_node.node_count += 1
                        current_node.node_sum += value
                        match = 1
                if match == 0:
                    branch = data_node(field, level = current_node.lvl + 1)
                    branch.node_response = record
                    branch.node_count += 1
                    branch.node_sum += value
                    current_node.branches.append(branch)
                    current_node = branch
            #print("\t" * current_node.lvl + str(current_node.node_title) + " " + record + " " + str(current_node.node_response))

    def retrieve_fields(self, fields):
        # Takes the user inputted fields of interest and finds the indicies of the item in the header file
        self.fields = []
        self.field_inds = []
        for field in fields:
            if field.lower() not in self.header:
                raise Exception("'{}' field not found".format(field))
            else:
                self.fields.append(field.lower())
                self.field_inds.append(self.header.index(field))

    def retrieve_header(self, file_path):
        # Retrieve the header from the given .csv file and returns a list of the fields
        with open(file_path, 'r', errors='ignore') as  file_in:
            line = file_in.readline()
            line = [item.lower() for item in line.strip().split('","')]
            line[0] = "id"
            if line[-1][-1] == line[-1][line[-1].find('"')]:
                line[-1] = line[-1][:-1]
            self.header = line

class data_node():
    def __init__(self, title):
        self.node_title = title
        self.node_response = ""
        self.node_count = 0
        self.node_sum = 0
        self.branches = []

if __name__ == "__main__":
    app = main(["term", "loan_amnt", "settlement_amount"])

print(len(app.head_node.branches))
