# utils/hardcoded_data_dicts/ubuntu_os.py
# Contains dictionary data for 'ubuntu os' parameter

UBUNTU_10_10_32_OR_UBUNTU_ANY_32_OR_UBUNTU_ANY_ANY = {
    'Ubuntu 10.10',
    'Ubuntu 10.10+, SteamOS+',
    'Ubuntu 10.10+',
    'Ubuntu 10.10 or higher',
    'Ubuntu Linux, version 10.10 or later',
    'x86/x86_64'
    'Ubuntu',
    'Ubuntu / SteamOS 94',
    'Any',
    'Ubuntu or equivalent',
    'Any distribution',
    'Ubuntu or similar',
    'any',
    'Ubuntu LTS',
    'TBD',
}
UBUNTU_10_10_64_OR_UBUNTU_ANY_64 = {
    '64 bit',
    '64-bit OS',
    '64-bit',
    'Requires a 64-bit processor and operating system',
    'Ubuntu/SteamOS 64-bit'
}
UBUNTU_12_4_32 = {
    'Ubuntu 12.04+',
    'Ubuntu 12.04',
    'Ubuntu 12.04+ or Kernel 3.x+ based distributions',
    'Ubuntu 12.04 LTS',
    'Ubuntu 12.04+, SteamOS+',
    'Ubuntu 12.04 or later',
    'Ubuntu 12.04 (32/64bit)',
    'Ubuntu 12.04 or newer',
    'Ubuntu 12',
    'Ubuntu 12.04, SteamOS',
    'Ubuntu 12.04 or higher; SteamOS',
    'Ubuntu 32-bit 12.04+',
    'Ubuntu 12.04+ or SteamOS',
    'Ubuntu 12.04 LTS, fully updated',
    'Ubuntu 12.04 or higher',
    'Ubuntu 12.4',
    'Ubuntu 12.04 or Kernel 3.x+ distributions',
    'Ubuntu 12.04+ or equivalent',
    'Ubuntu 12.04 LTS or later',
    'Linux Ubuntu 12.04',
    'Ubuntu 12.04+ / SteamOS+',
    'Ubuntu 12.04 or SteamOS',
    'Ubuntu 12.04 and Newer',
    'Linux Ubuntu 12.04 or newer',
    'Steam OS, Linux Ubuntu 12.04'
}
UBUNTU_12_4_64 = {
    'Ubuntu 12.04 (64-bit)',
    'Ubuntu 12.04 (64 Bit only)'
}
UBUNTU_14_4_32 = {
    'Ubuntu 14.04 LTS',
    'Ubuntu 14.04',
    'Ubuntu 14.04 or Higher',
    'Ubuntu 14.04+, SteamOS+',
    'Ubuntu 14',
    'Ubuntu 14.04 or later',
    'Ubuntu Equivalent Distro',
    'Ubuntu 14.04+',
    'Ubuntu 14.04 or newer',
    'Ubuntu 14.04 / SteamOS',
    'Ubuntu 14 or above',
    'Ubuntu 14+'
}
UBUNTU_14_4_64 = {
    'Ubuntu 14.04 or Steam OS 2.0 (64 bit)',
    'Steam OS 2.0 / Ubuntu 14.04 LTS (64-bit)',
    'Ubuntu 14.04 or later (64-bit)'
}
UBUNTU_16_4_32 = {
    'Ubuntu 16.04+',
    'Ubuntu 16.04',
    'Ubuntu 16.04 LTS',
    'Ubuntu 16.04 and Ubuntu 18.04',
    'Ubuntu 16.04 or later',
    'Ubuntu 16',
    'Steam OS or Ubuntu 16.04',
    'Ubuntu 16.04+, SteamOS',
    'Ubuntu 16.04 or higher',
    'Ubuntu 16.04+ / SteamOS',
    'Ubuntu 16.04 or newer',
    'Ubuntu 16.04.01'
}
UBUNTU_16_4_64 = {
    'Ubuntu 64-bit 16.04+',
    'Ubuntu 16.04 LTS (64bit)',
    'Ubuntu 16.04 (64bit)'
}
UBUNTU_18_4_32 = {
    'Ubuntu 20.04, Ubuntu 18.04, and CentOS 7',
    'Ubuntu 18.04',
    'Ubuntu 18.04.2 LTS',
    'Ubuntu 18.04+',
    'Ubuntu 18.04 LTS',
    'Ubuntu 18',
    'Ubuntu 20.04, Ubuntu 18.04, CentOS 7',
    'Ubuntu 18.04 or equivalent',
    'Ubuntu 18.04 or later'
}
UBUNTU_18_4_64 = {
    'Ubuntu 18.04 64-bit'
}
UBUNTU_20_4_32 = {
    'Ubuntu 20.04',
    'Ubuntu 20.04 or higher; SteamOS',
    'Ubuntu 20.04 LTS',
    'Ubuntu 20'
}
UBUNTU_20_4_64 = set()
UBUNTU_22_4_32 = {
    'Ubuntu 22.04',
    'Ubuntu 22.04 LTS'
}
UBUNTU_22_4_64 = set()

