from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Updated dataset
data = {
    "Square Footage": [2000, 3000, 1000],
    "Bedrooms": [3, 4, 2],
    "Bathrooms": [2, 3, 1],
    "Location": [1, 2, 3],  # Urban, Suburban, Rural
    "Year Built": [2010, 2015, 2000],
    "Quality": [4, 5, 3],   # Quality score
    "Amenities": [5, 4, 3], # Amenity score
    "Price": [300000, 500000, 150000]
}

# Prepare features and target
X = np.array([
    [2000, 3, 2, 1, 2010, 4, 5],
    [3000, 4, 3, 2, 2015, 5, 4],
    [1000, 2, 1, 3, 2000, 3, 3]
])
y = np.array([300000, 500000, 150000])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
import joblib
joblib.dump(model, "house_price_model.pkl")

# Example prediction
new_data = [[2500, 3, 2, 1, 2020, 4, 5]]  # Inputs
predicted_price = model.predict(new_data)
print(f"Predicted Price: ${predicted_price[0]:,.2f}")
