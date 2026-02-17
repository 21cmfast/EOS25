import py21cmfast as p21c
import numpy as np
from template2input import create_params_from_template
from time import time

cache = p21c.OutputCache('/ocean/projects/phy210034p/breitman/EOS25/')

inputs = p21c.InputParameters(**create_params_from_template("EOS25.toml"),
        node_redshifts=p21c.wrapper.inputs.get_logspaced_redshifts(
            min_redshift=5.0,
            z_step_factor=1.02,
            max_redshift=35.0,
        ),
        random_seed=42,
    ) 


initial_conditions = p21c.compute_initial_conditions(
    inputs=inputs, cache=cache, write=True
)

for z in inputs.node_redshifts:
    p21c.perturb_field(
    redshift=z, 
    initial_conditions=initial_conditions,
    write=True,cache=cache,
    )
