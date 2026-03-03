import json
import os

def update_metrics():
    # 1. Load the new numbers
    with open('stats.json', 'r') as f:
        data = json.load(f)

    badges = (
        f"![](https://img.shields.io/badge/Alerts_Triaged-{data['alerts_triaged']}-blue?style=for-the-badge&logo=google-cloud&logoColor=white) "
        f"![](https://img.shields.io/badge/Incidents_Resolved-{data['incidents_resolved']}-red?style=for-the-badge&logo=fortinet&logoColor=white) "
        f"![](https://img.shields.io/badge/Threats_Hunted-{data['threats_identified']}-orange?style=for-the-badge&logo=crowdstrike&logoColor=white)"
    )

    # 2. Read the current README
    with open('README.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 3. Find markers and surgically replace only what's between them
    new_lines = []
    skip = False
    for line in lines:
        if "" in line:
            new_lines.append(line)
            new_lines.append(badges + "\n")
            skip = True # Start ignoring the "old" junk/duplicates
        elif "" in line:
            new_lines.append(line)
            skip = False # Stop ignoring
        elif not skip:
            new_lines.append(line)

    # 4. Write back (this version prevents duplication)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    update_metrics()
