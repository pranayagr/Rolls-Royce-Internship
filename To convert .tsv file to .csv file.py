import pandas as pd

def structure_annotated_data(filename):
    df = pd.read_csv(filename, sep='\t')
    list_entities = df['Entity'].unique()
    dict_entities = {}
    for entity in list_entities:
        ## print(df['Content'][df['Entity'] == entity])
        dict_entities[entity] = df['Content'][df['Entity'] == entity].values.tolist()
    j = 'Cause'
    for i in dict_entities:
        if(len(dict_entities[i]) >= len(dict_entities[j])):
            j = i
    ## print(j)
    for i in dict_entities:
        for k in range(0,len(dict_entities[j])-len(dict_entities[i])):
            dict_entities[i].append(dict_entities[i])
    df1 = pd.DataFrame(dict_entities)
    df1.to_csv(f'data_{filename}.csv')