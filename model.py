import numpy as np
from sklearn.linear_model import LogisticRegression

# Train a simple model (example)
X = np.array([
    [5, 6, 0],
    [8, 4, 1],
    [2, 8, 0],
    [10, 3, 1]
])
y = np.array([0, 1, 0, 1])

model = LogisticRegression()
model.fit(X, y)

def predict_health(screen, sleep, eye):
    data = np.array([[screen, sleep, eye]])
    prediction = model.predict(data)
    return int(prediction[0])
