# Lending Club Data Analysis
import re
class main():
    def __init__(self, fields):
        files = ["C:\\Users\\M113455\\Desktop\\LoanStats_2018Q3.csv"]
        #files = ["C:\\Users\\manlo\\Desktop\\LendingClubData\\LoanStats_2018Q1.csv"]
        fields = fields
        self.head_node = data_node("head")
        self.retrieve_header(files[0])
        self.retrieve_fields(fields)
        for file in files:
            self.parse_file(file)

    def parse_file(self, file_path):
        """
        Takes a file path for a .csv file formatted with '","' as a seperator
        and retrieves the fields that were selected by the user along with the binary
        output of the loan_status column

        Calls the fill_tree function on the records and the values
        """
        with open(file_path, 'r', errors='ignore') as file_in:
            next(file_in)
            for line in file_in.readlines():
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
        """
        Starts with a head node from class construction and builds a tree based on the
        response data.
        """

        current_node = self.head_node
        # Zips together the fields of interest and their corresponding records
        for record, field in zip(records, self.fields):
            # If there are no branches, do:
            if not current_node.branches:
                # Create a new node for the field and adds the node to the
                # branches list of the current_node node before rewritting
                # the current node with the new node
                branch = data_node(field)
                current_node.branches.append(branch)
                current_node = branch
                # Adds the record to the node along with the loan_status binary value
                current_node.node_response = record
                current_node += value
            # If there are branches in the current node
            else:
                match = 0
                # steps through each node in the branches list and checks if the
                # response matches the current record
                branch = [i for i in current_node.branches if i.node_title == field and i.node_response == record]
                if branch:
                        # If the field and record match the current node the node
                        # value and count are updated with the current record
                        current_node = branch[0]
                        current_node += value

                else:
                    # Creates a new node to hold the new field/ record combination
                    branch = data_node(field)
                    branch.node_response = record
                    branch += value
                    current_node.branches.append(branch)
                    current_node = branch

    def retrieve_fields(self, fields):
        """
        Takes the user inputted fields of interest and finds the indicies of the item in the header file.
        Stores the fields and the field indicies.
        """
        self.fields = []
        self.field_inds = []
        for field in fields:
            if field.lower() not in self.header:
                raise Exception("'{}' field not found".format(field))
            else:
                self.fields.append(field.lower())
                self.field_inds.append(self.header.index(field))

    def retrieve_header(self, file_path):
        """
        Retrieve the header from the given .csv file and stores a list of the fields
        """
        with open(file_path, 'r', errors='ignore') as  file_in:
            line = file_in.readline()
            line = [item.lower() for item in line.strip().split('","')]
            line[0] = "id"
            if line[-1][-1] == line[-1][line[-1].find('"')]:
                line[-1] = line[-1][:-1]
            self.header = line

    def read_tree(self, node):
        if node.node_title != "head":
            print(node)
        if node.branches:
            for branch in node.branches:
                self.read_tree(branch)

class data_node():
    def __init__(self, title):
        self.node_title = title
        self.node_response = ""
        self.node_count = 0
        self.node_sum = 0
        self.branches = []

    def __add__(self, value):
        self.node_count += 1
        self.node_sum += value
        return self

    def __str__(self):
        return self.node_title + " [ "+ self.node_response + " ]: " + str(self.node_sum) + " ( " + str(self.node_count) + " )"

if __name__ == "__main__":
    app = main(["term", "loan_amnt", "settlement_amount"])

print(app.head_node)
