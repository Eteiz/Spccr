# utils/hardcoded_data_dicts/processor.py
# Contains dictionary data for 'processor' parameter

INTEL_DUAL_CORE_OR_PROCESSOR_ANY = {
    'Intel Dual Core',
    'Intel Dual-Core 2GHz or AMD Dual-Core 2GHz',
    'Intel Dual-Core 2.4 GHz'
}
INTEL_PENTIUM = {
    'Intel® Pentium® 4 2.0 GHz equivalent or faster processor',
    'Pentium 4 or higher, 2GHz',
    '1.2 GHz Pentium 4'
}
INTEL_CELERON = {
    'Intel Celeron',
    'Intel Celeron 1800 MHz',
    'Intel(R) Celeron(R) CPU G530 @2.40 GHz'
}
INTEL_CORE_2_DUO = {
    'Intel Core2 Duo or better',
    '2.0 Ghz Core 2 Duo',
    'Intel Core 2 Duo',
    'Core 2 Duo',
}
INTEL_CORE_2_DUO_E5200 = {
    'Intel Core 2 Duo E5200'
}
INTEL_CORE_2_DUO_E6320 = {
    'Intel Core 2 Duo E6320 (2*1866) or equivalent'
}
AMD_RYZEN_3_OR_INTEL_CORE_I3 = {
    'Intel Core i3',
    'Intel Core i3 2.00 GHz or AMD equivalent',
    'Intel Core i3 or equivalent',
    'Intel i3',
    'Intel Core i3 3.0 GHz',
}
INTEL_CORE_I3_M380 = {
    'Intel Core i3 M380'
}
INTEL_CORE_I3_4340 = {
    'Intel Core i3-4340 or better'
}
INTEL_CORE_I3_6100 = {
    'Intel Core i3-6100 / AMD FX-8350'
}
INTEL_CORE_I3_10100F = set()
AMD_RYZEN_5_OR_INTEL_CORE_I5 = {
    'Intel Core i5',
    'Intel Core i5 or AMD equivalent',
    'Intel i5',
    'Intel i5+',
    'Intel Core i5 or equivalent'
}
AMD_FX_6300_OR_INTEL_CORE_I5_4430 = {
    'Intel Core i5-4430 / AMD FX-6300'
}
INTEL_CORE_I5_4590 = {
    'Intel Core i5-4590 / AMD FX 8350',
    'Intel i5-4590 equivalent or greater',
    'Intel Core i5-4590 / AMD Ryzen 5 2600',
    'Intel Core i5-4590 (AMD FX 8350) or better',
    'Intel Core i5-4590, AMD FX 8350 equivalent or better',
    'Intel i5-4590 / AMD Ryzen 5 1500X or greater'
}
AMD_RYZEN_5_1500X_OR_INTEL_CORE_I5_7500 = {
    'Core i5-7500 / Ryzen 5 1600'
}
INTEL_CORE_I5_11400 = set()
AMD_RYZEN_5_5600X_OR_INTEL_CORE_I5_12600K = set()
INTEL_CORE_I5_13600K = set()
AMD_RYZEN_7_OR_INTEL_CORE_I7 = {
    'Intel Core i7'
}
AMD_RYZEN_7_5800X_OR_INTEL_CORE_I7_11700K = set()
INTEL_CORE_I7_12700K = set()
INTEL_CORE_I7_13700K = set()
AMD_RYZEN_9_5900X_OR_INTEL_CORE_I9_11900K = set()
INTEL_CORE_I9_12900K = set()
AMD_RYZEN_9_7950X_OR_INTEL_CORE_I9_13900K = set()

