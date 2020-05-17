class Sharks:

    def __init__(self, shark_list):
        self.shark_list = shark_list

    def print_all_sharks(self):
        for shark in self.shark_list:
            shark.print_identity()
            print("\n")
