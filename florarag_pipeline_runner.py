import subprocess

services = [
    ["python", "initialize_florarag_tables.py"],
    ["uvicorn", "florarag_api:app", "--host", "0.0.0.0", "--port", "8080"]
]

for service in services:
    subprocess.Popen(service)

input()
