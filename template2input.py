"""
Stolen from 21cmFAST repo.

"""

import contextlib
import logging
import tomllib
import warnings
from pathlib import Path

import attrs

from py21cmfast.wrapper._utils import camel_to_snake
from py21cmfast.wrapper.inputs import InputStruct

logger = logging.getLogger(__name__)


def _construct_param_objects(template_dict, **kwargs):
    input_classes = {c.__name__: c for c in InputStruct.__subclasses__()}

    input_dict = {}
    for k, c in input_classes.items():
        fieldnames = [field.name for field in attrs.fields(c)]
        kw_dict = {kk: kwargs.pop(kk) for kk in fieldnames if kk in kwargs}
        arg_dict = {**template_dict[k], **kw_dict}
        input_struct = c.new(arg_dict)
        input_dict[camel_to_snake(k)] = input_struct

    if kwargs:
        warnings.warn(
            f"Excess arguments to `create_params_from_template` will be ignored: {kwargs}",
            stacklevel=2,
        )

    return input_dict



def load_template_file(template_name: str | Path):
    """
    Handle the loading of template TOML files.

    First it checks for a file with the name given,
    then it checks for a native template with that name,
    throwing an error if neither are found.
    """
    if Path(template_name).is_file():
        with Path(template_name).open("rb") as template_file:
            return tomllib.load(template_file)

    raise ValueError("Invalid template path", template_name)


def create_params_from_template(template_name: str | Path, **kwargs):
    """
    Construct the required InputStruct instances for a run from a given template.

    Parameters
    ----------
    template_name: str,
        defines the name/alias of the native template (see templates/manifest.toml for a list)
        alternatively, is the path to a TOML file containing tables titled [CosmoParams],
        [SimulationOptions], [AstroParams] and [AstroOptions] with parameter settings

    Other Parameters
    ----------------
    Any other parameter passed is considered to be a name and
    value of a parameter in any of the `InputStruct` subclasses,
    and will be used to over-ride the template values.

    Returns
    -------
    input_dict : dict containing:
        cosmo_params : CosmoParams
            Instance containing cosmological parameters
        simulation_options : SimulationOptions
            Instance containing general run parameters
        simulation_options : MatterOptions
            Instance containing general run flags and enums
        astro_params : AstroParams
            Instance containing astrophysical parameters
        astro_options : AstroOptions
            Instance containing astrophysical flags and enums
    """
    template = load_template_file(template_name)

    return _construct_param_objects(template, **kwargs)
