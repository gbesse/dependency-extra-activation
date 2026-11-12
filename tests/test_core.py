import unittest,copy,json
from dependency_extra_activation import run
DEMO={'packages': [{'id': 'app', 'requirements': [{'package': 'engine', 'when_extra': 'fast', 'activate_extras': ['simd']}]}, {'id': 'engine', 'requirements': [{'package': 'native', 'when_extra': 'simd'}]}, {'id': 'native'}], 'roots': [{'package': 'app', 'extras': ['fast']}]}
class DomainTests(unittest.TestCase):
 def test_transitive_extra_activation(self):
  x=run(DEMO);self.assertEqual([r['package']for r in x['closure']],['app','engine','native'])
 def test_unused_extra_is_not_dependency(self):
  x=run(dict(DEMO,roots=[{'package':'app'}]));self.assertEqual(x['closure'],[{'package':'app','extras':[]}])
 def test_cycle_reaches_fixed_point(self):
  x=copy.deepcopy(DEMO);x['packages'][-1]['requirements']=[{'package':'app','activate_extras':['fast']}];self.assertEqual(len(run(x)['closure']),3)
