from pathlib import Path
import importlib.util
import unittest
R=Path(__file__).resolve().parents[1]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

class Evidence(unittest.TestCase):
    def setUp(self): self.m=load('evidence',R/'evidence-gated-lead-pipeline/references/evidence_gate.py')
    def test_spoofed_upwork_host_rejected(self):
        self.assertFalse(self.m.classify_evidence('https://www.upwork.com.attacker.example/freelance-jobs/apply/job_~123','Upwork')[1])
    def test_category_page_is_downgraded(self):
        lead,changed=self.m.apply_gate({'channel':'Upwork','evidence_url':'https://www.upwork.com/hire/editors/','acquisition_path':'RESPOND_TO_JOB_POST'})
        self.assertTrue(changed); self.assertEqual(lead['evidence_url_status'],'FLAGGED')
    def test_unknown_third_party_stays_unknown(self):
        lead,changed=self.m.apply_gate({'channel':'TikTok Shop','evidence_url':'https://example.org/post','acquisition_path':'RESPOND_TO_JOB_POST'})
        self.assertFalse(changed); self.assertEqual(lead['evidence_url_status'],'THIRD_PARTY')

class Ranking(unittest.TestCase):
    def test_unknown_and_nonfinite_views_are_not_verified(self):
        m=load('ranking',R/'product-video-reverse-search/scripts/extract_and_rank.py')
        for value in [None,'not a number',float('inf'),float('nan')]: self.assertIsNone(m.interaction_score(value))
        self.assertEqual(m.interaction_score(0),0)

if __name__=='__main__': unittest.main()
