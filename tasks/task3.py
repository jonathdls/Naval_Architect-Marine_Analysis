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
        self.wp_area = 0

    def natural_period_heave(self, mass, waterplane_area=None, added_mass=None):
        """
        Uncoupled and undamped natural period in heave
        :param mass: float
            Mass of structure [t]
        :param waterplane_area: float
            waterplane_area of structure [m^2]
        :param added_mass: float
            estimated added mass in heave for structure [t]
        :return:
        """
        if added_mass is not None and waterplane_area is not None:
            return round(2 * np.pi * np.sqrt((mass + added_mass) / (self.rho * self.grav * waterplane_area)), 1)
        elif added_mass is not None and self.wp_area != 0:
            return round(2 * np.pi * np.sqrt((mass + self.est_added_mass) / (self.rho * self.grav * self.wp_area)), 1)
        elif waterplane_area is not None:
            return round(2 * np.pi * np.sqrt((mass + self.est_added_mass) / (self.rho * self.grav * waterplane_area)), 1)
        elif self.wp_area != 0:
            return round(2 * np.pi * np.sqrt((mass + self.est_added_mass) / (self.rho * self.grav * self.wp_area)), 1)
        else:
            return ValueError("Make sure to have a positive waterplane area, can be calculated through SimplfiedBarge"
                              "or SimplifiedCylinder or manual input")


class SimplifiedCylinder(SimplifiedFloater):
    """
    Simplified calculation of cylinder added mass, and calculation of waterplane area
    Parameters
    ----------
    diameter : float
        diameter of cylinder [m]
    """

    def __init__(self, diameter: float):
        super().__init__()
        self.est_added_mass = 0
        self.diameter = diameter
        self.est_added_mass = self.estimated_added_mass
        self.wp_area = self.waterplane_area

    @property
    def estimated_added_mass(self):
        """
        Estimated heave added mass of a cylinder.
        return : Added mass [t]

        Notes
        -----
        The added mass for a cylinder is approximated by Lamb classical solution, 1932: A_33 = 1/3*rho*D^3
        """
        if self.diameter > 0:
            self.est_added_mass = 1 / 3 * self.rho * self.diameter ** 3
            return round(self.est_added_mass, 1)
        else:
            raise ValueError("Make sure to have positive input scalar")

    @property
    def waterplane_area(self):
        """
        Waterplane area of cylinder
        :return: Waterplane area of cylinder [m^2]
        """
        return np.pi * self.diameter**2 / 4


class SimplifiedBarge(SimplifiedFloater):
    """
    Simplified calculation of barge added mass, and calculation of waterplane area
    Parameters
    ----------
    width : float
        width of barge [m]
    draft : float
        draft of barge [m]
    length : float
        length of barge [m]
    """

    def __init__(self, width: float, draft: float, length: float):
        super().__init__()
        self.est_added_mass = 0
        self.width = width
        self.draft = draft
        self.length = length
        self.est_added_mass = self.estimated_added_mass
        self.wp_area = self.waterplane_area

    @property
    def estimated_added_mass(self):
        """
        Estimated heave added mass of a barge.
        return : Added mass [t]

        Notes
        -----
        The added mass for a barge is approximated by Lewis numerical study
        A_33 = cm * pi * rho * (width/2)^2 * length
        """
        if self.width > 0 and self.draft > 0 and self.length > 0:
            return self.estimated_added_mass_coefficient \
                                  * self.rho * np.pi * self.width**2 / 4 * self.length
        else:
            raise ValueError("Make sure to have positive input scalars")

    @property
    def estimated_added_mass_coefficient(self):
        """
        Estimation of added mass coefficient (cm) for a rectangular 2d geometry
        :return: estimated added mass coefficient of a rectangular approximated by line fit of Lewis numerical study
        """
        return 1.5937 * (self.draft/self.width)**0.121

    @property
    def waterplane_area(self):
        """
        Waterplane area of barge
        :return: Waterplane area [m^2]
        """
        return self.width * self.length
