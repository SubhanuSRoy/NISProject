# Save the trained model as a pickle file
pickle.dump(clf, open('dt_model.pkl', 'wb'))

# joblib.dump(clf, "random_forest_model.pkl")
print("Model saved as dt_model.pkl")