import numpy as np


class SimplifiedFloater:
    """
    Simplified calculation of uncoupled and undamped natural period in heave of a geometry
    Parameters
    ----------
    grav : float
        gravitation [m/s^2]
    rho : float
        density of water [t/m^3]
    """
    grav = 9.81
    rho = 1.025

    def __init__(self):
        self.est_added_mass = 0

    def natural_period_heave(self, mass, waterplane_area, added_mass=None):

        if added_mass is not None:
            return round(2 * np.pi * np.sqrt((mass + added_mass) / (self.rho * self.grav * waterplane_area)), 1)
        else:
            return round(2 * np.pi * np.sqrt((mass + self.est_added_mass) / (self.rho * self.grav * waterplane_area)), 1)


class SimplifiedCylinder(SimplifiedFloater):

    def __init__(self):
        super().__init__()
        self.est_added_mass = 0

    def estimated_added_mass(self, diameter: float):
        """
        Estimated heave added mass of a cylinder.
        diameter : float
            Diameter of cylinder [m]
        return : Added mass [kg]

        Notes
        -----
        The added mass for a cylinder is approximated by Lamb classical solution, 1932: A_33 = 1/3*rho*D^3
        """
        if diameter > 0:
            self.est_added_mass = 1 / 3 * self.rho * diameter ** 3
            return round(self.est_added_mass, 1)
        else:
            raise ValueError("Make sure to have positive input scalar")


class SimplifiedBarge(SimplifiedFloater):

    def __init__(self):
        super().__init__()
        self.est_added_mass = 0

    def estimated_added_mass(self, width: float, draft: float, length: float):
        """
        Estimated heave added mass of a barge.
        length : float
            Length of barge [m]
        width : float
            Width of barge [m]
        draft : draft of geometry
        return : Added mass [kg]

        Notes
        -----
        The added mass for a barge is approximated by Lewis numerical study (A_33 = cm * pi * rho * (width/2)^2 * length)
        """
        if width > 0 or draft > 0 or length > 0:
            self.est_added_mass = self.estimated_added_mass_coefficient(width, draft) \
                                  * self.rho * np.pi * width**2 / 4 * length
            return round(self.est_added_mass, 1)
        else:
            raise ValueError("Make sure to have positive input scalars")

    def estimated_added_mass_coefficient(self, width: float, draft: float):
        """
        Estimation of added mass coefficient for a rectangular 2d geometry
        :param width: with of geometry
        :param draft: draft of the geometry
        :return: estimated added mass coefficient of a rectangular approximated by line fit of Lewis numerical study
        """
        return 1.5937 * (draft/width)**0.121

