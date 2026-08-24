from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#load iris dataset
data = load_iris()
X,y = data.data,data.target

#split the dataset into training and testing sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#logistic regression model

#scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#logistic regression model
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train,y_train)

#predict on test data
y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f'Logistic Regression Accuracy: {accuracy:.4f}')

#experiment with different values of k
for k in range(1,11):
    #create KNN model
    knn = KNeighborsClassifier(n_neighbors=k)
    
    #fit the model on training data
    knn.fit(X_train,y_train)
    
    #make predictions on test data
    y_pred = knn.predict(X_test)
    
    #calculate accuracy
    accuracy = accuracy_score(y_test,y_pred)
    
    print(f'Accuracy for k={k}: {accuracy:.4f}')

    #calculate confusion matrix and classification report
    cm = confusion_matrix(y_test,y_pred)
    cr = classification_report(y_test,y_pred)
    #print(f'Confusion Matrix for k={k}:\n{cm}\n')
   # print(f'Classification Report for k={k}:\n{cr}\n')
