import json
import pandas as pd
with open('sample-data.json') as f:
    data = json.loads(f.read())
    my_df = pd.DataFrame(columns =["DN","Description","Speed","MTU"])
    for i in data['imdata']:
       my_df = my_df.append({"DN":i['l1PhysIf']['attributes']['dn'],
                "Description":i['l1PhysIf']['attributes']['descr'],
                "Speed":i['l1PhysIf']['attributes']['speed'],
                    "MTU":i['l1PhysIf']['attributes']['mtu']},ignore_index=True)
    clean_df= my_df.set_index('DN')
    print("Interface Status")
    print("================================================================================")
    print(clean_df)

      