UBUNTU_ALL = set().union(
    UBUNTU_10_10_32_OR_UBUNTU_ANY_32_OR_UBUNTU_ANY_ANY,
    UBUNTU_10_10_64_OR_UBUNTU_ANY_64,
    UBUNTU_12_4_32,
    UBUNTU_12_4_64,
    UBUNTU_14_4_32,
    UBUNTU_14_4_64,
    UBUNTU_16_4_32,
    UBUNTU_16_4_64,
    UBUNTU_18_4_32,
    UBUNTU_18_4_64,
    UBUNTU_20_4_32,
    UBUNTU_20_4_64,
    UBUNTU_22_4_32,
    UBUNTU_22_4_64,
)
UBUNTU_OS_MAPPING = {
    **{os_name: (0, None) for os_name in UBUNTU_10_10_32_OR_UBUNTU_ANY_32_OR_UBUNTU_ANY_ANY},
    **{os_name: (1, 16, 2) for os_name in UBUNTU_10_10_64_OR_UBUNTU_ANY_64},
    **{os_name: (2, None) for os_name in UBUNTU_12_4_32},
    **{os_name: (3, 16, 2) for os_name in UBUNTU_12_4_64},
    **{os_name: (4, None) for os_name in UBUNTU_14_4_32},
    **{os_name: (5, 16, 2) for os_name in UBUNTU_14_4_64},
    **{os_name: (6, None) for os_name in UBUNTU_16_4_32},
    **{os_name: (7, 16, 2) for os_name in UBUNTU_16_4_64},
    **{os_name: (8, None) for os_name in UBUNTU_18_4_32},
    **{os_name: (9, 16, 2) for os_name in UBUNTU_18_4_64},
    **{os_name: (10, None) for os_name in UBUNTU_20_4_32},
    **{os_name: (11, 16, 2) for os_name in UBUNTU_20_4_64},
    **{os_name: (12, None) for os_name in UBUNTU_22_4_32},
    **{os_name: (13, 16, 2) for os_name in UBUNTU_22_4_64},
}
UBUNTU_OS_DICT = [
    'Ubuntu 10.10 32-bit or any 32-bit or any',
    'Ubuntu 10.10 64-bit or any 64-bit',
    'Ubuntu 12.4 32-bit',
    'Ubuntu 12.4 64-bit',
    'Ubuntu 14.4 32-bit',
    'Ubuntu 14.4 64-bit',
    'Ubuntu 16.4 32-bit',
    'Ubuntu 16.4 64-bit',
    'Ubuntu 18.4 32-bit',
    'Ubuntu 18.4 64-bit',
    'Ubuntu 20.4 32-bit',
    'Ubuntu 20.4 64-bit',
    'Ubuntu 22.4 32-bit',
    'Ubuntu 22.4 64-bit',
]