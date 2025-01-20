# utils/hardcoded_data_dicts/graphics.py
# Contains dictionary data for 'graphics' parameter

INTEL_UHD_GRAPHICS_OR_GRAPHICS_ANY = {
    'Intel HD Graphics',
    'Intel HD 4000',
    'Intel HD Graphics 4000',
    'Intel HD graphics',
    'Intel HD Graphics 3000',
    'Intel HD Graphics 4000 or better',
    'Intel HD Graphics, AMD Radeon Graphics, NVIDIA GeForce',
    'Integrated Graphics',
    'Integrated graphics',
    'Integrated',
    'Integrated Graphics Chip',
    'N/A',
    'any',
    'TBD',
    'Any'
    'GeForce 7600 GS (512 MB) or equivalent'
}
NVIDIA_GEFORCE_GTX_1050_OR_AMD_RADEON_GRAPHICS_OR_INTEL_IRIS_XE_GRAPHICS = {
    'GTX 970',
    'NVIDIA GTX 970 / AMD Radeon R9 290',
    'NVIDIA GeForce GTX 970',
    'GTX 1050',
    'NVIDIA GTX 970',
    'NVIDIA GeForce® GTX 970 / AMD Radeon™ R9 290 equivalent or greater',
    'NVIDIA GeForce GTX 970, AMD Radeon R9 290 equivalent or better',
    'GTX 960',
    'NVIDIA GeForce GTX 960',
    'NVIDIA GeForce GTX 1050',
    'NVIDIA GeForce GTX 960 2GB / AMD Radeon R7 370 2GB',
    'GeForce GTX 970',
    'NVIDIA GeForce 450 or higher with 1GB Memory',
    'GeForce 9800GTX+ (1GB)',
    'NVIDIA GeForce 9600 GSO 512',
    'Nvidia 450 GTS / Radeon HD 5750 or better',
    'NVIDIA GeForce 470 GTX or AMD Radeon 6870 HD series card or higher',
    'GeForce EN9600 GT'
}
NVIDIA_GEFORCE_GTX_1050_TI = set()
NVIDIA_GEFORCE_GTX_1060 = {
    'GTX 1060',
    'NVIDIA GeForce GTX 1060'
}
NVIDIA_GEFORCE_GTX_1070 = set()
AMD_RADEON_RX_580_OR_NVIDIA_GEFORCE_GTX_1080 = set()
NVIDIA_GEFORCE_GTX_1650 = set()
AMD_RADEON_TM_GRAPHICS_OR_NVIDIA_GEFORCE_GTX_1650_TI = set()
AMD_RADEON_RX_580_2048SP = set()
NVIDIA_GEFORCE_GTX_1660 = set()
NVIDIA_GEFORCE_GTX_1660_SUPER = set()
NVIDIA_GEFORCE_GTX_1660_TI = set()
NVIDIA_GEFORCE_RTX_2060 = set()
NVIDIA_GEFORCE_RTX_2060_SUPER = set()
NVIDIA_GEFORCE_RTX_2070_OR_AMD_RADEON_RX_5700_XT = set()
NVIDIA_GEFORCE_RTX_2070_SUPER = set()
NVIDIA_GEFORCE_RTX_3050 = set()
NVIDIA_GEFORCE_RTX_3060 = set()
AMD_RADEON_RX_6600 = set()
NVIDIA_GEFORCE_RTX_3060_TI_OR_AMD_RADEON_RX_6700_XT = set()
NVIDIA_GEFORCE_RTX_3070 = set()
NVIDIA_GEFORCE_RTX_3070_TI = set()
NVIDIA_GEFORCE_RTX_3080 = set()
NVIDIA_GEFORCE_RTX_3080_TI = set()
NVIDIA_GEFORCE_RTX_4060 = set()
NVIDIA_GEFORCE_RTX_4060_TI = set()
NVIDIA_GEFORCE_RTX_4070 = set()
NVIDIA_GEFORCE_RTX_4070_SUPER = set()
NVIDIA_GEFORCE_RTX_4070_TI = set()
NVIDIA_GEFORCE_RTX_4070_TI_SUPER = set()
NVIDIA_GEFORCE_RTX_4080 = set()
NVIDIA_GEFORCE_RTX_4080_SUPER = set()
NVIDIA_GEFORCE_RTX_4090 = set()

