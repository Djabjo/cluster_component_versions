import requests
import json

REPOS = [
    "prometheus/prometheus",
    "grafana/loki",
    "kubernetes/kubernetes",
    "ingress-nginx/ingress-nginx",
    "wal-g/wal-g",
    "argoproj/argo-cd",
    "prometheus/node_exporter",
    "prometheus-community/postgres_exporter",
    "oliver006/redis_exporter"
]

def get_latest_version(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["tag_name"]
    return "N/A"

table = "| Программа          | Версия     |\n|--------------------|------------|\n" #18
for repo in REPOS:
    name = repo.split("/")[-1]
    version = get_latest_version(repo)
    lenname = 18 - len(name)
    lenversion = 8 - len(version)
    table += f"| {name} {" " * lenname}| {version} {" " * lenversion }  |\n"

with open('README.md', 'w') as file:
    file.write(table)
