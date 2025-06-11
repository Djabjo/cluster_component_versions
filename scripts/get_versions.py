import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

REPOS = [
    "prometheus/prometheus",
    "grafana/loki",
    "kubernetes/kubernetes",
    "kubernetes/ingress-nginx",
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
    table.append({'Component': name, 'Version': version})

df = pd.DataFrame(table)

fig, ax = plt.subplots(figsize=(6, 4))
ax.axis('off')
table = ax.table(cellText=df.values,
                 colLabels=df.columns,     
                 loc='center',
                 cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)
fig.subplots_adjust(top=1, bottom=0)  
plt.tight_layout(pad=0)


plt.gca().set_axis_off()  # Отключаем оси
plt.margins(0,0)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)



plt.savefig('output.png', dpi=400, bbox_inches='tight', pad_inches=0)
# plt.show() , pad_inches=0