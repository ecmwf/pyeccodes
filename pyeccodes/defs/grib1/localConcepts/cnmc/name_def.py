import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'calibrated forecast, wind speed (gust)'

        if table2Version == 207 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'calibrated forecast, large-scale snowfall rate w.e.'

        if table2Version == 207 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'calibrated forecast, total precipitation rate'

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'smoothed forecast, wind speed (gust)'

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'smoothed forecast, soil temperature'

        if table2Version == 206 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, large-scale snowfall rate w.e.'

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, cloud cover high'

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, cloud cover medium'

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, cloud cover low'

        if table2Version == 206 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, total cloud cover'

        if table2Version == 206 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'smoothed forecast, total precipitation rate'

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'smoothed forecast, v comp. of wind'

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'smoothed forecast, u comp. of wind'

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'smoothed forecast, dew point temp.'

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'smoothed forecast, minimum temp.'

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'smoothed forecast, maximum temp.'

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'smoothed forecast, temperature'

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 'Synth. Sat. radiance clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 'Synth. Sat. radiance cloudy'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 'Synth. Sat. brightness temperature clear sky'

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 'Synth. Sat. brightness temperature cloudy'

        if table2Version == 204 and indicatorOfParameter == 16:
            return 'Monthly Mean of RMS of difference IA-AN of kinetic energy'

        if table2Version == 204 and indicatorOfParameter == 15:
            return 'Monthly Mean of RMS of difference FG-AN of kinetic energy'

        if table2Version == 204 and indicatorOfParameter == 14:
            return 'Monthly Mean of RMS of difference IA-AN of vert.velocity (pressure)'

        if table2Version == 204 and indicatorOfParameter == 13:
            return 'Monthly Mean of RMS of difference FG-AN of vert.velocity (pressure)'

        if table2Version == 204 and indicatorOfParameter == 12:
            return 'Monthly Mean of RMS of difference IA-AN of temperature'

        if table2Version == 204 and indicatorOfParameter == 11:
            return 'Monthly Mean of RMS of difference FG-AN of temperature'

        if table2Version == 204 and indicatorOfParameter == 10:
            return 'Monthly Mean of RMS of difference IA-AN of relative humidity'

        if table2Version == 204 and indicatorOfParameter == 9:
            return 'Monthly Mean of RMS of difference FG-AN of relative humidity'

        if table2Version == 204 and indicatorOfParameter == 8:
            return 'Monthly Mean of RMS of difference IA-AN of geopotential'

        if table2Version == 204 and indicatorOfParameter == 7:
            return 'Monthly Mean of RMS of difference FG-AN of geopotential'

        if table2Version == 204 and indicatorOfParameter == 6:
            return 'Monthly Mean of RMS of difference IA-AN of v-component of wind'

        if table2Version == 204 and indicatorOfParameter == 5:
            return 'Monthly Mean of RMS of difference FG-AN of v-component of wind'

        if table2Version == 204 and indicatorOfParameter == 4:
            return 'Monthly Mean of RMS of difference IA-AN of u-component of wind'

        if table2Version == 204 and indicatorOfParameter == 3:
            return 'Monthly Mean of RMS of difference FG-AN of u-component of wind'

        if table2Version == 204 and indicatorOfParameter == 2:
            return 'Monthly Mean of RMS of difference IA-AN of pressure reduced to MSL'

        if table2Version == 204 and indicatorOfParameter == 1:
            return 'Monthly Mean of RMS of difference FG-AN of pressure reduced to MSL'

        if table2Version == 203 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 'modified cloud cover for media'

        if table2Version == 203 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 'modified cloud depth for media'

        if table2Version == 203 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 100:
            return 'Icing Grade (1=LGT,2=MOD,3=SEV)'

        if table2Version == 203 and indicatorOfParameter == 157 and indicatorOfTypeOfLevel == 1:
            return 'Ceiling'

        if table2Version == 203 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 100:
            return 'Aequivalentpotentielle Temperatur'

        if table2Version == 203 and indicatorOfParameter == 140 and indicatorOfTypeOfLevel == 1:
            return 'KO index'

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 'Druck einer isentropen Flaeche'

        if table2Version == 203 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 100:
            return 'YIPV Wind Y-Komp     Wind Y-Komponente auf isentropen Flaechen'

        if table2Version == 203 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 100:
            return 'XIPV Wind X-Komp     Wind X-Komponente auf isentropen Flaechen'

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 'Isentrope potentielle Vorticity'

        if table2Version == 203 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 100:
            return 'Qn-Vektor Q isother-senkr-KompQn ,Komp. Q-Vektor senkrecht zu den Isothermen'

        if table2Version == 203 and indicatorOfParameter == 109 and indicatorOfTypeOfLevel == 100:
            return 'Winddivergenz'

        if table2Version == 203 and indicatorOfParameter == 107 and indicatorOfTypeOfLevel == 101:
            return 'Schichtdicken-Advektion'

        if table2Version == 203 and indicatorOfParameter == 103 and indicatorOfTypeOfLevel == 101:
            return 'Geo Temperatur Adv  geostrophische Schichtdickenadvektion'

        if table2Version == 203 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 100:
            return 'geostrophische  Vorticityadvektion'

        if table2Version == 203 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 1:
            return 'weather interpretation (WMO)'

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 'Konv.-U-Grenze-nn   Hoehe der Konvektionsuntergrenze ueber nn'

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'Konvektions-U-GrenzeHoehe der Konvektionsuntergrenze ueber Grund'

        if table2Version == 203 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 1:
            return 'NiederschlagBew.-ArtKombination Niederschl.-Bew.-Blautherm. (283..407)'

        if table2Version == 203 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 100:
            return 'absolute vorticity advection'

        if table2Version == 203 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 'storm relative helicity'

        if table2Version == 203 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 'wind shear'

        if table2Version == 202 and indicatorOfParameter == 248 and indicatorOfTypeOfLevel == 1:
            return 'UV_Index_Maximum_W  UV_Index clouded (W), daily maximum'

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'Gravity wave dissipation (vertical integral)'

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Gravity wave dissipation (vertical integral)'

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'v-momentum flux due to SSO-effects'

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'v-momentum flux due to SSO-effects'

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'u-momentum flux due to SSO-effects'

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'u-momentum flux due to SSO-effects'

        if table2Version == 202 and indicatorOfParameter == 229 and indicatorOfTypeOfLevel == 1:
            return 'Ba140  - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 228 and indicatorOfTypeOfLevel == 1:
            return 'Ba140 - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 227:
            return 'Air concentration of Barium 40'

        if table2Version == 202 and indicatorOfParameter == 226 and indicatorOfTypeOfLevel == 1:
            return 'I131o  - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 225 and indicatorOfTypeOfLevel == 1:
            return 'I131o  - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 224:
            return 'I131o  - concentration'

        if table2Version == 202 and indicatorOfParameter == 223 and indicatorOfTypeOfLevel == 1:
            return 'I131g  - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 222 and indicatorOfTypeOfLevel == 1:
            return 'Xe133  - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 221:
            return 'I131g - concentration'

        if table2Version == 202 and indicatorOfParameter == 220 and indicatorOfTypeOfLevel == 1:
            return 'Xe133  - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 219 and indicatorOfTypeOfLevel == 1:
            return 'Xe133  - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 218:
            return 'Air concentration of Xenon 133 (Xe133  - concentration)'

        if table2Version == 202 and indicatorOfParameter == 217 and indicatorOfTypeOfLevel == 1:
            return 'TRACER - wet deposition'

        if table2Version == 202 and indicatorOfParameter == 216 and indicatorOfTypeOfLevel == 1:
            return 'TRACER - dry deposition'

        if table2Version == 202 and indicatorOfParameter == 215:
            return 'TRACER - concentration'

        if table2Version == 202 and indicatorOfParameter == 214 and indicatorOfTypeOfLevel == 1:
            return 'Kr85-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 213 and indicatorOfTypeOfLevel == 1:
            return 'Kr85-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 212:
            return 'Air concentration of Krypton 85  (Kr85-concentration)'

        if table2Version == 202 and indicatorOfParameter == 211 and indicatorOfTypeOfLevel == 1:
            return 'Zr95-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 210 and indicatorOfTypeOfLevel == 1:
            return 'Zr95-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 209:
            return 'Air concentration of Zirconium 95 (Zr95-concentration)'

        if table2Version == 202 and indicatorOfParameter == 208 and indicatorOfTypeOfLevel == 1:
            return 'Te132-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 207 and indicatorOfTypeOfLevel == 1:
            return 'Te132-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 206:
            return 'Air concentration of Tellurium 132 (Te132-concentration)'

        if table2Version == 202 and indicatorOfParameter == 205 and indicatorOfTypeOfLevel == 1:
            return 'Cs137-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 'Cs137-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 203:
            return 'Cs137-concentration'

        if table2Version == 202 and indicatorOfParameter == 202 and indicatorOfTypeOfLevel == 1:
            return 'I131-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 201 and indicatorOfTypeOfLevel == 1:
            return 'I131-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 200:
            return 'I131-concentration'

        if table2Version == 202 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 1:
            return 'Sr90-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 1:
            return 'Sr90-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 197:
            return 'Air concentration of Strontium 90'

        if table2Version == 202 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 1:
            return 'Ru103-wet deposition'

        if table2Version == 202 and indicatorOfParameter == 195 and indicatorOfTypeOfLevel == 1:
            return 'Ru103-dry deposition'

        if table2Version == 202 and indicatorOfParameter == 194:
            return 'Air concentration of Ruthenium 103 (Ru103- concentration)'

        if table2Version == 202 and indicatorOfParameter == 180 and indicatorOfTypeOfLevel == 110:
            return 'Ozone Mixing Ratio'

        if table2Version == 202 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 'Delay of the GPS signal trough dry atmos.'

        if table2Version == 202 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'Delay of the GPS signal trough wet atmos.'

        if table2Version == 202 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 'Delay of the GPS signal trough the (total) atm.'

        if table2Version == 202 and indicatorOfParameter == 120 and indicatorOfTypeOfLevel == 110:
            return 'Friction velocity'

        if table2Version == 202 and indicatorOfParameter == 115 and indicatorOfTypeOfLevel == 1:
            return 'geographical longitude'

        if table2Version == 202 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 1:
            return 'geographical latitude'

        if table2Version == 202 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1:
            return 'Coriolis parameter'

        if table2Version == 202 and indicatorOfParameter == 105 and indicatorOfTypeOfLevel == 1:
            return 'water vapor flux'

        if table2Version == 202 and indicatorOfParameter == 104 and indicatorOfTypeOfLevel == 110:
            return 'tendency of specific humidity'

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return 'Sea salt aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 93:
            return 'Sea salt aerosol'

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return 'Black carbon aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 92:
            return 'Black carbon aerosol'

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return 'Organic aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 91:
            return 'Organic aerosol'

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return 'Total soil dust aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 86:
            return 'Total soil dust aerosol'

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 'Total sulfate aerosol (12M)'

        if table2Version == 202 and indicatorOfParameter == 84:
            return 'Total sulfate aerosol'

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 'ratio of monthly mean NDVI (normalized differential vegetation index) to annual maximum'

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 3:
            return 'normalized differential vegetation index (NDVI)'

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 'normalized differential vegetation index'

        if table2Version == 202 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 'deciduous forest'

        if table2Version == 202 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'evergreen forest'

        topLevel = h.get_l('topLevel')
        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 'variance of soil moisture content (10-100)'

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'variance of soil moisture content (0-10)'

        if table2Version == 202 and indicatorOfParameter == 71:
            return 'Orographie + Land-Meer-Verteilung'

        if table2Version == 202 and indicatorOfParameter == 70 and indicatorOfTypeOfLevel == 1:
            return 'Min Leaf area index'

        if table2Version == 202 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 1:
            return 'Max Leaf area index'

        if table2Version == 202 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 1:
            return 'Plant covering degree in the quiescent phas'

        if table2Version == 202 and indicatorOfParameter == 67 and indicatorOfTypeOfLevel == 1:
            return 'Plant covering degree in the vegetation phase'

        if table2Version == 202 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 'vertically integrated ozone content (climatological)'

        if table2Version == 202 and indicatorOfParameter == 64 and indicatorOfTypeOfLevel == 1:
            return 'height of ozone maximum (climatological)'

        if table2Version == 202 and indicatorOfParameter == 62 and indicatorOfTypeOfLevel == 1:
            return 'root depth of vegetation'

        if table2Version == 202 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 'Leaf area index'

        if table2Version == 202 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 'Soil Type'

        if table2Version == 202 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 1 and level == 0 and timeRangeIndicator == 0:
            return 'surface emissivity'

        if table2Version == 202 and indicatorOfParameter == 49 and indicatorOfTypeOfLevel == 1:
            return 'Slope of sub-gridscale orography'

        if table2Version == 202 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 1:
            return 'Angle of sub-gridscale orography'

        if table2Version == 202 and indicatorOfParameter == 47 and indicatorOfTypeOfLevel == 1:
            return 'Anisotropy of sub-gridscale orography'

        if table2Version == 202 and indicatorOfParameter == 46 and indicatorOfTypeOfLevel == 1:
            return 'Standard deviation of sub-grid scale orography'

        if table2Version == 202 and indicatorOfParameter == 45 and indicatorOfTypeOfLevel == 110:
            return 'meridional wind tendency due to subgrid scale oro.'

        if table2Version == 202 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 'zonal wind tendency due to subgrid scale oro.'

        if table2Version == 202 and indicatorOfParameter == 42 and level == 100:
            return 'analysis error(standard deviation), v-comp. of wind'

        if table2Version == 202 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 100:
            return 'analysis error(standard deviation), u-comp. of wind'

        if table2Version == 202 and indicatorOfParameter == 40 and indicatorOfTypeOfLevel == 100:
            return 'analysis error(standard deviation), geopotential(gpm)'

        if table2Version == 202 and indicatorOfParameter == 19:
            return 'total directional spread'

        if table2Version == 202 and indicatorOfParameter == 18:
            return 'total Tm2 period'

        if table2Version == 202 and indicatorOfParameter == 17:
            return 'total Tm1 period'

        if table2Version == 202 and indicatorOfParameter == 10:
            return 'total wave mean period'

        if table2Version == 202 and indicatorOfParameter == 9:
            return 'total wave peak period'

        if table2Version == 202 and indicatorOfParameter == 8:
            return 'swell peak period'

        if table2Version == 202 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 102:
            return 'swell mean period'

        if table2Version == 202 and indicatorOfParameter == 7:
            return 'wind sea peak period'

        if table2Version == 202 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 102:
            return 'wind sea mean period'

        if table2Version == 202 and indicatorOfParameter == 4:
            return 'total wave direction'

        if table2Version == 201 and indicatorOfParameter == 243 and indicatorOfTypeOfLevel == 1:
            return 'moisture convergence for Kuo-type closure'

        if table2Version == 201 and indicatorOfParameter == 241 and indicatorOfTypeOfLevel == 1:
            return 'Convective Available Potential Energy'

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 'Massflux at convective cloud base'

        if table2Version == 201 and indicatorOfParameter == 239:
            return 'residuum of soil moisture'

        if table2Version == 201 and indicatorOfParameter == 238:
            return 'total forcing at soil surface'

        if table2Version == 201 and indicatorOfParameter == 237:
            return 'total transpiration from all soil layers'

        if table2Version == 201 and indicatorOfParameter == 236:
            return 'sum of contributions to evaporation'

        if table2Version == 201 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 110:
            return 'Effective transmissivity of solar radiation'

        if table2Version == 201 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 110:
            return 'unknown'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 'Base reflectivity (cmax)'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 'Base reflectivity'

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 'Base reflectivity'

        if table2Version == 201 and indicatorOfParameter == 215 and indicatorOfTypeOfLevel == 1:
            return 'sea Ice Temperature'

        if table2Version == 201 and indicatorOfParameter == 212 and indicatorOfTypeOfLevel == 1:
            return 'Minimal Stomatal Resistance'

        if table2Version == 201 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 'Snow temperature (top of snow)'

        if table2Version == 201 and indicatorOfParameter == 200 and indicatorOfTypeOfLevel == 1:
            return 'Plant Canopy Surface Water'

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 'soil ice content (multilayers)'

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 'Column-integrated Soil Moisture (multilayers)'

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 'Soil Temperature (multilayers)'

        if table2Version == 201 and indicatorOfParameter == 194 and indicatorOfTypeOfLevel == 100:
            return 'Air concentration of Ruthenium 103'

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10 and timeRangeIndicator == 2:
            return 'maximum Wind 10m'

        if table2Version == 201 and indicatorOfParameter == 173 and indicatorOfTypeOfLevel == 1:
            return 'mixed layer depth'

        if table2Version == 201 and indicatorOfParameter == 171 and indicatorOfTypeOfLevel == 1:
            return 'Turbulent transfer coefficient for heat (and Moisture)'

        if table2Version == 201 and indicatorOfParameter == 170 and indicatorOfTypeOfLevel == 1:
            return 'Turbulent transfer coefficient for impulse'

        if table2Version == 201 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 109:
            return 'Turbulent diffusion coefficient for heat (and moisture)'

        if table2Version == 201 and indicatorOfParameter == 153 and indicatorOfTypeOfLevel == 109:
            return 'Turbulent diffusioncoefficient for momentum'

        if table2Version == 201 and indicatorOfParameter == 152 and indicatorOfTypeOfLevel == 109:
            return 'Turbulent Kinetic Energy'

        if table2Version == 201 and indicatorOfParameter == 149 and indicatorOfTypeOfLevel == 110:
            return 'Kinetic Energy'

        if table2Version == 201 and indicatorOfParameter == 148 and indicatorOfTypeOfLevel == 109:
            return 'Tendency of turbulent kinetic energy'

        if table2Version == 201 and indicatorOfParameter == 147:
            return 'Convective turbulent kinetic enery'

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 'Convective Inhibition, mean layer'

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 'Convective Available Potential Energy, mean layer'

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 'Convective Inhibition, most unstable'

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 'Convective Available Potential Energy, most unstable'

        if table2Version == 201 and indicatorOfParameter == 142 and indicatorOfTypeOfLevel == 1:
            return 'supercell detection index 2 (only rot. up drafts)'

        if table2Version == 201 and indicatorOfParameter == 141 and indicatorOfTypeOfLevel == 1:
            return 'supercell detection index 1 (rot. up+down drafts)'

        if table2Version == 201 and indicatorOfParameter == 139 and indicatorOfTypeOfLevel == 110:
            return 'Pressure perturbation'

        if table2Version == 201 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 1:
            return 'Snow density'

        if table2Version == 201 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Graupel (snow pellets) precipitation rate'

        if table2Version == 201 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 1:
            return 'Graupel (snow pellets) precipitation rate'

        if table2Version == 201 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 110:
            return 'tendency of specific cloud ice content due to grid scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 129 and indicatorOfTypeOfLevel == 1:
            return 'Fresh snow factor (weighting function for albedo indicating freshness of snow)'

        if table2Version == 201 and indicatorOfParameter == 127 and indicatorOfTypeOfLevel == 110:
            return 'tendency of specific cloud liquid water content due to grid scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 110:
            return 'Specific humitiy tendency due to grid scale precipitation'

        if table2Version == 201 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 110:
            return 'Temperature tendency due to grid scale precipation'

        if table2Version == 201 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 'snow amount, grid-scale plus convective'

        if table2Version == 201 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 'rain amount, grid-scale plus convective'

        if table2Version == 201 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Convective rain rate (s)'

        if table2Version == 201 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 'Convective snowfall rate water equivalent'

        if table2Version == 201 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 'Convective rain rate'

        if table2Version == 201 and indicatorOfParameter == 102 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Large scale rain rate (s)'

        if table2Version == 201 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 1:
            return 'Large scale snowfall rate water equivalent'

        if table2Version == 201 and indicatorOfParameter == 100 and indicatorOfTypeOfLevel == 1:
            return 'Large scale rain rate'

        if table2Version == 201 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 110:
            return 'Specific content of precipitation particles (needed for water loadin)g'

        if table2Version == 201 and indicatorOfParameter == 89 and indicatorOfTypeOfLevel == 110:
            return 'tendency of  specific cloud ice content due to convection'

        if table2Version == 201 and indicatorOfParameter == 88 and indicatorOfTypeOfLevel == 110:
            return 'Tendency of specific cloud liquid water content due to conversion'

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 'Height of snow fall limit'

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 'height of 0 degree celsius level code 0,3,6 ?'

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 'height of top of dry convection'

        if table2Version == 201 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 110:
            return 'meridional wind tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 110:
            return 'zonal wind tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 110:
            return 'Specific humitiy tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 110:
            return 'Temperature tendency due to convection'

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'top index (vertical level) of main convective cloud (i)'

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 'base index (vertical level) of main convective cloud (i)'

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 'Height of Convective Cloud Top (i)'

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 'Height of Convective Cloud Base (i)'

        if table2Version == 201 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 110:
            return 'specific cloud water content, convective cloud'

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 'cloud top above msl, shallow convection'

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 'cloud base above msl, shallow convection'

        if table2Version == 201 and indicatorOfParameter == 53:
            return 'cloud cover CL (0..8)'

        if table2Version == 201 and indicatorOfParameter == 52:
            return 'cloud cover CM (0..8)'

        if table2Version == 201 and indicatorOfParameter == 51:
            return 'cloud cover CH (0..8)'

        if table2Version == 201 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 'subgridscale cloud ice'

        if table2Version == 201 and indicatorOfParameter == 43 and indicatorOfTypeOfLevel == 110:
            return 'subgrid scale cloud water'

        if table2Version == 201 and indicatorOfParameter == 42 and indicatorOfTypeOfLevel == 1:
            return 'vertical integral of divergence of total water content (s)'

        if table2Version == 201 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 1:
            return 'Total Column integrated water (all components incl. precipitation)'

        if table2Version == 201 and indicatorOfParameter == 40:
            return 'Total column integrated grauple'

        if table2Version == 201 and indicatorOfParameter == 39 and indicatorOfTypeOfLevel == 110:
            return 'Grauple'

        if table2Version == 201 and indicatorOfParameter == 38 and indicatorOfTypeOfLevel == 1:
            return 'Total column integrated snow'

        if table2Version == 201 and indicatorOfParameter == 37 and indicatorOfTypeOfLevel == 1:
            return 'Total column integrated rain'

        if table2Version == 201 and indicatorOfParameter == 36 and indicatorOfTypeOfLevel == 110:
            return 'Snow mixing ratio'

        if table2Version == 201 and indicatorOfParameter == 35 and indicatorOfTypeOfLevel == 110:
            return 'Rain mixing ratio'

        if table2Version == 201 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 110:
            return 'Cloud Ice Mixing Ratio'

        if table2Version == 201 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 'Cloud Mixing Ratio'

        if table2Version == 201 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 'Non-Convective Cloud Cover, grid scale'

        if table2Version == 201 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 'Cloud cover'

        if table2Version == 201 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'Stomatal Resistance'

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 'Sunshine'

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 'Latent heat flux from plants'

        if table2Version == 201 and indicatorOfParameter == 18 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Latent heat flux from bare soil'

        if table2Version == 201 and indicatorOfParameter == 14 and indicatorOfTypeOfLevel == 110:
            return 'Thermal radiation heating rate'

        if table2Version == 201 and indicatorOfParameter == 13 and indicatorOfTypeOfLevel == 110:
            return 'Solar radiation heating rate'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'Photosynthetically active radiation'

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Photosynthetically active radiation (m) (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Momentum Flux, V-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Momentum Flux, U-Component (m)'

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Sensible Heat Net Flux (m)'

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Latent Heat Net Flux (m)'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 'Net long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'Net long wave radiation flux (m) (on the model top)'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 'Net short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 'Net short wave radiation flux (m) (on the model top)'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'Net long wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Net long wave radiation flux (m) (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 'Net short wave radiation flux'

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Net short wave radiation flux (m) (at the surface)'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 'Mean period of swell waves'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'Significant height of swell waves'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'Direction of swell waves'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 'Mean period of wind waves'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'Significant height of wind waves'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'Direction of wind waves'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'Significant height of combined wind waves and swell'

        if table2Version == 2 and indicatorOfParameter == 92 and indicatorOfTypeOfLevel == 1:
            return 'sea Ice Thickness'

        if table2Version == 2 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 'Sea Ice Cover ( 0= free, 1=cover)'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and bottomLevel == 10 and timeRangeIndicator == 4 and topLevel == 0:
            return 'Water Runoff (s)'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and timeRangeIndicator == 4 and topLevel == 10 and bottomLevel == 190:
            return 'Water Runoff (10-190)'

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and timeRangeIndicator == 4 and topLevel == 10 and bottomLevel == 100:
            return 'Water Runoff (10-100)'

        if table2Version == 2 and indicatorOfParameter == 87 and indicatorOfTypeOfLevel == 1:
            return 'Plant cover'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 100 and topLevel == 10:
            return 'Column-integrated Soil Moisture (2) 10-100cm'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 'Column-integrated Soil Moisture (1) 0 -10 cm'

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 190 and topLevel == 100:
            return 'Column-integrated Soil Moisture'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 'Soil Temperature'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 'Soil Temperature'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 'Soil Temperature (41 cm depth)'

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 'Soil Temperature  ( 36 cm depth, vv=0h)'

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 'Albedo (in short-wave)'

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1:
            return 'Albedo (in short-wave)'

        if table2Version == 2 and indicatorOfParameter == 83 and indicatorOfTypeOfLevel == 1:
            return 'Surface Roughness length Surface Roughness'

        if table2Version == 2 and indicatorOfParameter == 81 and indicatorOfTypeOfLevel == 1:
            return 'Land Cover (1=land, 0=sea)'

        if table2Version == 2 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Large-Scale snowfall rate water equivalent (s)'

        if table2Version == 2 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Convective Snowfall rate water equivalent (s)'

        if table2Version == 2 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 'Total Column-Integrated Cloud Water'

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 'Cloud Cover (0 - 400 hPa)'

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 'Cloud Cover (400 - 800 hPa)'

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 'Cloud Cover (800 hPa - Soil)'

        if table2Version == 2 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 110:
            return 'Convective Cloud Cover'

        if table2Version == 2 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return 'Total Cloud Cover'

        if table2Version == 2 and indicatorOfParameter == 66 and indicatorOfTypeOfLevel == 1:
            return 'Snow Depth'

        if table2Version == 2 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 'Snow depth water equivalent'

        if table2Version == 2 and indicatorOfParameter == 63 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Convective Precipitation rate'

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 'Large-Scale Precipitation rate'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Total Precipitation rate (S)'

        if table2Version == 2 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 1:
            return 'Total Column-Integrated Cloud Ice'

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 'Evaporation (s)'

        if table2Version == 2 and indicatorOfParameter == 54 and indicatorOfTypeOfLevel == 1:
            return 'Total column integrated water vapour'

        if table2Version == 2 and indicatorOfParameter == 52:
            return 'Relative Humidity'

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Relative Humidity'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'Specific Humidity'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'Specific Humidity (2m)'

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 'Specific Humidity (S)'

        if table2Version == 2 and indicatorOfParameter == 40:
            return 'Vertical Velocity (Geometric) (w)'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'Vertical Velocity (Pressure) ( omega=dp/dt )'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'V component of wind'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'V component of wind'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'U component of wind'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'U component of wind'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 110:
            return 'Wind speed (SP)'

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'Wind speed (SP_10M)'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 'Wind Direction (DD)'

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'Wind Direction (DD_10M)'

        if table2Version == 2 and indicatorOfParameter == 30:
            return 'Wave spectra (3)'

        if table2Version == 2 and indicatorOfParameter == 29:
            return 'Wave spectra (2)'

        if table2Version == 2 and indicatorOfParameter == 28:
            return 'Wave spectra (1)'

        if table2Version == 2 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1:
            return 'Radar spectra (1)'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return '2m Dew Point Temperature (AV)'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return '2m Dew Point Temperature'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'Min 2m Temperature (i)'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 'Max 2m Temperature (i)'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'Temperature'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 'Climat. temperature, 2m Temperature'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return '2m Temperature (AV)'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 'Temperature (G)'

        if table2Version == 2 and indicatorOfParameter == 10 and indicatorOfTypeOfLevel == 1:
            return 'Total Column Integrated Ozone'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 'Geometric Height of the layer limits above sea level(NN)'

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 'Geometric Height of the earths surface above sea level'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'Geopotential'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 'Geopotential (full lev)'

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 'Geopotential (S)'

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 'Pressure Tendency (S)'

        if table2Version == 2 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 102:
            return 'Pressure Reduced to MSL'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'Pressure'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pressure (S) (not reduced)'

    return wrapped
