class Transaction():
    def __init__(self,data,amount,timestamp):
        self.data=data
        self.amount=amount
        self.timestamp=timestamp

    def to_string(self):
        return "\nDescription: \t{0}\nAmount: \t{1}\nTimestamp: \t{2}".format(self.data,self.amount,self.timestamp)