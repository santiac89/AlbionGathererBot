class MoveOperation():
    def __init__(self, parameters):
        self.time = parameters[0] if 0 in parameters else 0
        self.position = parameters[1] if 1 in parameters else [0, 0]
        self.direction = parameters[2] if 2 in parameters else 0
        self.new_position = parameters[3] if 3 in parameters else [0, 0]
        self.speed = parameters[4] if 4 in parameters else 0