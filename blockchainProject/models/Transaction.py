import datetime


class Transaction:
    def __init__(self, subscriber_count):
        self.timestamp = datetime.datetime.now()
        self.subscriber_count = subscriber_count
