# Lending Club Data Analysis

class main():
    def __init__(self, fields):
        #file = "C:\\Users\\M113455\\Desktop\\LoanStats_2018Q3.csv"
        files = ["C:\\Users\\manlo\\Desktop\\LendingClubData\\LoanStats_2018Q1.csv"]
        fields = fields
        head = head_node()
        head.retrieve_header(files[0])
        head.retrieve_fields(fields)
        for file in files:
            head.parse_file(file)

class head_node():

    def parse_file(self, file_path):
        with open(file_path, 'r', errors='ignore') as file_in:
            next(file_in)
            for j, line in enumerate(file_in.readlines()):
                line = line.strip().split('","')
                if line[16] == 'Current':
                    continue
                records = [line[i] for i in self.field_inds]
                print(records)
                if j > 1:
                    break

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
    def __init__(self):
        node_title = ""
        node_response = ""
        node_count = 0
        node_sum = 0

if __name__ == "__main__":
    app = main(["id", "member_id", "loan_amnt", "settlement_amount"])
