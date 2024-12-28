Code Explanation

Model Integration:
A machine learning model (house_price_model.pkl) is loaded using joblib.
The model predicts house prices based on user inputs like square footage, number of bedrooms, bathrooms, location, etc.

GUI Elements:
The main window is created using Tkinter, with a title, dimensions, and an icon.
The interface includes input fields, labels, a prediction button, and a result display.
The ttk.Style() method is used to customize the styling of labels, buttons, and entry fields.

Input Fields:
The inputs are collected using Tkinter Entry widgets. These fields include:
Square footage
Number of bedrooms
Number of bathrooms
Location (Urban=1, Suburban=2, Rural=3)
Year built
Quality (1-5 rating)
Amenities (1-5 rating)
Price Prediction:

The application gathers user inputs and feeds them to the machine learning model to predict the house price.
The predicted price is displayed in a result frame on the GUI.

Theme Toggle:
The toggle_theme function allows users to switch between light and dark themes by changing the background and text colors.

Error Handling:
The application ensures valid numeric inputs. If the user enters invalid data, an error message is shown.
