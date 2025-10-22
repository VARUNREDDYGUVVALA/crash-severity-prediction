Import the data from the link
https://data.cityofchicago.org/api/views/85ca-t3if/rows.csv?accessType=DOWNLOAD

1. Open the Jupyter notebook and Change the path as per location where the data is stored

file_path = "../traffic-crashes-crashes/Traffic_Crashes_-_Crashes.csv" (Change this line in the code)


2. Run all the cells one by one

Save this models in your local path for deployment
# Save model and scaler to disk
joblib.dump(rf_model, '/working/random_forest_top10.pkl')
joblib.dump(scaler, '/working/scaler_top10.pkl')
joblib.dump(top_10_features, '/working/top10_features.pkl')

** Change path as per your system

For Flask deployment
Install Flask (!pip install Flask)

Make a folder or just put my folder in the local drive.

Just type cd [path of your drive where your folder is stored]
then after accessing you will see cd/[your location]/[Flask folder name]
Then type python app.py and then you will receive local server link
Copy and paste in browser you will get an UI
