from pathlib import Path
import importlib.util, unittest, tempfile, subprocess, sys, json, zipfile, io, os

R=Path(__file__).resolve().parents[1]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

class SecurityGate(unittest.TestCase):
    script=R/'github-secret-gated-baseline/scripts/gate_scan.py'
    def scan(self,root,*args): return subprocess.run([sys.executable,str(self.script),*args],cwd=root,capture_output=True,text=True)
    def test_clean_and_secret_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'config.py'; p.write_text('value = 123\n')
            self.assertEqual(self.scan(d).returncode,0)
            fake='nvapi-'+'Ab9Zx7Qw5Er3Ty1Ui2Op4As6Df8Gh0Jk'
            p.write_text('value = "'+fake+'"\n')
            result=self.scan(d); self.assertEqual(result.returncode,1); self.assertNotIn(fake,result.stdout)
    def test_tracked_not_git_fails(self):
        with tempfile.TemporaryDirectory() as d: self.assertNotEqual(self.scan(d,'--tracked').returncode,0)
    def test_empty_scope_is_error(self):
        with tempfile.TemporaryDirectory() as d: self.assertEqual(self.scan(d).returncode,2)
    def test_env_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/'.env').write_text('EMPTY='); self.assertEqual(self.scan(d).returncode,1)

class Assets(unittest.TestCase):
    def test_absolute_relative_relationships_and_xml_attributes(self):
        m=load('xlsx',R/'product-real-asset-library/scripts/xlsx_cellimage_map.py')
        for target in ['/xl/worksheets/sheet1.xml','worksheets/sheet1.xml']:
            with zipfile.ZipFile(io.BytesIO(),'w') as z:
                z.writestr('xl/workbook.xml','<workbook xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet r:id="rId1" name="A &amp; B" /></sheets></workbook>')
                z.writestr('xl/_rels/workbook.xml.rels',f'<Relationships><Relationship Target="{target}" Id="rId1" /></Relationships>')
                self.assertEqual(m.sheet_map(z),{'A & B':'xl/worksheets/sheet1.xml'})
    def test_relationship_escape_rejected(self):
        m=load('xlsx',R/'product-real-asset-library/scripts/xlsx_cellimage_map.py')
        with self.assertRaises(ValueError): m.resolve_target('../../private')
    def test_xml_text_entities(self):
        m=load('xlsx',R/'product-real-asset-library/scripts/xlsx_cellimage_map.py')
        self.assertEqual(m.text_of('<t>A &amp; B</t>'),'A & B')

class Legibility(unittest.TestCase):
    def setUp(self): self.m=load('legibility',R/'ai-asset-legibility-audit/references/legibility_audit.py')
    def test_roi_outside_image_rejected(self):
        import numpy as np
        for box in [(-1,0,2,2),(0,0,10,2),(0,0,0,2)]:
            with self.assertRaises(ValueError): self.m.crop(np.zeros((5,5)),box)
    def test_empty_and_full_masks_do_not_pass(self):
        import numpy as np
        ref=np.zeros((10,10),bool); ref[1:4,1:4]=True
        self.assertFalse(self.m._coverage_ok(np.zeros_like(ref),ref)); self.assertFalse(self.m._coverage_ok(np.ones_like(ref),ref))
    def test_nonfinite_is_unknown(self):
        for v in [float('nan'),float('inf'),-float('inf')]: self.assertEqual(self.m.verdict_from_best(v)[0],'UNKNOWN')

class Anchors(unittest.TestCase):
    def test_counterexample_and_source_preserved(self):
        m=load('anchor',R/'falsifiable-assertion-anchors/scripts/check_anchor.py')
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'value.py'; p.write_text('VALUE=2\n')
            result=m.verify(d,'value.py','VALUE=2','VALUE=1',[sys.executable,'-c','import value; assert value.VALUE==2'])
            self.assertEqual(result['status'],'PASS'); self.assertEqual(p.read_text(),'VALUE=2\n')
    def test_tautology_fails(self):
        m=load('anchor',R/'falsifiable-assertion-anchors/scripts/check_anchor.py')
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/'value.py').write_text('VALUE=2\n')
            self.assertEqual(m.verify(d,'value.py','VALUE=2','VALUE=1',[sys.executable,'-c','assert True'])['status'],'FAIL')
    def test_missing_anchor_rejected(self):
        m=load('anchor',R/'falsifiable-assertion-anchors/scripts/check_anchor.py')
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/'value.py').write_text('VALUE=2\n')
            with self.assertRaises(ValueError): m.verify(d,'value.py','VALUE=3','VALUE=1',[sys.executable,'-c','assert True'])

class Gallery(unittest.TestCase):
    def fixture(self,d,**overrides):
        p=Path(d); (p/'a.png').write_bytes(b'fixture-only'); (p/'b.png').write_bytes(b'fixture-only')
        card={'anchor':'a.png','image':'b.png','prompt':'<script>bad</script>','status':'UNKNOWN'}; card.update(overrides)
        manifest=p/'manifest.json'; manifest.write_text(json.dumps({'anchor':'a.png','variants':[card]})); return manifest
    def test_gallery_escapes_prompt_and_copies(self):
        m=load('gallery',R/'same-object-visual-dictionary/scripts/build_gallery.py')
        with tempfile.TemporaryDirectory() as d:
            page=m.build(self.fixture(d),Path(d)/'out'); self.assertNotIn('<script>',page.read_text()); self.assertEqual(len(list((page.parent/'images').iterdir())),2)
    def test_mixed_anchor_rejected(self):
        m=load('gallery',R/'same-object-visual-dictionary/scripts/build_gallery.py')
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): m.build(self.fixture(d,anchor='other.png'),Path(d)/'out')
    def test_path_escape_rejected(self):
        m=load('gallery',R/'same-object-visual-dictionary/scripts/build_gallery.py')
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): m.build(self.fixture(d,image='../outside.png'),Path(d)/'out')

if __name__=='__main__': unittest.main(verbosity=2)
