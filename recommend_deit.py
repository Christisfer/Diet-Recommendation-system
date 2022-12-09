import pandas as pd
from sklearn.neighbors import NearestNeighbors

calories_data=[2100,1650,1900]
new_dataframe = pd.DataFrame()
process_database = pd.DataFrame()
model = NearestNeighbors(n_neighbors=5,algorithm='brute',metric='euclidean',n_jobs=1)
def load_data():
    new_dataframe = pd.read_csv('meal_recom_data.csv')
    process_database = new_dataframe.loc[:,['calories','protein']]
    model = NearestNeighbors(n_neighbors=5,algorithm='brute',metric='euclidean',n_jobs=1)
    model.fit(process_database)
    return new_dataframe,process_database,model

def getTargetMeals(target_df): 
  distances, indices = model.kneighbors(
           target_df,
            n_neighbors=10)
  return indices.squeeze().tolist()

def getRecomm(diabetic_type,weight):
  total_calories = calories_data[diabetic_type]
  total_protein = weight*1.5
  # for breakfast
  target_df_breakfast = pd.DataFrame([{'calories':total_calories*0.15,'protein':total_protein*0.15}])
  indices_breakfast = getTargetMeals(target_df_breakfast)
  print("\nbreakfast items")
  print(new_dataframe.iloc[indices_breakfast,[1]])
  # for lunch
  target_df_lunch = pd.DataFrame([{'calories':total_calories*0.4,'protein':total_protein*0.4}])
  indices_lunch = getTargetMeals(target_df_lunch)
  print("\nlunch items")
  print(new_dataframe.iloc[indices_lunch,[1]])
  # evening snack
  target_df_evening = pd.DataFrame([{'calories':total_calories*0.15,'protein':total_protein*0.15}])
  indices_evening = getTargetMeals(target_df_evening)
  print("\nevening snacks items")
  for i in indices_evening:
    print(new_dataframe.iloc[i,[1]])
#   print(new_dataframe.iloc[indices_evening,[1]])
  # dinner
  target_df_dinner = pd.DataFrame([{'calories':total_calories*0.3,'protein':total_protein*0.3}])
  indices_dinner = getTargetMeals(target_df_dinner)
  print("\ndinner items")

  print(new_dataframe.iloc[indices_dinner,[1]])

if __name__=='__main__':
    new_dataframe,process_database,model = load_data()
    diabetic_type = int(input("Enter diabetic type : "))
    weight = int(input("Enter weight : "))
    getRecomm(diabetic_type,weight)
