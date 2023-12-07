#Quaye Richard
# 14 October 2023
#Testing and fixing functions

import pytest
from get_water import *

def qr_test_water_column_height():
    assert qr_water_column_height(36.6, 9.1) == 45.7

def qr_test_pressure_gain_from_water_height():
    assert qr_pressure_gain_from_water_height(45.7) == 448.46

def qr_test_pressure_loss_from_pipe():
    assert qr_pressure_loss_from_pipe(0.28687, 1524.0, 0.013, 1.65) == 90.35
    assert qr_pressure_loss_from_pipe(0.048692, 15.2, 0.018, 1.75) == 4.86

def qr_test_pressure_loss_from_fittings():
    assert qr_pressure_loss_from_fittings(0, 3) == 0
    assert qr_pressure_loss_from_fittings(1.65, 0) == 0
    assert pytest.approx(qr_pressure_loss_from_fittings(1.65, 2), abs=0.001) == -0.109
    assert pytest.approx(qr_pressure_loss_from_fittings(1.75, 2), abs=0.001) == -0.122
    assert pytest.approx(qr_pressure_loss_from_fittings(1.75, 5), abs=0.001) == -0.306

def test_reynolds_number():
    assert test_reynolds_number(0.048692, 0) == 0
    assert test_reynolds_number(0.048692, 1.65) == 80069
    assert test_reynolds_number(0.048692, 1.75) == 84922
    assert test_reynolds_number(0.28687, 1.65) == 471729
    assert test_reynolds_number(0.28687, 1.75) == 500318

def qr_test_pressure_loss_from_pipe_reduction():
    assert pytest.approx(qr_pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692), abs=0.001) == 0
    assert pytest.approx(qr_pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692), abs=0.001) == -163.744
    assert pytest.approx(qr_pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692), abs=0.001) == -184.182

if __name__ == "__main__":
    pytest.main()



