import json
import re

# Load your professional numbers
with open('stats.json', 'r') as f:
    data = json.load(f)

# Define the dynamic badges
# You can change colors here: blue, red, orange, green, etc.
badges = (
    f"![](https://img.shields.io/badge/Alerts_Triaged-{data['alerts_triaged']}-blue?style=for-the-badge&logo=google-cloud&logoColor=white) "
    f"![](https://img.shields.io/badge/Incidents_Resolved-{data['incidents_resolved']}-red?style=for-the-badge&logo=fortinet&logoColor=white) "
    f"![](https://img.shields.io/badge/Threats_Hunted-{data['threats_identified']}-orange?style=for-the-badge&logo=crowdstrike&logoColor=white) "
    f"![](https://img.shields.io/badge/System_Uptime-{data['uptime_maintained']}-green?style=for-the-badge&logo=linux&logoColor=white)"
)

# Update README
with open('README.md', 'r') as f:
    content = f.read()

# Replace content between markers
updated_content = re.sub(r".*?", 
                         f"\n{badges}\n", 
                         content, flags=re.DOTALL)

with open('README.md', 'w') as f:
    f.write(updated_content)
