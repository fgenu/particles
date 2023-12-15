class Particle:

    def __init__(self, _x, _y, _restricted=False):
        self.m_x = _x
        self.m_y = _y
        self.m_restricted = _restricted
        self.m_neighbours = []
        self.m_velocity = (0, 0)
        self.m_is_external_force_applied = False

    def setX(self, _x):
        self.m_x = _x

    def setY(self, _y):
        self.m_y = _y

    def getX(self):
        return self.m_x

    def getY(self):
        return self.m_y

    def isRestricted(self):
        return self.m_restricted

    def setRestricted(self, _restricted):
        self.m_restricted = _restricted

    def isExternalForceApplied(self):
        return self.m_is_external_force_applied

    def setIsExternalForceApplied(self, _is_external_force_applied):
        self.m_is_external_force_applied = _is_external_force_applied

    def getNeighbours(self):
        return self.m_neighbours

    def makeNeighbourTo(self, _neighbour: "Particle"):
        if _neighbour in self.m_neighbours or self in _neighbour.m_neighbours:
            return
        self.m_neighbours.append(_neighbour)
        _neighbour.m_neighbours.append(self)

    def setVelocity(self, _velocity):
        self.m_velocity = _velocity

    def getVelocity(self):
        return self.m_velocity
