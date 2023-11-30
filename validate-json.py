import sys
import json
import jsonschema
from jsonschema.exceptions import ValidationError
from pathlib import Path

# https://codebeautify.org/json-to-json-schema-generator


def validate_json(file_path):
    with open(file_path) as filename:
        cfg = json.load(filename)

    version = cfg.get("version")
    if version is None:
        print(f"Config {filename} is not valid as it is missing version attribute")
        return 1

    try:
        schema_path = f"schema/{version}/schema.json"
        with open(schema_path) as schema_file:
            schema = json.load(schema_file)

        jsonschema.validate(cfg, schema)

    except ValidationError as e:
        print(f"Config {filename} is not valid. Exception: {e}")
        # raise ValueError("Not valid json.")
        return 1

    return 0


def validate_directory():
    errors = 0
    json_files = (file for file in Path("config/").rglob("*.json"))
    for file_path in json_files:
        errors += validate_json(str(file_path))
    return errors


if __name__ == "__main__":
    errors = validate_directory()
    print(f"Number of files that have issues: {errors}")
    sys.exit(errors)
