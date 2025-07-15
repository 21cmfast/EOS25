import py21cmfast as p21c
import numpy as np
from template2input import create_params_from_template
import argparse

parser.add_argument("--z_idx", type = int)
z_idx = parser.parse_args().z_idx

cache = p21c.OutputCache('/ocean/projects/phy210034p/breitman/EOS25/EOS25_L4095_HIIDIM1365_DIM2048')

inputs = p21c.InputParameters(**create_params_from_template("EOS25_full.toml"),
        node_redshifts=p21c.wrapper.inputs.get_logspaced_redshifts(
            min_redshift=5.0,
            z_step_factor=1.02,
            max_redshift=35.0,
        ),
        random_seed=1234,
    )

initial_conditions = p21c.io.h5.read_output_struct("/ocean/projects/phy210034p/breitman/EOS25/EOS25_L4095_HIIDIM1365_DIM2048/aa3f843276bd385be155ef7cef5ac7c8/1234/InitialConditions.h5")

z = inputs.node_redshifts[z_idx]

p21c.perturb_field(redshift=z, 
                   initial_conditions=initial_conditions,
                   write=True,
                   cache=cache,
)
    
