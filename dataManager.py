import requests
from collections import Counter

class DataManager:

    def __init__(self) -> None:
        
        self.__comment_url = "https://jsonplaceholder.typicode.com/comments"
        self.__post_url = "https://jsonplaceholder.typicode.com/posts"
        self.__filter_post = "https://jsonplaceholder.typicode.com/posts/"
        self.__metaData = {"post_id":"id", "post_title":"title", "post_body":"body"}
    
    def get_top_total_comments(self, n=5):
        try:
            __posts = requests.get(self.__post_url).json()
            __comments = requests.get(self.__comment_url).json()
            totalComments = dict(sorted(self.__get_total_post_by_id(__comments).items(), key=lambda item: item[1])[:n])
            data = [{"post_id":k["id"], "post_title":k["title"], "post_body":k["body"], "total_number_of_comments":totalComments[i]} for i in totalComments for k in __posts if k["id"] == i ]
            return data
        except Exception as e:
            return None
    
    def __get_total_post_by_id(self, data):
        try:
            return dict(Counter([x["postId"] for x in data]))
        except Exception as e :
            return None
    
    def __filter_by_args(self, args, data):
        try:
            tempdata = None
            for k, v in args.items():
                if isinstance(v, int):
                    if tempdata == None:
                        tempdata = [x for x in data if x[k] == v]
                    else:
                        tempdata = [x for x  in tempdata if x[k] == v]
                elif isinstance(v, str):
                    if tempdata == None:
                        tempdata = [x for x in data if v in x[k]]
                    else:
                        tempdata = [x for x  in tempdata if v in x[k]]
                else:
                    tempdata = None
            return tempdata
        except Exception as e:
            print(e)
            return "Invalid filter parameters."
    
    def __parse_key(self, args):
        for k,v in self.__metaData.items():
            if k in args["data"].keys():
                args["data"][v] = args["data"].pop(k)
        return args
    
    def parse_arguments(self,args):
        if isinstance(args, dict) and len(args) > 0:
            __data = None
            argsKeys = [self.__metaData[x] if x in self.__metaData else x for x in args["data"].keys()]
            if args["mode"] == 0: #comments
                __data = requests.get(self.__comment_url).json()
            elif args["mode"] == 1: #posts
                __data = requests.get(self.__post_url).json()
                args = self.__parse_key(args)
            else:
                return f"Invalid mode: {args['mode']}"
            __keys = [*set([x for y in __data for x in y])]
            notValidKeys = list(set(argsKeys).difference(__keys))
            if len(notValidKeys) != 0:
                return f"Invalid arguments: {notValidKeys}"
            __filteredData = self.__filter_by_args(args["data"], __data) 
            return __filteredData if __filteredData != None else "There are no records."
        else:
            return "There are no parameters."
# {
#     "mode":"comments",
#     "data":{
#         "name":"test"
#     }
# }

# Question 1
# {
#     "data": 5
# }
# Question 2

# {
#     "mode":1,
#     "data":{
#         "title":"provident"
#     }
# }

