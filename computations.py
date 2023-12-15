from math import dist

import numpy


def compute_elastic_force(p1, p2, k, distance_between_particles_at_rest):
    distance = dist(
        [p1.getX(), p1.getY()],
        [p2.getX(), p2.getY()]
    )
    displacement = distance - distance_between_particles_at_rest
    force_magnitude = k * displacement
    # Direction from p1 to p2
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    # Normalise
    force_x = (dx / distance) * force_magnitude
    force_y = (dy / distance) * force_magnitude
    return numpy.array([force_x, force_y])


def apply_particle_movement_step(particles, step, elasticity, particle_mass, applied_force, particle_distance_at_rest):
    for particle in particles:
        if not particle.isRestricted():
            resultant_force = numpy.array([0, 0])
            if particle.isExternalForceApplied():
                resultant_force = resultant_force + applied_force
            for neighbour in particle.getNeighbours():
                resultant_force = resultant_force + compute_elastic_force(particle, neighbour, elasticity,
                                                                          particle_distance_at_rest)
            acceleration = resultant_force / particle_mass
            particle.setVelocity(particle.getVelocity() + acceleration * step)
            particle.setX(particle.getX() + particle.getVelocity()[0] * step)
            particle.setY(particle.getY() + particle.getVelocity()[1] * step)
