dic1 = {'cat': 'I am a cat', 'dog': 'I am a dog'}
dic2 = {'lion': 'I am a lion', 'tiger': 'I am a tiger'}

animals_update = {}
animals_unpacking = {}

# for item in (dic1, dic2):
#     animals.update(item)

# using update method
print('#################################Update########################################')
animals_update.update(dic1)
animals_update.update(dic2)
print(animals_update)

# using unpacking
print('#################################Unpacking########################################')
animals_unpacking = {**dic1, **dic2}
print(animals_unpacking)