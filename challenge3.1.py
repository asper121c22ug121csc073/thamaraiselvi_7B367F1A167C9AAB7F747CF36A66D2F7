"""
write a function called linear_search_product that takes the list of products and a target  product
name as input. the function should perform a linear search to find the target product in the list and
return a list of indices all occurences of the product if found, or an empty list if_the product is not 
found.
"""


def linearsearchproduct(productlist, targetproduct):
   indices = []

   for index, product in enumerate(productlist):
    if product == targetproduct:
     indices.append(index)
 
   return indices


# example usage:
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = linearsearchproduct(products, target)
print(result)











