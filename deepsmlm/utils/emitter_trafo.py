import torch
from deepsmlm.generic import emitter

"""
Predefined transformations, e.g. for the SMLM challenge.
Factors and shifts are with respect to (possibly) changed axis, i.e. in the new system.
"""

challenge_import = {
    'desc': 'Challenge data transformation to match this framework.',
    'xy_unit': 'nm',
    'px_size': (100., 100.),
    'xyz_axis': (1, 0, 2),
    'xyz_nm_factor': (1., 1., -1.),
    'xyz_nm_shift': (-150., -50., 0.),
    'xyz_px_factor': None,
    'xyz_px_shift': None,
    'frame_ix_shift': -1
}


def transform_emitter(em: emitter.EmitterSet, trafo: dict) -> emitter.EmitterSet:

    mod_em = em.clone()

    """Modify 'Meta'"""
    mod_em.xy_unit = trafo['xy_unit'] if trafo['xy_unit'] is not None else mod_em.xy_unit
    mod_em.px_size = torch.tensor(trafo['px_size']) if trafo['px_size'] is not None else mod_em.px_size

    """Modify proper attributes"""
    if trafo['xyz_axis'] is not None:
        mod_em.xyz = mod_em.xyz[:, trafo['xyz_axis']]

    if trafo['xyz_nm_factor'] is not None:
        mod_em.xyz_nm *= torch.tensor(trafo['xyz_nm_factor'])

    if trafo['xyz_nm_shift'] is not None:
        mod_em.xyz_nm += torch.tensor(trafo['xyz_nm_shift'])

    if trafo['xyz_px_factor'] is not None:
        mod_em.xyz_px *= torch.tensor(trafo['xyz_px_factor'])

    if trafo['xyz_px_shift'] is not None:
        mod_em.xyz_px += torch.tensor(trafo['xyz_px_shift'])

    if trafo['frame_ix_shift'] is not None:
        mod_em.frame_ix += torch.tensor(trafo['frame_ix_shift'])

    return mod_em
