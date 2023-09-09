import pandas as pd
import numpy as np

#Entrenamiento 

data = pd.read_csv("party_data.csv")

#separación demográfica 

X = data['partido popular']
y = data['partido socialista obrero español']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#vectorización 

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

#algoritmo de regresión

model = LogisticRegression()
model.fit(X_train_vec, y_train)

# predicción

partido_nuevo = ["https://www.voxespana.es/"]
partido_nuevo_vec = vectorizer.transform(partido_nuevo)
prediccion = model.predict(partido_nuevo_vec)

if prediccion[0] == 1:
    print("partido popular")
else:
    print("partido sociialista obrero español")