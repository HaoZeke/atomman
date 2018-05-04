# Standard Python libraries
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

# 
try:
    import spglib
    has_spglib = True
except:
    has_spglib = False

def dump(system):
    """
    Convert an atomman.System into the cell tuple used by spglib.
    
    Parameters
    ----------
    system : atomman.System
        A atomman representation of a system.
    
    Returns
    -------
    tuple
        (lattice, positions, and numbers) used as inputs for spglib.
    """
    
    assert has_spglib, 'spglib not imported'
    
    # Get lattice information
    lattice = system.box.vects
    
    # Get atomic positions (in reduced coordinates)
    positions = system.atoms_prop(key='pos', scale=True)
    
    # Get atom numbers (atypes)
    numbers = system.atoms.atype
    
    return (lattice, positions, numbers)