PROCESSOR_ALL = set().union(
    INTEL_DUAL_CORE_OR_PROCESSOR_ANY,
    INTEL_PENTIUM,
    INTEL_CELERON,
    INTEL_CORE_2_DUO,
    INTEL_CORE_2_DUO_E5200,
    INTEL_CORE_2_DUO_E6320,
    AMD_RYZEN_3_OR_INTEL_CORE_I3,
    INTEL_CORE_I3_M380,
    INTEL_CORE_I3_4340,
    INTEL_CORE_I3_6100,
    INTEL_CORE_I3_10100F,
    AMD_RYZEN_5_OR_INTEL_CORE_I5,
    AMD_FX_6300_OR_INTEL_CORE_I5_4430,
    INTEL_CORE_I5_4590,
    AMD_RYZEN_5_1500X_OR_INTEL_CORE_I5_7500,
    INTEL_CORE_I5_11400,
    AMD_RYZEN_5_5600X_OR_INTEL_CORE_I5_12600K,
    INTEL_CORE_I5_13600K,
    AMD_RYZEN_7_OR_INTEL_CORE_I7,
    AMD_RYZEN_7_5800X_OR_INTEL_CORE_I7_11700K,
    INTEL_CORE_I7_12700K,
    INTEL_CORE_I7_13700K,
    AMD_RYZEN_9_5900X_OR_INTEL_CORE_I9_11900K,
    INTEL_CORE_I9_12900K,
    AMD_RYZEN_9_7950X_OR_INTEL_CORE_I9_13900K
)
PROCESSOR_MAPPING = {
    **{proc: (0, None) for proc in INTEL_DUAL_CORE_OR_PROCESSOR_ANY},
    **{proc: (1, None) for proc in INTEL_PENTIUM},
    **{proc: (2, None) for proc in INTEL_CELERON},
    **{proc: (3, None) for proc in INTEL_CORE_2_DUO},
    **{proc: (4, None) for proc in INTEL_CORE_2_DUO_E5200},
    **{proc: (5, None) for proc in INTEL_CORE_2_DUO_E6320},
    **{proc: (6, None) for proc in AMD_RYZEN_3_OR_INTEL_CORE_I3},
    **{proc: (7, None) for proc in INTEL_CORE_I3_M380},
    **{proc: (8, None) for proc in INTEL_CORE_I3_4340},
    **{proc: (9, None) for proc in INTEL_CORE_I3_6100},
    **{proc: (10, None) for proc in INTEL_CORE_I3_10100F},
    **{proc: (11, None) for proc in AMD_RYZEN_5_OR_INTEL_CORE_I5},
    **{proc: (12, None) for proc in AMD_FX_6300_OR_INTEL_CORE_I5_4430},
    **{proc: (13, None) for proc in INTEL_CORE_I5_4590},
    **{proc: (14, None) for proc in AMD_RYZEN_5_1500X_OR_INTEL_CORE_I5_7500},
    **{proc: (15, None) for proc in INTEL_CORE_I5_11400},
    **{proc: (16, None) for proc in AMD_RYZEN_5_5600X_OR_INTEL_CORE_I5_12600K},
    **{proc: (17, None) for proc in INTEL_CORE_I5_13600K},
    **{proc: (18, None) for proc in AMD_RYZEN_7_OR_INTEL_CORE_I7},
    **{proc: (19, None) for proc in AMD_RYZEN_7_5800X_OR_INTEL_CORE_I7_11700K},
    **{proc: (20, None) for proc in INTEL_CORE_I7_12700K},
    **{proc: (21, None) for proc in INTEL_CORE_I7_13700K},
    **{proc: (22, None) for proc in AMD_RYZEN_9_5900X_OR_INTEL_CORE_I9_11900K},
    **{proc: (23, None) for proc in INTEL_CORE_I9_12900K},
    **{proc: (24, None) for proc in AMD_RYZEN_9_7950X_OR_INTEL_CORE_I9_13900K},
}
PROCESSOR_DICT = [
    'Intel Dual Core or any',
    'Intel Pentium',
    'Intel Celeron',
    'Intel Core 2 Duo',
    'Intel Core 2 Duo E5200',
    'Intel Core 2 Duo E6320',
    'AMD Ryzen 3 or Intel Core i3',
    'Intel Core i3 M380',
    'Intel Core i3 4340',
    'Intel Core i3 6100',
    'Intel Core i3 10100F',
    'AMD Ryzen 5 or Intel Core i5',
    'AMD FX 6300 or Intel Core i5 4430',
    'Intel Core i5 4590',
    'AMD Ryzen 5 1500X or Intel Core i5 7500',
    'Intel Core i5 11400',
    'AMD Ryzen 5 5600X or Intel Core i5 12600K',
    'Intel Core i5 13600K',
    'AMD Ryzen 7 or Intel Core i7',
    'AMD Ryzen 7 5800X or Intel Core i7 11700K',
    'Intel Core i7 12700K',
    'Intel Core i7 13700K',
    'AMD Ryzen 9 5900X or Intel Core i9 11900K',
    'Intel Core i9 12900K',
    'AMD Ryzen 9 7950X or Intel Core i9 13900K',
]