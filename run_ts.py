import py21cmfast as p21c
from py21cmfast.io.caching import RunCache
import numpy as np
from template2input import create_params_from_template
import argparse

parser.add_argument("--z_idx", type = int)
z_idx = parser.parse_args().z_idx

cache = p21c.OutputCache('/ocean/projects/phy210034p/breitman/EOS25/EOS25_L2100_HIIDIM1400_DIM4200')

inputs = p21c.InputParameter.from_template("EOS25_full.toml", random_seed=1234)
runcache = RunCache.from_inputs(inputs, cache=cache)
initial_conditions = runcache.get_ics()
inputs = initial_conditions.inputs  # use the real inputs, with correct node_redshifts
z = inputs.node_redshifts[z_idx]

halolist_init = p21c.determine_halo_list(
    redshift=inputs.node_redshifts[-1],
    initial_conditions=initial_conditions,
    inputs=inputs
)

pt_halos = p21c.perturb_halo_list(
    halo_field=halolist_init, initial_conditions=initial_conditions,
)

#Load the PF pt_field
halo_box = p21c.compute_halo_grid(perturbed_field=pt_field, 
                                  perturbed_halo_list=pt_halos, 
                                  initial_conditions=initial_conditions
                                  )

# Make list of all previous hbox_arr += [this_halobox]

this_xraysrouce = p21c.compute_xray_source_field(
                        redshift=z,
                        hboxes=hbox_arr,
                        write=True,
                    )
this_spin_temp = p21c.compute_spin_temperature(
                    inputs=inputs,
                    previous_spin_temp=getattr(prev_coeval, "ts_box", None),
                    perturbed_field=this_perturbed_field,
                    xray_source_box=this_xraysrouce,
                    write=True,
                )
