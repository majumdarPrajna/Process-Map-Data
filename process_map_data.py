import json
from collections import defaultdict

def load_data():
    """Load and parse JSON data (Replace with file reading if needed)."""
    locations_json = [
        {"id": "loc_01", "latitude": 37.7749, "longitude": -122.4194},
        {"id": "loc_04", "latitude": 27.8749, "longitude": 122.4194},
        {"id": "loc_05", "latitude": 57.2749, "longitude": -112.4344},
        {"id": "loc_06", "latitude": 14.0522, "longitude": -119.2531},
        {"id": "loc_07", "latitude": 64.0522, "longitude": -108.2330},
        {"id": "loc_02", "latitude": 34.0522, "longitude": -118.2437},
        {"id": "loc_08", "latitude": 24.0522, "longitude": -168.2197},
        {"id": "loc_03", "latitude": 40.7128, "longitude": -74.0060}
    ]

    metadata_json = [
        {"id": "loc_01", "type": "restaurant", "rating": 4.5, "reviews": 120},
        {"id": "loc_04", "type": "restaurant", "rating": 4.1, "reviews": 500},
        {"id": "loc_05", "type": "restaurant", "rating": 3.7, "reviews": 110},
        {"id": "loc_02", "type": "hotel", "rating": 4.2, "reviews": 200},
        {"id": "loc_06", "type": "hotel", "rating": 4.0, "reviews": 700},
        {"id": "loc_07", "type": "hotel", "rating": 2.0, "reviews": 900},
        {"id": "loc_03", "type": "cafe", "rating": 4.7, "reviews": 150},
        {"id": "loc_08", "type": "cafe", "rating": 4.5, "reviews": 750}
    ]
    return locations_json, metadata_json

def merge_data(locations, metadata):
    """Merge locations with metadata based on matching id."""
    location_data = {loc["id"]: loc for loc in locations}
    merged_data = []
    
    for meta in metadata:
        if meta["id"] in location_data:
            merged_data.append({**location_data[meta["id"]], **meta})
    
    return merged_data

def analyze_data(merged_data):
    """Analyze data to compute required metrics."""
    type_count = defaultdict(int)
    type_ratings = defaultdict(list)
    most_reviews = {"id": None, "reviews": 0}
    incomplete_data = []
    
    for loc in merged_data:
        loc_type = loc.get("type")
        type_count[loc_type] += 1
        type_ratings[loc_type].append(loc.get("rating", 0))
        
        if loc.get("reviews", 0) > most_reviews["reviews"]:
            most_reviews = {"id": loc["id"], "reviews": loc["reviews"]}
        
        # Check for incomplete data
        if any(k not in loc for k in ["id", "latitude", "longitude", "type", "rating", "reviews"]):
            incomplete_data.append(loc)
    
    average_ratings = {k: sum(v) / len(v) for k, v in type_ratings.items() if v}
    
    return type_count, average_ratings, most_reviews, incomplete_data

def main():
    """Main function to execute data processing and analysis."""
    locations, metadata = load_data()
    merged_data = merge_data(locations, metadata)
    type_count, avg_ratings, most_reviews, incomplete_data = analyze_data(merged_data)
    
    print("Valid Points per Type:", dict(type_count))
    print("Average Ratings per Type:", avg_ratings)
    print("Location with Most Reviews:", most_reviews)
    print("Incomplete Data:", incomplete_data if incomplete_data else "None")

if __name__ == "__main__":
    main()