GRAPHICS_ALL = set.union(
    INTEL_UHD_GRAPHICS_OR_GRAPHICS_ANY,
    NVIDIA_GEFORCE_GTX_1050_OR_AMD_RADEON_GRAPHICS_OR_INTEL_IRIS_XE_GRAPHICS,
    NVIDIA_GEFORCE_GTX_1050_TI,
    NVIDIA_GEFORCE_GTX_1060,
    NVIDIA_GEFORCE_GTX_1070,
    AMD_RADEON_RX_580_OR_NVIDIA_GEFORCE_GTX_1080,
    NVIDIA_GEFORCE_GTX_1650,
    AMD_RADEON_TM_GRAPHICS_OR_NVIDIA_GEFORCE_GTX_1650_TI,
    AMD_RADEON_RX_580_2048SP,
    NVIDIA_GEFORCE_GTX_1660,
    NVIDIA_GEFORCE_GTX_1660_SUPER,
    NVIDIA_GEFORCE_GTX_1660_TI,
    NVIDIA_GEFORCE_RTX_2060,
    NVIDIA_GEFORCE_RTX_2060_SUPER,
    NVIDIA_GEFORCE_RTX_2070_OR_AMD_RADEON_RX_5700_XT,
    NVIDIA_GEFORCE_RTX_2070_SUPER,
    NVIDIA_GEFORCE_RTX_3050,
    NVIDIA_GEFORCE_RTX_3060,
    AMD_RADEON_RX_6600,
    NVIDIA_GEFORCE_RTX_3060_TI_OR_AMD_RADEON_RX_6700_XT,
    NVIDIA_GEFORCE_RTX_3070,
    NVIDIA_GEFORCE_RTX_3070_TI,
    NVIDIA_GEFORCE_RTX_3080,
    NVIDIA_GEFORCE_RTX_3080_TI,
    NVIDIA_GEFORCE_RTX_4060,
    NVIDIA_GEFORCE_RTX_4060_TI,
    NVIDIA_GEFORCE_RTX_4070,
    NVIDIA_GEFORCE_RTX_4070_SUPER,
    NVIDIA_GEFORCE_RTX_4070_TI,
    NVIDIA_GEFORCE_RTX_4070_TI_SUPER,
    NVIDIA_GEFORCE_RTX_4080,
    NVIDIA_GEFORCE_RTX_4080_SUPER,
    NVIDIA_GEFORCE_RTX_4090,
)
GRAPHICS_MAPPING = {
    **{graphics: (0, None) for graphics in INTEL_UHD_GRAPHICS_OR_GRAPHICS_ANY},
    **{graphics: (1, None) for graphics in NVIDIA_GEFORCE_GTX_1050_OR_AMD_RADEON_GRAPHICS_OR_INTEL_IRIS_XE_GRAPHICS},
    **{graphics: (2, None) for graphics in NVIDIA_GEFORCE_GTX_1050_TI},
    **{graphics: (3, None) for graphics in NVIDIA_GEFORCE_GTX_1060},
    **{graphics: (4, None) for graphics in NVIDIA_GEFORCE_GTX_1070},
    **{graphics: (5, None) for graphics in AMD_RADEON_RX_580_OR_NVIDIA_GEFORCE_GTX_1080},
    **{graphics: (6, None) for graphics in NVIDIA_GEFORCE_GTX_1650},
    **{graphics: (7, None) for graphics in AMD_RADEON_TM_GRAPHICS_OR_NVIDIA_GEFORCE_GTX_1650_TI},
    **{graphics: (8, None) for graphics in AMD_RADEON_RX_580_2048SP},
    **{graphics: (9, None) for graphics in NVIDIA_GEFORCE_GTX_1660},
    **{graphics: (10, None) for graphics in NVIDIA_GEFORCE_GTX_1660_SUPER},
    **{graphics: (11, None) for graphics in NVIDIA_GEFORCE_GTX_1660_TI},
    **{graphics: (12, None) for graphics in NVIDIA_GEFORCE_RTX_2060},
    **{graphics: (13, None) for graphics in NVIDIA_GEFORCE_RTX_2060_SUPER},
    **{graphics: (14, None) for graphics in NVIDIA_GEFORCE_RTX_2070_OR_AMD_RADEON_RX_5700_XT},
    **{graphics: (15, None) for graphics in NVIDIA_GEFORCE_RTX_2070_SUPER},
    **{graphics: (16, None) for graphics in NVIDIA_GEFORCE_RTX_3050},
    **{graphics: (17, None) for graphics in NVIDIA_GEFORCE_RTX_3060 | AMD_RADEON_RX_6600},
    **{graphics: (18, None) for graphics in NVIDIA_GEFORCE_RTX_3060_TI_OR_AMD_RADEON_RX_6700_XT},
    **{graphics: (19, None) for graphics in NVIDIA_GEFORCE_RTX_3070},
    **{graphics: (20, None) for graphics in NVIDIA_GEFORCE_RTX_3070_TI},
    **{graphics: (21, None) for graphics in NVIDIA_GEFORCE_RTX_3080},
    **{graphics: (22, None) for graphics in NVIDIA_GEFORCE_RTX_3080_TI},
    **{graphics: (23, None) for graphics in NVIDIA_GEFORCE_RTX_4060},
    **{graphics: (24, None) for graphics in NVIDIA_GEFORCE_RTX_4060_TI},
    **{graphics: (25, None) for graphics in NVIDIA_GEFORCE_RTX_4070},
    **{graphics: (26, None) for graphics in NVIDIA_GEFORCE_RTX_4070_SUPER},
    **{graphics: (27, None) for graphics in NVIDIA_GEFORCE_RTX_4070_TI},
    **{graphics: (28, None) for graphics in NVIDIA_GEFORCE_RTX_4070_TI_SUPER},
    **{graphics: (29, None) for graphics in NVIDIA_GEFORCE_RTX_4080},
    **{graphics: (30, None) for graphics in NVIDIA_GEFORCE_RTX_4080_SUPER},
    **{graphics: (31, None) for graphics in NVIDIA_GEFORCE_RTX_4090},
}
GRAPHICS_DICT = [
    'Intel UHD Graphics or any',
    'Nvidia GeForce GTX 1050 or AMD Radeon Graphics or Intel Iris Xe Graphics',
    'Nvidia GeForce GTX 1050 Ti',
    'Nvidia GeForce GTX 1060',
    'Nvidia GeForce GTX 1070',
    'AMD Radeon RX 580 or Nvidia GeForce GTX 1080',
    'Nvidia GeForce GTX 1650',
    'AMD Radeon TM Graphics or Nvidia GeForce GTX 1650 Ti',
    'AMD Radeon RX 580 2048SP',
    'Nvidia GeForce GTX 1660',
    'Nvidia GeForce GTX 1660 Super',
    'Nvidia GeForce GTX 1660 Ti',
    'Nvidia GeForce RTX 2060',
    'Nvidia GeForce RTX 2060 Super',
    'Nvidia GeForce RTX 2070 or AMD Radeon RX 5700 XT',
    'Nvidia GeForce RTX 2070 Super',
    'Nvidia GeForce RTX 3050',
    'Nvidia GeForce RTX 3060 or AMD Radeon RX 6600',
    'Nvidia GeForce RTX 3060 Ti or AMD Radeon RX 6700 XT',
    'Nvidia GeForce RTX 3070',
    'Nvidia GeForce RTX 3070 Ti',
    'Nvidia GeForce RTX 3080',
    'Nvidia GeForce RTX 3080 Ti',
    'Nvidia GeForce RTX 4060',
    'Nvidia GeForce RTX 4060 Ti',
    'Nvidia GeForce RTX 4070',
    'Nvidia GeForce RTX 4070 Super',
    'Nvidia GeForce RTX 4070 Ti',
    'Nvidia GeForce RTX 4070 Ti Super',
    'Nvidia GeForce RTX 4080',
    'Nvidia GeForce RTX 4080 Super',
    'Nvidia GeForce RTX 4090',
]