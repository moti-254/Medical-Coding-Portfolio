services = [
    "Patient consultation - 30 minutes",
    "X-ray chest",
    "Physical therapy session - 1 hour",
    "Blood test - routine",
    "Ultrasound abdominal"
]

coding_rules = {
    "consultation": "E/M001",
    "x-ray": "RAD001",
    "physical therapy": "PT001",
    "blood test": "LAB001",
    "ultrasound": "ULS001"
}

for service in services:
    code_assigned = "UNKNOWN"
    for keyword, code in coding_rules.items():
        if keyword.lower() in service.lower():
            code_assigned = code
            break
    print(f"Service: {service} -> Code: {code_assigned}")
