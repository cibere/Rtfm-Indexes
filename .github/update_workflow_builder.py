# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pyyaml",
# ]
# ///

import pathlib

import yaml

gh_dir = pathlib.Path(__file__).parent
workflow_dir = gh_dir / "workflows"
workflow_file = workflow_dir / "auto_update.yml"

parsers_dir = gh_dir.parent / "_parsers"


def iter_parser_files():
    for file in parsers_dir.glob("*.py"):
        if not file.name.startswith("_"):
            yield file

 
def build_tree():
    files = [p.name.removesuffix(".py") for p in iter_parser_files()]
    return {
        "name": "Auto Update",
        "on": {
            "workflow_dispatch": {
                "inputs": {
                    "parser": {
                        "description": "the parser to run",
                        "required": False,
                        "default": "all",
                        "type": "choice",
                        "options": ["all", *files],
                    }
                }
            },
            "schedule": [{"cron": "23 23 * * *"}],
        },
        "jobs": {
            "update": {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"uses": "actions/checkout@v4"},
                    *[
                        {
                            "name": f"index {file}",
                            "if": f"${{{{ inputs.parser == 'all' || inputs.parser == '{file}' }}}}",
                            "uses": "cibere/Rtfm-Indexes@run-parser-action",
                            "with": {
                                "filename": file,
                                "error_hook": "${{ secrets.INDEX_ERROR_HOOK_URL }}",
                            },
                        }
                        for file in files
                    ],
                    {
                        "name": "Push Changes",
                        "continue-on-error": True,
                        "run": 'git fetch\ngit pull\ngit add indexes\ngit -c user.name="github-actions[bot]" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" commit --author="cibere <71997063+cibere@users.noreply.github.com>" -m "Auto Update Indexes"\ngit push',
                    },
                ],
            }
        },
    }


def main():
    workflow_file.write_text(yaml.dump(build_tree()))


if __name__ == "__main__":
    main()
