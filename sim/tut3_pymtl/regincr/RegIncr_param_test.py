import pytest

from random import sample
from pymtl import *
from pclib.test import run_test_vector_sim, mk_test_case_table
from RegIncr import RegIncr

def mk_test_vector_table(nbits, inputs):
  inputs.extend([0])

  test_vector_table = [('in_ out*')]
  last_result = '?'
  for input_ in inputs:
    test_vector_table.append( [input_, last_result])
    last_result = Bits(nbits, input_ + 1, trunc=True)

  return test_vector_table

@pytest.mark.parametrize( "n", [3,4,5,6])
def test_random(n, dump_vcd):
  run_test_vector_sim(RegIncr(bitwidth=n),
    mk_test_vector_table(n, sample(range(2**n),2) ), dump_vcd)