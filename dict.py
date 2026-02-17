a=[{
    "name":"harry",
    "age":22,
    "address":"nagaon",
    "food":{
        "veg":"cabbage",
        "nonveg":"egg"
    }

    
}]
for info in a[0]["food"].values():
    print(info)

# print(a["food"]["veg"])