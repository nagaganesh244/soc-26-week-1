def average_confidence(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def filter_detections(detections, threshold):
    filtered = []
    for detection in detections:
        if detection["confidence"] >= threshold:
            filtered.append(detection)

    return filtered

detections = [
    {
        "label": "person",
        "confidence": 0.92,
        "box": [120, 80, 200, 300]
    },
    {
        "label": "cat",
        "confidence": 0.45,
        "box": [30, 50, 100, 140]
    },
    {
        "label": "dog",
        "confidence": 0.78,
        "box": [200, 100, 280, 220]
    }
]

scores = []
for detection in detections:
    scores.append(detection["confidence"])
print("Confidence Scores:")
print(scores)

print("\nAverage Confidence:")
print(average_confidence(scores))

print("\nFiltered Detections (Threshold = 0.7):")
filtered = filter_detections(detections, 0.7)
print(filtered)
