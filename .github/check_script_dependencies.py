# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "certifi==2025.1.31",
#     "charset-normalizer==3.4.1",
#     "idna==3.10",
#     "requests==2.32.3",
#     "urllib3==2.3.0",
# ]
# ///

from pathlib import Path
import subprocess, requests
from typing import Iterator

github_dir = Path(__file__).parent
root = github_dir.parent
indexers = root / "indexers"

def run(*args: str) -> tuple[str, str]:
    proc = subprocess.run(args, capture_output=True)
    data = proc.stdout.decode(), proc.stderr.decode()
    #print(f"Ran command {args!r}.\nstdout: {data[0]!r}\nstderr: {data[1]!r}")

    return data

def git(*args: str) -> tuple[str, str]:
    return run("git", "-c", 'user.name="github-actions[bot]"', '-c', 'user.email="41898282+github-actions[bot]@users.noreply.github.com"', *args)

def uv(*args: str) -> tuple[str, str]:
    return run("uv", *args)

def get_script_requirements(script: Path) -> Iterator[str]:
    stdout, stderr = uv("export", "--script", script.as_posix())
    
    for line in stdout.splitlines():
        line = line.strip()

        if line.startswith(("#", "-")):
            continue
        yield line.removesuffix(" \\")

def get_latest_version(package: str) -> str:
    response = requests.get(f'https://pypi.org/pypi/{package}/json')
    return response.json()['info']['version']

def main():
    for script in indexers.rglob("*.py"):
        for req in get_script_requirements(script):
            name, current = req.split(";")[0].split("==")
            latest = get_latest_version(name)

            uv("add", "--script", script.as_posix(), f"{name}=={latest}")

            if latest != current:
                print(f"{script} - {name} updated from {current} to {latest}")

if __name__ == '__main__':
    main()
