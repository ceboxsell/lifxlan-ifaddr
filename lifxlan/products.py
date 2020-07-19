# coding=utf-8
product_map = {
               1: "Original 1000",
               3: "Color 650",
               10: "White 800 (Low Voltage)",
               11: "White 800 (High Voltage)",
               18: "White 900 BR30 (Low Voltage)",
               20: "Color 1000 BR30",
               22: "Color 1000",
               27: "LIFX A19",
               28: "LIFX BR30",
               29: "LIFX+ A19",
               30: "LIFX+ BR30",
               31: "LIFX Z",
               32: "LIFX Z 2",
               36: "LIFX Downlight",
               37: "LIFX Downlight",
               38: "LIFX Beam",
               43: "LIFX A19",
               44: "LIFX BR30",
               45: "LIFX+ A19",
               46: "LIFX+ BR30",
               49: "LIFX Mini",
               50: "LIFX Mini Warm to White",
               51: "LIFX Mini White",
               52: "LIFX GU10",
               55: "LIFX Tile",
               57: "LIFX Candle",
               59: "LIFX Mini Color",
               60: "LIFX Mini Warm to White",
               61: "LIFX Mini White",
               62: "LIFX A19",
               63: "LIFX BR30",
               64: "LIFX+ A19",
               65: "LIFX+ BR30",
               68: "LIFX Candle",
               81: "LIFX Candle Warm to White",
               82: "LIFX Filament"
              }

# Identifies which products are lights.
# Currently all LIFX products that speak the LAN protocol are lights.
# However, the protocol was written to allow addition of other kinds
# of devices, so it's important to be able to differentiate.
light_products = [1, 3, 10, 11, 18, 20, 22, 27, 28, 29, 30, 31, 32, 36, 37, 38, 43, 44, 45, 46, 49, 50, 51, 52, 55, 57, 59, 60, 61, 62, 63, 64, 65, 68, 81, 82]

features_map = {
                1: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                3: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                10: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2700,
                     "max_kelvin": 6500},
                11: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2700,
                     "max_kelvin": 6500},
                18: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2700,
                     "max_kelvin": 6500},
                20: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                22: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                27: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                28: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                29: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                30: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                31: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": True,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                32: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": True,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                36: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                37: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                38: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": True,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                43: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                44: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                45: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                46: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                49: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                50: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 1500,
                     "max_kelvin": 4000},
                51: {"color": False,
                     "temperature": False,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2700,
                     "max_kelvin": 2700},
                52: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                55: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": True,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                57: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 1500,
                     "max_kelvin": 9000},
                59: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                60: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 1500,
                     "max_kelvin": 4000},
                61: {"color": False,
                     "temperature": False,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2700,
                     "max_kelvin": 2700},
                62: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                63: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                64: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                65: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2500,
                     "max_kelvin": 9000},
                68: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 1500,
                     "max_kelvin": 9000},
                81: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2200,
                     "max_kelvin": 6500},
                82: {"color": False,
                     "temperature": False,
                     "infrared": False,
                     "multizone": False,
                     "chain": False,
                     "min_kelvin": 2000,
                     "max_kelvin": 2000}
               }