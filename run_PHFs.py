import py21cmfast as p21c
from py21cmfast.io.caching import RunCache, CacheConfig
import numpy as np

p21c.config['HALO_CATALOG_MEM_FACTOR'] = 2.

cache = p21c.OutputCache('/home/dbreitman/EOS25/TEST_L600_HIIDIM400_DIM1200_NO_PERTURN_ON_HIGH_RES')


inputs = p21c.InputParameters.from_template("/home/dbreitman/EOS25/TEST_L600_HIIDIM400_DIM1200_NO_PERTURN_ON_HIGH_RES/config-7dd812.toml", random_seed=1234)
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
    
