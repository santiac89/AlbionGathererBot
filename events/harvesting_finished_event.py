class HarvestingFinishedEvent:
    def __init__(self, parameters):
        self.userObjectId = 0
        self.objectId = 0
        self.standardAmount = 0
        self.itemId = 0
        self.collectorBonusAmount = 0
        self.premiumBonusAmount = 0
        self.currentPossibleDegradationProcesses = 0

        if 0 in parameters:
            self.userObjectId = parameters[0]

        if 3 in parameters:
            self.objectId = parameters[3]

        if 4 in parameters:
            self.itemId = parameters[4]

        if 5 in parameters:
            self.standardAmount = parameters[5]

        if 6 in parameters:
            self.collectorBonusAmount = parameters[6]

        if 7 in parameters:
            self.premiumBonusAmount = parameters[7]

        if 8 in parameters:
            self.currentPossibleDegradationProcesses = parameters[8] 