"""Synthetic validation records only: these are not human reviews/personas."""
import unittest
from review_gate import assess,DIMENSIONS

def fixture(id,packet):
 v={'reviewer_id':id,'viewing_context':'SYNTHETIC TEST','prior_exposure':'SYNTHETIC TEST','human':'on','independent':'on','all_media':'on'}
 for w in (1440,390):
  v[f'{w}_preference']='TIE';v[f'{w}_reason']='SYNTHETIC TEST ONLY'
  for d in DIMENSIONS:
   for l in ('X','Y'):v[f'{w}_{d}_{l}']='NA'
 return {'schema':'creative-quality-human-response/1','packet':packet,'source':'SELF_REPORTED_HUMAN_UNVERIFIED','values':v}

class GateTests(unittest.TestCase):
 def test_empty_is_waiting(self):
  r=assess([]);self.assertFalse(r['intake_complete']);self.assertEqual(r['gate'],'AWAITING_HUMAN_REVIEW')
 def test_complete_forms_do_not_certify_humans(self):
  r=assess([fixture('synthetic-1','R1'),fixture('synthetic-2','R2')]);self.assertTrue(r['intake_complete']);self.assertEqual(r['gate'],'AWAITING_HUMAN_REVIEW');self.assertEqual(r['owner_acceptance'],'NOT_GIVEN')
 def test_duplicate_id_or_packet_rejected(self):
  self.assertFalse(assess([fixture('same','R1'),fixture('same','R1')])['intake_complete'])
 def test_missing_viewport_reason_rejected(self):
  r=fixture('synthetic-1','R1');del r['values']['390_reason'];self.assertFalse(assess([r,fixture('synthetic-2','R2')])['intake_complete'])
if __name__=='__main__':unittest.main()
