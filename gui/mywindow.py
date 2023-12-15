from PyQt5.QtWidgets import QMainWindow
from simulation import Simulation
from gui.simulationcanvas import SimulationCanvas


class MyWindow(QMainWindow):
    def __init__(self, simulation: "Simulation"):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Particle simulation")
        self.canvas = SimulationCanvas(simulation)
        self.setCentralWidget(self.canvas)

    def update_simulation(self):
        self.canvas.simulation.run_step()
        self.canvas.update()
