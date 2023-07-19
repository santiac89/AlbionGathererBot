class LeaveEvent:
    def __init__(self, parameters):
        self.objectId = 0

        if 0 in parameters:
            self.objectId = parameters[0]