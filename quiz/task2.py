class MooringChain:
    """
    Model of mooring chain cross section
    Parameters
    ----------
    quality : str
        Chain material quality (R3, R3S, R4, R4S or R5)
    stud : bool
        Studded chain (True) or studless chain (False)
    References
    ----------
    .. [1] DNVGL-OS-E302, "Offshore mooring chain", 2015
    """

    def __init__(self, quality: str, stud: bool):
        self.stud = stud
        if quality.upper() not in ['R3', 'R3S', 'R4', 'R4S', 'R5']:
            raise ValueError(f"Invalid chain quality: '{quality.upper()}'")
        self.quality = quality.upper()

    def factor_strength(self):
        """float: Ratio of breaking strength to `diameter^2 * (44 - 0.08*diameter)` per [1] for the
        specified material quality (kN / mm^2 - ich)."""
        quality_strength = dict(R3=0.0223, R3S=0.0249, R4=0.0274, R4S=0.0304, R5=0.0320)
        return quality_strength[self.quality]

    def factor_dry_weight(self):
        """float: Ratio of unit length dry weight to diameter squared per [1] (N / m^2 / m)."""
        if self.stud:
            return 0.0219 * 1.e6 * 9.81
        elif not self.stud:
            return 0.0200 * 1.e6 * 9.81

    def breaking_strength(self, diameter: float):
        """
        Chain breaking strength aka. MBL.
        Parameters
        ----------
        diameter : float
            Cross section diameter (m).
        Returns
        -------
        float
            Cross section breaking strength (N).
        Notes
        -----
        The strength is calculated as `factor_strength * (diameter*1000)^2 * (44 - 0.08*diameter*1000) * 1000`
        (with SI units). See [1].
        """
        return self.factor_strength() * pow(diameter * 1000, 2) * (44 - 0.08 * diameter * 1000) * 1000

    def dry_weight(self, diameter: float):
        """
        Cross section dry weight per unit length.
        Parameters
        ----------
        diameter : float
            Diameter (m) of cross section for which the corresponding break load should be returned
        Returns
        -------
        float
            Dry weight per unit length of chain (N / m)
        """
        return self.factor_dry_weight() * pow(diameter, 2)
