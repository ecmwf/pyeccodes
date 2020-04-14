def load(h):
    return ({'abbr': 'icXgl',
             'code': 1,
             'title': 'icXgl',
             'units': 'ICON global,icogl or icrgl or icigl'},
            {'abbr': 'icXeu',
             'code': 2,
             'title': 'icXeu',
             'units': 'ICON europe,icoeu or icreu or icieu'},
            {'abbr': 'icXde',
             'code': 3,
             'title': 'icXde',
             'units': 'ICON germany, icode or icrde or icide'},
            {'abbr': 'dwd', 'code': 4, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 5, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 6, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 7, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 8, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 9, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 10, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 11, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 12, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 13, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 14, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 15, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 16, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 17, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 18, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'dwd', 'code': 19, 'title': 'dwd', 'units': 'reserved ICON DWD'},
            {'abbr': 'icX1b', 'code': 20, 'title': 'icX1b', 'units': 'ICON Bw 1'},
            {'abbr': 'bw', 'code': 21, 'title': 'bw', 'units': 'reserved ICON Bw'},
            {'abbr': 'bw', 'code': 22, 'title': 'bw', 'units': 'reserved ICON Bw'},
            {'abbr': 'bw', 'code': 23, 'title': 'bw', 'units': 'reserved ICON Bw'},
            {'abbr': 'bw', 'code': 24, 'title': 'bw', 'units': 'reserved ICON Bw'},
            {'abbr': 'an2mo', 'code': 25, 'title': 'an2mo', 'units': 'old name: AN2MO'},
            {'abbr': 'icrerr',
             'code': 26,
             'title': 'icrerr',
             'units': 'ICON analysis error'},
            {'abbr': 'dwd',
             'code': 27,
             'title': 'dwd',
             'units': 'reserved ICON analysis error'},
            {'abbr': 'analy', 'code': 33, 'title': 'analy', 'units': 'old name: ANALY'},
            {'abbr': 34, 'code': 34, 'title': '034', 'units': 'old name: WAMIT'},
            {'abbr': 'ecpeps_fc',
             'code': 36,
             'title': 'ecpeps_fc',
             'units': 'old name: GPEPS'},
            {'abbr': 'noagm_fc',
             'code': 37,
             'title': 'noagm_fc',
             'units': 'old name: KWGFS'},
            {'abbr': 'noaa_gf05',
             'code': 38,
             'title': 'noaa_gf05',
             'units': 'old name: KWGF5'},
            {'abbr': 'b106_fc',
             'code': 44,
             'title': 'b106_fc',
             'units': 'old name: B106V'},
            {'abbr': 's106_fc',
             'code': 49,
             'title': 's106_fc',
             'units': 'old name: S106V'},
            {'abbr': 'an1mo', 'code': 53, 'title': 'an1mo', 'units': 'old name: AN1MO'},
            {'abbr': 'em3_an', 'code': 58, 'title': 'em3_an', 'units': 'old name: EM3AN'},
            {'abbr': 'em3_fc', 'code': 59, 'title': 'em3_fc', 'units': 'old name: EM3MO'},
            {'abbr': 'ecgm_fc',
             'code': 61,
             'title': 'ecgm_fc',
             'units': 'old name: ECMFM'},
            {'abbr': 64, 'code': 64, 'title': '064', 'units': 'old name: KWBCM'},
            {'abbr': 'mfrgm_fc',
             'code': 65,
             'title': 'mfrgm_fc',
             'units': 'old name: LFPWM'},
            {'abbr': 'noasice1_fc',
             'code': 68,
             'title': 'noasice1_fc',
             'units': 'old name: KWB01'},
            {'abbr': 'ecgsm_fc',
             'code': 69,
             'title': 'ecgsm_fc',
             'units': 'old name: SGGLO'},
            {'abbr': 'b106_an',
             'code': 74,
             'title': 'b106_an',
             'units': 'old name: B106A'},
            {'abbr': 'ecmsm_fc',
             'code': 75,
             'title': 'ecmsm_fc',
             'units': 'old name: SGMED'},
            {'abbr': 's106_an',
             'code': 79,
             'title': 's106_an',
             'units': 'old name: S106A'},
            {'abbr': 'ecle_fcprob',
             'code': 80,
             'title': 'ecle_fcprob',
             'units': 'old name: ECENS'},
            {'abbr': 'normw', 'code': 81, 'title': 'normw', 'units': 'old name: NORMW'},
            {'abbr': 'norm3', 'code': 84, 'title': 'norm3', 'units': 'old name: NORM3'},
            {'abbr': 85, 'code': 85, 'title': '085', 'units': 'old name: SGNAT'},
            {'abbr': 86, 'code': 86, 'title': '086', 'units': 'old name: SGESH'},
            {'abbr': 87, 'code': 87, 'title': '087', 'units': 'old name: SGBAL'},
            {'abbr': 'dm3_fcmean',
             'code': 88,
             'title': 'dm3_fcmean',
             'units': 'old name: MOMI3'},
            {'abbr': 'p106_an',
             'code': 94,
             'title': 'p106_an',
             'units': 'old name: P106A'},
            {'abbr': 'dm3_an', 'code': 111, 'title': 'dm3_an', 'units': 'old name: DM3AN'},
            {'abbr': 'dm3_fc', 'code': 112, 'title': 'dm3_fc', 'units': 'old name: DM3MO'},
            {'abbr': 'dm4_an', 'code': 115, 'title': 'dm4_an', 'units': 'old name: DM4AN'},
            {'abbr': 'dm4_fc', 'code': 116, 'title': 'dm4_fc', 'units': 'old name: DM4MO'},
            {'abbr': 'ukmgmp_fc',
             'code': 121,
             'title': 'ukmgmp_fc',
             'units': 'old name: WAFTF'},
            {'abbr': 'ukmgmpt_fc',
             'code': 122,
             'title': 'ukmgmpt_fc',
             'units': 'old name: WAFSZ'},
            {'abbr': 'noasice2_fc',
             'code': 123,
             'title': 'noasice2_fc',
             'units': 'old name: KWB02'},
            {'abbr': 'noasice3_fc',
             'code': 124,
             'title': 'noasice3_fc',
             'units': 'old name: KWB03'},
            {'abbr': 'noasice4_fc',
             'code': 126,
             'title': 'noasice4_fc',
             'units': 'old name: KWB04'},
            {'abbr': 'ukmlm_fcnat',
             'code': 127,
             'title': 'ukmlm_fcnat',
             'units': 'old name: NAEGR'},
            {'abbr': 'c1_an', 'code': 131, 'title': 'c1_an', 'units': 'old name: LM1AN'},
            {'abbr': 'c1_fc', 'code': 132, 'title': 'c1_fc', 'units': 'old name: LM1MO'},
            {'abbr': 'c2_an', 'code': 134, 'title': 'c2_an', 'units': 'old name: LM2AN'},
            {'abbr': 'c2_fc', 'code': 135, 'title': 'c2_fc', 'units': 'old name: LM2MO'},
            {'abbr': 'c3_an', 'code': 137, 'title': 'c3_an', 'units': 'old name: LM3AN'},
            {'abbr': 'c3_fc', 'code': 138, 'title': 'c3_fc', 'units': 'old name: LM3MO'},
            {'abbr': 'cd2', 'code': 139, 'title': 'cd2'},
            {'abbr': 'ecgm_diag_fc05',
             'code': 140,
             'title': 'ecgm_diag_fc05',
             'units': 'old name: keiner'},
            {'abbr': 'i032_an',
             'code': 141,
             'title': 'i032_an',
             'units': 'old name: I032A'},
            {'abbr': 'i048_an',
             'code': 143,
             'title': 'i048_an',
             'units': 'old name: I048A'},
            {'abbr': 'i064_an',
             'code': 145,
             'title': 'i064_an',
             'units': 'old name: I064A'},
            {'abbr': 'i096_an',
             'code': 147,
             'title': 'i096_an',
             'units': 'old name: I096A'},
            {'abbr': 'i096_fc',
             'code': 148,
             'title': 'i096_fc',
             'units': 'old name: I096F'},
            {'abbr': 'i128_an',
             'code': 149,
             'title': 'i128_an',
             'units': 'old name: I128A'},
            {'abbr': 'i128_fc',
             'code': 150,
             'title': 'i128_fc',
             'units': 'old name: I128F'},
            {'abbr': 'r096_an',
             'code': 157,
             'title': 'r096_an',
             'units': 'old name: R096A'},
            {'abbr': 'r128_an',
             'code': 159,
             'title': 'r128_an',
             'units': 'old name: R128A'},
            {'abbr': 'r128_fc',
             'code': 160,
             'title': 'r128_fc',
             'units': 'old name: R128F'},
            {'abbr': 'i192_an',
             'code': 173,
             'title': 'i192_an',
             'units': 'old name: I192A'},
            {'abbr': 'i192_fc',
             'code': 174,
             'title': 'i192_fc',
             'units': 'old name: I192F'},
            {'abbr': 'i256_an',
             'code': 175,
             'title': 'i256_an',
             'units': 'old name: I256A'},
            {'abbr': 'i256_fc',
             'code': 176,
             'title': 'i256_fc',
             'units': 'old name: I256F'},
            {'abbr': 'r192_an',
             'code': 185,
             'title': 'r192_an',
             'units': 'old name: R192A'},
            {'abbr': 'r192_fc',
             'code': 186,
             'title': 'r192_fc',
             'units': 'old name: R192F'},
            {'abbr': 'r256_an',
             'code': 187,
             'title': 'r256_an',
             'units': 'old name: R256A'},
            {'abbr': 'r256_fc',
             'code': 188,
             'title': 'r256_fc',
             'units': 'old name: R256F'},
            {'abbr': 'r128_anerr',
             'code': 194,
             'title': 'r128_anerr',
             'units': 'old name: E128A'},
            {'abbr': 'r192_anerr',
             'code': 195,
             'title': 'r192_anerr',
             'units': 'old name: E192A'},
            {'abbr': 'r256_anerr',
             'code': 196,
             'title': 'r256_anerr',
             'units': 'old name: E256A'},
            {'abbr': 'gsm_fc', 'code': 197, 'title': 'gsm_fc', 'units': 'old name: SGGM0'},
            {'abbr': 'msm_fc', 'code': 198, 'title': 'msm_fc', 'units': 'old name: SGGM1'},
            {'abbr': 'gsm_fc025',
             'code': 199,
             'title': 'gsm_fc025',
             'units': 'old name: SGGM2'},
            {'abbr': 'lsm_fc', 'code': 201, 'title': 'lsm_fc', 'units': 'old name: SGLM0'},
            {'abbr': 202, 'code': 202, 'title': '202', 'units': 'old name: SGLM1'},
            {'abbr': 'bshsice_fc',
             'code': 205,
             'title': 'bshsice_fc',
             'units': 'old name: SGBSH'},
            {'abbr': 'i384_an',
             'code': 206,
             'title': 'i384_an',
             'units': 'old name: I384A'},
            {'abbr': 'i384_fc',
             'code': 207,
             'title': 'i384_fc',
             'units': 'old name: I384F'},
            {'abbr': 'r384_an',
             'code': 208,
             'title': 'r384_an',
             'units': 'old name: R384A'},
            {'abbr': 'r384_fc',
             'code': 209,
             'title': 'r384_fc',
             'units': 'old name: R384F'},
            {'abbr': 'r384_anerr',
             'code': 210,
             'title': 'r384_anerr',
             'units': 'old name: E384A'},
            {'abbr': 'ukmgm_fcnat',
             'code': 211,
             'title': 'ukmgm_fcnat',
             'units': 'old name: EGMES'},
            {'abbr': 'mfrlm_fcnat',
             'code': 212,
             'title': 'mfrlm_fcnat',
             'units': 'old name: LFMES'},
            {'abbr': 'c4_fc', 'code': 213, 'title': 'c4_fc', 'units': 'old name: LM4MO'},
            {'abbr': 'c4_an', 'code': 214, 'title': 'c4_an', 'units': 'old name: LM4AN'},
            {'abbr': 'c5e_fc', 'code': 215, 'title': 'c5e_fc', 'units': 'old name: LM5MO'},
            {'abbr': 'c5e_an', 'code': 216, 'title': 'c5e_an', 'units': 'old name: LM5AN'},
            {'abbr': 'c6e_fc', 'code': 217, 'title': 'c6e_fc', 'units': 'old name: LM6MO'},
            {'abbr': 'c6e_an', 'code': 218, 'title': 'c6e_an', 'units': 'old name: LM6AN'},
            {'abbr': 'c7e_fc',
             'code': 219,
             'title': 'c7e_fc',
             'units': 'old name:LM7MO,LEPS'},
            {'abbr': 225, 'code': 225, 'title': '225', 'units': 'old name: SGBS1'})
