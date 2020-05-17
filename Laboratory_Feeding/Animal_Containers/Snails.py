class Snails:

    def __init__(self, snail_list):
        self.snail_list = snail_list

    def print_all_snails(self):
        for snail in self.snail_list:
            snail.print_identity()
            print("\n")