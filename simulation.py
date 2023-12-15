import json
import time

import numpy

import computations
from gui.simulationcanvas import SimulationCanvas

from particle import Particle


class Simulation:
    def __init__(self):
        # Simulation parameters
        self.time_step = 0.1
        self.max_time = 100
        self.applied_external_force = numpy.array([-0.5, 0])
        # Material parameters
        self.particle_mass = 10
        self.particle_distance_at_rest = 25
        self.elasticity = 1
        # Load model
        self.particles = self.load_model()

    def load_model(self):
        particles = []
        data = json.load(open('mesh.json', 'r'))
        for point in data["points"]:
            x = point[0]
            y = point[1]
            particles.append(Particle(x, y))
        for i in range(0, len(data["neighbourhoods"])):
            for neighbour_index in data["neighbourhoods"][i]:
                particles[i].makeNeighbourTo(particles[int(neighbour_index)])
        # For this simulation, all leftmost particles are restricted
        min_x = min(particle.getX() for particle in particles)
        for particle in particles:
            if particle.getX() == min_x:
                particle.setRestricted(True)
        # For this simulation, a force is applied to all rightmost particles
        max_x = max(particle.getX() for particle in particles)
        for particle in particles:
            if particle.getX() == max_x:
                particle.setIsExternalForceApplied(True)
        return particles

    def run_step(self):
        computations.apply_particle_movement_step(self.particles, self.time_step, self.elasticity,
                                                  self.particle_mass, self.applied_external_force,
                                                  self.particle_distance_at_rest)
