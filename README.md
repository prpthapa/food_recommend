# Food Recommender System

A content-based Food Recommender System built with **Streamlit**, **Pandas**, and precomputed similarity metrics. The application recommends top 5 related dishes based on shared features such as ingredients, cuisine origin, category, and food descriptions.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dataset & Features](#dataset--features)
- [Prerequisites & Installation](#prerequisites--installation)
- [Running the Application](#running-the-application)
- [Example Usage](#example-usage)
- [Code Breakdown (`backend/app.py`)](#code-breakdown-backendapppy)
- [Suggested Improvements](#suggested-improvements)

---

## Overview

The Food Recommender System uses content-based filtering to suggest similar dishes. When a user selects a dish from the dropdown menu, the model calculates the most similar food items using a precomputed cosine similarity matrix generated from tokenized and processed food features (ingredients, category, origin, and descriptions).

---

## How It Works

1. **Data Loading**: Loads the pickled dictionary (`food_dict.pkl`) and converts it into a Pandas DataFrame.
2. **Similarity Matrix**: Loads `similarity.pkl`, a 500x500 pairwise cosine similarity matrix.
3. **User Selection**: The user selects a dish via the Streamlit dropdown (`st.selectbox`).
4. **Recommendation Logic**:
   - Locates the index of the selected item in the dataset.
   - Extracts the corresponding similarity score vector.
   - Sorts items by descending similarity score.
   - Selects the top 5 closest matches (excluding the selected item itself).
5. **Display**: Streamlit outputs the recommended food names upon clicking the **Recommend** button.

---

## Project Structure

```text
food/
├── backend/
│   └── app.py              # Streamlit web application & recommendation logic
├── food_dict.pkl           # Pickled dictionary containing 500 food items and metadata
├── similarity.pkl          # Pickled (500, 500) cosine similarity matrix
└── README.md               # Project documentation
```

---

## Dataset & Features

The `food_dict.pkl` dataset contains 500 food items with the following columns:

| Column | Description |
|---|---|
| `id` | Unique identifier for each food item |
| `item` | Name of the food item (e.g., Dal, Bhat, Tarkari) |
| `category` | Food category (e.g., staple, curry, snack) |
| `ingredients` | Key ingredients used in the dish |
| `origin` | Culinary origin (e.g., Nepal, India) |
| `description` | Textual description of the dish |
| `food_features` | Combined, preprocessed text features used for vectorization and similarity computation |

---

## Prerequisites & Installation

### 1. Requirements

- Python 3.10 or higher
- Required packages:
  - `streamlit`
  - `pandas`
  - `numpy`
  - `scikit-learn`

### 2. Setup Virtual Environment

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install streamlit pandas numpy scikit-learn
```

---

## Running the Application

> **Note:** Run the command from the root `food/` directory so the relative paths to `food_dict.pkl` and `similarity.pkl` resolve correctly.

```bash
streamlit run backend/app.py
```

Once started, open your browser and navigate to:
```text
http://localhost:8501
```

---

## Example Usage

1. Launch the app using `streamlit run backend/app.py`.
2. In the dropdown menu, select **Dal**.
3. Click the **Recommend** button.
4. The system displays the top 5 recommended dishes:
   - **Thakali Set**
   - **Khichdi**
   - **Jimbu**
   - **Chamre**
   - **Bangla Daal**

---

