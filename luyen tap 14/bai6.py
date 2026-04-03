layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}

val_12 = layers["layer-12"]
print(f"Giá trị của layer-12 là: {val_12}")
val_31 = layers["layer-11"]["layer-22"]["layer-31"]
print(f"Giá trị của layer-31 là: {val_31}")
