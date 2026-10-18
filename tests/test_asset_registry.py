"""Offline external-asset registry schema tests."""
import json
from pathlib import Path
import unittest
SCHEMA = Path(__file__).resolve().parents[1]/"assets"/"manifests"/"asset-registry.schema.json"
class AssetRegistryTests(unittest.TestCase):
    def test_required_authority_fields(self):
        schema = json.loads(SCHEMA.read_text())
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        required = set(schema["properties"]["assets"]["items"]["required"])
        self.assertTrue({"logical_id","provider","object_id","sha256","rights","approval"} <= required)
    def test_schema_validation(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema unavailable")
        schema=json.loads(SCHEMA.read_text())
        good={"registry_version":"0.1","assets":[{"logical_id":"sample/hero/front","provider":"user-local","object_id":"placeholder","sha256":"f"*64,"rights":"verify before commercial use","approval":"UNKNOWN"}]}
        jsonschema.validate(good,schema)
        good["assets"][0]["sha256"]="invalid"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(good,schema)
if __name__=="__main__":
    unittest.main()
