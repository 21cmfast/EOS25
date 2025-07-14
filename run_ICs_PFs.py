import py21cmfast as p21c
import numpy as np
from template2input import create_params_from_template

cache = p21c.OutputCache('/ocean/projects/phy210034p/breitman/EoS25')

inputs = p21c.InputParameters.from_template(
        'latest-dhalos',
        node_redshifts=p21c.wrapper.inputs.get_logspaced_redshifts(
            min_redshift=5.0,
            z_step_factor=1.02,
            max_redshift=35.0,
        ),
        random_seed=1234,
    ).evolve_input_structs(HII_DIM=1300, 
                           BOX_LEN=2000,
                           DIM = 1300*2,
                           KEEP_3D_VELOCITIES=True, 
                           APPLY_RSDS=False,
                           N_THREADS=25, 
                           MINIMIZE_MEMORY=False, #This gives me a seg fault
                           SAMPLER_MIN_MASS=1e9)


initial_conditions = p21c.compute_initial_conditions(
    inputs=inputs, cache=cache, write=True
)

for z in inputs.node_redshifts:
    p21c.perturb_field(
    redshift=z, 
    initial_conditions=initial_conditions,
    write=True,cache=cache,
    )
