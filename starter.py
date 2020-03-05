import pandas as pd

def transform_df(dfA, dfB):
    '''
    Implement the function. Return the resultant dataframe.
    An evaluation program shall call the function and use the returned dataframe.
        ## The table will look like this
        customer, peppery, light, smooth, sweetened, dark
        A,        3      , 2    , 1     , 1        ,    1
        B,
        C,
    '''
    pass


# Below is a sample to develop your method:

# Products
tableA = [(10, 'peppery, light'),
         (11, 'peppery, smooth, dark'),
         (12, 'sweetened'),
         (13, 'sweetened')]
labels = ['product', 'tags']
dfA = pd.DataFrame.from_records(tableA, columns=labels)

# Purchases
tableB = [('A', 10),
           ('A', 11),
           ('B', 11),
           ('C', 10),
           ('C', 12),
           ('B', 11),
           ('A', 10),
           ('C', 12),
           ('D', 13),
           ('A', 13)]
labels = ['customer', 'product']
dfB = pd.DataFrame.from_records(tableB, columns=labels)

# Call merging function
res_df = transform_df(dfA, dfB)

# Now consider that tableB is read from a SQL database and has over two hundred million rows, and table A has 100 rows.
# How would you change your approach in the transform_df function to optimize the time it takes to run
# Write your answer in improvements.txt.

