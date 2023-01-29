X = 10
Y = 100

disposible_mask = X * 100
cloth_mask = Y * 10

if disposible_mask == cloth_mask:
    print("cloth")
elif disposible_mask < cloth_mask:
    print("disposible")
else:
    print("cloth")

print(disposible_mask , cloth_mask)