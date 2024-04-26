def compactObject(obj):
    final = [] if type(obj) == list else {}
    
    if (type(obj) == list):
        for x in obj:
            if (type(x) == list or type(x) == dict):
                final.append(compactObject(x))
            else:
                if bool(x): final.append(x)
    else:
        for i, j in obj.items():
            if (type(j) == list or type(j) == dict):
                final[i] = compactObject(j)
            else:
                if bool(j): final[i] = j
            
    return final


# Run the function
if __name__ == "__main__":
    obj = {"a": None, "b": [False, 1]}
    print(compactObject(obj))  # {'b': [1]}