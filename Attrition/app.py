from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the pre-trained model using joblib
try:
    model = joblib.load('attrition_model.pkl')
    print(type(model))  # Debug: print the type of the loaded model
except Exception as e:
    raise RuntimeError("Error loading model: {}".format(e))

# Ensure model has 'predict' method
if not hasattr(model, 'predict'):
    raise ValueError("Loaded model is not a valid model object.")

# Define the path for the CSV file
csv_file_path = 'dataset.csv'

# Route for the input form
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Form submitted, processing data...") 
    try:
        # Retrieve form data and ensure correct types for each feature
        form_data = {
            'Business Travel': request.form['Business Travel'],
            'Department': request.form['Department'],
            'Education Field': request.form['Education Field'], 
            'Gender': request.form['Gender'],  # Keep as string for encoding later
            'Job Role': request.form['Job Role'],
            'Marital Status': request.form['Marital Status'],
            'Over Time': request.form['Over Time'],  # Keep as string for encoding later
            'Training Times Last Year': int(request.form['Training Times Last Year']),

            'Age': int(request.form['Age']),
            'Distance From Home': float(request.form['Distance From Home']),
            'Education': request.form['Education'],
            'Environment Satisfaction': request.form['Environment Satisfaction'],
            'Job Satisfaction': request.form['Job Satisfaction'],

            'Monthly Income': float(request.form['Monthly Income']),
            'Number of Companies Worked': int(request.form['Num Companies Worked']),
            'Percent Salary Hike': float(request.form['Percent Salary Hike']),
            'Relationship Satisfaction': request.form['Relationship Satisfaction'],

            'Total Working Years': float(request.form['Total Working Years']),
            'Years At Company': float(request.form['Years At Company']),
            
            
            'Years With Current Manager': int(request.form['Years With Current Manager']),
            'Years in Current Role': float(request.form['Years In Current Role']),
            
            
            'Work Life Balance': request.form['Work Life Balance'],
            
            
            
        }

        # Convert the form data to a DataFrame
        input_df = pd.DataFrame(form_data, index=[0])

        # One-hot encode categorical features
        input_df_encoded = pd.get_dummies(input_df, columns=['Gender', 'Job Role', 'Department', 
                                                              'Over Time', 'Marital Status', 
                                                              'Business Travel', 'Education', 
                                                              'Education Field'], drop_first=True)

        # Define expected features based on the model's training
        expected_features = model.feature_names_in_  # Get feature names from the model

        # Creates an empty DataFrame (input_data_final) with all the expected features, 
        # initialized to 0. This ensures that even if some features are missing from the input, 
        # the DataFrame will have the correct structure.
        input_data_final = pd.DataFrame(0, index=[0], columns=expected_features)

        # Fill in the appropriate values based on the input data
        for feature in expected_features:
            if feature in input_df_encoded.columns:
                input_data_final.loc[0, feature] = input_df_encoded[feature].values[0]
            elif feature in input_df.columns:
                input_data_final.loc[0, feature] = input_df[feature].values[0]

        # Ensure all data types are compatible(convert the input_data_final dataframe to float)
        input_data_final = input_data_final.astype(float)

        # Make prediction
        prediction = model.predict(input_data_final)

        # Debugging: Print the prediction and form data
        print("Prediction:", prediction[0])
        print("Form Data:", form_data)

        # Save input data to CSV
        if not os.path.isfile(csv_file_path):
            input_df.to_csv(csv_file_path, index=False)  # Write header if file doesn't exist
        else:
            input_df.to_csv(csv_file_path, mode='a', header=False, index=False)  # Append without header

 # Return the prediction as JSON
        return jsonify({'prediction': 'Yes' if prediction[0] == 1 else 'No', 'form_data': form_data})   # model output 1 = YES , otherwise NO 

    except Exception as e:
        print("Error:", e)  
        return jsonify({'error': str(e)}), 400  # Return the error message as JSON

if __name__ == '__main__':
    app.run(debug=True)