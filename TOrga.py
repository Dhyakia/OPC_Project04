class Player:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def recall(self):
        print(f'You have called {self.first_name} - { self.last_name}')


if __name__ == "__main__":
    testP = Player('Prénom', 'Nom')
    testP.recall
