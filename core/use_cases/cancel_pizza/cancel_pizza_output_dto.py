class CancelPizzaOutputDTO:
    def __init__(self, status: str = "", message: str = ""):
        self.status = status
        self.message = message
        self.data = {}