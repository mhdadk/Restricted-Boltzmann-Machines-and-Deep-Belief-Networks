import torch
import pandas as pd

class CSVDataset(torch.utils.data.Dataset):
    
    def __init__(self, x_csv_path, window_length = 50):
        
        # load csv file as dataframe
        
        self.x = pd.read_csv(x_csv_path,header = None)
        
        # specify how many samples in a window
        
        self.window_length = window_length
    
    def __len__(self): # number of windows
        
        return int(len(self.x) / self.window_length)
        
    def __getitem__(self,idx):
        
        # get sample numbers for window start and end        
        
        start = idx*self.window_length
        end = start + self.window_length
        
        # extract window and convert to NumPy array
        
        window = self.x.iloc[start:end,2].to_numpy(copy = True)
        
        # convert window to torch column tensor
        
        window = torch.from_numpy(window)
        
        # convert to one-hot encoding
        
        window = torch.nn.functional.one_hot(window - 1).to(torch.float)
                
        return window

if __name__ == '__main__':
    
    path = '../data/train.csv'
    dataset = CSVDataset(path)
    
    x = dataset[len(dataset)-1]
