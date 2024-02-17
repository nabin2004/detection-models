import pickle

# listed = ['Ball','Cat','dog','bill','concat']


# with open('ds.pkl','wb') as file:
#     pickle.dump(listed,file)
    
with open('ds.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    
print(loaded_data)
    
    