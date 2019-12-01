# This file shall be deleted so to ensure that the coiled code is used.


def model_test_scaling(full_scale_diameter):
    """
    Scales and prints statistical parameters from 5 model test measurement channels in the specified full scale.
    The model test scale is defined by the waterline diameter of the full scale unit.

    Parameters
    ----------
    full_scale_diameter: float
        Water line diameter (m) of full scale unit, which the model test data is scaled to
    """
    model_scale_data = [{'channel': 1,
                         'name': 'Heave',
                         'max_value': 0.1,
                         'min_value': -0.098,
                         'std_value': 0.02913,
                         'mean_value': -0.00000011,
                         'unit': 'm',
                         'factor': 1},
                        {'channel': 2,
                         'name': 'Pitch',
                         'max_value': 10.832,
                         'min_value': -7.259,
                         'std_value': 2.031,
                         'mean_value': 0.149,
                         'unit': 'deg',
                         'factor': 0},
                        {'channel': 3,
                         'name': 'Vertical acceleration',
                         'max_value': 1.932,
                         'min_value': -2.028,
                         'std_value': 0.62124,
                         'mean_value': -0.0011,
                         'unit': 'm/s^2',
                         'factor': 0},
                        {'channel': 4,
                         'name': 'Bilge box bending moment',
                         'max_value': 0.000864635,
                         'min_value': -0.00060473969,
                         'std_value': 0.00013577,
                         'mean_value': 0.00004477,
                         'unit': 'kNm',
                         'factor': 3.5},  # built-in error (should be 4)
                        {'channel': 5,
                         'name': 'Tension, line 3',
                         'max_value': 0.0234897,
                         'min_value': 0.00259679,
                         'std_value': 0.00224897959,
                         'mean_value': 0.008546,
                         'unit': 'kN',
                         'factor': 3}
                        ]

    print("{:1} {:<24} {:<5} {:>9} {:>9} {:>9} {:>9}".format('#', 'Name', 'Unit', 'Max', 'Min', 'Std', 'Mean'))
    for d in model_scale_data:
        chn = d['channel']
        name = d['name']
        unit = d['unit']
        max_v = froude_multiplier(d['max_value'], full_scale_diameter, d['factor'])
        min_v = froude_multiplier(d['min_value'], full_scale_diameter, d['factor'])
        std_v = froude_multiplier(d['std_value'], full_scale_diameter, d['factor'])
        mean_v = froude_multiplier(d['mean_value'], full_scale_diameter, d['factor'])
        print("{:1} {:<24} {:<5} {:>9.2f} {:>9.2f} {:>9.2f} {:>9.2f}".format(chn, name, unit, max_v, min_v, std_v, mean_v))


def froude_multiplier(value, scale, factor ):
    return value * scale ** factor
