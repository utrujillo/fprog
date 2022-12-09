import pandas as pd

# Create DataFrame
dataFrame = pd.DataFrame([[10, 15], [20, 25], [30, 35], [40, 45]],index=['w', 'x', 'y', 'z'],columns=['a', 'b'])
print( dataFrame )
dataFrame = dataFrame.drop('z')
print( dataFrame )