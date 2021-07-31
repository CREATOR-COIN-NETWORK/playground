class Block():
    def __init__(self, previous_block, block_data):
        self.previous_block = previous_block
        self.block_data = block_data

    def debug(self):
        print(
            f'\n'
            f'** DEBUG\n'
            f'{self}\n'
            f'{self.__dict__}\n'
            f'** END DEBUG\n'
        )


nb = Block(None, "information is here")

nb.debug()
