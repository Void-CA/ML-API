import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# load the data
iris = load_iris()
X, y = iris.data, iris.target

# filtering just two classes to make it simpler
X, y = X[y != 2], y[y != 2]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
