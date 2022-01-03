

from app.Net.execute_model import execute_model
import os

if __name__ == "__main__":
    
    model = execute_model()
    # print(os.path.exists("app/Net/.bacteria_trained.hdf5"))
    print(model)