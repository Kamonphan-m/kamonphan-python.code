# Set relationships  ตรวจสอบความสัมพันธ์ หรือการเปรียบเทียบระหว่าง set
all_animals = {"dog", "cat", "bird", "fish", "rabbit", "hamster"}
pets = {"dog", "cat", "rabbit"}
mammals = {"dog", "cat", "rabbit", "hamster"}
small_pets = {"cat", "rabbit", "hamster"}

print(f"All animals: {all_animals}")
print(f"Pets: {pets}")
print(f"Mammals: {mammals}")
print(f"Small pets: {small_pets}")

# Subset and superset เซ็ท set เป็นซับเซ็บ ของอีนี่ไหม
print(f"Are pets subset of all animals? {pets.issubset(all_animals)}")
print(f"Are all animals superset of pets? {all_animals.issuperset(pets)}")

# Disjoint sets (no common elements) มีสามาชิกซ้ำกันบ้างไหม
birds = {"eagle", "sparrow", "parrot"}
print(f"Birds: {birds}")
print(f"Are mammals and birds disjoint? {mammals.isdisjoint(birds)}")
print(f"Are pets and small_pets disjoint? {pets.isdisjoint(small_pets)}")

# Set equality การถามว่า เซ็ท A เท่ากับทุกสมาชิก เซ็ต B ไหม ถามว่าจริง  ไม่จริง
pets_copy = {"dog", "cat", "rabbit"}
print(f"Are pets equal to pets_copy? {pets == pets_copy}")

# Length and membership การถามจำนวนสมาชิก เช่น มี ปลา อยู่ใน mammals ไหม
print(f"Number of mammals: {len(mammals)}")
print(f"Is 'dog' in mammals? {'dog' in mammals}")
print(f"Is 'fish' in mammals? {'fish' in mammals}")