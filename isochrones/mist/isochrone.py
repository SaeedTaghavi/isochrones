
from ..isochrone import FastIsochrone
from .grid import MISTModelGrid

class MIST_Isochrone(FastIsochrone):
    """MESA Isochrones and Stellar Tracks

    :param bands: (optional)
        List of desired photometric bands.  Default list of bands is
        ``['G','B','V','J','H','K','W1','W2','W3','g','r','i','z','Kepler']``.
        Here ``B`` and ``V`` are Tycho-2 mags, `griz` are SDSS, and ``G`` is
        Gaia G-band.

    Details of models are `here <http://waps.cfa.harvard.edu/MIST/>`_.

    """
    name = 'mist'
    eep_col = 'EEP'
    age_col = 'log10_isochrone_age_yr'
    feh_col = '[Fe/H]'
    mass_col = 'star_mass'
    logTeff_col = 'log_Teff'
    logg_col = 'log_g'
    logL_col = 'log_L'
    modelgrid = MISTModelGrid
    default_bands = ('G','B','V','J','H','K','W1','W2','W3','g','r','i','z','Kepler')

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version', MISTModelGrid.default_kwargs['version'])
        if self.version == '1.1':
            self.default_bands = self.default_bands + ('TESS', 'BP', 'RP')

        super().__init__(*args, **kwargs)
