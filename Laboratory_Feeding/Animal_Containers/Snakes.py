class Snakes:

    def __init__(self, snake_list):
        self.snake_list = snake_list

    def print_all_snakes(self):
        for snake in self.snake_list:
            snake.print_identity()
            print("\n")