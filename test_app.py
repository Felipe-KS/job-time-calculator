from typing import final
import pytest
import manageString
import calculation

def test_treating_string_format():
    string = "felipe = SU 08:00 - 12:00\n"
    assert manageString.treatingString(string) == "FELIPE=SU08:00-12:00"

def test_braking_string():
    string = "FELIPE=MO08:00-18:00,SU08:00-12:00"
    assert manageString.breakingStr(string) == ["FELIPE", [["MO",["08:00","18:00"]],["SU",["08:00","12:00"]]]]

def test_duplicatin_separators():
    string = "FELIPE==MO08:00-18:00,SU08:00-12:00"
    assert manageString.breakingStr(string) == -3

def test_invalid_day():
    l = [["ML",["08:00","18:00"]]]
    assert calculation.calculatingPayment(l) == [-1]

def test_payment_calculation():
    time = [["MO",["10:00","18:00"]],["SU",["10:00","12:00"]]]
    assert calculation.calculatingPayment(time) == [120.0, 40.0]

def test_time_00_00():
    time = ["23:00","00:00"]
    assert calculation.findPeriod(time) == [0,0,1]

def test_timestart_bigger_than_timestop():
    time = ["18:00","10:00"]
    assert calculation.findPeriod(time) == -2

@pytest.mark.parametrize("time, response", [(["12:80","15:00"], -2), (["24:00", "03:00"], -2)])
def test_time_of_work_bigger_than_normal_minutes(time, response):
    assert calculation.findPeriod(time) == response

def test_time_is_not_number():
    time = ["AA:00","10:00"]
    assert calculation.findPeriod(time) == -2