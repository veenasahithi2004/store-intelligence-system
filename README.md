# 🛍️ AI Store Intelligence System

## Overview

AI Store Intelligence System is a retail analytics platform that combines CCTV video analytics and POS transaction data to generate actionable business insights for store managers.

The system uses computer vision to analyze customer movement inside the store and combines it with sales data to understand customer behavior, engagement, and conversion performance.

---

## Features

### 📊 Sales Analytics

* Total Revenue Analysis
* Order Analysis
* Average Basket Value
* Top Performing Brands
* Top Selling Categories

### 🎥 Visitor Analytics

* Multi-Camera Visitor Counting
* Zone-wise Traffic Analysis
* Customer Dwell Time Analysis
* Store Traffic Distribution

### 📈 Business Intelligence

* Conversion Rate Calculation
* Customer Engagement Metrics
* Revenue vs Traffic Correlation
* Executive Business Insights

---

## Store Zones

| Camera | Zone                 |
| ------ | -------------------- |
| CAM 1  | Skincare             |
| CAM 2  | Makeup               |
| CAM 3  | Entrance             |
| CAM 4  | Storage / Staff Area |
| CAM 5  | Checkout             |

---

## Results

### Store Performance

* Revenue: ₹34,331.71
* Orders: 24
* Average Basket Value: ₹339.92
* Conversion Rate: 35%

### Zone Traffic

| Zone     | Visitors |
| -------- | -------- |
| Makeup   | 124      |
| Skincare | 69       |
| Entrance | 62       |
| Checkout | 43       |
| Storage  | 3        |

### Customer Engagement

* Average Dwell Time: 15.36 seconds
* Longest Stay: 125.89 seconds
* Valid Visitors: 40

---

## Technology Stack

### Computer Vision

* YOLOv8
* ByteTrack
* OpenCV

### Analytics

* Pandas
* NumPy

### Dashboard

* Streamlit
* Plotly

---

## Project Structure

```text
store-intelligence/

├── dashboard/
│   ├── app.py
│   └── current_layout.png
│
├── pipeline/
│   ├── detect.py
│   ├── visitor_counter.py
│   ├── all_cameras.py
│   └── dwell_time.py
│
├── data/
│   ├── Brigade_Bangalore_10_April_26.csv
│   └── Store Layout Files
│
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Future Improvements

* Cross-Camera Person Re-Identification
* Heatmap Generation
* Shelf Interaction Analytics
* Product Recommendation Engine
* Real-Time Monitoring Dashboard

---

## Business Impact

The system helps retailers understand:

* Customer traffic patterns
* High-performing store zones
* Customer engagement behavior
* Revenue-driving product categories
* Store conversion effectiveness
