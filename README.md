# Process Map Data

## 📌 Project Overview
This project processes map location data by merging geographical coordinates with metadata such as type, rating, and reviews. The script provides insights like:
- Number of locations per category (restaurant, hotel, cafe, etc.)
- Average ratings per category
- The location with the highest number of reviews
- Identification of incomplete data entries

## ⚡ Features
- Parses and merges location and metadata JSON data.
- Computes key metrics such as average ratings and most reviewed locations.
- Checks for missing or incomplete data entries.

## 🛠️ Installation & Setup
### **Prerequisites**
Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

### **Clone the Repository**
$ git clone https://github.com/majumdarPrajna/process_map_data.git
$ cd process_map_data

### **Run the Script**
$ python process_map_data.py


## 📊 Output Example
Valid Points per Type: {'restaurant': 3, 'hotel': 3, 'cafe': 2}
Average Ratings per Type: {'restaurant': 4.1, 'hotel': 3.4, 'cafe': 4.6}
Location with Most Reviews: {'id': 'loc_07', 'reviews': 900}
Incomplete Data: None



