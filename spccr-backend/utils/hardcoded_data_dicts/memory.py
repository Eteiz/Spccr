# utils/hardcoded_data_dicts/memory.py
# Contains dictionary data for 'memory' parameter

MEM_100_MB_OR_MEM_ANY = {
    '100 MB RAM',
    '100 MB'
}
MEM_128_MB = {
    '128 MB RAM',
    '123 MB'
}
MEM_200_MB = {
   '200 MB RAM',
    '200 MB'
}
MEM_256_MB = {
    '256 MB RAM',
    '256 MB'
}
MEM_500_MB = {
    '500 MB RAM',
    '500 MB'
}
MEM_512_MB = {
    '512 MB RAM',
    '512 MB'
}
MEM_1000_MB = {
    '1000 MB RAM',
    '1000 MB'
}
MEM_1_GB = {
    '1 GB RAM',
    '1024 MB RAM',
    '1 GB',
    '1024 MB'
}
MEM_2000_MB = {
    '2000 MB RAM',
    '2000 MB'
}
MEM_2_GB = {
    '2 GB RAM',
    '2048 MB RAM',
    '2 GB',
    '2048 MB'
}
MEM_3_GB = {
    '3 GB RAM',
    '3 GB'
}
MEM_4000_MB = {
    '4000 MB RAM',
    '4000 MB'
}
MEM_4_GB = {
    '4 GB RAM',
    '4096 MB RAM',
    '4 GB',
    '4096 MB'
}
MEM_6_GB = {
    '6 GB RAM',
    '6 GB'
}
MEM_8_GB = {
    '8 GB RAM',
    '8 GB'
}
MEM_12_GB = {
    '12 GB RAM',
    '12 GB'
}
MEM_16_GB = {
    '16 GB RAM',
    '16 GB'
}
MEM_32_GB = set()

MEM_ALL = set().union(
    MEM_100_MB_OR_MEM_ANY,
    MEM_128_MB,
    MEM_200_MB,
    MEM_256_MB,
    MEM_500_MB,
    MEM_512_MB,
    MEM_1000_MB,
    MEM_1_GB,
    MEM_2000_MB,
    MEM_2_GB,
    MEM_3_GB,
    MEM_4000_MB,
    MEM_4_GB,
    MEM_6_GB,
    MEM_8_GB,
    MEM_12_GB,
    MEM_16_GB,
    MEM_32_GB
)
MEMORY_MAPPING = {
    **{mem: (0, None) for mem in MEM_100_MB_OR_MEM_ANY},
    **{mem: (1, None) for mem in MEM_128_MB},
    **{mem: (2, None) for mem in MEM_200_MB},
    **{mem: (3, None) for mem in MEM_256_MB},
    **{mem: (4, None) for mem in MEM_500_MB},
    **{mem: (5, None) for mem in MEM_512_MB},
    **{mem: (6, None) for mem in MEM_1000_MB},
    **{mem: (7, None) for mem in MEM_1_GB},
    **{mem: (8, None) for mem in MEM_2000_MB},
    **{mem: (9, None) for mem in MEM_2_GB},
    **{mem: (10, None) for mem in MEM_3_GB},
    **{mem: (11, None) for mem in MEM_4000_MB},
    **{mem: (12, None) for mem in MEM_4_GB},
    **{mem: (13, None) for mem in MEM_6_GB},
    **{mem: (14, None) for mem in MEM_8_GB},
    **{mem: (15, None) for mem in MEM_12_GB},
    **{mem: (16, None) for mem in MEM_16_GB},
    **{mem: (17, None) for mem in MEM_32_GB},
}
MEMORY_DICT = [
    '100 MB or any',
    '128 MB',
    '200 MB',
    '256 MB',
    '500 MB',
    '512 MB',
    '1000 MB',
    '1 GB',
    '2000 MB',
    '2 GB',
    '3 GB',
    '4000 MB',
    '4 GB',
    '6 GB',
    '8 GB',
    '12 GB',
    '16 GB',
    '32 GB'
]