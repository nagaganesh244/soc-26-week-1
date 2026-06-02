def filter_detections(detections, threshold):
    filtered = []
    for detection in detections:
        if detection["confidence"] >= threshold:
            filtered.append(detection)
    return filtered
def test_filter_detections():
    detections = [
        {"label": "person", "confidence": 0.90},
        {"label": "cat", "confidence": 0.40},
        {"label": "dog", "confidence": 0.75}
    ]
    result = filter_detections(detections, 0.7)
    assert len(result) == 2
    assert result[0]["label"] == "person"
    assert result[1]["label"] == "dog"

    print("Test Passed")
test_filter_detections()
