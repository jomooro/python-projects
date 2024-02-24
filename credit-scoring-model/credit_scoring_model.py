import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification

def generate_synthetic_data():
    """Generate synthetic financial data."""
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=8,
        n_redundant=2,
        random_state=42
    )
    columns = [f"feature_{i}" for i in range(X.shape[1])]
    data = pd.DataFrame(X, columns=columns)
    data['creditworthiness_label'] = y
    return data

def save_data_to_csv(data, filename='data.csv'):
    """Save DataFrame to a CSV file."""
    data.to_csv(filename, index=False)

def load_data_from_csv(filename='data.csv'):
    """Load historical financial data from a CSV file."""
    return pd.read_csv(filename)

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    """Train a RandomForestClassifier and evaluate its performance."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)
    return accuracy, classification_rep

# Generate synthetic financial data
data = generate_synthetic_data()

# Save the DataFrame to a CSV file
save_data_to_csv(data)

# Load your historical financial data into a Pandas DataFrame
data = load_data_from_csv()

# Split the data into training and testing sets
X = data.drop('creditworthiness_label', axis=1)
y = data['creditworthiness_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model and evaluate its performance
accuracy, classification_rep = train_and_evaluate_model(X_train, X_test, y_train, y_test)

# Print the results
print(f'Accuracy: {accuracy}')
print('Classification Report:\n', classification_rep)
