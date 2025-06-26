import json

with open("results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("template.md", "r", encoding="utf-8") as f:
    template = f.read()

report = template.format(
    abstract="This project uses NDVI anomaly detection to identify potential archaeological sites in the Amazon...",
    background="The Amazon basin holds many secrets...",
    methodology=f"We used {', '.join(data['algorithms'])} on NDVI data to extract anomaly regions...",
    key_findings=f"Maximum NDVI: {data['max_ndvi']}, Candidate Sites: {data['candidate_count']}",
    interpretation=data["cultural_context"] + "\n\n" + data["fuwa_insight"],
    conclusion="These anomalies suggest previously undocumented land use or settlements...",
    metadata=f"Coordinates: {data['locations'][0]['lat']}, {data['locations'][0]['lon']}",
    footnote="Generated with ❤️ and Codex."
)

with open("generated_report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ Report generated successfully: generated_report.md")
