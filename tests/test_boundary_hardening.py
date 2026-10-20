"""Independent checks for test-oracle sensitivity and candidate/release separation."""
import copy,json,os,shutil,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from validation import harness as h,candidate_integrity as integrity

class BoundaryTests(unittest.TestCase):
    def test_historical_evidence_and_attestation_unchanged(self):
        self.assertTrue(integrity.preserved_history())

    def test_candidate_inventory_and_scope(self):
        report=integrity.check()
        self.assertFalse(report['release_approved'])
        self.assertEqual(report['source_files'],74)
        self.assertEqual(set(report['changed_from_release']),integrity.ALLOWED_CHANGES)

    def test_original_release_builder_still_refuses_candidate(self):
        builder=h.module_from(h.ROOT/'packaging/build.py','boundary_original_builder')
        with self.assertRaisesRegex(ValueError,'Baseline source changed'):builder.payloads()

    def test_candidate_tampering_is_detected(self):
        manifest=json.loads((integrity.CANDIDATE/'source-manifest.json').read_text())
        manifest['files_sha256']['SKILL.md']='0'*64
        with self.assertRaisesRegex(ValueError,'differs'):integrity.check(manifest=manifest)

    def test_original_failure_cannot_be_waived_in_candidate(self):
        expected=h.expectations('candidate')
        original=json.loads((h.ROOT/'validation/known_findings.json').read_text())
        self.assertEqual(len(original['expected_failures']),16)
        self.assertEqual(expected['expected_failures'],[])
        for id in original['expected_failures']:
            review=h.expectation_errors([{'id':id,'outcome':'FAIL','actual':'sabotage'}],expected['expected_failures'])
            self.assertEqual(review['unexpected_failures'],[id])

    def test_descriptor_walk_resists_directory_swap(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td);root=base/'root';root.mkdir();child=root/'child';child.mkdir()
            (child/'asset.txt').write_text('ALLOWED')
            outside=base/'outside';outside.mkdir();(outside/'asset.txt').write_text('FORBIDDEN')
            root_fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY);real_open=os.open
            def swapped(path,flags,*args,**kwargs):
                fd=real_open(path,flags,*args,**kwargs)
                if path=='child':
                    child.rename(root/'original');child.symlink_to(outside,target_is_directory=True)
                return fd
            try:
                with patch.object(h.preview.os,'open',side_effect=swapped):fd=h.preview.open_bounded(root_fd,('child','asset.txt'))
                with os.fdopen(fd,'rb') as file:self.assertEqual(file.read(),b'ALLOWED')
            finally:os.close(root_fd)

    def test_special_files_not_part_of_ordinary_assets(self):
        # Path grammar is independently checked, beyond HTTP status/body assertions.
        for value in ('/../outside','/%2e%2e/outside','/%252e%252e/outside','/.hidden','/%00','/%5c'):
            with self.assertRaises((ValueError,UnicodeError)):h.preview.request_parts(value)
        self.assertEqual(h.preview.request_parts('/assets/a%20b.css?v=1'),(('assets','a b.css'),False))

    def test_cyclic_imports_terminate_and_unlinked_files_do_not_invalidate(self):
        with tempfile.TemporaryDirectory() as td:
            root,record=h.site_fixture(Path(td));(root/'a.js').write_text('import "./b.js";');(root/'b.js').write_text('import "./a.js";')
            (root/'index.html').write_text((root/'index.html').read_text().replace('</body>','<script src="a.js"></script></body>'))
            before=h.revision.snapshot(root,['hero','facts'])
            (root/'unused.js').write_text('unrelated')
            after=h.revision.snapshot(root,['hero','facts'])
            self.assertEqual(before,after)
            self.assertIn('b.js',after['global_files'])

if __name__=='__main__':unittest.main()
