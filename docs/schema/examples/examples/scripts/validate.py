"""
validate.py

Validates annotation JSON files in examples/ against schema/annotation.schema.json.
This mirrors the QA step I run on my own annotation batches before submission:
checking every required field is present, correctly typed, and meets minimum
content-length thresholds before a batch goes out.

Usage:
    python scripts/validate.py
"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    sys.exit("Missing dependency. Install with: pip install jsonschema")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "annotation.schema.json"
EXAMPLES_DIR = ROOT / "examples"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(schema, path: Path) -> list[str]:
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(data), key=str):
        errors.append(f"{path.name}: {err.message}")
    return errors


def main():
    schema = load_schema()
    json_examples = sorted(EXAMPLES_DIR.glob("*.json"))

    if not json_examples:
        print("No JSON example files found in examples/.")
        return

    total_errors = []
    for path in json_examples:
        errors = validate_file(schema, path)
        if errors:
            total_errors.extend(errors)
            print(f"✗ {path.name} — {len(errors)} issue(s)")
            for e in errors:
                print(f"    - {e}")
        else:
            print(f"✓ {path.name} — valid")

    print()
    if total_errors:
        print(f"{len(total_errors)} total issue(s) found.")
        sys.exit(1)
    else:
        print(f"All {len(json_examples)} example annotation(s) passed validation.")


if __name__ == "__main__":
    main()
