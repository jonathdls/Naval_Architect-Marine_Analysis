import numpy as np


class Floater:
    """
    Simplified floater with calculation of uncoupled and undamped natural period in heave of a geometry
    Parameters
    ----------
    mass : float
        mass of floater [kg]
    added_mass : float
        added mass in heave, A33, of floater [kg]
    waterplane_area : float
        waterplane area of floater [m^2]
    """
    grav = 9.81
    rho = 1025

    def __init__(self, mass: float, added_mass: float, waterplane_area: float):
        self.mass = mass
        self.added_mass = added_mass
        self.wp_area = waterplane_area

    @property
    def natural_period_heave(self):
        """ float: uncoupled and undamped natural period in heave [s]"""
        return 2 * np.pi * np.sqrt((self.mass + self.added_mass) / (self.rho * self.grav * self.wp_area))


class Cylinder(Floater):
    """
    Simplified cylinder
    Parameters
    ----------
    mass : float
        mass of cylinder [kg]
    diameter : float
        diameter of cylinder [m]
    added_mass : float (optional)
        added mass in heave, A33, of floater [kg], estimated if None
    """
    def __init__(self, mass: float, diameter: float, added_mass: float = None):
        self.diameter = diameter
        super().__init__(mass=mass,
                         added_mass=added_mass or self.estimated_added_mass,
                         waterplane_area=self.waterplane_area)

    @property
    def estimated_added_mass(self):
        """ float: the added mass for a cylinder [kg] is approximated by Lamb classical solution, 1932:
        A_33 = 1/3*rho*D^3 """

        if self.diameter > 0:
            return round(1 / 3 * self.rho * self.diameter ** 3, 1)
        else:
            raise ValueError("Make sure to define diameter as a positive input scalar")

    @property
    def waterplane_area(self):
        """ float: Waterplane area of cylinder [m^2] """
        return np.pi * self.diameter**2 / 4


class Barge(Floater):
    """
    Simplified Barge
    Parameters
    ----------
    mass : float
        mass of barge [kg]
    width : float
        width of barge [m]
    draft : float
        draft of barge [m]
    length : float
        length of barge [m]
    added_mass : float (optional)
        added mass in heave, A33, of floater [kg], estimated if None
    """
    def __init__(self, mass: float, width: float, draft: float, length: float, added_mass: float = None):
        self.width = width
        self.draft = draft
        self.length = length
        super().__init__(mass=mass,
                         added_mass=added_mass or self.estimated_added_mass,
                         waterplane_area=self.waterplane_area)

    @property
    def estimated_added_mass(self):
        """ float: estimated heave added mass of a barge [kg] approximated by Lewis numerical study
        A_33 = cm * pi * rho * (width/2)^2 * length """
        if self.width > 0 and self.draft > 0 and self.length > 0:
            return self.estimated_added_mass_coefficient \
                     * self.rho * np.pi * self.width**2 / 4 * self.length
        else:
            raise ValueError("Make sure to define barge geometry by positive input scalars")

    @property
    def estimated_added_mass_coefficient(self):
        """ float: estimated added mass coefficient (cm) [-] fro a rectangular cross section approximated
        by line fit of Lewis numerical study.
        """
        return 1.5937 * (self.draft/self.width)**0.121

    @property
    def waterplane_area(self):
        """ float: waterplane area of barge [m^2] """
        return self.width * self.length
