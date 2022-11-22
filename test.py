import requests
import pandas as pd
import json


pd.set_option('display.max_rows', None)

#comments
url1 = "https://jsonplaceholder.typicode.com/comments"
#posts
url2 = "https://jsonplaceholder.typicode.com/posts"

r1 = requests.get(url1).json()
r2 = requests.get(url2).json()
df = pd.DataFrame.from_records(r1)
# print(df.groupby(['postId'])['postId'].count())
print(json.dumps(r1[0], indent=4))
# print(json.dumps(r2[0], indent=4))
