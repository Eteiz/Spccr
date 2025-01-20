# utils/hardcoded_data_dicts/windows_os.py
# Contains dictionary data for 'windows os' parameter

WINDOWS_XP_32_OR_WINDOWS_ANY_32_OR_WINDOWS_ANY_ANY = {
    'Windows XP',
    'Windows XP/Vista/7/8/10',
    'Windows XP/Vista/7/8',
    'Windows XP, Vista, 7, 8, 10',
    'Windows XP or later',
    'Windows XP or higher',
    'Windows XP, Vista, 7, 8/8.1, 10',
    'Windows XP and newer',
    'Windows XP, Vista, 7, 8, or 10',
    'Windows XP/Windows Vista/Windows 7/8/10',
    'Windows XP SP3',
    'Windows XP+',
    'XP',
    'Windows XP / Vista / 7 / 8 / 10',
    'Windows XP, 7, Vista, 8, 8.1, 10',
    'Windows XP SP2',
    'Windows XP or newer',
    'Windows'
}
WINDOWS_XP_64_OR_WINDOWS_ANY_64 = {
    'Requires a 64-bit processor and operating system'
}
WINDOWS_VISTA_32 = {
    'Windows Vista',
    'Windows 7, Vista, 8, 8.1, 10, 11',
    'Windows Vista or greater',
    'Windows Vista/7/8/10'
}
WINDOWS_VISTA_64 = set()
WINDOWS_7_32 = {
    'Windows 7',
    'Windows 7 or later',
    'Windows 7/8/10',
    'Windows 7+',
    'Windows 7 or higher',
    'Windows 7 or newer',
    'Windows 7 SP1+',
    '7',
    'Windows 7 SP1',
    'Windows 7 / 8 / 10',
    'Windows 7/8/8.1/10',
    'Windows 7 and above',
    'Windows 7 SP1, Windows 8.1 or later, Windows 10',
    'Microsoft® Windows® 7/8/8.1/10 (32bit/64bit)',
    'Windows® 7/8/8.1/10',
    'Windows 7 or above',
    'Windows 7 SP1 or newer',
    'windows 7',
    'Windows 7 / 8 / 8.1 / 10',
    'Windows 7 (SP1+), Windows 10 and Windows 11',
    'Windows 7/8/10/11',
    'WindowsR 7/8/8.1/10 (32bit/64bit)',
    'Windows 7, Windows 8, Windows 10',
    'Windows 7 / 8 / 10 / 11',
    'Windows7/8/10',
    'Windows 7 (SP1+) and Windows 10',
    'Windows 7, 8, 8.1, 10',
    'Windows 7, 8, 10, 11',
    'Microsoft Windows 7',
    'Windows 7 (SP1+)',
    'Windows7',
    'Windows 10, Windows 8, Windows 7 32-bit',
    'Windows 7,8,10',
    'Windows 7 and up',
    'Windows 7/8/8.1/10 (32bit/64bit)',
    'Window 7',
    'Windows 7, 8 or 10',
    'Windows 7 or greater',
    'Windows 7; 8; 10',
    'Windows 7 or Higher',
    'Windows 7 / 8.1 / 10',
    'Windows 7 or better'
}
WINDOWS_7_64 = {
    'Windows 7 64-bit',
    'Windows 7 64bit',
    'Windows 7 64 bit',
    'Windows 7/8/10 64-bit',
    'Windows 7 (64bit)',
    '64-bit Windows 7, Windows 8.1, Windows 10',
    'Windows 7/8.1/10 (64bit)',
    'Windows 7 x64',
    'Windows 10 64-Bit',
    'Windows 7 (64 bit)',
    'Windows 7/8.1/10 (64-bit versions)',
    'Windows 7 (64-bit)',
}
WINDOWS_8_32 = {
    'Windows 8'
}
WINDOWS_8_64 = set()
WINDOWS_8_1_32 = {
    'Windows 8.1',
    'windows 8'
}
WINDOWS_8_1_64 = set()
WINDOWS_10_32 = {
    'Windows 10',
    '10',
    'Windows 10/11',
    'Windows 10+',
    'windows 10',
    'Windows10',
    'Windows 10 or later',
    'Windows 10 or newer',
    'Win 10',
    'Windows 10 / 11',
    'Windows 10, 11',
    'Windows 10, Windows 11',
    'Windows 10 or 11',
    'win10',
    'Window 10'
}
WINDOWS_10_64 = {
    'Windows 10 64-bit',
    'Windows 10 64bit',
    'Windows 10 64 bit',
    'Windows 10 (64-bit)',
    '64-bit Windows 10',
    'Windows 10 x64',
    'Windows 10 (64bit)',
    'Windows 10 (64 bit)',
    'Windows 10 64Bit',
    'Windows 10 64 Bit',
    'Windows 10 - 64 bit'
}
WINDOWS_11_32 = {
    'Windows 11'
}
WINDOWS_11_64 = set()

WINDOWS_ALL = set().union(
    WINDOWS_XP_32_OR_WINDOWS_ANY_32_OR_WINDOWS_ANY_ANY,
    WINDOWS_XP_64_OR_WINDOWS_ANY_64,
    WINDOWS_VISTA_32,
    WINDOWS_VISTA_64,
    WINDOWS_7_32,
    WINDOWS_7_64,
    WINDOWS_8_32,
    WINDOWS_8_64,
    WINDOWS_8_1_32,
    WINDOWS_8_1_64,
    WINDOWS_10_32,
    WINDOWS_10_64,
    WINDOWS_11_32,
    WINDOWS_11_64,
)
WINDOWS_OS_MAPPING = {
    **{os_name: (0, None) for os_name in WINDOWS_XP_32_OR_WINDOWS_ANY_32_OR_WINDOWS_ANY_ANY},
    **{os_name: (1, 16, 2) for os_name in WINDOWS_XP_64_OR_WINDOWS_ANY_64},
    **{os_name: (2, None) for os_name in WINDOWS_VISTA_32},
    **{os_name: (3, 16, 2) for os_name in WINDOWS_VISTA_64},
    **{os_name: (4, None) for os_name in WINDOWS_7_32},
    **{os_name: (5, 16, 2) for os_name in WINDOWS_7_64},
    **{os_name: (6, None) for os_name in WINDOWS_8_32},
    **{os_name: (7, 16, 2) for os_name in WINDOWS_8_64},
    **{os_name: (8, None) for os_name in WINDOWS_8_1_32},
    **{os_name: (9, 16, 2) for os_name in WINDOWS_8_1_64},
    **{os_name: (10, None) for os_name in WINDOWS_10_32},
    **{os_name: (11, 16, 2) for os_name in WINDOWS_10_64},
    **{os_name: (12, None) for os_name in WINDOWS_11_32},
    **{os_name: (13, 16, 2) for os_name in WINDOWS_11_64},
}
WINDOWS_OS_DICT = [
    'Windows XP 32-bit or any 32-bit or any',
    'Windows XP 64-bit or any 64-bit',
    'Windows Vista 32-bit',
    'Windows Vista 64-bit',
    'Windows 7 32-bit',
    'Windows 7 64-bit',
    'Windows 8 32-bit',
    'Windows 8 64-bit',
    'Windows 8.1 32-bit',
    'Windows 8.1 64-bit',
    'Windows 10 32-bit',
    'Windows 10 64-bit',
    'Windows 11 32-bit',
    'Windows 11 64-bit',
]