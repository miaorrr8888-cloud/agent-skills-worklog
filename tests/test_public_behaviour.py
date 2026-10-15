from pathlib import Path
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
R=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

class PublicBehaviour(unittest.TestCase):
    def test_identical_images_produce_similarity_report(self):
        from PIL import Image,ImageDraw
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder); image=Image.new('L',(120,80),0); draw=ImageDraw.Draw(image)
            draw.rectangle((20,15,30,65),fill=255); draw.rectangle((30,15,80,25),fill=255)
            draw.rectangle((60,40,80,50),fill=255); image.save(p/'truth.png')
            command=[sys.executable,str(R/'ai-asset-legibility-audit/references/legibility_audit.py'),
                     '--truth',str(p/'truth.png'),'--test',str(p/'truth.png'),
                     '--truth-box','0,0,120,80','--test-box','0,0,120,80','--out',str(p/'qa')]
            result=subprocess.run(command,capture_output=True,env={**os.environ,'PYTHONUTF8':'1'})
            self.assertEqual(result.returncode,0,result.stdout.decode('utf-8',errors='replace'))
            report=json.loads((p/'qa/legibility_verdict.json').read_text())
            self.assertEqual(report['verdict'],'HIGH_SIMILARITY')
            self.assertGreater(report['best_iou'],0.99)

    def test_low_similarity_does_not_claim_generated_origin(self):
        m=load('similarity',R/'ai-asset-legibility-audit/references/legibility_audit.py')
        label,note=m.verdict_from_best(0.1)
        self.assertEqual(label,'LOW_SIMILARITY'); self.assertIn('unknown',note)

    def test_profile_path_rejected_without_opening_content(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder); (p/'browser_profile').mkdir(); (p/'browser_profile/Cookies').write_bytes(b'fixture')
            result=subprocess.run([sys.executable,str(R/'github-secret-gated-baseline/scripts/gate_scan.py')],cwd=p,capture_output=True)
            self.assertEqual(result.returncode,1); self.assertIn(b'sensitive_or_symlink_path',result.stdout)

    def test_external_state_requires_note_and_human_flag(self):
        m=load('ceiling',R/'evidence-gated-lead-pipeline/references/automation_ceiling.py')
        self.assertFalse(m.check_advance('CONTACT_READY','CONTACTED',human=False)[0])
        self.assertFalse(m.check_advance('CONTACT_READY','CONTACTED',human=True)[0])
        self.assertTrue(m.check_advance('CONTACT_READY','CONTACTED',note='manually sent; receipt available',human=True)[0])

if __name__=='__main__': unittest.main()
