import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

REPOS = [
    "prometheus/prometheus",
    "grafana/loki",
    "kubernetes/kubernetes",
    "kubernetes/ingress-nginxdfs",
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

table = []
for repo in REPOS:
    name = repo.split("/")[-1]
    version = get_latest_version(repo)
    table.append({'component': name, 'version': version})

df = pd.DataFrame(table)

fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('off')
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 loc='center',
                 cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)
plt.tight_layout()

plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()