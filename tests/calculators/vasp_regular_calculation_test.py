# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize('valid_input', ['incar', 'kpoints', 'poscar',
                         'potcar', 'restart'])
def test_input_port_availability(valid_input):
    from aiida.plugins import CalculationFactory
    inputs = CalculationFactory('cusp.vasp').get_builder()._valid_fields
    assert valid_input in inputs
