import numpy as np


class NaturalPeriod:
    """
    Simplified calculation of added mass, and uncoupled and undamped natural period in heave of a geometry
    Parameters
    ----------
    geometry : str
        shape of the hull (cylindrical, square)
    grav : float
        gravitation [m/s^2]
    rho : float
        density of water [t/m^3]
    """

    grav = 9.81
    rho = 1.025

    def __init__(self, geometry: str):
        if geometry.lower() not in ['cylinder', 'barge']:
            raise ValueError(f"Invalid geometry: '{geometry.lower()}'")
        self.geometry = geometry.lower()

    def added_mass(self, diameter=None, width=None, draft=None, length=None):
        """
        Approximated heave added mass of a geometry.
        diameter : float
            Diameter of cylinder [m]
        length : float
            Length of barge [m]
        width : float
            Width of barge [m]
        draft : draft of geometry
        return : Added mass [kg]

        Notes
        -----
        The added mass for a barge is approximated by formula: A_33 = 0.8*rho*B*D*L
        The added mass for a cylinder is approximated by Lamb classical solution, 1932: A_33 = 1/3*rho*D^3
        """
        if self.geometry in 'cylinder' and diameter is not None:
            return round(1/3 * self.rho * diameter**3, 1)
        elif self.geometry in 'barge' and (width and draft and length) is not None:
            return round(0.8 * self.rho * width * draft * length, 1)
        else:
            raise ValueError(f"Invalid combination of geometry: {self.geometry} and characteristic lengths. "
                             f"If geometry is barge give: width, draft and length. "
                             f"If geometry is cylinder: give diameter")

    def natural_period_heave(self, mass, waterplane_area, added_mass):
        """
        Uncoupled and undamped natural period in heave.
        :param mass : mass of structure [t]
        :param added_mass : the added mass of the structure [t]
        :param waterplane_area : water plane area of structure [m^2]
        :return: natural period in heave [s]
        """
        return round(2 * np.pi * np.sqrt((mass + added_mass) / (self.rho * self.grav * waterplane_area)), 1)
