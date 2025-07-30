import py21cmfast as p21c
from py21cmfast.io.caching import RunCache, CacheConfig
import numpy as np

p21c.config['HALO_CATALOG_MEM_FACTOR'] = 1.4

cache = p21c.OutputCache('/ocean/projects/phy210034p/breitman/EOS25/EOS25_L2100_HIIDIM1400_DIM4200')


inputs = p21c.InputParameters.from_template("EOS25.toml", random_seed=1234)
runcache = RunCache.from_inputs(inputs, cache=cache)
initial_conditions = runcache.get_ics()
inputs = initial_conditions.inputs  # use the real inputs, with correct node_redshifts

p21c.drivers.coeval.evolve_perturb_halos(inputs=inputs,
                    initial_conditions=initial_conditions,
                    regenerate=False,
                    all_redshifts=inputs.node_redshifts,
                    write=CacheConfig(),
                    cache=cache,
)
    
