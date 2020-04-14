import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 228 and indicatorOfParameter == 254:
            return 'ASCAT second soil moisture CDF matching parameter'

        if table2Version == 228 and indicatorOfParameter == 253:
            return 'ASCAT first soil moisture CDF matching parameter'

        if table2Version == 228 and indicatorOfParameter == 247:
            return '100 metre V wind component'

        if table2Version == 228 and indicatorOfParameter == 246:
            return '100 metre U wind component'

        if table2Version == 228 and indicatorOfParameter == 136:
            return 'U-tendency from non-orographic wave drag'

        if table2Version == 228 and indicatorOfParameter == 134:
            return 'V-tendency from non-orographic wave drag'

        if table2Version == 211 and indicatorOfParameter == 117:
            return 'Wildfire Flux of Dimethyl Sulfide (DMS) (C2H6S)'

        if table2Version == 211 and indicatorOfParameter == 116:
            return 'Wildfire Flux of Ammonia (NH3)'

        if table2Version == 211 and indicatorOfParameter == 115:
            return 'Wildfire Flux of Acetone (C3H6O)'

        if table2Version == 211 and indicatorOfParameter == 114:
            return 'Wildfire Flux of Acetaldehyde (C2H4O)'

        if table2Version == 211 and indicatorOfParameter == 113:
            return 'Wildfire Flux of Formaldehyde (CH2O)'

        if table2Version == 211 and indicatorOfParameter == 112:
            return 'Wildfire Flux of Higher Alkanes (CnH2n+2, C>=4)'

        if table2Version == 211 and indicatorOfParameter == 111:
            return 'Wildfire Flux of Higher Alkenes (CnH2n, C>=4)'

        if table2Version == 211 and indicatorOfParameter == 110:
            return 'Wildfire Flux of Toluene_lump (C7H8+ C6H6 + C8H10)'

        if table2Version == 211 and indicatorOfParameter == 109:
            return 'Wildfire Flux of Terpenes (C5H8)n'

        if table2Version == 211 and indicatorOfParameter == 108:
            return 'Wildfire Flux of Isoprene (C5H8)'

        if table2Version == 211 and indicatorOfParameter == 107:
            return 'Wildfire Flux of Propene (C3H6)'

        if table2Version == 211 and indicatorOfParameter == 106:
            return 'Wildfire Flux of Ethene (C2H4)'

        if table2Version == 211 and indicatorOfParameter == 105:
            return 'Wildfire Flux of Propane (C3H8)'

        if table2Version == 211 and indicatorOfParameter == 104:
            return 'Wildfire Flux of Ethanol (C2H5OH)'

        if table2Version == 211 and indicatorOfParameter == 103:
            return 'Wildfire Flux of Methanol (CH3OH)'

        if table2Version == 211 and indicatorOfParameter == 102:
            return 'Wildfire flux of Sulfur Dioxide'

        if table2Version == 211 and indicatorOfParameter == 101:
            return 'Wildfire radiative power maximum'

        if table2Version == 210 and indicatorOfParameter == 117:
            return 'Wildfire Flux of Dimethyl Sulfide (DMS) (C2H6S)'

        if table2Version == 210 and indicatorOfParameter == 116:
            return 'Wildfire Flux of Ammonia (NH3)'

        if table2Version == 210 and indicatorOfParameter == 115:
            return 'Wildfire Flux of Acetone (C3H6O)'

        if table2Version == 210 and indicatorOfParameter == 114:
            return 'Wildfire Flux of Acetaldehyde (C2H4O)'

        if table2Version == 210 and indicatorOfParameter == 113:
            return 'Wildfire Flux of Formaldehyde (CH2O)'

        if table2Version == 210 and indicatorOfParameter == 112:
            return 'Wildfire Flux of Higher Alkanes (CnH2n+2, C>=4)'

        if table2Version == 210 and indicatorOfParameter == 111:
            return 'Wildfire Flux of Higher Alkenes (CnH2n, C>=4)'

        if table2Version == 210 and indicatorOfParameter == 110:
            return 'Wildfire Flux of Toluene_lump (C7H8+ C6H6 + C8H10)'

        if table2Version == 210 and indicatorOfParameter == 109:
            return 'Wildfire Flux of Terpenes (C5H8)n'

        if table2Version == 210 and indicatorOfParameter == 108:
            return 'Wildfire Flux of Isoprene (C5H8)'

        if table2Version == 210 and indicatorOfParameter == 107:
            return 'Wildfire Flux of Propene (C3H6)'

        if table2Version == 210 and indicatorOfParameter == 106:
            return 'Wildfire Flux of Ethene (C2H4)'

        if table2Version == 210 and indicatorOfParameter == 105:
            return 'Wildfire Flux of Propane (C3H8)'

        if table2Version == 210 and indicatorOfParameter == 104:
            return 'Wildfire Flux of Ethanol (C2H5OH)'

        if table2Version == 210 and indicatorOfParameter == 103:
            return 'Wildfire Flux of Methanol (CH3OH)'

        if table2Version == 210 and indicatorOfParameter == 102:
            return 'Wildfire flux of Sulfur Dioxide'

        if table2Version == 210 and indicatorOfParameter == 101:
            return 'Wildfire radiative power maximum'

        if table2Version == 140 and indicatorOfParameter == 216:
            return 'V-component stokes drift'

        if table2Version == 140 and indicatorOfParameter == 215:
            return 'U-component stokes drift'

        if table2Version == 234 and indicatorOfParameter == 228:
            return 'Total precipitation significance'

        if table2Version == 234 and indicatorOfParameter == 167:
            return '2 metre temperature significance'

        if table2Version == 234 and indicatorOfParameter == 151:
            return 'Mean sea level pressure significance'

        if table2Version == 234 and indicatorOfParameter == 139:
            return 'Surface temperature significance'

        if table2Version == 230 and indicatorOfParameter == 212:
            return 'TOA incident solar radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 210:
            return 'Surface net solar radiation, clear sky (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 209:
            return 'Top net thermal radiation, clear sky (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 208:
            return 'Top net solar radiation, clear sky (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 205:
            return 'Runoff (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 198:
            return 'Skin reservoir content (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 196:
            return 'Meridional component of gravity wave stress (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 195:
            return 'Longitudinal component of gravity wave stress (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 189:
            return 'Sunshine duration (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 182:
            return 'Evaporation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 181:
            return 'North-South surface stress (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 180:
            return 'East-West surface stress (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 179:
            return 'Top net thermal radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 178:
            return 'Top net solar radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 176:
            return 'Surface net solar radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 147:
            return 'Surface latent heat flux (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 144:
            return 'Snowfall (convective + stratiform) (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 143:
            return 'Convective precipitation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 142:
            return 'Stratiform precipitation (Large-scale precipitation) (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 58:
            return 'Photosynthetically active radiation at the surface (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 57:
            return 'Downward UV radiation at the surface (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 46:
            return 'Solar duration (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 45:
            return 'Snowmelt (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 44:
            return 'Snow evaporation (variable resolution)'

        if table2Version == 228 and indicatorOfParameter == 228:
            return 'Total Precipitation'

        if table2Version == 228 and indicatorOfParameter == 171:
            return 'Wilting point'

        if table2Version == 228 and indicatorOfParameter == 170:
            return 'Field capacity'

        if table2Version == 228 and indicatorOfParameter == 164:
            return 'Total Cloud Cover'

        if table2Version == 228 and indicatorOfParameter == 144:
            return 'Snow Fall water equivalent'

        if table2Version == 228 and indicatorOfParameter == 141:
            return 'Snow depth water equivalent'

        if table2Version == 228 and indicatorOfParameter == 139:
            return 'Soil Temperature'

        if table2Version == 228 and indicatorOfParameter == 132:
            return 'Neutral wind at 10 m v-component'

        if table2Version == 228 and indicatorOfParameter == 131:
            return 'Neutral wind at 10 m u-component'

        if table2Version == 228 and indicatorOfParameter == 39:
            return 'Soil Moisture'

        if table2Version == 228 and indicatorOfParameter == 19:
            return 'Trapping layer top height'

        if table2Version == 228 and indicatorOfParameter == 18:
            return 'Trapping layer base height'

        if table2Version == 228 and indicatorOfParameter == 17:
            return 'Duct base height'

        if table2Version == 228 and indicatorOfParameter == 16:
            return 'Mean vertical gradient of refractivity inside trapping layer'

        if table2Version == 228 and indicatorOfParameter == 15:
            return 'Minimum vertical gradient of refractivity inside trapping layer'

        if table2Version == 228 and indicatorOfParameter == 14:
            return 'Lake ice depth'

        if table2Version == 228 and indicatorOfParameter == 13:
            return 'Lake ice temperature'

        if table2Version == 228 and indicatorOfParameter == 12:
            return 'Lake shape factor'

        if table2Version == 228 and indicatorOfParameter == 11:
            return 'Lake total layer temperature'

        if table2Version == 228 and indicatorOfParameter == 10:
            return 'Lake bottom temperature'

        if table2Version == 228 and indicatorOfParameter == 9:
            return 'Lake mix-layer depth'

        if table2Version == 228 and indicatorOfParameter == 8:
            return 'Lake mix-layer temperature'

        if table2Version == 228 and indicatorOfParameter == 7:
            return 'Lake depth'

        if table2Version == 228 and indicatorOfParameter == 6:
            return 'Mean total cloud cover'

        if table2Version == 228 and indicatorOfParameter == 5:
            return 'Mean of 10 metre wind speed'

        if table2Version == 228 and indicatorOfParameter == 4:
            return 'Mean temperature at 2 metres'

        if table2Version == 228 and indicatorOfParameter == 3:
            return 'Friction velocity'

        if table2Version == 228 and indicatorOfParameter == 2:
            return 'Orography'

        if table2Version == 228 and indicatorOfParameter == 1:
            return 'Convective inhibition'

        if table2Version == 220 and indicatorOfParameter == 228:
            return 'Total precipitation observation count'

        if table2Version == 211 and indicatorOfParameter == 216:
            return 'Total Aerosol Optical Depth at 1240nm'

        if table2Version == 211 and indicatorOfParameter == 215:
            return 'Total Aerosol Optical Depth at 865nm'

        if table2Version == 211 and indicatorOfParameter == 214:
            return 'Total Aerosol Optical Depth at 670nm'

        if table2Version == 211 and indicatorOfParameter == 213:
            return 'Total Aerosol Optical Depth at 469nm'

        if table2Version == 211 and indicatorOfParameter == 212:
            return 'Sulphate Aerosol Optical Depth at 550nm'

        if table2Version == 211 and indicatorOfParameter == 211:
            return 'Black Carbon Aerosol Optical Depth at 550nm'

        if table2Version == 211 and indicatorOfParameter == 210:
            return 'Organic Matter Aerosol Optical Depth at 550nm'

        if table2Version == 211 and indicatorOfParameter == 209:
            return 'Dust Aerosol Optical Depth at 550nm'

        if table2Version == 211 and indicatorOfParameter == 208:
            return 'Sea Salt Aerosol Optical Depth at 550nm'

        if table2Version == 211 and indicatorOfParameter == 207:
            return 'Total Aerosol Optical Depth at 550nm'

        if table2Version == 211 and indicatorOfParameter == 206:
            return 'GEMS Total column ozone'

        if table2Version == 211 and indicatorOfParameter == 203:
            return 'GEMS Ozone'

        if table2Version == 211 and indicatorOfParameter == 185:
            return 'Anthropogenic Emissions of Sulphur Hexafluoride'

        if table2Version == 211 and indicatorOfParameter == 184:
            return 'Total column Sulphur Hexafluoride'

        if table2Version == 211 and indicatorOfParameter == 183:
            return 'Total column Radon'

        if table2Version == 211 and indicatorOfParameter == 182:
            return 'Sulphur Hexafluoride'

        if table2Version == 211 and indicatorOfParameter == 181:
            return 'Radon'

        if table2Version == 211 and indicatorOfParameter == 166:
            return 'Surface flux reactive tracer 10'

        if table2Version == 211 and indicatorOfParameter == 165:
            return 'Surface flux reactive tracer 9'

        if table2Version == 211 and indicatorOfParameter == 164:
            return 'Surface flux reactive tracer 8'

        if table2Version == 211 and indicatorOfParameter == 163:
            return 'Surface flux reactive tracer 7'

        if table2Version == 211 and indicatorOfParameter == 162:
            return 'Surface flux reactive tracer 6'

        if table2Version == 211 and indicatorOfParameter == 161:
            return 'Surface flux reactive tracer 5'

        if table2Version == 211 and indicatorOfParameter == 160:
            return 'Surface flux reactive tracer 4'

        if table2Version == 211 and indicatorOfParameter == 159:
            return 'Surface flux reactive tracer 3'

        if table2Version == 211 and indicatorOfParameter == 158:
            return 'Surface flux reactive tracer 2'

        if table2Version == 211 and indicatorOfParameter == 157:
            return 'Surface flux reactive tracer 1'

        if table2Version == 211 and indicatorOfParameter == 156:
            return 'Surface flux GEMS Ozone'

        if table2Version == 211 and indicatorOfParameter == 155:
            return 'Surface flux Formaldehyde'

        if table2Version == 211 and indicatorOfParameter == 154:
            return 'Surface flux Carbon monoxide'

        if table2Version == 211 and indicatorOfParameter == 153:
            return 'Surface flux Sulphur dioxide'

        if table2Version == 211 and indicatorOfParameter == 152:
            return 'Surface flux Nitrogen dioxide'

        if table2Version == 211 and indicatorOfParameter == 151:
            return 'Surface flux Nitrogen oxides'

        if table2Version == 211 and indicatorOfParameter == 150:
            return 'Total column GRG tracer 10'

        if table2Version == 211 and indicatorOfParameter == 149:
            return 'Reactive tracer 10 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 148:
            return 'Total column GRG tracer 9'

        if table2Version == 211 and indicatorOfParameter == 147:
            return 'Reactive tracer 9 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 146:
            return 'Total column GRG tracer 8'

        if table2Version == 211 and indicatorOfParameter == 145:
            return 'Reactive tracer 8 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 144:
            return 'Total column GRG tracer 7'

        if table2Version == 211 and indicatorOfParameter == 143:
            return 'Reactive tracer 7 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 142:
            return 'Total column GRG tracer 6'

        if table2Version == 211 and indicatorOfParameter == 141:
            return 'Reactive tracer 6 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 140:
            return 'Total column GRG tracer 5'

        if table2Version == 211 and indicatorOfParameter == 139:
            return 'Reactive tracer 5 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 138:
            return 'Total column GRG tracer 4'

        if table2Version == 211 and indicatorOfParameter == 137:
            return 'Reactive tracer 4 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 136:
            return 'Total column GRG tracer 3'

        if table2Version == 211 and indicatorOfParameter == 135:
            return 'Reactive tracer 3 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 134:
            return 'Total column GRG tracer 2'

        if table2Version == 211 and indicatorOfParameter == 133:
            return 'Reactive tracer 2 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 132:
            return 'Total column GRG tracer 1'

        if table2Version == 211 and indicatorOfParameter == 131:
            return 'Reactive tracer 1 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 130:
            return 'Total Column Nitrogen Oxides'

        if table2Version == 211 and indicatorOfParameter == 129:
            return 'Nitrogen Oxides'

        if table2Version == 211 and indicatorOfParameter == 128:
            return 'Total column Formaldehyde'

        if table2Version == 211 and indicatorOfParameter == 127:
            return 'Total column Carbon monoxide'

        if table2Version == 211 and indicatorOfParameter == 126:
            return 'Total column Sulphur dioxide'

        if table2Version == 211 and indicatorOfParameter == 125:
            return 'Total column Nitrogen dioxide'

        if table2Version == 211 and indicatorOfParameter == 124:
            return 'Formaldehyde'

        if table2Version == 211 and indicatorOfParameter == 123:
            return 'Carbon monoxide'

        if table2Version == 211 and indicatorOfParameter == 122:
            return 'Sulphur dioxide'

        if table2Version == 211 and indicatorOfParameter == 121:
            return 'Nitrogen dioxide'

        if table2Version == 211 and indicatorOfParameter == 100:
            return 'Wildfire combustion rate'

        if table2Version == 211 and indicatorOfParameter == 99:
            return 'Wildfire radiative power'

        if table2Version == 211 and indicatorOfParameter == 98:
            return 'Wildfire observed area'

        if table2Version == 211 and indicatorOfParameter == 97:
            return 'Wildfire fraction of area observed'

        if table2Version == 211 and indicatorOfParameter == 96:
            return 'Wildfire Fuel Load: Carbon per unit area'

        if table2Version == 211 and indicatorOfParameter == 95:
            return 'Wildfire Combustion Completeness'

        if table2Version == 211 and indicatorOfParameter == 94:
            return 'Wildfire vegetation map index'

        if table2Version == 211 and indicatorOfParameter == 93:
            return 'Wildfire fraction of C4 plants'

        if table2Version == 211 and indicatorOfParameter == 92:
            return 'Wildfire overall flux of burnt Carbon'

        if table2Version == 211 and indicatorOfParameter == 91:
            return 'Wildfire flux of Black Carbon'

        if table2Version == 211 and indicatorOfParameter == 90:
            return 'Wildfire flux of Organic Carbon'

        if table2Version == 211 and indicatorOfParameter == 89:
            return 'Wildfire flux of Total Carbon in Aerosols'

        if table2Version == 211 and indicatorOfParameter == 88:
            return 'Wildfire flux of Total Particulate Matter'

        if table2Version == 211 and indicatorOfParameter == 87:
            return 'Wildfire flux of Particulate Matter PM2.5'

        if table2Version == 211 and indicatorOfParameter == 86:
            return 'Wildfire flux of Nitrous Oxide'

        if table2Version == 211 and indicatorOfParameter == 85:
            return 'Wildfire flux of Nitrogen Oxides NOx'

        if table2Version == 211 and indicatorOfParameter == 84:
            return 'Wildfire flux of Hydrogen'

        if table2Version == 211 and indicatorOfParameter == 83:
            return 'Wildfire flux of Non-Methane Hydro-Carbons'

        if table2Version == 211 and indicatorOfParameter == 82:
            return 'Wildfire flux of Methane'

        if table2Version == 211 and indicatorOfParameter == 81:
            return 'Wildfire flux of Carbon Monoxide'

        if table2Version == 211 and indicatorOfParameter == 80:
            return 'Wildfire flux of Carbon Dioxide'

        if table2Version == 211 and indicatorOfParameter == 71:
            return 'Methane loss rate due to radical hydroxyl (OH)'

        if table2Version == 211 and indicatorOfParameter == 70:
            return 'Methane Surface Fluxes'

        if table2Version == 211 and indicatorOfParameter == 69:
            return 'Anthropogenic emissions of Carbon Dioxide'

        if table2Version == 211 and indicatorOfParameter == 68:
            return 'Natural biosphere flux of Carbon Dioxide'

        if table2Version == 211 and indicatorOfParameter == 67:
            return 'Ocean flux of Carbon Dioxide'

        if table2Version == 211 and indicatorOfParameter == 66:
            return 'Total column Nitrous oxide'

        if table2Version == 211 and indicatorOfParameter == 65:
            return 'Total column Methane'

        if table2Version == 211 and indicatorOfParameter == 64:
            return 'Total column Carbon Dioxide'

        if table2Version == 211 and indicatorOfParameter == 63:
            return 'Nitrous oxide'

        if table2Version == 211 and indicatorOfParameter == 62:
            return 'Methane'

        if table2Version == 211 and indicatorOfParameter == 61:
            return 'Carbon Dioxide'

        if table2Version == 211 and indicatorOfParameter == 54:
            return 'Soil clay content'

        if table2Version == 211 and indicatorOfParameter == 53:
            return 'Lifting threshold speed'

        if table2Version == 211 and indicatorOfParameter == 52:
            return 'Dust emission potential'

        if table2Version == 211 and indicatorOfParameter == 51:
            return 'Aerosol large mode optical depth'

        if table2Version == 211 and indicatorOfParameter == 50:
            return 'Aerosol small mode optical depth'

        if table2Version == 211 and indicatorOfParameter == 49:
            return 'Aerosol precursor optical depth'

        if table2Version == 211 and indicatorOfParameter == 48:
            return 'Aerosol large mode mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 47:
            return 'Aerosol small mode mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 46:
            return 'Aerosol precursor mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 42:
            return 'Aerosol type 12 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 41:
            return 'Aerosol type 11 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 40:
            return 'Aerosol type 10 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 39:
            return 'Aerosol type 9 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 38:
            return 'Aerosol type 8 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 37:
            return 'Aerosol type 7 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 36:
            return 'Aerosol type 6 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 35:
            return 'Aerosol type 5 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 34:
            return 'Aerosol type 4 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 33:
            return 'Aerosol type 3 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 32:
            return 'Aerosol type 2 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 31:
            return 'Aerosol type 1 sink/loss accumulated'

        if table2Version == 211 and indicatorOfParameter == 27:
            return 'Aerosol type 12 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 26:
            return 'Aerosol type 11 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 25:
            return 'Aerosol type 10 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 24:
            return 'Aerosol type 9 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 23:
            return 'Aerosol type 8 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 22:
            return 'Aerosol type 7 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 21:
            return 'Aerosol type 6 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 20:
            return 'Aerosol type 5 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 19:
            return 'Aerosol type 4 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 18:
            return 'Aerosol type 3 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 17:
            return 'Aerosol type 2 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 16:
            return 'Aerosol type 1 source/gain accumulated'

        if table2Version == 211 and indicatorOfParameter == 12:
            return 'Aerosol type 12 mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 11:
            return 'Sulphate Aerosol Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 10:
            return 'Hydrophobic Black Carbon Aerosol Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 9:
            return 'Hydrophilic Black Carbon Aerosol Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 8:
            return 'Hydrophobic Organic Matter Aerosol Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 7:
            return 'Hydrophilic Organic Matter Aerosol Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 6:
            return 'Dust Aerosol (0.9 - 20 um) Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 5:
            return 'Dust Aerosol (0.55 - 0.9 um) Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 4:
            return 'Dust Aerosol (0.03 - 0.55 um) Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 3:
            return 'Sea Salt Aerosol (5 - 20 um) Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 2:
            return 'Sea Salt Aerosol (0.5 - 5 um) Mixing Ratio'

        if table2Version == 211 and indicatorOfParameter == 1:
            return 'Sea Salt Aerosol (0.03 - 0.5 um) Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 216:
            return 'Total Aerosol Optical Depth at 1240nm'

        if table2Version == 210 and indicatorOfParameter == 215:
            return 'Total Aerosol Optical Depth at 865nm'

        if table2Version == 210 and indicatorOfParameter == 214:
            return 'Total Aerosol Optical Depth at 670nm'

        if table2Version == 210 and indicatorOfParameter == 213:
            return 'Total Aerosol Optical Depth at 469nm'

        if table2Version == 210 and indicatorOfParameter == 212:
            return 'Sulphate Aerosol Optical Depth at 550nm'

        if table2Version == 210 and indicatorOfParameter == 211:
            return 'Black Carbon Aerosol Optical Depth at 550nm'

        if table2Version == 210 and indicatorOfParameter == 210:
            return 'Organic Matter Aerosol Optical Depth at 550nm'

        if table2Version == 210 and indicatorOfParameter == 209:
            return 'Dust Aerosol Optical Depth at 550nm'

        if table2Version == 210 and indicatorOfParameter == 208:
            return 'Sea Salt Aerosol Optical Depth at 550nm'

        if table2Version == 210 and indicatorOfParameter == 207:
            return 'Total Aerosol Optical Depth at 550nm'

        if table2Version == 210 and indicatorOfParameter == 206:
            return 'GEMS Total column ozone'

        if table2Version == 210 and indicatorOfParameter == 203:
            return 'GEMS Ozone'

        if table2Version == 210 and indicatorOfParameter == 185:
            return 'Anthropogenic Emissions of Sulphur Hexafluoride'

        if table2Version == 210 and indicatorOfParameter == 184:
            return 'Total column Sulphur Hexafluoride'

        if table2Version == 210 and indicatorOfParameter == 183:
            return 'Total column Radon'

        if table2Version == 210 and indicatorOfParameter == 182:
            return 'Sulphur Hexafluoride'

        if table2Version == 210 and indicatorOfParameter == 181:
            return 'Radon'

        if table2Version == 210 and indicatorOfParameter == 166:
            return 'Surface flux reactive tracer 10'

        if table2Version == 210 and indicatorOfParameter == 165:
            return 'Surface flux reactive tracer 9'

        if table2Version == 210 and indicatorOfParameter == 164:
            return 'Surface flux reactive tracer 8'

        if table2Version == 210 and indicatorOfParameter == 163:
            return 'Surface flux reactive tracer 7'

        if table2Version == 210 and indicatorOfParameter == 162:
            return 'Surface flux reactive tracer 6'

        if table2Version == 210 and indicatorOfParameter == 161:
            return 'Surface flux reactive tracer 5'

        if table2Version == 210 and indicatorOfParameter == 160:
            return 'Surface flux reactive tracer 4'

        if table2Version == 210 and indicatorOfParameter == 159:
            return 'Surface flux reactive tracer 3'

        if table2Version == 210 and indicatorOfParameter == 158:
            return 'Surface flux reactive tracer 2'

        if table2Version == 210 and indicatorOfParameter == 157:
            return 'Surface flux reactive tracer 1'

        if table2Version == 210 and indicatorOfParameter == 156:
            return 'Surface flux GEMS Ozone'

        if table2Version == 210 and indicatorOfParameter == 155:
            return 'Surface flux Formaldehyde'

        if table2Version == 210 and indicatorOfParameter == 154:
            return 'Surface flux Carbon monoxide'

        if table2Version == 210 and indicatorOfParameter == 153:
            return 'Surface flux Sulphur dioxide'

        if table2Version == 210 and indicatorOfParameter == 152:
            return 'Surface flux Nitrogen dioxide'

        if table2Version == 210 and indicatorOfParameter == 151:
            return 'Surface flux Nitrogen oxides'

        if table2Version == 210 and indicatorOfParameter == 150:
            return 'Total column GRG tracer 10'

        if table2Version == 210 and indicatorOfParameter == 149:
            return 'Reactive tracer 10 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 148:
            return 'Total column GRG tracer 9'

        if table2Version == 210 and indicatorOfParameter == 147:
            return 'Reactive tracer 9 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 146:
            return 'Total column GRG tracer 8'

        if table2Version == 210 and indicatorOfParameter == 145:
            return 'Reactive tracer 8 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 144:
            return 'Total column GRG tracer 7'

        if table2Version == 210 and indicatorOfParameter == 143:
            return 'Reactive tracer 7 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 142:
            return 'Total column GRG tracer 6'

        if table2Version == 210 and indicatorOfParameter == 141:
            return 'Reactive tracer 6 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 140:
            return 'Total column GRG tracer 5'

        if table2Version == 210 and indicatorOfParameter == 139:
            return 'Reactive tracer 5 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 138:
            return 'Total column GRG tracer 4'

        if table2Version == 210 and indicatorOfParameter == 137:
            return 'Reactive tracer 4 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 136:
            return 'Total column GRG tracer 3'

        if table2Version == 210 and indicatorOfParameter == 135:
            return 'Reactive tracer 3 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 134:
            return 'Total column GRG tracer 2'

        if table2Version == 210 and indicatorOfParameter == 133:
            return 'Reactive tracer 2 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 132:
            return 'Total column GRG tracer 1'

        if table2Version == 210 and indicatorOfParameter == 131:
            return 'Reactive tracer 1 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 130:
            return 'Total Column Nitrogen Oxides'

        if table2Version == 210 and indicatorOfParameter == 129:
            return 'Nitrogen Oxides'

        if table2Version == 210 and indicatorOfParameter == 128:
            return 'Total column Formaldehyde'

        if table2Version == 210 and indicatorOfParameter == 127:
            return 'Total column Carbon monoxide'

        if table2Version == 210 and indicatorOfParameter == 126:
            return 'Total column Sulphur dioxide'

        if table2Version == 210 and indicatorOfParameter == 125:
            return 'Total column Nitrogen dioxide'

        if table2Version == 210 and indicatorOfParameter == 124:
            return 'Formaldehyde'

        if table2Version == 210 and indicatorOfParameter == 123:
            return 'Carbon monoxide'

        if table2Version == 210 and indicatorOfParameter == 122:
            return 'Sulphur dioxide'

        if table2Version == 210 and indicatorOfParameter == 121:
            return 'Nitrogen dioxide'

        if table2Version == 210 and indicatorOfParameter == 100:
            return 'Wildfire combustion rate'

        if table2Version == 210 and indicatorOfParameter == 99:
            return 'Wildfire radiative power'

        if table2Version == 210 and indicatorOfParameter == 98:
            return 'Number of positive FRP pixels per grid cell'

        if table2Version == 210 and indicatorOfParameter == 97:
            return 'Wildfire fraction of area observed'

        if table2Version == 210 and indicatorOfParameter == 96:
            return 'Wildfire Fuel Load: Carbon per unit area'

        if table2Version == 210 and indicatorOfParameter == 95:
            return 'Wildfire Combustion Completeness'

        if table2Version == 210 and indicatorOfParameter == 94:
            return 'Wildfire vegetation map index'

        if table2Version == 210 and indicatorOfParameter == 93:
            return 'Wildfire fraction of C4 plants'

        if table2Version == 210 and indicatorOfParameter == 92:
            return 'Wildfire overall flux of burnt Carbon'

        if table2Version == 210 and indicatorOfParameter == 91:
            return 'Wildfire flux of Black Carbon'

        if table2Version == 210 and indicatorOfParameter == 90:
            return 'Wildfire flux of Organic Carbon'

        if table2Version == 210 and indicatorOfParameter == 89:
            return 'Wildfire flux of Total Carbon in Aerosols'

        if table2Version == 210 and indicatorOfParameter == 88:
            return 'Wildfire flux of Total Particulate Matter'

        if table2Version == 210 and indicatorOfParameter == 87:
            return 'Wildfire flux of Particulate Matter PM2.5'

        if table2Version == 210 and indicatorOfParameter == 86:
            return 'Wildfire flux of Nitrous Oxide'

        if table2Version == 210 and indicatorOfParameter == 85:
            return 'Wildfire flux of Nitrogen Oxides NOx'

        if table2Version == 210 and indicatorOfParameter == 84:
            return 'Wildfire flux of Hydrogen'

        if table2Version == 210 and indicatorOfParameter == 83:
            return 'Wildfire flux of Non-Methane Hydro-Carbons'

        if table2Version == 210 and indicatorOfParameter == 82:
            return 'Wildfire flux of Methane'

        if table2Version == 210 and indicatorOfParameter == 81:
            return 'Wildfire flux of Carbon Monoxide'

        if table2Version == 210 and indicatorOfParameter == 80:
            return 'Wildfire flux of Carbon Dioxide'

        if table2Version == 210 and indicatorOfParameter == 71:
            return 'Methane loss rate due to radical hydroxyl (OH)'

        if table2Version == 210 and indicatorOfParameter == 70:
            return 'Methane Surface Fluxes'

        if table2Version == 210 and indicatorOfParameter == 69:
            return 'Anthropogenic emissions of Carbon Dioxide'

        if table2Version == 210 and indicatorOfParameter == 68:
            return 'Natural biosphere flux of Carbon Dioxide'

        if table2Version == 210 and indicatorOfParameter == 67:
            return 'Ocean flux of Carbon Dioxide'

        if table2Version == 210 and indicatorOfParameter == 66:
            return 'Total column Nitrous oxide'

        if table2Version == 210 and indicatorOfParameter == 65:
            return 'CH4 column-mean molar fraction'

        if table2Version == 210 and indicatorOfParameter == 64:
            return 'CO2 column-mean molar fraction'

        if table2Version == 210 and indicatorOfParameter == 63:
            return 'Nitrous oxide'

        if table2Version == 210 and indicatorOfParameter == 62:
            return 'Methane'

        if table2Version == 210 and indicatorOfParameter == 61:
            return 'Carbon Dioxide'

        if table2Version == 210 and indicatorOfParameter == 54:
            return 'Soil clay content'

        if table2Version == 210 and indicatorOfParameter == 53:
            return 'Lifting threshold speed'

        if table2Version == 210 and indicatorOfParameter == 52:
            return 'Dust emission potential'

        if table2Version == 210 and indicatorOfParameter == 51:
            return 'Aerosol large mode optical depth'

        if table2Version == 210 and indicatorOfParameter == 50:
            return 'Aerosol small mode optical depth'

        if table2Version == 210 and indicatorOfParameter == 49:
            return 'Aerosol precursor optical depth'

        if table2Version == 210 and indicatorOfParameter == 48:
            return 'Aerosol large mode mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 47:
            return 'Aerosol small mode mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 46:
            return 'Aerosol precursor mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 42:
            return 'Aerosol type 12 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 41:
            return 'Aerosol type 11 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 40:
            return 'Aerosol type 10 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 39:
            return 'Aerosol type 9 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 38:
            return 'Aerosol type 8 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 37:
            return 'Aerosol type 7 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 36:
            return 'Aerosol type 6 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 35:
            return 'Aerosol type 5 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 34:
            return 'Aerosol type 4 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 33:
            return 'Aerosol type 3 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 32:
            return 'Aerosol type 2 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 31:
            return 'Aerosol type 1 sink/loss accumulated'

        if table2Version == 210 and indicatorOfParameter == 27:
            return 'Aerosol type 12 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 26:
            return 'Aerosol type 11 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 25:
            return 'Aerosol type 10 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 24:
            return 'Aerosol type 9 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 23:
            return 'Aerosol type 8 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 22:
            return 'Aerosol type 7 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 21:
            return 'Aerosol type 6 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 20:
            return 'Aerosol type 5 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 19:
            return 'Aerosol type 4 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 18:
            return 'Aerosol type 3 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 17:
            return 'Aerosol type 2 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 16:
            return 'Aerosol type 1 source/gain accumulated'

        if table2Version == 210 and indicatorOfParameter == 12:
            return 'SO2 precursor mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 11:
            return 'Sulphate Aerosol Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 10:
            return 'Hydrophobic Black Carbon Aerosol Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 9:
            return 'Hydrophilic Black Carbon Aerosol Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 8:
            return 'Hydrophobic Organic Matter Aerosol Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 7:
            return 'Hydrophilic Organic Matter Aerosol Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 6:
            return 'Dust Aerosol (0.9 - 20 um) Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 5:
            return 'Dust Aerosol (0.55 - 0.9 um) Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 4:
            return 'Dust Aerosol (0.03 - 0.55 um) Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 3:
            return 'Sea Salt Aerosol (5 - 20 um) Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 2:
            return 'Sea Salt Aerosol (0.5 - 5 um) Mixing Ratio'

        if table2Version == 210 and indicatorOfParameter == 1:
            return 'Sea Salt Aerosol (0.03 - 0.5 um) Mixing Ratio'

        if table2Version == 201 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 201 and indicatorOfParameter == 241:
            return 'convective available potential energy'

        if table2Version == 201 and indicatorOfParameter == 215:
            return 'ice surface temperature'

        if table2Version == 201 and indicatorOfParameter == 203:
            return 'snow temperature'

        if table2Version == 201 and indicatorOfParameter == 200:
            return 'water content of interception store'

        if table2Version == 201 and indicatorOfParameter == 187:
            return 'Maximum wind velocity'

        if table2Version == 201 and indicatorOfParameter == 150:
            return 'coefficient of horizontal diffusion'

        if table2Version == 201 and indicatorOfParameter == 139:
            return 'deviation of pressure from reference value'

        if table2Version == 201 and indicatorOfParameter == 113:
            return 'surface precipitation amount, rain, convective'

        if table2Version == 201 and indicatorOfParameter == 112:
            return 'surface precipitation rate, snow, convective'

        if table2Version == 201 and indicatorOfParameter == 111:
            return 'surface precipitation rate, rain, convective'

        if table2Version == 201 and indicatorOfParameter == 102:
            return 'surface precipitation amount, rain, grid scale'

        if table2Version == 201 and indicatorOfParameter == 101:
            return 'surface precipitation rate, snow, grid scale'

        if table2Version == 201 and indicatorOfParameter == 100:
            return 'surface precipitation rate, rain, grid scale'

        if table2Version == 201 and indicatorOfParameter == 99:
            return 'spec. content of precip. particles'

        if table2Version == 201 and indicatorOfParameter == 85:
            return 'height of snow-fall limit'

        if table2Version == 201 and indicatorOfParameter == 84:
            return 'height of 0 degree Celsius isotherm above msl'

        if table2Version == 201 and indicatorOfParameter == 83:
            return 'dry convection top index'

        if table2Version == 201 and indicatorOfParameter == 82:
            return 'top of dry convection (above msl)'

        if table2Version == 201 and indicatorOfParameter == 81:
            return 'convective divergence tendency'

        if table2Version == 201 and indicatorOfParameter == 80:
            return 'convective vorticity tendency'

        if table2Version == 201 and indicatorOfParameter == 79:
            return 'convective momentum tendency (Y-component)'

        if table2Version == 201 and indicatorOfParameter == 78:
            return 'convective momentum tendency (X-component)'

        if table2Version == 201 and indicatorOfParameter == 77:
            return 'convective tendency of total water'

        if table2Version == 201 and indicatorOfParameter == 76:
            return 'convective tendency of total heat'

        if table2Version == 201 and indicatorOfParameter == 75:
            return 'convective tendency of specific humidity'

        if table2Version == 201 and indicatorOfParameter == 74:
            return 'convective temperature tendency'

        if table2Version == 201 and indicatorOfParameter == 73:
            return 'convection top index'

        if table2Version == 201 and indicatorOfParameter == 72:
            return 'convection base index'

        if table2Version == 201 and indicatorOfParameter == 71:
            return 'KO-index'

        if table2Version == 201 and indicatorOfParameter == 70:
            return 'convective layers (00...77)  (BKE)'

        if table2Version == 201 and indicatorOfParameter == 69:
            return 'cloud top, convective clouds (above msl)'

        if table2Version == 201 and indicatorOfParameter == 68:
            return 'cloud base, convective clouds (above msl)'

        if table2Version == 201 and indicatorOfParameter == 67:
            return 'entrainment parameter, convection'

        if table2Version == 201 and indicatorOfParameter == 66:
            return 'Updraft velocity, convection'

        if table2Version == 201 and indicatorOfParameter == 65:
            return 'convective mass flux'

        if table2Version == 201 and indicatorOfParameter == 64:
            return 'cloud ice content, conv clouds, vert integrated'

        if table2Version == 201 and indicatorOfParameter == 63:
            return 'specific cloud ice content, convective clouds'

        if table2Version == 201 and indicatorOfParameter == 62:
            return 'cloud water content, conv clouds, vert integrated'

        if table2Version == 201 and indicatorOfParameter == 61:
            return 'specific cloud water content, convective clouds'

        if table2Version == 201 and indicatorOfParameter == 60:
            return 'cloud cover, convective cirrus'

        if table2Version == 201 and indicatorOfParameter == 56:
            return 'fog'

        if table2Version == 201 and indicatorOfParameter == 55:
            return 'fog (0..8)'

        if table2Version == 201 and indicatorOfParameter == 54:
            return 'total cloud cover (0..8)'

        if table2Version == 201 and indicatorOfParameter == 53:
            return 'cloud cover CL (0..8)'

        if table2Version == 201 and indicatorOfParameter == 52:
            return 'cloud cover CM (0..8)'

        if table2Version == 201 and indicatorOfParameter == 51:
            return 'cloud cover CH (0..8)'

        if table2Version == 201 and indicatorOfParameter == 50:
            return 'cloud covers CH_CM_CL (000...888)'

        if table2Version == 201 and indicatorOfParameter == 42:
            return 'vert. integral of divergence of tot. water content'

        if table2Version == 201 and indicatorOfParameter == 41:
            return 'total column water'

        if table2Version == 201 and indicatorOfParameter == 38:
            return 'specific snow content, gs, vert. integrated'

        if table2Version == 201 and indicatorOfParameter == 37:
            return 'specific rainwater content, gs, vert. integrated'

        if table2Version == 201 and indicatorOfParameter == 36:
            return 'specific snow content, grid scale'

        if table2Version == 201 and indicatorOfParameter == 35:
            return 'specific rainwater content, grid scale'

        if table2Version == 201 and indicatorOfParameter == 34:
            return 'cloud ice content, grid scale, vert integrated'

        if table2Version == 201 and indicatorOfParameter == 33:
            return 'specific cloud ice content, grid scale'

        if table2Version == 201 and indicatorOfParameter == 32:
            return 'cloud water content, grid scale, vert integrated'

        if table2Version == 201 and indicatorOfParameter == 31:
            return 'specific cloud water content'

        if table2Version == 201 and indicatorOfParameter == 30:
            return 'cloud cover, grid scale'

        if table2Version == 201 and indicatorOfParameter == 29:
            return 'fractional cloud cover'

        if table2Version == 201 and indicatorOfParameter == 17:
            return 'soil heat flux, bottom of layer'

        if table2Version == 201 and indicatorOfParameter == 16:
            return 'soil heat flux, surface'

        if table2Version == 201 and indicatorOfParameter == 15:
            return 'total radiative heating rate'

        if table2Version == 201 and indicatorOfParameter == 14:
            return 'longwave radiative heating rate'

        if table2Version == 201 and indicatorOfParameter == 13:
            return 'shortwave radiative heating rate'

        if table2Version == 201 and indicatorOfParameter == 12:
            return 'upw longw radiant flux density, cloudy part'

        if table2Version == 201 and indicatorOfParameter == 11:
            return 'downw longw radiant flux density, cloudfree part'

        if table2Version == 201 and indicatorOfParameter == 10:
            return 'upw shortw radiant flux density, cloudy part'

        if table2Version == 201 and indicatorOfParameter == 9:
            return 'downw shortw radiant flux density, cloudfree part'

        if table2Version == 201 and indicatorOfParameter == 8:
            return 'total net radiative flux density'

        if table2Version == 201 and indicatorOfParameter == 7:
            return 'net longwave flux'

        if table2Version == 201 and indicatorOfParameter == 6:
            return 'net shortwave flux'

        if table2Version == 201 and indicatorOfParameter == 5:
            return 'downwd photosynthetic active radiant flux density'

        if table2Version == 201 and indicatorOfParameter == 4:
            return 'upward longwave radiant flux density'

        if table2Version == 201 and indicatorOfParameter == 3:
            return 'downward longwave radiant flux density'

        if table2Version == 201 and indicatorOfParameter == 2:
            return 'upward shortwave radiant flux density'

        if table2Version == 201 and indicatorOfParameter == 1:
            return 'downward shortwave radiant flux density'

        if table2Version == 200 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature difference'

        if table2Version == 190 and indicatorOfParameter == 229:
            return 'Total soil moisture'

        if table2Version == 190 and indicatorOfParameter == 173:
            return 'Roughness length'

        if table2Version == 190 and indicatorOfParameter == 171:
            return 'Wilting point'

        if table2Version == 190 and indicatorOfParameter == 170:
            return 'Field capacity'

        if table2Version == 190 and indicatorOfParameter == 141:
            return 'Snow depth'

        if table2Version == 180 and indicatorOfParameter == 179:
            return 'Top net thermal radiation'

        if table2Version == 180 and indicatorOfParameter == 178:
            return 'Top net solar radiation'

        if table2Version == 180 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation'

        if table2Version == 180 and indicatorOfParameter == 176:
            return 'Surface net solar radiation'

        if table2Version == 180 and indicatorOfParameter == 149:
            return 'Total soil wetness'

        if table2Version == 175 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 175 and indicatorOfParameter == 236:
            return 'Soil temperature layer 4'

        if table2Version == 175 and indicatorOfParameter == 202:
            return '1.5m temperature - minimum in the last 24 hours'

        if table2Version == 175 and indicatorOfParameter == 201:
            return '1.5m temperature - maximum in the last 24 hours'

        if table2Version == 175 and indicatorOfParameter == 183:
            return 'Soil temperature layer 3'

        if table2Version == 175 and indicatorOfParameter == 175:
            return 'Average salinity in upper 293.4m'

        if table2Version == 175 and indicatorOfParameter == 170:
            return 'Soil temperature layer 2'

        if table2Version == 175 and indicatorOfParameter == 168:
            return '1.5m dewpoint temperature'

        if table2Version == 175 and indicatorOfParameter == 167:
            return '1.5m temperature'

        if table2Version == 175 and indicatorOfParameter == 164:
            return 'Average potential temperature in upper 293.4m'

        if table2Version == 175 and indicatorOfParameter == 139:
            return 'Soil temperature layer 1'

        if table2Version == 175 and indicatorOfParameter == 111:
            return 'Ocean mean ice depth'

        if table2Version == 175 and indicatorOfParameter == 110:
            return 'Ocean ice concentration'

        if table2Version == 175 and indicatorOfParameter == 90:
            return 'Top outgoing solar radiation'

        if table2Version == 175 and indicatorOfParameter == 89:
            return 'Top incoming solar radiation'

        if table2Version == 175 and indicatorOfParameter == 88:
            return '1.5m dewpoint temperature over land'

        if table2Version == 175 and indicatorOfParameter == 87:
            return '1.5m temperature over land'

        if table2Version == 175 and indicatorOfParameter == 86:
            return '10m V wind over land'

        if table2Version == 175 and indicatorOfParameter == 85:
            return '10m U wind over land'

        if table2Version == 175 and indicatorOfParameter == 83:
            return 'Net primary productivity'

        if table2Version == 175 and indicatorOfParameter == 55:
            return '1.5m temperature - mean in the last 24 hours'

        if table2Version == 175 and indicatorOfParameter == 49:
            return '10m wind gust in the last 24 hours'

        if table2Version == 175 and indicatorOfParameter == 42:
            return 'Volumetric soil water layer 4'

        if table2Version == 175 and indicatorOfParameter == 41:
            return 'Volumetric soil water layer 3'

        if table2Version == 175 and indicatorOfParameter == 40:
            return 'Volumetric soil water layer 2'

        if table2Version == 175 and indicatorOfParameter == 39:
            return 'Volumetric soil water layer 1'

        if table2Version == 175 and indicatorOfParameter == 34:
            return 'Open-sea surface temperature'

        if table2Version == 175 and indicatorOfParameter == 31:
            return 'Fraction of sea-ice in sea'

        if table2Version == 175 and indicatorOfParameter == 6:
            return 'Total soil moisture'

        if table2Version == 174 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 174 and indicatorOfParameter == 236:
            return 'Soil temperature layer 4'

        if table2Version == 174 and indicatorOfParameter == 202:
            return '1.5m temperature - minimum in the last 24 hours'

        if table2Version == 174 and indicatorOfParameter == 201:
            return '1.5m temperature - maximum in the last 24 hours'

        if table2Version == 174 and indicatorOfParameter == 183:
            return 'Soil temperature layer 3'

        if table2Version == 174 and indicatorOfParameter == 175:
            return 'Average salinity in upper 293.4m'

        if table2Version == 174 and indicatorOfParameter == 170:
            return 'Soil temperature layer 2'

        if table2Version == 174 and indicatorOfParameter == 168:
            return '1.5m dewpoint temperature'

        if table2Version == 174 and indicatorOfParameter == 167:
            return '1.5m temperature'

        if table2Version == 174 and indicatorOfParameter == 164:
            return 'Average potential temperature in upper 293.4m'

        if table2Version == 174 and indicatorOfParameter == 139:
            return 'Soil temperature layer 1'

        if table2Version == 174 and indicatorOfParameter == 111:
            return 'Ocean mean ice depth'

        if table2Version == 174 and indicatorOfParameter == 110:
            return 'Ocean ice concentration'

        if table2Version == 174 and indicatorOfParameter == 99:
            return 'Liquid water potential temperature'

        if table2Version == 174 and indicatorOfParameter == 98:
            return 'Sea-ice thickness'

        if table2Version == 174 and indicatorOfParameter == 95:
            return '1.5m specific humidity'

        if table2Version == 174 and indicatorOfParameter == 94:
            return 'Mean sea surface temperature'

        if table2Version == 174 and indicatorOfParameter == 90:
            return 'Top outgoing solar radiation'

        if table2Version == 174 and indicatorOfParameter == 89:
            return 'Top incoming solar radiation'

        if table2Version == 174 and indicatorOfParameter == 88:
            return '1.5m dewpoint temperature over land'

        if table2Version == 174 and indicatorOfParameter == 87:
            return '1.5m temperature over land'

        if table2Version == 174 and indicatorOfParameter == 86:
            return '10m V wind over land'

        if table2Version == 174 and indicatorOfParameter == 85:
            return '10m U wind over land'

        if table2Version == 174 and indicatorOfParameter == 83:
            return 'Net primary productivity'

        if table2Version == 174 and indicatorOfParameter == 55:
            return '1.5m temperature - mean in the last 24 hours'

        if table2Version == 174 and indicatorOfParameter == 49:
            return '10 metre wind gust in the last 24 hours'

        if table2Version == 174 and indicatorOfParameter == 42:
            return 'Volumetric soil water layer 4'

        if table2Version == 174 and indicatorOfParameter == 41:
            return 'Volumetric soil water layer 3'

        if table2Version == 174 and indicatorOfParameter == 40:
            return 'Volumetric soil water layer 2'

        if table2Version == 174 and indicatorOfParameter == 39:
            return 'Volumetric soil water layer 1'

        if table2Version == 174 and indicatorOfParameter == 34:
            return 'Open-sea surface temperature'

        if table2Version == 174 and indicatorOfParameter == 31:
            return 'Fraction of sea-ice in sea'

        if table2Version == 174 and indicatorOfParameter == 9:
            return 'Sub-surface runoff'

        if table2Version == 174 and indicatorOfParameter == 8:
            return 'Surface runoff'

        if table2Version == 174 and indicatorOfParameter == 6:
            return 'Total soil moisture'

        if table2Version == 173 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 173 and indicatorOfParameter == 240:
            return 'Large scale snowfall anomaly'

        if table2Version == 173 and indicatorOfParameter == 239:
            return 'Convective snowfall anomaly'

        if table2Version == 173 and indicatorOfParameter == 228:
            return 'Total precipitation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 212:
            return 'Solar insolation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky anomaly'

        if table2Version == 173 and indicatorOfParameter == 210:
            return 'Surface net solar radiation, clear sky anomaly'

        if table2Version == 173 and indicatorOfParameter == 209:
            return 'Top net thermal radiation, clear sky anomaly'

        if table2Version == 173 and indicatorOfParameter == 208:
            return 'Top net solar radiation, clear sky anomaly'

        if table2Version == 173 and indicatorOfParameter == 205:
            return 'Runoff anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation anomaly'

        if table2Version == 173 and indicatorOfParameter == 196:
            return 'Meridional component of gravity wave stress anomaly'

        if table2Version == 173 and indicatorOfParameter == 195:
            return 'Longitudinal component of gravity wave stress anomaly'

        if table2Version == 173 and indicatorOfParameter == 189:
            return 'Sunshine duration anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 182:
            return 'Evaporation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 181:
            return 'North-South surface stress anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 180:
            return 'East-West surface stress anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 179:
            return 'Top thermal radiation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 178:
            return 'Top solar radiation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 177:
            return 'Surface thermal radiation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 176:
            return 'Surface solar radiation anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 154:
            return 'Long-wave heating rate anomaly'

        if table2Version == 173 and indicatorOfParameter == 153:
            return 'Short-wave heating rate anomaly'

        if table2Version == 173 and indicatorOfParameter == 149:
            return 'Surface net radiation anomaly'

        if table2Version == 173 and indicatorOfParameter == 147:
            return 'Surface latent heat flux anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation anomaly'

        if table2Version == 173 and indicatorOfParameter == 144:
            return 'Snowfall (convective + stratiform) anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 143:
            return 'Mean convective precipitation rate anomaly'

        if table2Version == 173 and indicatorOfParameter == 142:
            return 'Stratiform precipitation (Large-scale precipitation) anomalous rate of accumulation'

        if table2Version == 173 and indicatorOfParameter == 50:
            return 'Large-scale precipitation fraction anomaly'

        if table2Version == 173 and indicatorOfParameter == 48:
            return 'Magnitude of turbulent surface stress anomaly'

        if table2Version == 173 and indicatorOfParameter == 45:
            return 'Snowmelt anomaly'

        if table2Version == 173 and indicatorOfParameter == 44:
            return 'Snow evaporation anomaly'

        if table2Version == 172 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 172 and indicatorOfParameter == 240:
            return 'Large scale snowfall'

        if table2Version == 172 and indicatorOfParameter == 239:
            return 'Convective snowfall'

        if table2Version == 172 and indicatorOfParameter == 228:
            return 'Mean total precipitation rate'

        if table2Version == 172 and indicatorOfParameter == 212:
            return 'Solar insolation rate of accumulation'

        if table2Version == 172 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky'

        if table2Version == 172 and indicatorOfParameter == 210:
            return 'Surface net solar radiation, clear sky'

        if table2Version == 172 and indicatorOfParameter == 209:
            return 'Top net thermal radiation, clear sky'

        if table2Version == 172 and indicatorOfParameter == 208:
            return 'Top net solar radiation, clear sky'

        if table2Version == 172 and indicatorOfParameter == 205:
            return 'Mean runoff rate'

        if table2Version == 172 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation'

        if table2Version == 172 and indicatorOfParameter == 196:
            return 'Meridional component of gravity wave stress'

        if table2Version == 172 and indicatorOfParameter == 195:
            return 'Longitudinal component of gravity wave stress'

        if table2Version == 172 and indicatorOfParameter == 189:
            return 'Mean sunshine duration rate'

        if table2Version == 172 and indicatorOfParameter == 182:
            return 'Evaporation'

        if table2Version == 172 and indicatorOfParameter == 181:
            return 'North-South surface stress rate of accumulation'

        if table2Version == 172 and indicatorOfParameter == 180:
            return 'East-West surface stress rate of accumulation'

        if table2Version == 172 and indicatorOfParameter == 179:
            return 'Mean top net thermal radiation flux'

        if table2Version == 172 and indicatorOfParameter == 178:
            return 'Mean top net solar radiation flux'

        if table2Version == 172 and indicatorOfParameter == 177:
            return 'Mean surface net thermal radiation flux'

        if table2Version == 172 and indicatorOfParameter == 176:
            return 'Mean surface net solar radiation flux'

        if table2Version == 172 and indicatorOfParameter == 175:
            return 'Mean surface downward thermal radiation flux'

        if table2Version == 172 and indicatorOfParameter == 169:
            return 'Mean surface downward solar radiation flux'

        if table2Version == 172 and indicatorOfParameter == 154:
            return 'Mean long-wave heating rate'

        if table2Version == 172 and indicatorOfParameter == 153:
            return 'Mean short-wave heating rate'

        if table2Version == 172 and indicatorOfParameter == 149:
            return 'Mean surface net radiation flux'

        if table2Version == 172 and indicatorOfParameter == 147:
            return 'Mean surface latent heat flux'

        if table2Version == 172 and indicatorOfParameter == 146:
            return 'Mean surface sensible heat flux'

        if table2Version == 172 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation'

        if table2Version == 172 and indicatorOfParameter == 144:
            return 'Mean total snowfall rate'

        if table2Version == 172 and indicatorOfParameter == 143:
            return 'Mean convective precipitation rate'

        if table2Version == 172 and indicatorOfParameter == 142:
            return 'Mean large-scale precipitation rate'

        if table2Version == 172 and indicatorOfParameter == 50:
            return 'Mean large-scale precipitation fraction'

        if table2Version == 172 and indicatorOfParameter == 48:
            return 'Magnitude of turbulent surface stress'

        if table2Version == 172 and indicatorOfParameter == 45:
            return 'Snowmelt'

        if table2Version == 172 and indicatorOfParameter == 44:
            return 'Snow evaporation'

        if table2Version == 171 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 171 and indicatorOfParameter == 254:
            return 'Adiabatic tendency of meridional wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 253:
            return 'Adiabatic tendency of zonal wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 252:
            return 'Adiabatic tendency of humidity anomaly'

        if table2Version == 171 and indicatorOfParameter == 251:
            return 'Adiabatic tendency of temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 250:
            return 'Ice age anomaly'

        if table2Version == 171 and indicatorOfParameter == 249:
            return 'Accumulated ice water tendency anomaly'

        if table2Version == 171 and indicatorOfParameter == 248:
            return 'Cloud cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 247:
            return 'Cloud ice water content anomaly'

        if table2Version == 171 and indicatorOfParameter == 246:
            return 'Cloud liquid water content anomaly'

        if table2Version == 171 and indicatorOfParameter == 245:
            return 'Forecast logarithm of surface roughness for heat anomaly'

        if table2Version == 171 and indicatorOfParameter == 244:
            return 'Forecast surface roughness anomaly'

        if table2Version == 171 and indicatorOfParameter == 243:
            return 'Forecast albedo anomaly'

        if table2Version == 171 and indicatorOfParameter == 242:
            return 'Accumulated liquid water tendency anomaly'

        if table2Version == 171 and indicatorOfParameter == 241:
            return 'Accumulated cloud fraction tendency anomaly'

        if table2Version == 171 and indicatorOfParameter == 240:
            return 'Large scale snowfall anomaly'

        if table2Version == 171 and indicatorOfParameter == 239:
            return 'Convective snowfall anomaly'

        if table2Version == 171 and indicatorOfParameter == 238:
            return 'Temperature of snow layer anomaly'

        if table2Version == 171 and indicatorOfParameter == 237:
            return 'Soil wetness level 4 anomaly'

        if table2Version == 171 and indicatorOfParameter == 236:
            return 'Soil temperature level 4 anomaly'

        if table2Version == 171 and indicatorOfParameter == 235:
            return 'Skin temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 234:
            return 'Logarithm of surface roughness length for heat anomaly'

        if table2Version == 171 and indicatorOfParameter == 233:
            return 'Apparent surface humidity anomaly'

        if table2Version == 171 and indicatorOfParameter == 232:
            return 'Instantaneous moisture flux anomaly'

        if table2Version == 171 and indicatorOfParameter == 231:
            return 'Instantaneous surface heat flux anomaly'

        if table2Version == 171 and indicatorOfParameter == 230:
            return 'Instantaneous Y surface stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 229:
            return 'Instantaneous X surface stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 228:
            return 'Total precipitation anomaly'

        if table2Version == 171 and indicatorOfParameter == 227:
            return 'Change from removal of negative humidity anomaly'

        if table2Version == 171 and indicatorOfParameter == 226:
            return 'Humidity tendency by large-scale condensation anomaly'

        if table2Version == 171 and indicatorOfParameter == 225:
            return 'Humidity tendency by cumulus convection anomaly'

        if table2Version == 171 and indicatorOfParameter == 224:
            return 'Vertical diffusion of humidity anomaly'

        if table2Version == 171 and indicatorOfParameter == 223:
            return 'Convective tendency of meridional wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 222:
            return 'Convective tendency of zonal wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 221:
            return 'North-South gravity wave drag tendency anomaly'

        if table2Version == 171 and indicatorOfParameter == 220:
            return 'East-West gravity wave drag tendency anomaly'

        if table2Version == 171 and indicatorOfParameter == 219:
            return 'Vertical diffusion of meridional wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 218:
            return 'Vertical diffusion of zonal wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 217:
            return 'Diabatic heating by large-scale condensation anomaly'

        if table2Version == 171 and indicatorOfParameter == 216:
            return 'Diabatic heating by cumulus convection anomaly'

        if table2Version == 171 and indicatorOfParameter == 215:
            return 'Diabatic heating by vertical diffusion anomaly'

        if table2Version == 171 and indicatorOfParameter == 214:
            return 'Diabatic heating by radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 212:
            return 'Solar insolation anomaly'

        if table2Version == 171 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky anomaly'

        if table2Version == 171 and indicatorOfParameter == 210:
            return 'Surface net solar radiation clear sky anomaly'

        if table2Version == 171 and indicatorOfParameter == 209:
            return 'Top net thermal radiation clear sky anomaly'

        if table2Version == 171 and indicatorOfParameter == 208:
            return 'Top net solar radiation clear sky anomaly'

        if table2Version == 171 and indicatorOfParameter == 207:
            return '10 metre wind speed anomaly'

        if table2Version == 171 and indicatorOfParameter == 206:
            return 'Total column ozone anomaly'

        if table2Version == 171 and indicatorOfParameter == 205:
            return 'Runoff anomaly'

        if table2Version == 171 and indicatorOfParameter == 204:
            return 'Precipitation analysis weights anomaly'

        if table2Version == 171 and indicatorOfParameter == 203:
            return 'Ozone mass mixing ratio anomaly'

        if table2Version == 171 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres anomaly'

        if table2Version == 171 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres anomaly'

        if table2Version == 171 and indicatorOfParameter == 200:
            return 'Variance of sub-gridscale orography anomaly'

        if table2Version == 171 and indicatorOfParameter == 199:
            return 'Vegetation fraction anomaly'

        if table2Version == 171 and indicatorOfParameter == 198:
            return 'Skin reservoir content anomaly'

        if table2Version == 171 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation anomaly'

        if table2Version == 171 and indicatorOfParameter == 196:
            return 'Meridional component of gravity wave stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 195:
            return 'Longitudinal component of gravity wave stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 194:
            return 'Brightness temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance anomaly'

        if table2Version == 171 and indicatorOfParameter == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance anomaly'

        if table2Version == 171 and indicatorOfParameter == 191:
            return 'North-South component of sub-gridscale orographic variance anomaly'

        if table2Version == 171 and indicatorOfParameter == 190:
            return 'East-West component of sub-gridscale orographic variance anomaly'

        if table2Version == 171 and indicatorOfParameter == 189:
            return 'Sunshine duration anomaly'

        if table2Version == 171 and indicatorOfParameter == 188:
            return 'High cloud cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 187:
            return 'Medium cloud cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 186:
            return 'Low cloud cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 185:
            return 'Convective cloud cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 184:
            return 'Soil wetness anomaly level 3'

        if table2Version == 171 and indicatorOfParameter == 183:
            return 'Soil temperature anomaly level 3'

        if table2Version == 171 and indicatorOfParameter == 182:
            return 'Evaporation anomaly'

        if table2Version == 171 and indicatorOfParameter == 181:
            return 'North-South surface stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 180:
            return 'East-West surface stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 179:
            return 'Top net thermal radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 178:
            return 'Top net solar radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 176:
            return 'Surface net solar radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards anomaly'

        if table2Version == 171 and indicatorOfParameter == 174:
            return 'Albedo anomaly'

        if table2Version == 171 and indicatorOfParameter == 173:
            return 'Surface roughness anomaly'

        if table2Version == 171 and indicatorOfParameter == 171:
            return 'Soil wetness anomaly level 2'

        if table2Version == 171 and indicatorOfParameter == 170:
            return 'Soil temperature anomaly level 2'

        if table2Version == 171 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards anomaly'

        if table2Version == 171 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 167:
            return '2 metre temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 166:
            return '10 metre V wind component anomaly'

        if table2Version == 171 and indicatorOfParameter == 165:
            return '10 metre U wind component anomaly'

        if table2Version == 171 and indicatorOfParameter == 164:
            return 'Total cloud cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 163:
            return 'Slope of sub-gridscale orography anomaly'

        if table2Version == 171 and indicatorOfParameter == 162:
            return 'Angle of sub-gridscale orography anomaly'

        if table2Version == 171 and indicatorOfParameter == 161:
            return 'Anisotropy of sub-gridscale orography anomaly'

        if table2Version == 171 and indicatorOfParameter == 160:
            return 'Standard deviation of orography anomaly'

        if table2Version == 171 and indicatorOfParameter == 159:
            return 'Boundary layer height anomaly'

        if table2Version == 171 and indicatorOfParameter == 158:
            return 'Tendency of surface pressure anomaly'

        if table2Version == 171 and indicatorOfParameter == 157:
            return 'Relative humidity anomaly'

        if table2Version == 171 and indicatorOfParameter == 156:
            return 'Height anomaly'

        if table2Version == 171 and indicatorOfParameter == 155:
            return 'Relative divergence anomaly'

        if table2Version == 171 and indicatorOfParameter == 154:
            return 'Long-wave heating rate anomaly'

        if table2Version == 171 and indicatorOfParameter == 153:
            return 'Short-wave heating rate anomaly'

        if table2Version == 171 and indicatorOfParameter == 152:
            return 'Logarithm of surface pressure anomaly'

        if table2Version == 171 and indicatorOfParameter == 151:
            return 'Mean sea level pressure anomaly'

        if table2Version == 171 and indicatorOfParameter == 150:
            return 'Top net radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 149:
            return 'Surface net radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 148:
            return 'Charnock anomaly'

        if table2Version == 171 and indicatorOfParameter == 147:
            return 'Surface latent heat flux anomaly'

        if table2Version == 171 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux anomaly'

        if table2Version == 171 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation anomaly'

        if table2Version == 171 and indicatorOfParameter == 144:
            return 'Snowfall (convective + stratiform) anomaly'

        if table2Version == 171 and indicatorOfParameter == 143:
            return 'Convective precipitation anomaly'

        if table2Version == 171 and indicatorOfParameter == 142:
            return 'Stratiform precipitation (Large-scale precipitation) anomaly'

        if table2Version == 171 and indicatorOfParameter == 141:
            return 'Snow depth anomaly'

        if table2Version == 171 and indicatorOfParameter == 140:
            return 'Soil wetness anomaly level 1'

        if table2Version == 171 and indicatorOfParameter == 139:
            return 'Soil temperature anomaly level 1'

        if table2Version == 171 and indicatorOfParameter == 138:
            return 'Relative vorticity anomaly'

        if table2Version == 171 and indicatorOfParameter == 137:
            return 'Total column water vapour anomaly'

        if table2Version == 171 and indicatorOfParameter == 136:
            return 'Total column water anomaly'

        if table2Version == 171 and indicatorOfParameter == 135:
            return 'Vertical velocity (pressure) anomaly'

        if table2Version == 171 and indicatorOfParameter == 134:
            return 'Surface pressure anomaly'

        if table2Version == 171 and indicatorOfParameter == 133:
            return 'Specific humidity anomaly'

        if table2Version == 171 and indicatorOfParameter == 132:
            return 'V component of wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 131:
            return 'U component of wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 130:
            return 'Temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 129:
            return 'Geopotential anomaly'

        if table2Version == 171 and indicatorOfParameter == 128:
            return 'Budget values anomaly'

        if table2Version == 171 and indicatorOfParameter == 127:
            return 'Atmospheric tide anomaly'

        if table2Version == 171 and indicatorOfParameter == 126:
            return 'Generic parameter for sensitive area prediction'

        if table2Version == 171 and indicatorOfParameter == 125:
            return 'Vertically integrated total energy anomaly'

        if table2Version == 171 and indicatorOfParameter == 79:
            return 'Total column ice water anomaly'

        if table2Version == 171 and indicatorOfParameter == 78:
            return 'Total column liquid water anomaly'

        if table2Version == 171 and indicatorOfParameter == 65:
            return 'Skin temperature difference anomaly'

        if table2Version == 171 and indicatorOfParameter == 64:
            return 'Finish time for skin temperature difference anomaly'

        if table2Version == 171 and indicatorOfParameter == 63:
            return 'Start time for skin temperature difference anomaly'

        if table2Version == 171 and indicatorOfParameter == 62:
            return 'Observation count anomaly'

        if table2Version == 171 and indicatorOfParameter == 61:
            return 'Total precipitation from observations anomaly'

        if table2Version == 171 and indicatorOfParameter == 60:
            return 'Potential vorticity anomaly'

        if table2Version == 171 and indicatorOfParameter == 59:
            return 'Convective available potential energy anomaly'

        if table2Version == 171 and indicatorOfParameter == 58:
            return 'Photosynthetically active radiation at the surface anomaly'

        if table2Version == 171 and indicatorOfParameter == 57:
            return 'Downward UV radiation at the surface anomaly'

        if table2Version == 171 and indicatorOfParameter == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours anomaly'

        if table2Version == 171 and indicatorOfParameter == 55:
            return 'Mean 2 metre temperature in the last 24 hours anomaly'

        if table2Version == 171 and indicatorOfParameter == 54:
            return 'Pressure anomaly'

        if table2Version == 171 and indicatorOfParameter == 53:
            return 'Montgomery potential anomaly'

        if table2Version == 171 and indicatorOfParameter == 52:
            return 'Minimum 2 metre temperature in the last 24 hours anomaly'

        if table2Version == 171 and indicatorOfParameter == 51:
            return 'Maximum 2 metre temperature in the last 24 hours anomaly'

        if table2Version == 171 and indicatorOfParameter == 50:
            return 'Large-scale precipitation fraction anomaly'

        if table2Version == 171 and indicatorOfParameter == 49:
            return '10 metre wind gust anomaly'

        if table2Version == 171 and indicatorOfParameter == 48:
            return 'Magnitude of turbulent surface stress anomaly'

        if table2Version == 171 and indicatorOfParameter == 47:
            return 'Direct solar radiation anomaly'

        if table2Version == 171 and indicatorOfParameter == 46:
            return 'Solar duration anomaly'

        if table2Version == 171 and indicatorOfParameter == 45:
            return 'Snowmelt anomaly'

        if table2Version == 171 and indicatorOfParameter == 44:
            return 'Snow evaporation anomaly'

        if table2Version == 171 and indicatorOfParameter == 43:
            return 'Soil type anomaly'

        if table2Version == 171 and indicatorOfParameter == 42:
            return 'Volumetric soil water anomaly layer 4'

        if table2Version == 171 and indicatorOfParameter == 41:
            return 'Volumetric soil water anomaly layer 3'

        if table2Version == 171 and indicatorOfParameter == 40:
            return 'Volumetric soil water anomaly layer 2'

        if table2Version == 171 and indicatorOfParameter == 39:
            return 'Volumetric soil water anomaly layer 1'

        if table2Version == 171 and indicatorOfParameter == 38:
            return 'Ice surface temperature anomaly layer 4'

        if table2Version == 171 and indicatorOfParameter == 37:
            return 'Ice surface temperature anomaly layer 3'

        if table2Version == 171 and indicatorOfParameter == 36:
            return 'Ice surface temperature anomaly layer 2'

        if table2Version == 171 and indicatorOfParameter == 35:
            return 'Ice surface temperature anomaly layer 1'

        if table2Version == 171 and indicatorOfParameter == 34:
            return 'Sea surface temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 33:
            return 'Snow density anomaly'

        if table2Version == 171 and indicatorOfParameter == 32:
            return 'Snow albedo anomaly'

        if table2Version == 171 and indicatorOfParameter == 31:
            return 'Sea-ice cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 30:
            return 'Type of high vegetation anomaly'

        if table2Version == 171 and indicatorOfParameter == 29:
            return 'Type of low vegetation anomaly'

        if table2Version == 171 and indicatorOfParameter == 28:
            return 'High vegetation cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 27:
            return 'Low vegetation cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 26:
            return 'Lake cover anomaly'

        if table2Version == 171 and indicatorOfParameter == 23:
            return 'Unbalanced component of divergence anomaly'

        if table2Version == 171 and indicatorOfParameter == 22:
            return 'Unbalanced component of logarithm of surface pressure anomaly'

        if table2Version == 171 and indicatorOfParameter == 21:
            return 'Unbalanced component of temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 14:
            return 'V component of rotational wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 13:
            return 'U component of rotational wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 12:
            return 'V component of divergent wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 11:
            return 'U component of divergent wind anomaly'

        if table2Version == 171 and indicatorOfParameter == 5:
            return 'Saturated equivalent potential temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 4:
            return 'Equivalent potential temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 3:
            return 'Potential temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 2:
            return 'Velocity potential anomaly'

        if table2Version == 171 and indicatorOfParameter == 1:
            return 'Stream function anomaly'

        if table2Version == 170 and indicatorOfParameter == 179:
            return 'Top net thermal radiation'

        if table2Version == 170 and indicatorOfParameter == 171:
            return 'Soil wetness level 2'

        if table2Version == 170 and indicatorOfParameter == 149:
            return 'Total soil moisture'

        if table2Version == 162 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 162 and indicatorOfParameter == 233:
            return 'Variance of ozone'

        if table2Version == 162 and indicatorOfParameter == 232:
            return 'Covariance of omega/ozone'

        if table2Version == 162 and indicatorOfParameter == 231:
            return 'Covariance of v component/ozone'

        if table2Version == 162 and indicatorOfParameter == 230:
            return 'Covariance of u component/ozone'

        if table2Version == 162 and indicatorOfParameter == 229:
            return 'Variance of relative humidity'

        if table2Version == 162 and indicatorOfParameter == 227:
            return 'Variance of surface pressure'

        if table2Version == 162 and indicatorOfParameter == 226:
            return 'Variance of omega'

        if table2Version == 162 and indicatorOfParameter == 225:
            return 'Covariance of omega/v component'

        if table2Version == 162 and indicatorOfParameter == 224:
            return 'Covariance of omega/u component'

        if table2Version == 162 and indicatorOfParameter == 223:
            return 'Covariance of omega/specific humidity'

        if table2Version == 162 and indicatorOfParameter == 222:
            return 'Covariance of omega/temperature'

        if table2Version == 162 and indicatorOfParameter == 221:
            return 'Covariance of omega/geopotential'

        if table2Version == 162 and indicatorOfParameter == 220:
            return 'Variance of v component'

        if table2Version == 162 and indicatorOfParameter == 219:
            return 'Covariance of v component/u component'

        if table2Version == 162 and indicatorOfParameter == 218:
            return 'Covariance of v component/specific humidity'

        if table2Version == 162 and indicatorOfParameter == 217:
            return 'Covariance of v component/temperature'

        if table2Version == 162 and indicatorOfParameter == 216:
            return 'Covariance of v component/geopotential'

        if table2Version == 162 and indicatorOfParameter == 215:
            return 'Variance of u component'

        if table2Version == 162 and indicatorOfParameter == 214:
            return 'Covariance of u component/specific humidity'

        if table2Version == 162 and indicatorOfParameter == 213:
            return 'Covariance of u component/temperature'

        if table2Version == 162 and indicatorOfParameter == 212:
            return 'Covariance of u component/geopotential'

        if table2Version == 162 and indicatorOfParameter == 211:
            return 'Variance of specific humidity'

        if table2Version == 162 and indicatorOfParameter == 210:
            return 'Covariance of temperature/specific humidity'

        if table2Version == 162 and indicatorOfParameter == 209:
            return 'Covariance of geopotential/specific humidity'

        if table2Version == 162 and indicatorOfParameter == 208:
            return 'Variance of temperature'

        if table2Version == 162 and indicatorOfParameter == 207:
            return 'Covariance of geopotential/temperature'

        if table2Version == 162 and indicatorOfParameter == 206:
            return 'Variance of geopotential'

        if table2Version == 162 and indicatorOfParameter == 113:
            return 'Tendency of v component due to physics'

        if table2Version == 162 and indicatorOfParameter == 112:
            return 'Tendency of u component due to physics'

        if table2Version == 162 and indicatorOfParameter == 111:
            return 'Tendency of specific humidity due to physics'

        if table2Version == 162 and indicatorOfParameter == 110:
            return 'Tendency of temperature due to physics'

        if table2Version == 162 and indicatorOfParameter == 109:
            return 'Turbulent diffusion coefficient for heat'

        if table2Version == 162 and indicatorOfParameter == 108:
            return 'Total precipitation flux'

        if table2Version == 162 and indicatorOfParameter == 107:
            return 'Downdraught detrainment rate'

        if table2Version == 162 and indicatorOfParameter == 106:
            return 'Updraught detrainment rate'

        if table2Version == 162 and indicatorOfParameter == 105:
            return 'Downdraught mass flux'

        if table2Version == 162 and indicatorOfParameter == 104:
            return 'Updraught mass flux'

        if table2Version == 162 and indicatorOfParameter == 103:
            return 'Tendency of clear sky long wave radiation'

        if table2Version == 162 and indicatorOfParameter == 102:
            return 'Tendency of clear sky short wave radiation'

        if table2Version == 162 and indicatorOfParameter == 101:
            return 'Tendency of long wave radiation'

        if table2Version == 162 and indicatorOfParameter == 100:
            return 'Tendency of short wave radiation'

        if table2Version == 162 and indicatorOfParameter == 87:
            return 'Vertical integral of divergence of ozone flux'

        if table2Version == 162 and indicatorOfParameter == 86:
            return 'Vertical integral of divergence of total energy flux'

        if table2Version == 162 and indicatorOfParameter == 85:
            return 'Vertical integral of divergence of geopotential flux'

        if table2Version == 162 and indicatorOfParameter == 84:
            return 'Vertical integral of divergence of moisture flux'

        if table2Version == 162 and indicatorOfParameter == 83:
            return 'Vertical integral of divergence of thermal energy flux'

        if table2Version == 162 and indicatorOfParameter == 82:
            return 'Vertical integral of divergence of kinetic energy flux'

        if table2Version == 162 and indicatorOfParameter == 81:
            return 'Vertical integral of divergence of mass flux'

        if table2Version == 162 and indicatorOfParameter == 78:
            return 'Vertical integral of northward ozone flux'

        if table2Version == 162 and indicatorOfParameter == 77:
            return 'Vertical integral of eastward ozone flux'

        if table2Version == 162 and indicatorOfParameter == 76:
            return 'Vertical integral of northward total energy flux'

        if table2Version == 162 and indicatorOfParameter == 75:
            return 'Vertical integral of eastward total energy flux'

        if table2Version == 162 and indicatorOfParameter == 74:
            return 'Vertical integral of northward geopotential flux'

        if table2Version == 162 and indicatorOfParameter == 73:
            return 'Vertical integral of eastward geopotential flux'

        if table2Version == 162 and indicatorOfParameter == 72:
            return 'Vertical integral of northward water vapour flux'

        if table2Version == 162 and indicatorOfParameter == 71:
            return 'Vertical integral of eastward water vapour flux'

        if table2Version == 162 and indicatorOfParameter == 70:
            return 'Vertical integral of northward heat flux'

        if table2Version == 162 and indicatorOfParameter == 69:
            return 'Vertical integral of eastward heat flux'

        if table2Version == 162 and indicatorOfParameter == 68:
            return 'Vertical integral of northward kinetic energy flux'

        if table2Version == 162 and indicatorOfParameter == 67:
            return 'Vertical integral of eastward kinetic energy flux'

        if table2Version == 162 and indicatorOfParameter == 66:
            return 'Vertical integral of northward mass flux'

        if table2Version == 162 and indicatorOfParameter == 65:
            return 'Vertical integral of eastward mass flux'

        if table2Version == 162 and indicatorOfParameter == 64:
            return 'Vertical integral of energy conversion'

        if table2Version == 162 and indicatorOfParameter == 63:
            return 'Vertical integral of total energy'

        if table2Version == 162 and indicatorOfParameter == 62:
            return 'Vertical integral of potential+internal+latent energy'

        if table2Version == 162 and indicatorOfParameter == 61:
            return 'Vertical integral of potential+internal energy'

        if table2Version == 162 and indicatorOfParameter == 60:
            return 'Vertical integral of thermal energy'

        if table2Version == 162 and indicatorOfParameter == 59:
            return 'Vertical integral of kinetic energy'

        if table2Version == 162 and indicatorOfParameter == 58:
            return 'Vertical integral of ozone'

        if table2Version == 162 and indicatorOfParameter == 57:
            return 'Vertical integral of cloud frozen water'

        if table2Version == 162 and indicatorOfParameter == 56:
            return 'Vertical integral of cloud liquid water'

        if table2Version == 162 and indicatorOfParameter == 55:
            return 'Vertical integral of water vapour'

        if table2Version == 162 and indicatorOfParameter == 54:
            return 'Vertical integral of temperature'

        if table2Version == 162 and indicatorOfParameter == 53:
            return 'Vertical integral of mass of atmosphere'

        if table2Version == 162 and indicatorOfParameter == 51:
            return 'Surface geopotential'

        if table2Version == 160 and indicatorOfParameter == 254:
            return 'Heaviside beta function'

        if table2Version == 160 and indicatorOfParameter == 249:
            return 'Gravity wave dissipation flux'

        if table2Version == 160 and indicatorOfParameter == 247:
            return 'Momentum flux'

        if table2Version == 160 and indicatorOfParameter == 246:
            return '10 metre wind speed'

        if table2Version == 160 and indicatorOfParameter == 243:
            return 'Forecast albedo'

        if table2Version == 160 and indicatorOfParameter == 242:
            return 'Cloud cover'

        if table2Version == 160 and indicatorOfParameter == 241:
            return 'Cloud liquid water content'

        if table2Version == 160 and indicatorOfParameter == 240:
            return 'Large scale snowfall'

        if table2Version == 160 and indicatorOfParameter == 239:
            return 'Convective snowfall'

        if table2Version == 160 and indicatorOfParameter == 231:
            return 'Instantaneous surface heat flux'

        if table2Version == 160 and indicatorOfParameter == 226:
            return 'Standard deviation of vertical velocity'

        if table2Version == 160 and indicatorOfParameter == 225:
            return 'Covariance of W component and V component'

        if table2Version == 160 and indicatorOfParameter == 224:
            return 'Covariance of W component and U component'

        if table2Version == 160 and indicatorOfParameter == 223:
            return 'Covariance of W component and specific humidity'

        if table2Version == 160 and indicatorOfParameter == 222:
            return 'Covariance of W component and temperature'

        if table2Version == 160 and indicatorOfParameter == 221:
            return 'Covariance of W component and geopotential'

        if table2Version == 160 and indicatorOfParameter == 220:
            return 'Standard deviation of V component'

        if table2Version == 160 and indicatorOfParameter == 219:
            return 'Covariance of V component and U component'

        if table2Version == 160 and indicatorOfParameter == 218:
            return 'Covariance of V component and specific humidity'

        if table2Version == 160 and indicatorOfParameter == 217:
            return 'Covariance of V component and temperature'

        if table2Version == 160 and indicatorOfParameter == 216:
            return 'Covariance of V component and geopotential'

        if table2Version == 160 and indicatorOfParameter == 215:
            return 'Standard deviation of U velocity'

        if table2Version == 160 and indicatorOfParameter == 214:
            return 'Covariance of U component and specific humidity'

        if table2Version == 160 and indicatorOfParameter == 213:
            return 'Covariance of U component and temperature'

        if table2Version == 160 and indicatorOfParameter == 212:
            return 'Covariance of U component and geopotential'

        if table2Version == 160 and indicatorOfParameter == 211:
            return 'Standard deviation of specific humidity'

        if table2Version == 160 and indicatorOfParameter == 210:
            return 'Covariance of specific humidity and temperature'

        if table2Version == 160 and indicatorOfParameter == 209:
            return 'Covariance of specific humidity and geopotential'

        if table2Version == 160 and indicatorOfParameter == 208:
            return 'Standard deviation of temperature'

        if table2Version == 160 and indicatorOfParameter == 207:
            return 'Covariance of temperature and geopotential'

        if table2Version == 160 and indicatorOfParameter == 206:
            return 'Standard deviation of geopotential'

        if table2Version == 160 and indicatorOfParameter == 205:
            return 'Runoff'

        if table2Version == 160 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres during averaging time'

        if table2Version == 160 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres during averaging time'

        if table2Version == 160 and indicatorOfParameter == 199:
            return 'Percentage of vegetation'

        if table2Version == 160 and indicatorOfParameter == 198:
            return 'Skin reservoir content'

        if table2Version == 160 and indicatorOfParameter == 184:
            return 'Soil wetness level 3'

        if table2Version == 160 and indicatorOfParameter == 182:
            return 'Evaporation'

        if table2Version == 160 and indicatorOfParameter == 181:
            return 'North-South surface stress'

        if table2Version == 160 and indicatorOfParameter == 180:
            return 'East-West surface stress'

        if table2Version == 160 and indicatorOfParameter == 171:
            return 'Soil wetness level 2'

        if table2Version == 160 and indicatorOfParameter == 157:
            return 'Relative humidity'

        if table2Version == 160 and indicatorOfParameter == 156:
            return 'Height'

        if table2Version == 160 and indicatorOfParameter == 144:
            return 'Snowfall'

        if table2Version == 160 and indicatorOfParameter == 143:
            return 'Convective precipitation'

        if table2Version == 160 and indicatorOfParameter == 142:
            return 'Large-scale precipitation'

        if table2Version == 160 and indicatorOfParameter == 141:
            return 'Snow depth'

        if table2Version == 160 and indicatorOfParameter == 140:
            return 'Soil wetness level 1'

        if table2Version == 160 and indicatorOfParameter == 137:
            return 'Precipitable water content'

        if table2Version == 160 and indicatorOfParameter == 135:
            return 'vertical velocity (pressure)'

        if table2Version == 160 and indicatorOfParameter == 49:
            return '10 metre wind gust during averaging time'

        if table2Version == 151 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 151 and indicatorOfParameter == 212:
            return 'Bias in salinity (applied)'

        if table2Version == 151 and indicatorOfParameter == 211:
            return 'Bias in temperature(applied)'

        if table2Version == 151 and indicatorOfParameter == 210:
            return 'FG bias in pressure'

        if table2Version == 151 and indicatorOfParameter == 209:
            return 'Applied bias in pressure'

        if table2Version == 151 and indicatorOfParameter == 208:
            return 'First guess bias in salinity'

        if table2Version == 151 and indicatorOfParameter == 207:
            return 'First guess bias in temperature'

        if table2Version == 151 and indicatorOfParameter == 206:
            return 'Estimated salinity bias from relaxation'

        if table2Version == 151 and indicatorOfParameter == 205:
            return 'Estimated temperature bias from relaxation'

        if table2Version == 151 and indicatorOfParameter == 204:
            return 'Bias in the meridional pressure gradient (applied)'

        if table2Version == 151 and indicatorOfParameter == 203:
            return 'Bias in the zonal pressure gradient (applied)'

        if table2Version == 151 and indicatorOfParameter == 202:
            return 'Salinity increment from relaxation term'

        if table2Version == 151 and indicatorOfParameter == 201:
            return 'Temperature increment from relaxation term'

        if table2Version == 151 and indicatorOfParameter == 200:
            return 'Estimated salinity bias from assimilation'

        if table2Version == 151 and indicatorOfParameter == 199:
            return 'Estimated temperature bias from assimilation'

        if table2Version == 151 and indicatorOfParameter == 194:
            return 'Salinity background error'

        if table2Version == 151 and indicatorOfParameter == 192:
            return 'Background Salinity'

        if table2Version == 151 and indicatorOfParameter == 191:
            return 'Salinity analysis error'

        if table2Version == 151 and indicatorOfParameter == 190:
            return 'Salinity increment (from salinity data)'

        if table2Version == 151 and indicatorOfParameter == 188:
            return 'Meridional Velocity increment (from balance operator)'

        if table2Version == 151 and indicatorOfParameter == 187:
            return 'Zonal Velocity increment (from balance operator)'

        if table2Version == 151 and indicatorOfParameter == 186:
            return 'Estimated Bias in Salinity'

        if table2Version == 151 and indicatorOfParameter == 185:
            return 'Estimated Bias in Temperature'

        if table2Version == 151 and indicatorOfParameter == 184:
            return 'Salinity increment'

        if table2Version == 151 and indicatorOfParameter == 183:
            return 'Analysed salinity'

        if table2Version == 151 and indicatorOfParameter == 182:
            return 'Potential temperature background error'

        if table2Version == 151 and indicatorOfParameter == 181:
            return 'Analysed potential temperature'

        if table2Version == 151 and indicatorOfParameter == 180:
            return 'Background potential temperature'

        if table2Version == 151 and indicatorOfParameter == 179:
            return 'Potential temperature analysis error'

        if table2Version == 151 and indicatorOfParameter == 178:
            return 'Potential temperature increment'

        if table2Version == 151 and indicatorOfParameter == 177:
            return 'Layer Thickness at vector points'

        if table2Version == 151 and indicatorOfParameter == 176:
            return 'Layer Thickness at scalar points'

        if table2Version == 151 and indicatorOfParameter == 175:
            return 'Average salinity in the upper 300m'

        if table2Version == 151 and indicatorOfParameter == 174:
            return 'Depth of salinity maximum'

        if table2Version == 151 and indicatorOfParameter == 173:
            return 'Salinity maximum'

        if table2Version == 151 and indicatorOfParameter == 172:
            return 'Depth of the velocity maximum'

        if table2Version == 151 and indicatorOfParameter == 171:
            return 'U velocity maximum'

        if table2Version == 151 and indicatorOfParameter == 170:
            return 'Vertically integrated meridional heat transport'

        if table2Version == 151 and indicatorOfParameter == 169:
            return 'Vertically integrated zonal heat transport'

        if table2Version == 151 and indicatorOfParameter == 168:
            return 'Vertically integrated meridional volume transport'

        if table2Version == 151 and indicatorOfParameter == 167:
            return 'Vertically integrated zonal volume transport'

        if table2Version == 151 and indicatorOfParameter == 166:
            return 'Vertically Integrated meridional velocity (previous time step)'

        if table2Version == 151 and indicatorOfParameter == 165:
            return 'Vertically integrated zonal velocity (previous time step)'

        if table2Version == 151 and indicatorOfParameter == 164:
            return 'Average potential temperature in the upper 300m'

        if table2Version == 151 and indicatorOfParameter == 163:
            return 'Depth of 20C isotherm'

        if table2Version == 151 and indicatorOfParameter == 162:
            return 'Heat flux correction'

        if table2Version == 151 and indicatorOfParameter == 161:
            return 'Diagnosed sea surface temperature error'

        if table2Version == 151 and indicatorOfParameter == 160:
            return 'Specified surface heat flux'

        if table2Version == 151 and indicatorOfParameter == 159:
            return 'Specified sea surface temperature'

        if table2Version == 151 and indicatorOfParameter == 158:
            return 'Precipitation - evaporation'

        if table2Version == 151 and indicatorOfParameter == 157:
            return 'Absorbed solar radiation'

        if table2Version == 151 and indicatorOfParameter == 156:
            return 'Net surface heat flux'

        if table2Version == 151 and indicatorOfParameter == 155:
            return 'Turbulent kinetic energy input'

        if table2Version == 151 and indicatorOfParameter == 154:
            return 'Surface downward northward stress'

        if table2Version == 151 and indicatorOfParameter == 153:
            return 'Surface downward eastward stress'

        if table2Version == 151 and indicatorOfParameter == 152:
            return 'Divergence of wind stress'

        if table2Version == 151 and indicatorOfParameter == 151:
            return 'Curl of Wind Stress'

        if table2Version == 151 and indicatorOfParameter == 150:
            return 'Steric height'

        if table2Version == 151 and indicatorOfParameter == 149:
            return 'Bottom Pressure (equivalent height)'

        if table2Version == 151 and indicatorOfParameter == 148:
            return 'Mixed layer depth'

        if table2Version == 151 and indicatorOfParameter == 147:
            return 'Ocean barotropic stream function'

        if table2Version == 151 and indicatorOfParameter == 146:
            return 'Sea level previous timestep'

        if table2Version == 151 and indicatorOfParameter == 145:
            return 'Sea surface height'

        if table2Version == 151 and indicatorOfParameter == 144:
            return 'VV product'

        if table2Version == 151 and indicatorOfParameter == 143:
            return 'UU product'

        if table2Version == 151 and indicatorOfParameter == 142:
            return 'VT product'

        if table2Version == 151 and indicatorOfParameter == 141:
            return 'UT product'

        if table2Version == 151 and indicatorOfParameter == 140:
            return 'UV product'

        if table2Version == 151 and indicatorOfParameter == 139:
            return 'Richardson number'

        if table2Version == 151 and indicatorOfParameter == 138:
            return 'Sea water sigma theta'

        if table2Version == 151 and indicatorOfParameter == 137:
            return 'Bottom level Depth'

        if table2Version == 151 and indicatorOfParameter == 136:
            return 'Vertical diffusivity'

        if table2Version == 151 and indicatorOfParameter == 135:
            return 'Vertical viscosity'

        if table2Version == 151 and indicatorOfParameter == 134:
            return 'Modulus of strain rate tensor'

        if table2Version == 151 and indicatorOfParameter == 133:
            return 'Upward sea water velocity'

        if table2Version == 151 and indicatorOfParameter == 132:
            return 'Northward sea water velocity'

        if table2Version == 151 and indicatorOfParameter == 131:
            return 'Eastward sea water velocity'

        if table2Version == 151 and indicatorOfParameter == 130:
            return 'Sea water practical salinity'

        if table2Version == 151 and indicatorOfParameter == 129:
            return 'Sea water potential temperature'

        if table2Version == 151 and indicatorOfParameter == 128:
            return 'In situ Temperature'

        if table2Version == 150 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 150 and indicatorOfParameter == 183:
            return 'Observed heat flux'

        if table2Version == 150 and indicatorOfParameter == 182:
            return 'Observed sea surface temperature'

        if table2Version == 150 and indicatorOfParameter == 181:
            return 'Heat flux correction'

        if table2Version == 150 and indicatorOfParameter == 180:
            return 'Diagnosed sea surface temperature error'

        if table2Version == 150 and indicatorOfParameter == 173:
            return 'P-E'

        if table2Version == 150 and indicatorOfParameter == 172:
            return 'Surface solar radiation'

        if table2Version == 150 and indicatorOfParameter == 171:
            return 'Net surface heat flux'

        if table2Version == 150 and indicatorOfParameter == 170:
            return 'Turbulent kinetic energy input'

        if table2Version == 150 and indicatorOfParameter == 169:
            return 'V stress'

        if table2Version == 150 and indicatorOfParameter == 168:
            return 'U stress'

        if table2Version == 150 and indicatorOfParameter == 155:
            return 'Depth'

        if table2Version == 150 and indicatorOfParameter == 154:
            return 'Mixed layer depth'

        if table2Version == 150 and indicatorOfParameter == 153:
            return 'Barotropic stream function'

        if table2Version == 150 and indicatorOfParameter == 152:
            return 'Sea level'

        if table2Version == 150 and indicatorOfParameter == 148:
            return 'VV - V~V~'

        if table2Version == 150 and indicatorOfParameter == 147:
            return 'UU - U~U~'

        if table2Version == 150 and indicatorOfParameter == 146:
            return 'VT - V~T~'

        if table2Version == 150 and indicatorOfParameter == 145:
            return 'UT - U~T~'

        if table2Version == 150 and indicatorOfParameter == 144:
            return 'UV - U~V~'

        if table2Version == 150 and indicatorOfParameter == 143:
            return 'V*V product'

        if table2Version == 150 and indicatorOfParameter == 142:
            return 'U*U product'

        if table2Version == 150 and indicatorOfParameter == 141:
            return 'V*T product'

        if table2Version == 150 and indicatorOfParameter == 140:
            return 'U*T product'

        if table2Version == 150 and indicatorOfParameter == 139:
            return 'U*V product'

        if table2Version == 150 and indicatorOfParameter == 137:
            return 'Richardson number'

        if table2Version == 150 and indicatorOfParameter == 135:
            return 'Ocean W wind component'

        if table2Version == 150 and indicatorOfParameter == 134:
            return 'Ocean V wind component'

        if table2Version == 150 and indicatorOfParameter == 133:
            return 'Ocean U wind component'

        if table2Version == 150 and indicatorOfParameter == 131:
            return 'Ocean potential density'

        if table2Version == 150 and indicatorOfParameter == 130:
            return 'Ocean salinity'

        if table2Version == 150 and indicatorOfParameter == 129:
            return 'Ocean potential temperature'

        if table2Version == 140 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 140 and indicatorOfParameter == 254:
            return 'Wave spectral peakedness'

        if table2Version == 140 and indicatorOfParameter == 253:
            return 'Benjamin-Feir index'

        if table2Version == 140 and indicatorOfParameter == 252:
            return 'Wave spectral kurtosis'

        if table2Version == 140 and indicatorOfParameter == 251:
            return '2D wave spectra (single)'

        if table2Version == 140 and indicatorOfParameter == 250:
            return '2D wave spectra (multiple)'

        if table2Version == 140 and indicatorOfParameter == 249:
            return '10 metre wind direction'

        if table2Version == 140 and indicatorOfParameter == 248:
            return 'Altimeter range relative correction'

        if table2Version == 140 and indicatorOfParameter == 247:
            return 'Altimeter corrected wave height'

        if table2Version == 140 and indicatorOfParameter == 246:
            return 'Altimeter wave height'

        if table2Version == 140 and indicatorOfParameter == 245:
            return '10 metre wind speed'

        if table2Version == 140 and indicatorOfParameter == 244:
            return 'Mean square slope of waves'

        if table2Version == 140 and indicatorOfParameter == 243:
            return 'Standard deviation of 10 metre wind speed'

        if table2Version == 140 and indicatorOfParameter == 242:
            return 'Mean wind direction'

        if table2Version == 140 and indicatorOfParameter == 241:
            return 'Mean of 10 metre wind speed'

        if table2Version == 140 and indicatorOfParameter == 240:
            return 'Standard deviation wave height'

        if table2Version == 140 and indicatorOfParameter == 239:
            return 'Mean period of total swell'

        if table2Version == 140 and indicatorOfParameter == 238:
            return 'Mean direction of total swell'

        if table2Version == 140 and indicatorOfParameter == 237:
            return 'Significant height of total swell'

        if table2Version == 140 and indicatorOfParameter == 236:
            return 'Mean period of wind waves'

        if table2Version == 140 and indicatorOfParameter == 235:
            return 'Mean direction of wind waves'

        if table2Version == 140 and indicatorOfParameter == 234:
            return 'Significant height of wind waves'

        if table2Version == 140 and indicatorOfParameter == 233:
            return 'Coefficient of drag with waves'

        if table2Version == 140 and indicatorOfParameter == 232:
            return 'Mean wave period'

        if table2Version == 140 and indicatorOfParameter == 231:
            return 'Peak wave period'

        if table2Version == 140 and indicatorOfParameter == 230:
            return 'Mean wave direction'

        if table2Version == 140 and indicatorOfParameter == 229:
            return 'Significant height of combined wind waves and swell'

        if table2Version == 140 and indicatorOfParameter == 228:
            return 'Wave spectral directional width for swell'

        if table2Version == 140 and indicatorOfParameter == 227:
            return 'Mean wave period based on second moment for swell'

        if table2Version == 140 and indicatorOfParameter == 226:
            return 'Mean wave period based on first moment for swell'

        if table2Version == 140 and indicatorOfParameter == 225:
            return 'Wave spectral directional width for wind waves'

        if table2Version == 140 and indicatorOfParameter == 224:
            return 'Mean wave period based on second moment for wind waves'

        if table2Version == 140 and indicatorOfParameter == 223:
            return 'Mean wave period based on first moment for wind waves'

        if table2Version == 140 and indicatorOfParameter == 222:
            return 'Wave spectral directional width'

        if table2Version == 140 and indicatorOfParameter == 221:
            return 'Mean zero-crossing wave period'

        if table2Version == 140 and indicatorOfParameter == 220:
            return 'Mean wave period based on first moment'

        if table2Version == 140 and indicatorOfParameter == 219:
            return 'Model bathymetry'

        if table2Version == 140 and indicatorOfParameter == 218:
            return 'Maximum individual wave height'

        if table2Version == 140 and indicatorOfParameter == 217:
            return 'Period corresponding to maximum individual wave height'

        if table2Version == 140 and indicatorOfParameter == 200:
            return 'Maximum of significant wave height'

        if table2Version == 133 and indicatorOfParameter == 92:
            return 'Low Cloud Cover probability greater than 99%'

        if table2Version == 133 and indicatorOfParameter == 91:
            return 'Low Cloud Cover probability greater than 90%'

        if table2Version == 133 and indicatorOfParameter == 90:
            return 'Low Cloud Cover probability greater than 80%'

        if table2Version == 133 and indicatorOfParameter == 89:
            return 'Low Cloud Cover probability greater than 70%'

        if table2Version == 133 and indicatorOfParameter == 88:
            return 'Low Cloud Cover probability greater than 60%'

        if table2Version == 133 and indicatorOfParameter == 87:
            return 'Low Cloud Cover probability greater than 50%'

        if table2Version == 133 and indicatorOfParameter == 86:
            return 'Low Cloud Cover probability greater than 40%'

        if table2Version == 133 and indicatorOfParameter == 85:
            return 'Low Cloud Cover probability greater than 30%'

        if table2Version == 133 and indicatorOfParameter == 84:
            return 'Low Cloud Cover probability greater than 20%'

        if table2Version == 133 and indicatorOfParameter == 83:
            return 'Low Cloud Cover probability greater than 10%'

        if table2Version == 133 and indicatorOfParameter == 82:
            return 'Medium Cloud Cover probability greater than 99%'

        if table2Version == 133 and indicatorOfParameter == 81:
            return 'Medium Cloud Cover probability greater than 90%'

        if table2Version == 133 and indicatorOfParameter == 80:
            return 'Medium Cloud Cover probability greater than 80%'

        if table2Version == 133 and indicatorOfParameter == 79:
            return 'Medium Cloud Cover probability greater than 70%'

        if table2Version == 133 and indicatorOfParameter == 78:
            return 'Medium Cloud Cover probability greater than 60%'

        if table2Version == 133 and indicatorOfParameter == 77:
            return 'Medium Cloud Cover probability greater than 50%'

        if table2Version == 133 and indicatorOfParameter == 76:
            return 'Medium Cloud Cover probability greater than 40%'

        if table2Version == 133 and indicatorOfParameter == 75:
            return 'Medium Cloud Cover probability greater than 30%'

        if table2Version == 133 and indicatorOfParameter == 74:
            return 'Medium Cloud Cover probability greater than 20%'

        if table2Version == 133 and indicatorOfParameter == 73:
            return 'Medium Cloud Cover probability greater than 10%'

        if table2Version == 133 and indicatorOfParameter == 72:
            return 'High Cloud Cover probability greater than 99%'

        if table2Version == 133 and indicatorOfParameter == 71:
            return 'High Cloud Cover probability greater than 90%'

        if table2Version == 133 and indicatorOfParameter == 70:
            return 'High Cloud Cover probability greater than 80%'

        if table2Version == 133 and indicatorOfParameter == 69:
            return 'High Cloud Cover probability greater than 70%'

        if table2Version == 133 and indicatorOfParameter == 68:
            return 'High Cloud Cover probability greater than 60%'

        if table2Version == 133 and indicatorOfParameter == 67:
            return 'High Cloud Cover probability greater than 50%'

        if table2Version == 133 and indicatorOfParameter == 66:
            return 'High Cloud Cover probability greater than 40%'

        if table2Version == 133 and indicatorOfParameter == 65:
            return 'High Cloud Cover probability greater than 30%'

        if table2Version == 133 and indicatorOfParameter == 64:
            return 'High Cloud Cover probability greater than 20%'

        if table2Version == 133 and indicatorOfParameter == 63:
            return 'High Cloud Cover probability greater than 10%'

        if table2Version == 133 and indicatorOfParameter == 62:
            return 'Total Cloud Cover probability greater than 99%'

        if table2Version == 133 and indicatorOfParameter == 61:
            return 'Total Cloud Cover probability greater than 90%'

        if table2Version == 133 and indicatorOfParameter == 60:
            return 'Total Cloud Cover probability greater than 80%'

        if table2Version == 133 and indicatorOfParameter == 59:
            return 'Total Cloud Cover probability greater than 70%'

        if table2Version == 133 and indicatorOfParameter == 58:
            return 'Total Cloud Cover probability greater than 60%'

        if table2Version == 133 and indicatorOfParameter == 57:
            return 'Total Cloud Cover probability greater than 50%'

        if table2Version == 133 and indicatorOfParameter == 56:
            return 'Total Cloud Cover probability greater than 40%'

        if table2Version == 133 and indicatorOfParameter == 55:
            return 'Total Cloud Cover probability greater than 30%'

        if table2Version == 133 and indicatorOfParameter == 54:
            return 'Total Cloud Cover probability greater than 20%'

        if table2Version == 133 and indicatorOfParameter == 53:
            return 'Total Cloud Cover probability greater than 10%'

        if table2Version == 133 and indicatorOfParameter == 52:
            return 'Snowfall probability of at least 300 mm'

        if table2Version == 133 and indicatorOfParameter == 51:
            return 'Snowfall probability of at least 200 mm'

        if table2Version == 133 and indicatorOfParameter == 50:
            return 'Snowfall probability of at least 150 mm'

        if table2Version == 133 and indicatorOfParameter == 49:
            return 'Snowfall probability of at least 100 mm'

        if table2Version == 133 and indicatorOfParameter == 48:
            return 'Snowfall probability of at least 80 mm'

        if table2Version == 133 and indicatorOfParameter == 47:
            return 'Snowfall probability of at least 60 mm'

        if table2Version == 133 and indicatorOfParameter == 46:
            return 'Snowfall probability of at least 40 mm'

        if table2Version == 133 and indicatorOfParameter == 45:
            return 'Snowfall probability of at least 20 mm'

        if table2Version == 133 and indicatorOfParameter == 44:
            return 'Snowfall probability of at least 10 mm'

        if table2Version == 133 and indicatorOfParameter == 43:
            return 'Snowfall probability of at least 5 mm'

        if table2Version == 133 and indicatorOfParameter == 42:
            return 'Snowfall probability of at least 1 mm'

        if table2Version == 133 and indicatorOfParameter == 41:
            return 'Total precipitation probability of at least 300 mm'

        if table2Version == 133 and indicatorOfParameter == 40:
            return 'Total precipitation probability of at least 200 mm'

        if table2Version == 133 and indicatorOfParameter == 39:
            return 'Total precipitation probability of at least 150 mm'

        if table2Version == 133 and indicatorOfParameter == 38:
            return 'Total precipitation probability of at least 100 mm'

        if table2Version == 133 and indicatorOfParameter == 37:
            return 'Total precipitation probability of at least 80 mm'

        if table2Version == 133 and indicatorOfParameter == 36:
            return 'Total precipitation probability of at least 60 mm'

        if table2Version == 133 and indicatorOfParameter == 35:
            return 'Total precipitation probability of at least 40 mm'

        if table2Version == 133 and indicatorOfParameter == 34:
            return 'Total precipitation probability of at least 20 mm'

        if table2Version == 133 and indicatorOfParameter == 33:
            return 'Total precipitation probability of at least 10 mm'

        if table2Version == 133 and indicatorOfParameter == 32:
            return 'Total precipitation probability of at least 5 mm'

        if table2Version == 133 and indicatorOfParameter == 31:
            return 'Total precipitation probability of at least 1 mm'

        if table2Version == 133 and indicatorOfParameter == 30:
            return '10 metre wind gust probability of at least 100 m/s'

        if table2Version == 133 and indicatorOfParameter == 29:
            return '10 metre wind gust probability of at least 75 m/s'

        if table2Version == 133 and indicatorOfParameter == 28:
            return '10 metre wind gust probability of at least 50 m/s'

        if table2Version == 133 and indicatorOfParameter == 27:
            return '10 metre wind gust probability of at least 35 m/s'

        if table2Version == 133 and indicatorOfParameter == 26:
            return '10 metre wind gust probability of at least 20 m/s'

        if table2Version == 133 and indicatorOfParameter == 25:
            return '10 metre wind speed probability of at least 50 m/s'

        if table2Version == 133 and indicatorOfParameter == 24:
            return '10 metre wind speed probability of at least 35 m/s'

        if table2Version == 133 and indicatorOfParameter == 23:
            return '10 metre wind speed probability of at least 20 m/s'

        if table2Version == 133 and indicatorOfParameter == 22:
            return '10 metre wind speed probability of at least 15 m/s'

        if table2Version == 133 and indicatorOfParameter == 21:
            return '10 metre wind speed probability of at least 10 m/s'

        if table2Version == 133 and indicatorOfParameter == 20:
            return 'Maximum 2 metre temperature probability greater than 45 C'

        if table2Version == 133 and indicatorOfParameter == 19:
            return 'Maximum 2 metre temperature probability greater than 40 C'

        if table2Version == 133 and indicatorOfParameter == 18:
            return 'Maximum 2 metre temperature probability greater than 35 C'

        if table2Version == 133 and indicatorOfParameter == 17:
            return 'Maximum 2 metre temperature probability greater than 30 C'

        if table2Version == 133 and indicatorOfParameter == 16:
            return 'Maximum 2 metre temperature probability greater than 25 C'

        if table2Version == 133 and indicatorOfParameter == 15:
            return 'Minimum 2 metre temperature probability less than 10 C'

        if table2Version == 133 and indicatorOfParameter == 14:
            return 'Minimum 2 metre temperature probability less than 5 C'

        if table2Version == 133 and indicatorOfParameter == 13:
            return 'Minimum 2 metre temperature probability less than 0 C'

        if table2Version == 133 and indicatorOfParameter == 12:
            return 'Minimum 2 metre temperature probability less than -5 C'

        if table2Version == 133 and indicatorOfParameter == 11:
            return 'Minimum 2 metre temperature probability less than -10 C'

        if table2Version == 133 and indicatorOfParameter == 10:
            return '2m temperature probability greater than 45 C'

        if table2Version == 133 and indicatorOfParameter == 9:
            return '2m temperature probability greater than 40 C'

        if table2Version == 133 and indicatorOfParameter == 8:
            return '2m temperature probability greater than 35 C'

        if table2Version == 133 and indicatorOfParameter == 7:
            return '2m temperature probability greater than 30 C'

        if table2Version == 133 and indicatorOfParameter == 6:
            return '2m temperature probability greater than 25 C'

        if table2Version == 133 and indicatorOfParameter == 5:
            return '2m temperature probability less than 10 C'

        if table2Version == 133 and indicatorOfParameter == 4:
            return '2m temperature probability less than 5 C'

        if table2Version == 133 and indicatorOfParameter == 3:
            return '2m temperature probability less than 0 C'

        if table2Version == 133 and indicatorOfParameter == 2:
            return '2m temperature probability less than -5 C'

        if table2Version == 133 and indicatorOfParameter == 1:
            return '2m temperature probability less than -10 C'

        if table2Version == 132 and indicatorOfParameter == 228:
            return 'Total precipitation index'

        if table2Version == 132 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres index'

        if table2Version == 132 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres index'

        if table2Version == 132 and indicatorOfParameter == 167:
            return '2 metre temperature index'

        if table2Version == 132 and indicatorOfParameter == 165:
            return '10 metre speed index'

        if table2Version == 132 and indicatorOfParameter == 144:
            return 'Snowfall index'

        if table2Version == 132 and indicatorOfParameter == 49:
            return '10 metre wind gust index'

        if table2Version == 131 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 131 and indicatorOfParameter == 232:
            return 'Mean wave period probability'

        if table2Version == 131 and indicatorOfParameter == 229:
            return 'Significant wave height probability'

        if table2Version == 131 and indicatorOfParameter == 228:
            return 'Total precipitation probability'

        if table2Version == 131 and indicatorOfParameter == 202:
            return 'Minimum 2 metre temperature probability'

        if table2Version == 131 and indicatorOfParameter == 201:
            return 'Maximum 2 metre temperature probability'

        if table2Version == 131 and indicatorOfParameter == 167:
            return '2 metre temperature probability'

        if table2Version == 131 and indicatorOfParameter == 165:
            return '10 metre speed probability'

        if table2Version == 131 and indicatorOfParameter == 164:
            return 'Total cloud cover probability'

        if table2Version == 131 and indicatorOfParameter == 151:
            return 'Mean sea level pressure probability'

        if table2Version == 131 and indicatorOfParameter == 144:
            return 'Snowfall (convective + stratiform) probability'

        if table2Version == 131 and indicatorOfParameter == 139:
            return 'Soil temperature level 1 probability'

        if table2Version == 131 and indicatorOfParameter == 130:
            return 'Temperature anomaly probability'

        if table2Version == 131 and indicatorOfParameter == 129:
            return 'Geopotential probability'

        if table2Version == 131 and indicatorOfParameter == 81:
            return 'Mean wave period of at least 15 s'

        if table2Version == 131 and indicatorOfParameter == 80:
            return 'Mean wave period of at least 12 s'

        if table2Version == 131 and indicatorOfParameter == 79:
            return 'Mean wave period of at least 10 s'

        if table2Version == 131 and indicatorOfParameter == 78:
            return 'Mean wave period of at least 8 s'

        if table2Version == 131 and indicatorOfParameter == 77:
            return 'Significant wave height of at least 8 m'

        if table2Version == 131 and indicatorOfParameter == 76:
            return 'Significant wave height of at least 6 m'

        if table2Version == 131 and indicatorOfParameter == 75:
            return 'Significant wave height of at least 4 m'

        if table2Version == 131 and indicatorOfParameter == 74:
            return 'Significant wave height of at least 2 m'

        if table2Version == 131 and indicatorOfParameter == 73:
            return '2 metre temperature less than 273.15 K'

        if table2Version == 131 and indicatorOfParameter == 72:
            return '10 metre wind gust of at least 25 m/s'

        if table2Version == 131 and indicatorOfParameter == 71:
            return '10 metre wind gust of at least 20 m/s'

        if table2Version == 131 and indicatorOfParameter == 70:
            return '10 metre wind gust of at least 15 m/s'

        if table2Version == 131 and indicatorOfParameter == 69:
            return '10 metre Wind speed of at least 15 m/s'

        if table2Version == 131 and indicatorOfParameter == 68:
            return '10 metre Wind speed of at least 10 m/s'

        if table2Version == 131 and indicatorOfParameter == 67:
            return 'Total precipitation rate of at least 5 mm/day'

        if table2Version == 131 and indicatorOfParameter == 66:
            return 'Total precipitation rate of at least 3 mm/day'

        if table2Version == 131 and indicatorOfParameter == 65:
            return 'Total precipitation rate less than 1 mm/day'

        if table2Version == 131 and indicatorOfParameter == 64:
            return 'Total precipitation less than 0.1 mm'

        if table2Version == 131 and indicatorOfParameter == 59:
            return 'Convective available potential energy probability'

        if table2Version == 131 and indicatorOfParameter == 49:
            return '10 metre wind gust probability'

        if table2Version == 131 and indicatorOfParameter == 25:
            return 'Temperature anomaly greater than +8 K'

        if table2Version == 131 and indicatorOfParameter == 24:
            return 'Temperature anomaly greater than +4 K'

        if table2Version == 131 and indicatorOfParameter == 23:
            return 'Temperature anomaly less than -4 K'

        if table2Version == 131 and indicatorOfParameter == 22:
            return 'Temperature anomaly less than -8 K'

        if table2Version == 131 and indicatorOfParameter == 21:
            return 'Temperature anomaly of at least +2 K'

        if table2Version == 131 and indicatorOfParameter == 20:
            return 'Temperature anomaly less than -2 K'

        if table2Version == 131 and indicatorOfParameter == 18:
            return 'Whiting index probability'

        if table2Version == 131 and indicatorOfParameter == 17:
            return 'Showalter index probability'

        if table2Version == 131 and indicatorOfParameter == 16:
            return 'Height of snowfall limit probability'

        if table2Version == 131 and indicatorOfParameter == 15:
            return 'Height of 0 degree isotherm probability'

        if table2Version == 131 and indicatorOfParameter == 10:
            return 'Mean sea level pressure anomaly of at least 0 Pa'

        if table2Version == 131 and indicatorOfParameter == 9:
            return 'Surface temperature anomaly of at least 0K'

        if table2Version == 131 and indicatorOfParameter == 8:
            return 'Total precipitation anomaly of at least 0 mm'

        if table2Version == 131 and indicatorOfParameter == 7:
            return 'Total precipitation anomaly of at least 10 mm'

        if table2Version == 131 and indicatorOfParameter == 6:
            return 'Total precipitation anomaly of at least 20 mm'

        if table2Version == 131 and indicatorOfParameter == 5:
            return '2m temperature anomaly of at most -2K'

        if table2Version == 131 and indicatorOfParameter == 4:
            return '2m temperature anomaly of at most -1K'

        if table2Version == 131 and indicatorOfParameter == 3:
            return '2m temperature anomaly of at least 0K'

        if table2Version == 131 and indicatorOfParameter == 2:
            return '2m temperature anomaly of at least +1K'

        if table2Version == 131 and indicatorOfParameter == 1:
            return '2m temperature anomaly of at least +2K'

        if table2Version == 130 and indicatorOfParameter == 232:
            return 'Mean vertical velocity'

        if table2Version == 130 and indicatorOfParameter == 231:
            return 'Adiabatic tendency of meridional wind'

        if table2Version == 130 and indicatorOfParameter == 230:
            return 'Adiabatic tendency of zonal wind'

        if table2Version == 130 and indicatorOfParameter == 229:
            return 'Adiabatic tendency of humidity'

        if table2Version == 130 and indicatorOfParameter == 228:
            return 'Adiabatic tendency of temperature'

        if table2Version == 130 and indicatorOfParameter == 226:
            return 'Humidity tendency by large-scale condensation'

        if table2Version == 130 and indicatorOfParameter == 225:
            return 'Humidity tendency by cumulus convection'

        if table2Version == 130 and indicatorOfParameter == 224:
            return 'Vertical diffusion of humidity'

        if table2Version == 130 and indicatorOfParameter == 221:
            return 'North-South gravity wave drag'

        if table2Version == 130 and indicatorOfParameter == 220:
            return 'East-West gravity wave drag'

        if table2Version == 130 and indicatorOfParameter == 219:
            return 'Vertical diffusion of meridional wind'

        if table2Version == 130 and indicatorOfParameter == 218:
            return 'Vertical diffusion of zonal wind'

        if table2Version == 130 and indicatorOfParameter == 217:
            return 'Diabatic heating by large-scale condensation'

        if table2Version == 130 and indicatorOfParameter == 216:
            return 'Diabatic heating by cumulus convection'

        if table2Version == 130 and indicatorOfParameter == 215:
            return 'Diabatic heating by vertical diffusion'

        if table2Version == 130 and indicatorOfParameter == 214:
            return 'Diabatic heating by radiation'

        if table2Version == 130 and indicatorOfParameter == 213:
            return 'Cloud fraction'

        if table2Version == 130 and indicatorOfParameter == 212:
            return 'Cloud liquid water'

        if table2Version == 130 and indicatorOfParameter == 211:
            return 'Top thermal radiation upward, clear sky'

        if table2Version == 130 and indicatorOfParameter == 210:
            return 'Top solar radiation upward, clear sky'

        if table2Version == 130 and indicatorOfParameter == 209:
            return 'Top thermal radiation upward'

        if table2Version == 130 and indicatorOfParameter == 208:
            return 'Top solar radiation upward'

        if table2Version == 129 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 129 and indicatorOfParameter == 254:
            return 'Adiabatic tendency of meridional wind gradient'

        if table2Version == 129 and indicatorOfParameter == 253:
            return 'Adiabatic tendency of zonal wind gradient'

        if table2Version == 129 and indicatorOfParameter == 252:
            return 'Adiabatic tendency of humidity gradient'

        if table2Version == 129 and indicatorOfParameter == 251:
            return 'Adiabatic tendency of temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 250:
            return 'Ice age gradient'

        if table2Version == 129 and indicatorOfParameter == 249:
            return 'Accumulated ice water tendency gradient'

        if table2Version == 129 and indicatorOfParameter == 248:
            return 'Cloud cover gradient'

        if table2Version == 129 and indicatorOfParameter == 247:
            return 'Specific cloud ice water content gradient'

        if table2Version == 129 and indicatorOfParameter == 246:
            return 'Specific cloud liquid water content gradient'

        if table2Version == 129 and indicatorOfParameter == 245:
            return 'Forecast logarithm of surface roughness for heat gradient'

        if table2Version == 129 and indicatorOfParameter == 244:
            return 'Forecast surface roughness gradient'

        if table2Version == 129 and indicatorOfParameter == 243:
            return 'Forecast albedo gradient'

        if table2Version == 129 and indicatorOfParameter == 242:
            return 'Accumulated liquid water tendency gradient'

        if table2Version == 129 and indicatorOfParameter == 241:
            return 'Accumulated cloud fraction tendency gradient'

        if table2Version == 129 and indicatorOfParameter == 240:
            return 'Large scale snowfall gradient'

        if table2Version == 129 and indicatorOfParameter == 239:
            return 'Convective snowfall gradient'

        if table2Version == 129 and indicatorOfParameter == 238:
            return 'Temperature of snow layer gradient'

        if table2Version == 129 and indicatorOfParameter == 237:
            return 'Soil wetness level 4 gradient'

        if table2Version == 129 and indicatorOfParameter == 236:
            return 'Soil temperature level 4 gradient'

        if table2Version == 129 and indicatorOfParameter == 235:
            return 'Skin temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 234:
            return 'Logarithm of surface roughness length for heat gradient'

        if table2Version == 129 and indicatorOfParameter == 233:
            return 'Apparent surface humidity gradient'

        if table2Version == 129 and indicatorOfParameter == 232:
            return 'Instantaneous moisture flux gradient'

        if table2Version == 129 and indicatorOfParameter == 231:
            return 'Instantaneous surface heat flux gradient'

        if table2Version == 129 and indicatorOfParameter == 230:
            return 'Instantaneous Y surface stress gradient'

        if table2Version == 129 and indicatorOfParameter == 229:
            return 'Instantaneous X surface stress gradient'

        if table2Version == 129 and indicatorOfParameter == 228:
            return 'Total precipitation gradient'

        if table2Version == 129 and indicatorOfParameter == 227:
            return 'Change from removal of negative humidity gradient'

        if table2Version == 129 and indicatorOfParameter == 226:
            return 'Humidity tendency by large-scale condensation gradient'

        if table2Version == 129 and indicatorOfParameter == 225:
            return 'Humidity tendency by cumulus convection gradient'

        if table2Version == 129 and indicatorOfParameter == 224:
            return 'Vertical diffusion of humidity gradient'

        if table2Version == 129 and indicatorOfParameter == 223:
            return 'Convective tendency of meridional wind gradient'

        if table2Version == 129 and indicatorOfParameter == 222:
            return 'Convective tendency of zonal wind gradient'

        if table2Version == 129 and indicatorOfParameter == 221:
            return 'North-South gravity wave drag tendency gradient'

        if table2Version == 129 and indicatorOfParameter == 220:
            return 'East-West gravity wave drag tendency gradient'

        if table2Version == 129 and indicatorOfParameter == 219:
            return 'Vertical diffusion of meridional wind gradient'

        if table2Version == 129 and indicatorOfParameter == 218:
            return 'Vertical diffusion of zonal wind gradient'

        if table2Version == 129 and indicatorOfParameter == 217:
            return 'Diabatic heating large-scale condensation gradient'

        if table2Version == 129 and indicatorOfParameter == 216:
            return 'Diabatic heating by cumulus convection gradient'

        if table2Version == 129 and indicatorOfParameter == 215:
            return 'Diabatic heating by vertical diffusion gradient'

        if table2Version == 129 and indicatorOfParameter == 214:
            return 'Diabatic heating by radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 212:
            return 'TOA incident solar radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky gradient'

        if table2Version == 129 and indicatorOfParameter == 210:
            return 'Surface net solar radiation, clear sky gradient'

        if table2Version == 129 and indicatorOfParameter == 209:
            return 'Top net thermal radiation, clear sky gradient'

        if table2Version == 129 and indicatorOfParameter == 208:
            return 'Top net solar radiation, clear sky gradient'

        if table2Version == 129 and indicatorOfParameter == 207:
            return '10 metre wind speed gradient'

        if table2Version == 129 and indicatorOfParameter == 206:
            return 'Total column ozone gradient'

        if table2Version == 129 and indicatorOfParameter == 205:
            return 'Runoff gradient'

        if table2Version == 129 and indicatorOfParameter == 204:
            return 'Precipitation analysis weights gradient'

        if table2Version == 129 and indicatorOfParameter == 203:
            return 'Ozone mass mixing ratio gradient'

        if table2Version == 129 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres since previous post-processing gradient'

        if table2Version == 129 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres since previous post-processing gradient'

        if table2Version == 129 and indicatorOfParameter == 200:
            return 'Variance of sub-gridscale orography gradient'

        if table2Version == 129 and indicatorOfParameter == 199:
            return 'Vegetation fraction gradient'

        if table2Version == 129 and indicatorOfParameter == 198:
            return 'Skin reservoir content gradient'

        if table2Version == 129 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation gradient'

        if table2Version == 129 and indicatorOfParameter == 196:
            return 'Meridional component of gravity wave stress gradient'

        if table2Version == 129 and indicatorOfParameter == 195:
            return 'Longitudinal component of gravity wave stress gradient'

        if table2Version == 129 and indicatorOfParameter == 194:
            return 'Brightness temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance gradient'

        if table2Version == 129 and indicatorOfParameter == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance gradient'

        if table2Version == 129 and indicatorOfParameter == 191:
            return 'North-South component of sub-gridscale orographic variance gradient'

        if table2Version == 129 and indicatorOfParameter == 190:
            return 'East-West component of sub-gridscale orographic variance gradient'

        if table2Version == 129 and indicatorOfParameter == 189:
            return 'Sunshine duration gradient'

        if table2Version == 129 and indicatorOfParameter == 188:
            return 'High cloud cover gradient'

        if table2Version == 129 and indicatorOfParameter == 187:
            return 'Medium cloud cover gradient'

        if table2Version == 129 and indicatorOfParameter == 186:
            return 'Low cloud cover gradient'

        if table2Version == 129 and indicatorOfParameter == 185:
            return 'Convective cloud cover gradient'

        if table2Version == 129 and indicatorOfParameter == 184:
            return 'Soil wetness level 3 gradient'

        if table2Version == 129 and indicatorOfParameter == 183:
            return 'Soil temperature level 3 gradient'

        if table2Version == 129 and indicatorOfParameter == 182:
            return 'Evaporation gradient'

        if table2Version == 129 and indicatorOfParameter == 181:
            return 'North-South surface stress gradient'

        if table2Version == 129 and indicatorOfParameter == 180:
            return 'East-West surface stress gradient'

        if table2Version == 129 and indicatorOfParameter == 179:
            return 'Top net thermal radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 178:
            return 'Top net solar radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 176:
            return 'Surface net solar radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards gradient'

        if table2Version == 129 and indicatorOfParameter == 174:
            return 'Albedo gradient'

        if table2Version == 129 and indicatorOfParameter == 173:
            return 'Surface roughness gradient'

        if table2Version == 129 and indicatorOfParameter == 172:
            return 'Land-sea mask gradient'

        if table2Version == 129 and indicatorOfParameter == 171:
            return 'Soil wetness level 2 gradient'

        if table2Version == 129 and indicatorOfParameter == 170:
            return 'Soil temperature level 2 gradient'

        if table2Version == 129 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards gradient'

        if table2Version == 129 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 167:
            return '2 metre temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 166:
            return '10 metre V wind component gradient'

        if table2Version == 129 and indicatorOfParameter == 165:
            return '10 metre U wind component gradient'

        if table2Version == 129 and indicatorOfParameter == 164:
            return 'Total cloud cover gradient'

        if table2Version == 129 and indicatorOfParameter == 163:
            return 'Slope of sub-gridscale orography gradient'

        if table2Version == 129 and indicatorOfParameter == 162:
            return 'Angle of sub-gridscale orography gradient'

        if table2Version == 129 and indicatorOfParameter == 161:
            return 'Anisotropy of sub-gridscale orography gradient'

        if table2Version == 129 and indicatorOfParameter == 160:
            return 'Standard deviation of orography gradient'

        if table2Version == 129 and indicatorOfParameter == 159:
            return 'Boundary layer height gradient'

        if table2Version == 129 and indicatorOfParameter == 158:
            return 'Tendency of surface pressure gradient'

        if table2Version == 129 and indicatorOfParameter == 157:
            return 'Relative humidity gradient'

        if table2Version == 129 and indicatorOfParameter == 156:
            return 'Height gradient'

        if table2Version == 129 and indicatorOfParameter == 155:
            return 'Divergence gradient'

        if table2Version == 129 and indicatorOfParameter == 154:
            return 'Long-wave heating rate gradient'

        if table2Version == 129 and indicatorOfParameter == 153:
            return 'Short-wave heating rate gradient'

        if table2Version == 129 and indicatorOfParameter == 152:
            return 'Logarithm of surface pressure gradient'

        if table2Version == 129 and indicatorOfParameter == 151:
            return 'Mean sea level pressure gradient'

        if table2Version == 129 and indicatorOfParameter == 150:
            return 'Top net radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 149:
            return 'Surface net radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 148:
            return 'Charnock gradient'

        if table2Version == 129 and indicatorOfParameter == 147:
            return 'Surface latent heat flux gradient'

        if table2Version == 129 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux gradient'

        if table2Version == 129 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation gradient'

        if table2Version == 129 and indicatorOfParameter == 144:
            return 'Snowfall (convective + stratiform) gradient'

        if table2Version == 129 and indicatorOfParameter == 143:
            return 'Convective precipitation gradient'

        if table2Version == 129 and indicatorOfParameter == 142:
            return 'Stratiform precipitation (Large-scale precipitation) gradient'

        if table2Version == 129 and indicatorOfParameter == 141:
            return 'Snow depth gradient'

        if table2Version == 129 and indicatorOfParameter == 140:
            return 'Soil wetness level 1 gradient'

        if table2Version == 129 and indicatorOfParameter == 139:
            return 'Soil temperature level 1 gradient'

        if table2Version == 129 and indicatorOfParameter == 138:
            return 'Vorticity (relative) gradient'

        if table2Version == 129 and indicatorOfParameter == 137:
            return 'Total column water vapour gradient'

        if table2Version == 129 and indicatorOfParameter == 136:
            return 'Total column water gradient'

        if table2Version == 129 and indicatorOfParameter == 135:
            return 'vertical velocity (pressure) gradient'

        if table2Version == 129 and indicatorOfParameter == 134:
            return 'Surface pressure gradient'

        if table2Version == 129 and indicatorOfParameter == 133:
            return 'Specific humidity gradient'

        if table2Version == 129 and indicatorOfParameter == 132:
            return 'V component of wind gradient'

        if table2Version == 129 and indicatorOfParameter == 131:
            return 'U component of wind gradient'

        if table2Version == 129 and indicatorOfParameter == 130:
            return 'Temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 129:
            return 'Geopotential gradient'

        if table2Version == 129 and indicatorOfParameter == 128:
            return 'Budget values gradient'

        if table2Version == 129 and indicatorOfParameter == 127:
            return 'Atmospheric tide gradient'

        if table2Version == 129 and indicatorOfParameter == 126:
            return 'Generic parameter for sensitive area prediction'

        if table2Version == 129 and indicatorOfParameter == 125:
            return 'Vertically integrated total energy'

        if table2Version == 129 and indicatorOfParameter == 123:
            return '10 metre wind gust in the last 6 hours gradient'

        if table2Version == 129 and indicatorOfParameter == 122:
            return 'Minimum temperature at 2 metres gradient'

        if table2Version == 129 and indicatorOfParameter == 121:
            return 'Maximum temperature at 2 metres gradient'

        if table2Version == 129 and indicatorOfParameter == 120:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 119:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 118:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 117:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 116:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 115:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 114:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 113:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 112:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 111:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 110:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 109:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 108:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 107:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 106:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 105:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 104:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 103:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 102:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 101:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 100:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 99:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 98:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 97:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 96:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 95:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 94:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 93:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 92:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 91:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 90:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 89:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 88:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 87:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 86:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 85:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 84:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 83:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 82:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 81:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 80:
            return 'Experimental product'

        if table2Version == 129 and indicatorOfParameter == 79:
            return 'Total column ice water'

        if table2Version == 129 and indicatorOfParameter == 78:
            return 'Total column liquid water'

        if table2Version == 129 and indicatorOfParameter == 71:
            return 'Biome cover, high vegetation'

        if table2Version == 129 and indicatorOfParameter == 70:
            return 'Biome cover, low vegetation'

        if table2Version == 129 and indicatorOfParameter == 69:
            return 'Minimum stomatal resistance, high vegetation'

        if table2Version == 129 and indicatorOfParameter == 68:
            return 'Minimum stomatal resistance, low vegetation'

        if table2Version == 129 and indicatorOfParameter == 67:
            return 'Leaf area index, high vegetation'

        if table2Version == 129 and indicatorOfParameter == 66:
            return 'Leaf area index, low vegetation'

        if table2Version == 129 and indicatorOfParameter == 65:
            return 'Skin temperature difference'

        if table2Version == 129 and indicatorOfParameter == 64:
            return 'Finish time for skin temperature difference'

        if table2Version == 129 and indicatorOfParameter == 63:
            return 'Start time for skin temperature difference'

        if table2Version == 129 and indicatorOfParameter == 62:
            return 'Observation count gradient'

        if table2Version == 129 and indicatorOfParameter == 61:
            return 'Total precipitation from observations gradient'

        if table2Version == 129 and indicatorOfParameter == 60:
            return 'Potential vorticity gradient'

        if table2Version == 129 and indicatorOfParameter == 59:
            return 'Convective available potential energy gradient'

        if table2Version == 129 and indicatorOfParameter == 58:
            return 'Photosynthetically active radiation at the surface gradient'

        if table2Version == 129 and indicatorOfParameter == 57:
            return 'Downward UV radiation at the surface gradient'

        if table2Version == 129 and indicatorOfParameter == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours gradient'

        if table2Version == 129 and indicatorOfParameter == 55:
            return 'Mean 2 metre temperature in the last 24 hours gradient'

        if table2Version == 129 and indicatorOfParameter == 54:
            return 'Pressure gradient'

        if table2Version == 129 and indicatorOfParameter == 53:
            return 'Montgomery potential gradient'

        if table2Version == 129 and indicatorOfParameter == 52:
            return 'Minimum 2 metre temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 51:
            return 'Maximum 2 metre temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 50:
            return 'Large-scale precipitation fraction gradient'

        if table2Version == 129 and indicatorOfParameter == 49:
            return '10 metre wind gust gradient'

        if table2Version == 129 and indicatorOfParameter == 48:
            return 'Magnitude of turbulent surface stress gradient'

        if table2Version == 129 and indicatorOfParameter == 47:
            return 'Direct solar radiation gradient'

        if table2Version == 129 and indicatorOfParameter == 46:
            return 'Solar duration gradient'

        if table2Version == 129 and indicatorOfParameter == 45:
            return 'Snowmelt gradient'

        if table2Version == 129 and indicatorOfParameter == 44:
            return 'Snow evaporation gradient'

        if table2Version == 129 and indicatorOfParameter == 43:
            return 'Soil type gradient'

        if table2Version == 129 and indicatorOfParameter == 42:
            return 'Volumetric soil water layer 4 gradient'

        if table2Version == 129 and indicatorOfParameter == 41:
            return 'Volumetric soil water layer 3 gradient'

        if table2Version == 129 and indicatorOfParameter == 40:
            return 'Volumetric soil water layer 2 gradient'

        if table2Version == 129 and indicatorOfParameter == 39:
            return 'Volumetric soil water layer 1 gradient'

        if table2Version == 129 and indicatorOfParameter == 38:
            return 'Ice surface temperature layer 4 gradient'

        if table2Version == 129 and indicatorOfParameter == 37:
            return 'Ice surface temperature layer 3 gradient'

        if table2Version == 129 and indicatorOfParameter == 36:
            return 'Ice surface temperature layer 2 gradient'

        if table2Version == 129 and indicatorOfParameter == 35:
            return 'Ice surface temperature layer 1 gradient'

        if table2Version == 129 and indicatorOfParameter == 34:
            return 'Sea surface temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 33:
            return 'Snow density gradient'

        if table2Version == 129 and indicatorOfParameter == 32:
            return 'Snow albedo gradient'

        if table2Version == 129 and indicatorOfParameter == 31:
            return 'Sea-ice cover gradient'

        if table2Version == 129 and indicatorOfParameter == 30:
            return 'Type of high vegetation gradient'

        if table2Version == 129 and indicatorOfParameter == 29:
            return 'Type of low vegetation gradient'

        if table2Version == 129 and indicatorOfParameter == 28:
            return 'High vegetation cover gradient'

        if table2Version == 129 and indicatorOfParameter == 27:
            return 'Low vegetation cover gradient'

        if table2Version == 129 and indicatorOfParameter == 26:
            return 'Lake cover gradient'

        if table2Version == 129 and indicatorOfParameter == 25:
            return 'Reserved for future unbalanced components'

        if table2Version == 129 and indicatorOfParameter == 24:
            return 'Reserved for future unbalanced components'

        if table2Version == 129 and indicatorOfParameter == 23:
            return 'Unbalanced component of divergence gradient'

        if table2Version == 129 and indicatorOfParameter == 22:
            return 'Unbalanced component of logarithm of surface pressure gradient'

        if table2Version == 129 and indicatorOfParameter == 21:
            return 'Unbalanced component of temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 14:
            return 'V component of rotational wind gradient'

        if table2Version == 129 and indicatorOfParameter == 13:
            return 'U component of rotational wind gradient'

        if table2Version == 129 and indicatorOfParameter == 12:
            return 'V component of divergent wind gradient'

        if table2Version == 129 and indicatorOfParameter == 11:
            return 'U component of divergent wind gradient'

        if table2Version == 129 and indicatorOfParameter == 5:
            return 'Saturated equivalent potential temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 4:
            return 'Equivalent potential temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 3:
            return 'Potential temperature gradient'

        if table2Version == 129 and indicatorOfParameter == 2:
            return 'Velocity potential gradient'

        if table2Version == 129 and indicatorOfParameter == 1:
            return 'Stream function gradient'

        if table2Version == 228 and indicatorOfParameter == 123:
            return 'Total totals index'

        if table2Version == 228 and indicatorOfParameter == 121:
            return 'K index'

        if table2Version == 228 and indicatorOfParameter == 109:
            return 'Ceiling'

        if table2Version == 254 and indicatorOfParameter == 48:
            return 'Total precipitation rate'

        if table2Version == 235 and indicatorOfParameter == 70:
            return 'Mean potential evaporation rate'

        if table2Version == 235 and indicatorOfParameter == 69:
            return 'Mean surface downward long-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 68:
            return 'Mean surface downward short-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 67:
            return 'Mean large-scale rain rate'

        if table2Version == 235 and indicatorOfParameter == 66:
            return 'Mean convective rain rate'

        if table2Version == 235 and indicatorOfParameter == 65:
            return 'Mean rain rate'

        if table2Version == 235 and indicatorOfParameter == 64:
            return 'Mean carbon dioxide ecosystem respiration flux'

        if table2Version == 235 and indicatorOfParameter == 63:
            return 'Mean carbon dioxide gross primary production flux'

        if table2Version == 235 and indicatorOfParameter == 62:
            return 'Mean carbon dioxide net ecosystem exchange flux'

        if table2Version == 235 and indicatorOfParameter == 61:
            return 'Mean surface diffuse short-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 60:
            return 'Mean surface diffuse short-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 59:
            return 'Mean surface direct short-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 58:
            return 'Mean surface direct short-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 57:
            return 'Mean large-scale snowfall rate'

        if table2Version == 235 and indicatorOfParameter == 56:
            return 'Mean convective snowfall rate'

        if table2Version == 235 and indicatorOfParameter == 55:
            return 'Mean total precipitation rate'

        if table2Version == 235 and indicatorOfParameter == 54:
            return 'Mean vertically integrated moisture divergence'

        if table2Version == 235 and indicatorOfParameter == 53:
            return 'Mean top downward short-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 52:
            return 'Mean surface net long-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 51:
            return 'Mean surface net short-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 50:
            return 'Mean top net long-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 49:
            return 'Mean top net short-wave radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 48:
            return 'Mean runoff rate'

        if table2Version == 235 and indicatorOfParameter == 47:
            return 'Mean gravity wave dissipation'

        if table2Version == 235 and indicatorOfParameter == 46:
            return 'Mean northward gravity wave surface stress'

        if table2Version == 235 and indicatorOfParameter == 45:
            return 'Mean eastward gravity wave surface stress'

        if table2Version == 235 and indicatorOfParameter == 44:
            return 'Sunshine duration fraction'

        if table2Version == 235 and indicatorOfParameter == 43:
            return 'Mean evaporation rate'

        if table2Version == 235 and indicatorOfParameter == 42:
            return 'Mean northward turbulent surface stress'

        if table2Version == 235 and indicatorOfParameter == 41:
            return 'Mean eastward turbulent surface stress'

        if table2Version == 235 and indicatorOfParameter == 40:
            return 'Mean top net long-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 39:
            return 'Mean top net short-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 38:
            return 'Mean surface net long-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 37:
            return 'Mean surface net short-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 36:
            return 'Mean surface downward long-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 35:
            return 'Mean surface downward short-wave radiation flux'

        if table2Version == 235 and indicatorOfParameter == 34:
            return 'Mean surface latent heat flux'

        if table2Version == 235 and indicatorOfParameter == 33:
            return 'Mean surface sensible heat flux'

        if table2Version == 235 and indicatorOfParameter == 32:
            return 'Mean boundary layer dissipation'

        if table2Version == 235 and indicatorOfParameter == 31:
            return 'Mean snowfall rate'

        if table2Version == 235 and indicatorOfParameter == 30:
            return 'Mean convective precipitation rate'

        if table2Version == 235 and indicatorOfParameter == 29:
            return 'Mean large-scale precipitation rate'

        if table2Version == 235 and indicatorOfParameter == 28:
            return 'Mean surface photosynthetically active radiation flux'

        if table2Version == 235 and indicatorOfParameter == 27:
            return 'Mean surface downward UV radiation flux'

        if table2Version == 235 and indicatorOfParameter == 26:
            return 'Mean large-scale precipitation fraction'

        if table2Version == 235 and indicatorOfParameter == 25:
            return 'Mean magnitude of turbulent surface stress'

        if table2Version == 235 and indicatorOfParameter == 24:
            return 'Mean snowmelt rate'

        if table2Version == 235 and indicatorOfParameter == 23:
            return 'Mean snow evaporation rate'

        if table2Version == 235 and indicatorOfParameter == 22:
            return 'Mean surface photosynthetically active radiation flux, clear sky'

        if table2Version == 235 and indicatorOfParameter == 21:
            return 'Mean sub-surface runoff rate'

        if table2Version == 235 and indicatorOfParameter == 20:
            return 'Mean surface runoff rate'

        if table2Version == 230 and indicatorOfParameter == 251:
            return 'Potential evaporation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 240:
            return 'Large-scale snowfall (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 239:
            return 'Convective snowfall (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 228:
            return 'Total precipitation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 216:
            return 'Accumulated freezing rain (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 213:
            return 'Vertically integrated moisture divergence (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 174:
            return 'Albedo (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 130:
            return 'Surface thermal radiation downward clear-sky (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 129:
            return 'Surface solar radiation downward clear-sky (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 82:
            return 'Accumulated Carbon Dioxide Ecosystem Respiration (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 81:
            return 'Accumulated Carbon Dioxide Gross Primary Production (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 80:
            return 'Accumulated Carbon Dioxide Net Ecosystem Exchange (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 50:
            return 'Large-scale precipitation fraction (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 47:
            return 'Direct solar radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 22:
            return 'Clear-sky direct solar radiation at surface (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 21:
            return 'Total sky direct solar radiation at surface (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 20:
            return 'Clear sky surface photosynthetically active radiation (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 9:
            return 'Sub-surface runoff (variable resolution)'

        if table2Version == 230 and indicatorOfParameter == 8:
            return 'Surface runoff (variable resolution)'

        if table2Version == 228 and indicatorOfParameter == 252:
            return 'Irrigation'

        if table2Version == 228 and indicatorOfParameter == 251:
            return 'Potential evaporation'

        if table2Version == 228 and indicatorOfParameter == 250:
            return 'Irrigation fraction'

        if table2Version == 228 and indicatorOfParameter == 249:
            return '100 metre wind speed'

        if table2Version == 228 and indicatorOfParameter == 245:
            return 'Surface albedo of diffuse radiation'

        if table2Version == 228 and indicatorOfParameter == 244:
            return 'Surface albedo of direct radiation'

        if table2Version == 228 and indicatorOfParameter == 243:
            return 'Surface solar radiation diffuse clear-sky'

        if table2Version == 228 and indicatorOfParameter == 242:
            return 'Surface solar radiation diffuse total sky'

        if table2Version == 228 and indicatorOfParameter == 241:
            return '200 metre wind speed'

        if table2Version == 228 and indicatorOfParameter == 240:
            return '200 metre V wind component'

        if table2Version == 228 and indicatorOfParameter == 239:
            return '200 metre U wind component'

        if table2Version == 228 and indicatorOfParameter == 230:
            return 'SMOS second Brightness Temperature Bias Correction parameter'

        if table2Version == 228 and indicatorOfParameter == 229:
            return 'SMOS first Brightness Temperature Bias Correction parameter'

        if table2Version == 228 and indicatorOfParameter == 227:
            return 'Minimum total precipitation rate since previous post-processing'

        if table2Version == 228 and indicatorOfParameter == 226:
            return 'Maximum total precipitation rate since previous post-processing'

        if table2Version == 228 and indicatorOfParameter == 225:
            return 'Minimum total precipitation rate in the last 6 hours'

        if table2Version == 228 and indicatorOfParameter == 224:
            return 'Maximum total precipitation rate in the last 6 hours'

        if table2Version == 228 and indicatorOfParameter == 223:
            return 'Minimum total precipitation rate in the last 3 hours'

        if table2Version == 228 and indicatorOfParameter == 222:
            return 'Maximum total precipitation rate in the last 3 hours'

        if table2Version == 228 and indicatorOfParameter == 221:
            return 'Large scale snowfall rate water equivalent'

        if table2Version == 228 and indicatorOfParameter == 220:
            return 'Convective snowfall rate water equivalent'

        if table2Version == 228 and indicatorOfParameter == 219:
            return 'Large scale rain rate'

        if table2Version == 228 and indicatorOfParameter == 218:
            return 'Convective rain rate'

        if table2Version == 228 and indicatorOfParameter == 217:
            return 'Instantaneous large-scale surface precipitation fraction'

        if table2Version == 228 and indicatorOfParameter == 216:
            return 'Accumulated freezing rain'

        if table2Version == 228 and indicatorOfParameter == 130:
            return 'Surface thermal radiation downward clear-sky'

        if table2Version == 228 and indicatorOfParameter == 129:
            return 'Surface solar radiation downward clear-sky'

        if table2Version == 228 and indicatorOfParameter == 94:
            return 'Ice temperature'

        if table2Version == 228 and indicatorOfParameter == 93:
            return 'Volumetric soil moisture'

        if table2Version == 228 and indicatorOfParameter == 92:
            return 'Soil texture fraction'

        if table2Version == 228 and indicatorOfParameter == 91:
            return 'Canopy cover fraction'

        if table2Version == 228 and indicatorOfParameter == 90:
            return 'Total column snow water'

        if table2Version == 228 and indicatorOfParameter == 89:
            return 'Total column rain water'

        if table2Version == 228 and indicatorOfParameter == 88:
            return 'Total column supercooled liquid water'

        if table2Version == 228 and indicatorOfParameter == 85:
            return 'Flux of Carbon Dioxide Ecosystem Respiration'

        if table2Version == 228 and indicatorOfParameter == 84:
            return 'Flux of Carbon Dioxide Gross Primary Production'

        if table2Version == 228 and indicatorOfParameter == 83:
            return 'Flux of Carbon Dioxide Net Ecosystem Exchange'

        if table2Version == 228 and indicatorOfParameter == 82:
            return 'Accumulated Carbon Dioxide Ecosystem Respiration'

        if table2Version == 228 and indicatorOfParameter == 81:
            return 'Accumulated Carbon Dioxide Gross Primary Production'

        if table2Version == 228 and indicatorOfParameter == 80:
            return 'Accumulated Carbon Dioxide Net Ecosystem Exchange'

        if table2Version == 228 and indicatorOfParameter == 79:
            return 'Rec coefficient from Biogenic Flux Adjustment System'

        if table2Version == 228 and indicatorOfParameter == 78:
            return 'GPP coefficient from Biogenic Flux Adjustment System'

        if table2Version == 228 and indicatorOfParameter == 74:
            return 'SMOS observation time for the satellite soil moisture data'

        if table2Version == 228 and indicatorOfParameter == 73:
            return 'SMOS number of observations per grid point'

        if table2Version == 228 and indicatorOfParameter == 72:
            return 'SMOS radio frequency interference probability'

        if table2Version == 228 and indicatorOfParameter == 71:
            return 'SMOS observed soil moisture uncertainty retrieved using neural network'

        if table2Version == 228 and indicatorOfParameter == 70:
            return 'SMOS observed soil moisture retrieved using neural network'

        if table2Version == 228 and indicatorOfParameter == 53:
            return 'Averaged cloud-to-ground lightning flash density in the last hour'

        if table2Version == 228 and indicatorOfParameter == 52:
            return 'Instantaneous cloud-to-ground lightning flash density'

        if table2Version == 228 and indicatorOfParameter == 51:
            return 'Averaged total lightning flash density in the last hour'

        if table2Version == 228 and indicatorOfParameter == 50:
            return 'Instantaneous total lightning flash density'

        if table2Version == 228 and indicatorOfParameter == 48:
            return 'Height of one-degree wet-bulb temperature'

        if table2Version == 228 and indicatorOfParameter == 47:
            return 'Height of zero-degree wet-bulb temperature'

        if table2Version == 228 and indicatorOfParameter == 46:
            return 'Height of convective cloud top'

        if table2Version == 228 and indicatorOfParameter == 44:
            return 'Convective available potential energy shear'

        if table2Version == 228 and indicatorOfParameter == 43:
            return 'Soil wetness index in layer 4'

        if table2Version == 228 and indicatorOfParameter == 42:
            return 'Soil wetness index in layer 3'

        if table2Version == 228 and indicatorOfParameter == 41:
            return 'Soil wetness index in layer 2'

        if table2Version == 228 and indicatorOfParameter == 40:
            return 'Soil wetness index in layer 1'

        if table2Version == 228 and indicatorOfParameter == 37:
            return '2 metre relative humidity with respect to water'

        if table2Version == 228 and indicatorOfParameter == 29:
            return 'Instantaneous 10 metre wind gust'

        if table2Version == 228 and indicatorOfParameter == 28:
            return '10 metre wind gust in the last 3 hours'

        if table2Version == 228 and indicatorOfParameter == 27:
            return 'Minimum temperature at 2 metres in the last 3 hours'

        if table2Version == 228 and indicatorOfParameter == 26:
            return 'Maximum temperature at 2 metres in the last 3 hours'

        if table2Version == 228 and indicatorOfParameter == 25:
            return 'Horizontal visibility'

        if table2Version == 228 and indicatorOfParameter == 24:
            return '0 degrees C isothermal level (atm)'

        if table2Version == 228 and indicatorOfParameter == 23:
            return 'Cloud base height'

        if table2Version == 228 and indicatorOfParameter == 22:
            return 'Clear-sky direct solar radiation at surface'

        if table2Version == 228 and indicatorOfParameter == 21:
            return 'Total sky direct solar radiation at surface'

        if table2Version == 228 and indicatorOfParameter == 20:
            return '-10 degrees C isothermal level (atm)'

        if table2Version == 221 and indicatorOfParameter == 56:
            return 'Nitrogen oxides Transp deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 55:
            return 'HYPROPO2 deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 54:
            return 'IC3H7O2 deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 53:
            return 'Acetone product deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 52:
            return 'Acetone deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 51:
            return 'Nitrate deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 50:
            return 'Methacrolein MVK  deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 49:
            return 'Terpenes deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 48:
            return 'Propene deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 47:
            return 'Propane deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 46:
            return 'Ethanol deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 45:
            return 'Ethane deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 44:
            return 'Methacrylic acid deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 43:
            return 'Formic acid deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 42:
            return 'Methanol deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 41:
            return 'Polar stratospheric cloud deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 40:
            return 'Amine deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 39:
            return 'NO to alkyl nitrate operator deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 38:
            return 'NO to NO2 operator deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 37:
            return 'PAR budget corrector deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 36:
            return 'Organic ethers deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 35:
            return 'Peroxy acetyl radical deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 34:
            return 'Pernitric acid deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 33:
            return 'Dinitrogen pentoxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 32:
            return 'Nitrate radical deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 31:
            return 'Nitrogen dioxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 30:
            return 'Hydroxyl radical deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 29:
            return 'Methylperoxy radical deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 28:
            return 'Hydroperoxy radical deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 27:
            return 'Nitrogen monoxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 26:
            return 'Lead deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 25:
            return 'Radon deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 24:
            return 'Stratospheric ozone deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 23:
            return 'Methyl glyoxal deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 22:
            return 'Methane sulfonic acid deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 21:
            return 'Ammonium deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 20:
            return 'Sulfate deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 19:
            return 'Ammonia deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 18:
            return 'Dimethyl sulfide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 17:
            return 'Sulfur dioxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 16:
            return 'Isoprene deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 15:
            return 'Organic nitrates deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 14:
            return 'Peroxides deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 13:
            return 'Peroxyacetyl nitrate deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 12:
            return 'Aldehydes deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 11:
            return 'Olefins deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 10:
            return 'Ethene deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 9:
            return 'Paraffins deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 8:
            return 'Formaldehyde deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 7:
            return 'Methyl peroxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 6:
            return 'Nitric acid deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 5:
            return 'Carbon monoxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 4:
            return 'Methane deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 3:
            return 'Hydrogen peroxide deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 2:
            return 'Nitrogen oxides deposition velocity'

        if table2Version == 221 and indicatorOfParameter == 1:
            return 'Ozone deposition velocity'

        if table2Version == 219 and indicatorOfParameter == 56:
            return 'Nitrogen oxides Transp emissions'

        if table2Version == 219 and indicatorOfParameter == 55:
            return 'HYPROPO2 emissions'

        if table2Version == 219 and indicatorOfParameter == 54:
            return 'IC3H7O2 emissions'

        if table2Version == 219 and indicatorOfParameter == 53:
            return 'Acetone product emissions'

        if table2Version == 219 and indicatorOfParameter == 52:
            return 'Acetone emissions'

        if table2Version == 219 and indicatorOfParameter == 51:
            return 'Nitrate emissions'

        if table2Version == 219 and indicatorOfParameter == 50:
            return 'Methacrolein MVK  emissions'

        if table2Version == 219 and indicatorOfParameter == 49:
            return 'Terpenes emissions'

        if table2Version == 219 and indicatorOfParameter == 48:
            return 'Propene emissions'

        if table2Version == 219 and indicatorOfParameter == 47:
            return 'Propane emissions'

        if table2Version == 219 and indicatorOfParameter == 46:
            return 'Ethanol emissions'

        if table2Version == 219 and indicatorOfParameter == 45:
            return 'Ethane emissions'

        if table2Version == 219 and indicatorOfParameter == 44:
            return 'Methacrylic acid emissions'

        if table2Version == 219 and indicatorOfParameter == 43:
            return 'Formic acid emissions'

        if table2Version == 219 and indicatorOfParameter == 42:
            return 'Methanol emissions'

        if table2Version == 219 and indicatorOfParameter == 41:
            return 'Polar stratospheric cloud emissions'

        if table2Version == 219 and indicatorOfParameter == 40:
            return 'Amine emissions'

        if table2Version == 219 and indicatorOfParameter == 39:
            return 'NO to alkyl nitrate operator emissions'

        if table2Version == 219 and indicatorOfParameter == 38:
            return 'NO to NO2 operator emissions'

        if table2Version == 219 and indicatorOfParameter == 37:
            return 'PAR budget corrector emissions'

        if table2Version == 219 and indicatorOfParameter == 36:
            return 'Organic ethers emissions'

        if table2Version == 219 and indicatorOfParameter == 35:
            return 'Peroxy acetyl radical emissions'

        if table2Version == 219 and indicatorOfParameter == 34:
            return 'Pernitric acid emissions'

        if table2Version == 219 and indicatorOfParameter == 33:
            return 'Dinitrogen pentoxide emissions'

        if table2Version == 219 and indicatorOfParameter == 32:
            return 'Nitrate radical emissions'

        if table2Version == 219 and indicatorOfParameter == 31:
            return 'Nitrogen dioxide emissions'

        if table2Version == 219 and indicatorOfParameter == 30:
            return 'Hydroxyl radical emissions'

        if table2Version == 219 and indicatorOfParameter == 29:
            return 'Methylperoxy radical emissions'

        if table2Version == 219 and indicatorOfParameter == 28:
            return 'Hydroperoxy radical emissions'

        if table2Version == 219 and indicatorOfParameter == 27:
            return 'Nitrogen monoxide emissions'

        if table2Version == 219 and indicatorOfParameter == 26:
            return 'Lead emissions'

        if table2Version == 219 and indicatorOfParameter == 25:
            return 'Radon emissions'

        if table2Version == 219 and indicatorOfParameter == 24:
            return 'Stratospheric ozone emissions'

        if table2Version == 219 and indicatorOfParameter == 23:
            return 'Methyl glyoxal emissions'

        if table2Version == 219 and indicatorOfParameter == 22:
            return 'Methane sulfonic acid emissions'

        if table2Version == 219 and indicatorOfParameter == 21:
            return 'Ammonium emissions'

        if table2Version == 219 and indicatorOfParameter == 20:
            return 'Sulfate emissions'

        if table2Version == 219 and indicatorOfParameter == 19:
            return 'Ammonia emissions'

        if table2Version == 219 and indicatorOfParameter == 18:
            return 'Dimethyl sulfide emissions'

        if table2Version == 219 and indicatorOfParameter == 17:
            return 'Sulfur dioxide emissions'

        if table2Version == 219 and indicatorOfParameter == 16:
            return 'Isoprene emissions'

        if table2Version == 219 and indicatorOfParameter == 15:
            return 'Organic nitrates emissions'

        if table2Version == 219 and indicatorOfParameter == 14:
            return 'Peroxides emissions'

        if table2Version == 219 and indicatorOfParameter == 13:
            return 'Peroxyacetyl nitrate emissions'

        if table2Version == 219 and indicatorOfParameter == 12:
            return 'Aldehydes emissions'

        if table2Version == 219 and indicatorOfParameter == 11:
            return 'Olefins emissions'

        if table2Version == 219 and indicatorOfParameter == 10:
            return 'Ethene emissions'

        if table2Version == 219 and indicatorOfParameter == 9:
            return 'Paraffins emissions'

        if table2Version == 219 and indicatorOfParameter == 8:
            return 'Formaldehyde emissions'

        if table2Version == 219 and indicatorOfParameter == 7:
            return 'Methyl peroxide emissions'

        if table2Version == 219 and indicatorOfParameter == 6:
            return 'Nitric acid emissions'

        if table2Version == 219 and indicatorOfParameter == 5:
            return 'Carbon monoxide emissions'

        if table2Version == 219 and indicatorOfParameter == 4:
            return 'Methane emissions'

        if table2Version == 219 and indicatorOfParameter == 3:
            return 'Hydrogen peroxide emissions'

        if table2Version == 219 and indicatorOfParameter == 2:
            return 'Nitrogen oxides emissions'

        if table2Version == 219 and indicatorOfParameter == 1:
            return 'Ozone emissions'

        if table2Version == 218 and indicatorOfParameter == 56:
            return 'Total column nitrogen oxides Transp'

        if table2Version == 218 and indicatorOfParameter == 55:
            return 'Total column HYPROPO2'

        if table2Version == 218 and indicatorOfParameter == 54:
            return 'Total column IC3H7O2'

        if table2Version == 218 and indicatorOfParameter == 53:
            return 'Total column acetone product'

        if table2Version == 218 and indicatorOfParameter == 52:
            return 'Total column acetone'

        if table2Version == 218 and indicatorOfParameter == 51:
            return 'Total column nitrate'

        if table2Version == 218 and indicatorOfParameter == 50:
            return 'Total column methacrolein MVK'

        if table2Version == 218 and indicatorOfParameter == 49:
            return 'Total column terpenes'

        if table2Version == 218 and indicatorOfParameter == 48:
            return 'Total column propene'

        if table2Version == 218 and indicatorOfParameter == 47:
            return 'Total column propane'

        if table2Version == 218 and indicatorOfParameter == 46:
            return 'Total column ethanol'

        if table2Version == 218 and indicatorOfParameter == 45:
            return 'Total column  ethane'

        if table2Version == 218 and indicatorOfParameter == 44:
            return 'Total column  methacrylic acid'

        if table2Version == 218 and indicatorOfParameter == 43:
            return 'Total column formic acid'

        if table2Version == 218 and indicatorOfParameter == 42:
            return 'Total column methanol'

        if table2Version == 218 and indicatorOfParameter == 41:
            return 'Total column  polar stratospheric cloud'

        if table2Version == 218 and indicatorOfParameter == 40:
            return 'Total column amine'

        if table2Version == 218 and indicatorOfParameter == 39:
            return 'Total column NO to alkyl nitrate operator'

        if table2Version == 218 and indicatorOfParameter == 38:
            return 'Total column NO to NO2 operator'

        if table2Version == 218 and indicatorOfParameter == 37:
            return 'Total column PAR budget corrector'

        if table2Version == 218 and indicatorOfParameter == 36:
            return 'Total column  organic ethers'

        if table2Version == 218 and indicatorOfParameter == 35:
            return 'Total column peroxy acetyl radical'

        if table2Version == 218 and indicatorOfParameter == 34:
            return 'Total column pernitric acid'

        if table2Version == 218 and indicatorOfParameter == 33:
            return 'Total column dinitrogen pentoxide'

        if table2Version == 218 and indicatorOfParameter == 32:
            return 'Total column nitrate radical'

        if table2Version == 218 and indicatorOfParameter == 30:
            return 'Total column hydroxyl radical'

        if table2Version == 218 and indicatorOfParameter == 29:
            return 'Total column methylperoxy radical'

        if table2Version == 218 and indicatorOfParameter == 28:
            return 'Total column hydroperoxy radical'

        if table2Version == 218 and indicatorOfParameter == 27:
            return 'Total column nitrogen monoxide'

        if table2Version == 218 and indicatorOfParameter == 26:
            return 'Total column  lead'

        if table2Version == 218 and indicatorOfParameter == 24:
            return 'Total column stratospheric ozone'

        if table2Version == 218 and indicatorOfParameter == 23:
            return 'Total column methyl glyoxal'

        if table2Version == 218 and indicatorOfParameter == 22:
            return 'Total column  methane sulfonic acid'

        if table2Version == 218 and indicatorOfParameter == 21:
            return 'Total column ammonium'

        if table2Version == 218 and indicatorOfParameter == 20:
            return 'Total column  sulfate'

        if table2Version == 218 and indicatorOfParameter == 19:
            return 'Total column ammonia'

        if table2Version == 218 and indicatorOfParameter == 18:
            return 'Total column dimethyl sulfide'

        if table2Version == 218 and indicatorOfParameter == 16:
            return 'Total column  isoprene'

        if table2Version == 218 and indicatorOfParameter == 15:
            return 'Total column organic nitrates'

        if table2Version == 218 and indicatorOfParameter == 14:
            return 'Total column peroxides'

        if table2Version == 218 and indicatorOfParameter == 13:
            return 'Total column  peroxyacetyl nitrate'

        if table2Version == 218 and indicatorOfParameter == 12:
            return 'Total column aldehydes'

        if table2Version == 218 and indicatorOfParameter == 11:
            return 'Total column olefins'

        if table2Version == 218 and indicatorOfParameter == 10:
            return 'Total column ethene'

        if table2Version == 218 and indicatorOfParameter == 9:
            return 'Total column paraffins'

        if table2Version == 218 and indicatorOfParameter == 7:
            return 'Total column methyl peroxide'

        if table2Version == 218 and indicatorOfParameter == 6:
            return 'Total column nitric acid'

        if table2Version == 218 and indicatorOfParameter == 4:
            return 'Total column methane'

        if table2Version == 218 and indicatorOfParameter == 3:
            return 'Total column hydrogen peroxide'

        if table2Version == 217 and indicatorOfParameter == 56:
            return 'Nitrogen oxides Transp'

        if table2Version == 217 and indicatorOfParameter == 55:
            return 'HYPROPO2'

        if table2Version == 217 and indicatorOfParameter == 54:
            return 'IC3H7O2'

        if table2Version == 217 and indicatorOfParameter == 53:
            return 'Acetone product'

        if table2Version == 217 and indicatorOfParameter == 52:
            return 'Acetone'

        if table2Version == 217 and indicatorOfParameter == 51:
            return 'Nitrate'

        if table2Version == 217 and indicatorOfParameter == 50:
            return 'Methacrolein MVK'

        if table2Version == 217 and indicatorOfParameter == 49:
            return 'Terpenes'

        if table2Version == 217 and indicatorOfParameter == 48:
            return 'Propene'

        if table2Version == 217 and indicatorOfParameter == 47:
            return 'Propane'

        if table2Version == 217 and indicatorOfParameter == 46:
            return 'Ethanol'

        if table2Version == 217 and indicatorOfParameter == 45:
            return 'Ethane'

        if table2Version == 217 and indicatorOfParameter == 44:
            return 'Methacrylic acid'

        if table2Version == 217 and indicatorOfParameter == 43:
            return 'Formic acid'

        if table2Version == 217 and indicatorOfParameter == 42:
            return 'Methanol'

        if table2Version == 217 and indicatorOfParameter == 41:
            return 'Polar stratospheric cloud'

        if table2Version == 217 and indicatorOfParameter == 40:
            return 'Amine'

        if table2Version == 217 and indicatorOfParameter == 39:
            return 'NO to alkyl nitrate operator'

        if table2Version == 217 and indicatorOfParameter == 38:
            return 'NO to NO2 operator'

        if table2Version == 217 and indicatorOfParameter == 37:
            return 'PAR budget corrector'

        if table2Version == 217 and indicatorOfParameter == 36:
            return 'Organic ethers'

        if table2Version == 217 and indicatorOfParameter == 35:
            return 'Peroxy acetyl radical'

        if table2Version == 217 and indicatorOfParameter == 34:
            return 'Pernitric acid'

        if table2Version == 217 and indicatorOfParameter == 33:
            return 'Dinitrogen pentoxide'

        if table2Version == 217 and indicatorOfParameter == 32:
            return 'Nitrate radical'

        if table2Version == 217 and indicatorOfParameter == 30:
            return 'Hydroxyl radical'

        if table2Version == 217 and indicatorOfParameter == 29:
            return 'Methylperoxy radical'

        if table2Version == 217 and indicatorOfParameter == 28:
            return 'Hydroperoxy radical'

        if table2Version == 217 and indicatorOfParameter == 27:
            return 'Nitrogen monoxide'

        if table2Version == 217 and indicatorOfParameter == 26:
            return 'Lead'

        if table2Version == 217 and indicatorOfParameter == 24:
            return 'Stratospheric ozone'

        if table2Version == 217 and indicatorOfParameter == 23:
            return 'Methyl glyoxal'

        if table2Version == 217 and indicatorOfParameter == 22:
            return 'Methane sulfonic acid'

        if table2Version == 217 and indicatorOfParameter == 21:
            return 'Ammonium'

        if table2Version == 217 and indicatorOfParameter == 20:
            return 'Sulfate'

        if table2Version == 217 and indicatorOfParameter == 19:
            return 'Ammonia'

        if table2Version == 217 and indicatorOfParameter == 18:
            return 'Dimethyl sulfide'

        if table2Version == 217 and indicatorOfParameter == 16:
            return 'Isoprene'

        if table2Version == 217 and indicatorOfParameter == 15:
            return 'Organic nitrates'

        if table2Version == 217 and indicatorOfParameter == 14:
            return 'Peroxides'

        if table2Version == 217 and indicatorOfParameter == 13:
            return 'Peroxyacetyl nitrate'

        if table2Version == 217 and indicatorOfParameter == 12:
            return 'Aldehydes'

        if table2Version == 217 and indicatorOfParameter == 11:
            return 'Olefins'

        if table2Version == 217 and indicatorOfParameter == 10:
            return 'Ethene'

        if table2Version == 217 and indicatorOfParameter == 9:
            return 'Paraffins'

        if table2Version == 217 and indicatorOfParameter == 7:
            return 'Methyl peroxide'

        if table2Version == 217 and indicatorOfParameter == 6:
            return 'Nitric acid'

        if table2Version == 217 and indicatorOfParameter == 4:
            return 'Methane (chemistry)'

        if table2Version == 217 and indicatorOfParameter == 3:
            return 'Hydrogen peroxide'

        if table2Version == 216 and indicatorOfParameter == 255:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 254:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 253:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 252:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 251:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 250:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 249:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 248:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 247:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 246:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 245:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 244:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 243:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 242:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 241:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 240:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 239:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 238:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 237:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 236:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 235:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 234:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 233:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 232:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 231:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 230:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 229:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 228:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 227:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 226:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 225:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 224:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 223:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 222:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 221:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 220:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 219:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 218:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 217:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 216:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 215:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 214:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 213:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 212:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 211:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 210:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 209:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 208:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 207:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 206:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 205:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 204:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 203:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 202:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 201:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 200:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 199:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 198:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 197:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 196:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 195:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 194:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 193:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 192:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 191:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 190:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 189:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 188:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 187:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 186:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 185:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 184:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 183:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 182:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 181:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 180:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 179:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 178:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 177:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 176:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 175:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 174:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 173:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 172:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 171:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 170:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 169:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 168:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 167:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 166:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 165:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 164:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 163:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 162:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 161:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 160:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 159:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 158:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 157:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 156:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 155:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 154:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 153:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 152:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 151:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 150:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 149:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 148:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 147:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 146:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 145:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 144:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 143:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 142:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 141:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 140:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 139:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 138:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 137:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 136:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 135:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 134:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 133:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 132:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 131:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 130:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 129:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 128:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 127:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 126:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 125:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 124:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 123:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 122:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 121:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 120:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 119:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 118:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 117:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 116:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 115:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 114:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 113:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 112:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 111:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 110:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 109:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 108:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 107:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 106:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 105:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 104:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 103:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 102:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 101:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 100:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 99:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 98:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 97:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 96:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 95:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 94:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 93:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 92:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 91:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 90:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 89:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 88:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 87:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 86:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 85:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 84:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 83:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 82:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 81:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 80:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 79:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 78:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 77:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 76:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 75:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 74:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 73:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 72:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 71:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 70:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 69:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 68:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 67:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 66:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 65:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 64:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 63:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 62:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 61:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 60:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 59:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 58:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 57:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 56:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 55:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 54:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 53:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 52:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 51:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 50:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 49:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 48:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 47:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 46:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 45:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 44:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 43:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 42:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 41:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 40:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 39:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 38:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 37:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 36:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 35:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 34:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 33:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 32:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 31:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 30:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 29:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 28:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 27:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 26:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 25:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 24:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 23:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 22:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 21:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 20:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 19:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 18:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 17:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 16:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 15:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 14:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 13:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 12:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 11:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 10:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 9:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 8:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 7:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 6:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 5:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 4:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 3:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 2:
            return 'Experimental product'

        if table2Version == 216 and indicatorOfParameter == 1:
            return 'Experimental product'

        if table2Version == 215 and indicatorOfParameter == 211:
            return 'Vertically integrated mass of ammonium aerosol'

        if table2Version == 215 and indicatorOfParameter == 210:
            return 'Negative fixer of ammonium aerosol'

        if table2Version == 215 and indicatorOfParameter == 209:
            return 'Wet deposition of ammonium aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 208:
            return 'Wet deposition of ammonium aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 207:
            return 'Sedimentation of ammonium aerosol'

        if table2Version == 215 and indicatorOfParameter == 206:
            return 'Dry deposition of ammonium aerosol'

        if table2Version == 215 and indicatorOfParameter == 205:
            return 'Source/gain of ammonium aerosol'

        if table2Version == 215 and indicatorOfParameter == 204:
            return 'Coarse-mode nitrate aerosol optical depth at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 203:
            return 'Fine-mode nitrate aerosol optical depth at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 202:
            return 'Vertically integrated mass of coarse-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 201:
            return 'Vertically integrated mass of fine-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 200:
            return 'Negative fixer of coarse-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 199:
            return 'Negative fixer of fine-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 198:
            return 'Wet deposition of coarse-mode nitrate aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 197:
            return 'Wet deposition of fine-mode nitrate aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 196:
            return 'Wet deposition of coarse-mode nitrate aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 195:
            return 'Wet deposition of fine-mode nitrate aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 194:
            return 'Sedimentation of coarse-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 193:
            return 'Sedimentation of fine-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 192:
            return 'Dry deposition of coarse-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 191:
            return 'Dry deposition of fine-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 190:
            return 'Source/gain of coarse-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 189:
            return 'Source/gain of fine-mode nitrate aerosol'

        if table2Version == 215 and indicatorOfParameter == 188:
            return 'Aerosol backscatter coefficient at 1064 nm (from ground)'

        if table2Version == 215 and indicatorOfParameter == 187:
            return 'Aerosol backscatter coefficient at 532 nm (from ground)'

        if table2Version == 215 and indicatorOfParameter == 186:
            return 'Aerosol backscatter coefficient at 355 nm (from ground)'

        if table2Version == 215 and indicatorOfParameter == 185:
            return 'Aerosol backscatter coefficient at 1064 nm (from top of atmosphere)'

        if table2Version == 215 and indicatorOfParameter == 184:
            return 'Aerosol backscatter coefficient at 532 nm (from top of atmosphere)'

        if table2Version == 215 and indicatorOfParameter == 183:
            return 'Aerosol backscatter coefficient at 355 nm (from top of atmosphere)'

        if table2Version == 215 and indicatorOfParameter == 182:
            return 'Aerosol extinction coefficient at 1064 nm'

        if table2Version == 215 and indicatorOfParameter == 181:
            return 'Aerosol extinction coefficient at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 180:
            return 'Aerosol extinction coefficient at 355 nm'

        if table2Version == 215 and indicatorOfParameter == 179:
            return 'Asymmetry factor at 2130 nm'

        if table2Version == 215 and indicatorOfParameter == 178:
            return 'Single scattering albedo at 2130 nm'

        if table2Version == 215 and indicatorOfParameter == 177:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 2130 nm'

        if table2Version == 215 and indicatorOfParameter == 176:
            return 'Total absorption aerosol optical depth at 2130 nm'

        if table2Version == 215 and indicatorOfParameter == 175:
            return 'Sulphur dioxide optical depth'

        if table2Version == 215 and indicatorOfParameter == 174:
            return 'Vertically integrated mass of sulphur dioxide'

        if table2Version == 215 and indicatorOfParameter == 173:
            return 'Negative fixer of sulphur dioxide'

        if table2Version == 215 and indicatorOfParameter == 172:
            return 'Wet deposition of sulphur dioxide by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 171:
            return 'Wet deposition of sulphur dioxide by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 170:
            return 'Sedimentation of sulphur dioxide'

        if table2Version == 215 and indicatorOfParameter == 169:
            return 'Dry deposition of sulphur dioxide'

        if table2Version == 215 and indicatorOfParameter == 168:
            return 'Source/gain of sulphur dioxide'

        if table2Version == 215 and indicatorOfParameter == 167:
            return 'Asymmetry factor at 1640 nm'

        if table2Version == 215 and indicatorOfParameter == 166:
            return 'Asymmetry factor at 1240 nm'

        if table2Version == 215 and indicatorOfParameter == 165:
            return 'Asymmetry factor at 1064 nm'

        if table2Version == 215 and indicatorOfParameter == 164:
            return 'Asymmetry factor at 1020 nm'

        if table2Version == 215 and indicatorOfParameter == 163:
            return 'Asymmetry factor at 865 nm'

        if table2Version == 215 and indicatorOfParameter == 162:
            return 'Asymmetry factor at 858 nm'

        if table2Version == 215 and indicatorOfParameter == 161:
            return 'Asymmetry factor at 800 nm'

        if table2Version == 215 and indicatorOfParameter == 160:
            return 'Asymmetry factor at 670 nm'

        if table2Version == 215 and indicatorOfParameter == 159:
            return 'Asymmetry factor at 645 nm'

        if table2Version == 215 and indicatorOfParameter == 158:
            return 'Asymmetry factor at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 157:
            return 'Asymmetry factor at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 156:
            return 'Asymmetry factor at 500 nm'

        if table2Version == 215 and indicatorOfParameter == 155:
            return 'Asymmetry factor at 469 nm'

        if table2Version == 215 and indicatorOfParameter == 154:
            return 'Asymmetry factor at 440 nm'

        if table2Version == 215 and indicatorOfParameter == 153:
            return 'Asymmetry factor at 400 nm'

        if table2Version == 215 and indicatorOfParameter == 152:
            return 'Asymmetry factor at 380 nm'

        if table2Version == 215 and indicatorOfParameter == 151:
            return 'Asymmetry factor at 355 nm'

        if table2Version == 215 and indicatorOfParameter == 150:
            return 'Asymmetry factor at 340 nm'

        if table2Version == 215 and indicatorOfParameter == 149:
            return 'Single scattering albedo at 1640 nm'

        if table2Version == 215 and indicatorOfParameter == 148:
            return 'Single scattering albedo at 1240 nm'

        if table2Version == 215 and indicatorOfParameter == 147:
            return 'Single scattering albedo at 1064 nm'

        if table2Version == 215 and indicatorOfParameter == 146:
            return 'Single scattering albedo at 1020 nm'

        if table2Version == 215 and indicatorOfParameter == 145:
            return 'Single scattering albedo at 865 nm'

        if table2Version == 215 and indicatorOfParameter == 144:
            return 'Single scattering albedo at 858 nm'

        if table2Version == 215 and indicatorOfParameter == 143:
            return 'Single scattering albedo at 800 nm'

        if table2Version == 215 and indicatorOfParameter == 142:
            return 'Single scattering albedo at 670 nm'

        if table2Version == 215 and indicatorOfParameter == 141:
            return 'Single scattering albedo at 645 nm'

        if table2Version == 215 and indicatorOfParameter == 140:
            return 'Single scattering albedo at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 139:
            return 'Single scattering albedo at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 138:
            return 'Single scattering albedo at 500 nm'

        if table2Version == 215 and indicatorOfParameter == 137:
            return 'Single scattering albedo at 469 nm'

        if table2Version == 215 and indicatorOfParameter == 136:
            return 'Single scattering albedo at 440 nm'

        if table2Version == 215 and indicatorOfParameter == 135:
            return 'Single scattering albedo at 400 nm'

        if table2Version == 215 and indicatorOfParameter == 134:
            return 'Single scattering albedo at 380 nm'

        if table2Version == 215 and indicatorOfParameter == 133:
            return 'Single scattering albedo at 355 nm'

        if table2Version == 215 and indicatorOfParameter == 132:
            return 'Single scattering albedo at 340 nm'

        if table2Version == 215 and indicatorOfParameter == 131:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1640 nm'

        if table2Version == 215 and indicatorOfParameter == 130:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1240 nm'

        if table2Version == 215 and indicatorOfParameter == 129:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1064 nm'

        if table2Version == 215 and indicatorOfParameter == 128:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1020 nm'

        if table2Version == 215 and indicatorOfParameter == 127:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 865 nm'

        if table2Version == 215 and indicatorOfParameter == 126:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 858 nm'

        if table2Version == 215 and indicatorOfParameter == 125:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 800 nm'

        if table2Version == 215 and indicatorOfParameter == 124:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 670 nm'

        if table2Version == 215 and indicatorOfParameter == 123:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 645 nm'

        if table2Version == 215 and indicatorOfParameter == 122:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 121:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 120:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 500 nm'

        if table2Version == 215 and indicatorOfParameter == 119:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 469 nm'

        if table2Version == 215 and indicatorOfParameter == 118:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 440 nm'

        if table2Version == 215 and indicatorOfParameter == 117:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 400 nm'

        if table2Version == 215 and indicatorOfParameter == 116:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 380 nm'

        if table2Version == 215 and indicatorOfParameter == 115:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 355 nm'

        if table2Version == 215 and indicatorOfParameter == 114:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 340 nm'

        if table2Version == 215 and indicatorOfParameter == 113:
            return 'Total absorption aerosol optical depth at 1640 nm'

        if table2Version == 215 and indicatorOfParameter == 112:
            return 'Total absorption aerosol optical depth at 1240 nm'

        if table2Version == 215 and indicatorOfParameter == 111:
            return 'Total absorption aerosol optical depth at 1064 nm'

        if table2Version == 215 and indicatorOfParameter == 110:
            return 'Total absorption aerosol optical depth at 1020 nm'

        if table2Version == 215 and indicatorOfParameter == 109:
            return 'Total absorption aerosol optical depth at 865 nm'

        if table2Version == 215 and indicatorOfParameter == 108:
            return 'Total absorption aerosol optical depth at 858 nm'

        if table2Version == 215 and indicatorOfParameter == 107:
            return 'Total absorption aerosol optical depth at 800 nm'

        if table2Version == 215 and indicatorOfParameter == 106:
            return 'Total absorption aerosol optical depth at 670 nm'

        if table2Version == 215 and indicatorOfParameter == 105:
            return 'Total absorption aerosol optical depth at 645 nm'

        if table2Version == 215 and indicatorOfParameter == 104:
            return 'Total absorption aerosol optical depth at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 103:
            return 'Total absorption aerosol optical depth at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 102:
            return 'Total absorption aerosol optical depth at 500 nm'

        if table2Version == 215 and indicatorOfParameter == 101:
            return 'Total absorption aerosol optical depth at 469 nm'

        if table2Version == 215 and indicatorOfParameter == 100:
            return 'Total absorption aerosol optical depth at 440 nm'

        if table2Version == 215 and indicatorOfParameter == 99:
            return 'Total absorption aerosol optical depth at 400 nm'

        if table2Version == 215 and indicatorOfParameter == 98:
            return 'Total absorption aerosol optical depth at 380 nm'

        if table2Version == 215 and indicatorOfParameter == 97:
            return 'Total absorption aerosol optical depth at 355 nm'

        if table2Version == 215 and indicatorOfParameter == 96:
            return 'Total absorption aerosol optical depth at 340 nm'

        if table2Version == 215 and indicatorOfParameter == 95:
            return 'Antropogenic (black carbon, organic matter, sulphate) aerosol optical thickness at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 94:
            return 'Natural (sea-salt and dust) aerosol optical thickness at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 93:
            return 'Total aerosol optical thickness at 532 nm'

        if table2Version == 215 and indicatorOfParameter == 92:
            return '10 metre wind gustiness dust emission potential'

        if table2Version == 215 and indicatorOfParameter == 91:
            return '10 metre wind speed dust emission potential'

        if table2Version == 215 and indicatorOfParameter == 90:
            return 'Effective (snow effect included) UV visible albedo for direct radiation'

        if table2Version == 215 and indicatorOfParameter == 89:
            return 'Accumulated total aerosol optical depth at 550 nm'

        if table2Version == 215 and indicatorOfParameter == 88:
            return 'Sulphate aerosol optical depth'

        if table2Version == 215 and indicatorOfParameter == 87:
            return 'Vertically integrated mass of sulphate aerosol'

        if table2Version == 215 and indicatorOfParameter == 86:
            return 'Negative fixer of sulphate aerosol'

        if table2Version == 215 and indicatorOfParameter == 85:
            return 'Wet deposition of sulphate aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 84:
            return 'Wet deposition of sulphate aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 83:
            return 'Sedimentation of sulphate aerosol'

        if table2Version == 215 and indicatorOfParameter == 82:
            return 'Dry deposition of sulphate aerosol'

        if table2Version == 215 and indicatorOfParameter == 81:
            return 'Source/gain of sulphate aerosol'

        if table2Version == 215 and indicatorOfParameter == 80:
            return 'Hydrophilic black carbon aerosol optical depth'

        if table2Version == 215 and indicatorOfParameter == 79:
            return 'Hydrophobic black carbon aerosol optical depth'

        if table2Version == 215 and indicatorOfParameter == 78:
            return 'Vertically integrated mass of hydrophilic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 77:
            return 'Vertically integrated mass of hydrophobic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 76:
            return 'Negative fixer of hydrophilic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 75:
            return 'Negative fixer of hydrophobic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 74:
            return 'Wet deposition of hydrophilic black carbon aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 73:
            return 'Wet deposition of hydrophobic black carbon aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 72:
            return 'Wet deposition of hydrophilic black carbon aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 71:
            return 'Wet deposition of hydrophobic black carbon aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 70:
            return 'Sedimentation of hydrophilic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 69:
            return 'Sedimentation of hydrophobic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 68:
            return 'Dry deposition of hydrophilic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 67:
            return 'Dry deposition of hydrophobic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 66:
            return 'Source/gain of hydrophilic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 65:
            return 'Source/gain of hydrophobic black carbon aerosol'

        if table2Version == 215 and indicatorOfParameter == 64:
            return 'Hydrophilic organic matter aerosol optical depth'

        if table2Version == 215 and indicatorOfParameter == 63:
            return 'Hydrophobic organic matter aerosol optical depth'

        if table2Version == 215 and indicatorOfParameter == 62:
            return 'Vertically integrated mass of hydrophilic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 61:
            return 'Vertically integrated mass of hydrophobic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 60:
            return 'Negative fixer of hydrophilic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 59:
            return 'Negative fixer of hydrophobic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 58:
            return 'Wet deposition of hydrophilic organic matter aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 57:
            return 'Wet deposition of hydrophobic organic matter aerosol by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 56:
            return 'Wet deposition of hydrophilic organic matter aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 55:
            return 'Wet deposition of hydrophobic organic matter aerosol by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 54:
            return 'Sedimentation of hydrophilic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 53:
            return 'Sedimentation of hydrophobic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 52:
            return 'Dry deposition of hydrophilic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 51:
            return 'Dry deposition of hydrophobic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 50:
            return 'Source/gain of hydrophilic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 49:
            return 'Source/gain of hydrophobic organic matter aerosol'

        if table2Version == 215 and indicatorOfParameter == 48:
            return 'Dust aerosol (9 - 20 um) optical depth'

        if table2Version == 215 and indicatorOfParameter == 47:
            return 'Dust aerosol (0.55 - 9 um) optical depth'

        if table2Version == 215 and indicatorOfParameter == 46:
            return 'Dust aerosol (0.03 - 0.55 um) optical depth'

        if table2Version == 215 and indicatorOfParameter == 45:
            return 'Vertically integrated mass of dust aerosol (9 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 44:
            return 'Vertically integrated mass of dust aerosol (0.55 - 9 um)'

        if table2Version == 215 and indicatorOfParameter == 43:
            return 'Vertically integrated mass of dust aerosol (0.03 - 0.55 um)'

        if table2Version == 215 and indicatorOfParameter == 42:
            return 'Negative fixer of dust aerosol (9 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 41:
            return 'Negative fixer of dust aerosol (0.55 - 9 um)'

        if table2Version == 215 and indicatorOfParameter == 40:
            return 'Negative fixer of dust aerosol (0.03 - 0.55 um)'

        if table2Version == 215 and indicatorOfParameter == 39:
            return 'Wet deposition of dust aerosol (9 - 20 um) by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 38:
            return 'Wet deposition of dust aerosol (0.55 - 9 um) by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 37:
            return 'Wet deposition of dust aerosol (0.03 - 0.55 um) by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 36:
            return 'Wet deposition of dust aerosol (9 - 20 um) by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 35:
            return 'Wet deposition of dust aerosol (0.55 - 9 um) by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 34:
            return 'Wet deposition of dust aerosol (0.03 - 0.55 um) by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 33:
            return 'Sedimentation of dust aerosol (9 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 32:
            return 'Sedimentation of dust aerosol (0.55 - 9 um)'

        if table2Version == 215 and indicatorOfParameter == 31:
            return 'Sedimentation of dust aerosol (0.03 - 0.55 um)'

        if table2Version == 215 and indicatorOfParameter == 30:
            return 'Dry deposition of dust aerosol (9 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 29:
            return 'Dry deposition of dust aerosol (0.55 - 9 um)'

        if table2Version == 215 and indicatorOfParameter == 28:
            return 'Dry deposition of dust aerosol (0.03 - 0.55 um)'

        if table2Version == 215 and indicatorOfParameter == 27:
            return 'Source/gain of dust aerosol (9 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 26:
            return 'Source/gain of dust aerosol (0.55 - 9 um)'

        if table2Version == 215 and indicatorOfParameter == 25:
            return 'Source/gain of dust aerosol (0.03 - 0.55 um)'

        if table2Version == 215 and indicatorOfParameter == 24:
            return 'Sea salt aerosol (5 - 20 um) optical depth'

        if table2Version == 215 and indicatorOfParameter == 23:
            return 'Sea salt aerosol (0.5 - 5 um) optical depth'

        if table2Version == 215 and indicatorOfParameter == 22:
            return 'Sea salt aerosol (0.03 - 0.5 um) optical depth'

        if table2Version == 215 and indicatorOfParameter == 21:
            return 'Vertically integrated mass of sea salt aerosol (5 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 20:
            return 'Vertically integrated mass of sea salt aerosol (0.5 - 5 um)'

        if table2Version == 215 and indicatorOfParameter == 19:
            return 'Vertically integrated mass of sea salt aerosol (0.03 - 0.5 um)'

        if table2Version == 215 and indicatorOfParameter == 18:
            return 'Negative fixer of sea salt aerosol (5 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 17:
            return 'Negative fixer of sea salt aerosol (0.5 - 5 um)'

        if table2Version == 215 and indicatorOfParameter == 16:
            return 'Negative fixer of sea salt aerosol (0.03 - 0.5 um)'

        if table2Version == 215 and indicatorOfParameter == 15:
            return 'Wet deposition of sea salt aerosol (5 - 20 um) by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 14:
            return 'Wet deposition of sea salt aerosol (0.5 - 5 um) by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 13:
            return 'Wet deposition of sea salt aerosol (0.03 - 0.5 um) by convective precipitation'

        if table2Version == 215 and indicatorOfParameter == 12:
            return 'Wet deposition of sea salt aerosol (5 - 20 um) by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 11:
            return 'Wet deposition of sea salt aerosol (0.5 - 5 um) by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 10:
            return 'Wet deposition of sea salt aerosol (0.03 - 0.5 um) by large-scale precipitation'

        if table2Version == 215 and indicatorOfParameter == 9:
            return 'Sedimentation of sea salt aerosol (5 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 8:
            return 'Sedimentation of sea salt aerosol (0.5 - 5 um)'

        if table2Version == 215 and indicatorOfParameter == 7:
            return 'Sedimentation of sea salt aerosol (0.03 - 0.5 um)'

        if table2Version == 215 and indicatorOfParameter == 6:
            return 'Dry deposition of sea salt aerosol (5 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 5:
            return 'Dry deposition of sea salt aerosol (0.5 - 5 um)'

        if table2Version == 215 and indicatorOfParameter == 4:
            return 'Dry deposition of sea salt aerosol (0.03 - 0.5 um)'

        if table2Version == 215 and indicatorOfParameter == 3:
            return 'Source/gain of sea salt aerosol (5 - 20 um)'

        if table2Version == 215 and indicatorOfParameter == 2:
            return 'Source/gain of sea salt aerosol (0.5 - 5 um)'

        if table2Version == 215 and indicatorOfParameter == 1:
            return 'Source/gain of sea salt aerosol (0.03 - 0.5 um)'

        if table2Version == 214 and indicatorOfParameter == 52:
            return 'Profile of optical thickness at 340 nm'

        if table2Version == 214 and indicatorOfParameter == 51:
            return 'Clear-sky surface UV spectral flux (395-400 nm)'

        if table2Version == 214 and indicatorOfParameter == 50:
            return 'Clear-sky surface UV spectral flux (390-395 nm)'

        if table2Version == 214 and indicatorOfParameter == 49:
            return 'Clear-sky surface UV spectral flux (385-390 nm)'

        if table2Version == 214 and indicatorOfParameter == 48:
            return 'Clear-sky surface UV spectral flux (380-385 nm)'

        if table2Version == 214 and indicatorOfParameter == 47:
            return 'Clear-sky surface UV spectral flux (375-380 nm)'

        if table2Version == 214 and indicatorOfParameter == 46:
            return 'Clear-sky surface UV spectral flux (370-375 nm)'

        if table2Version == 214 and indicatorOfParameter == 45:
            return 'Clear-sky surface UV spectral flux (365-370 nm)'

        if table2Version == 214 and indicatorOfParameter == 44:
            return 'Clear-sky surface UV spectral flux (360-365 nm)'

        if table2Version == 214 and indicatorOfParameter == 43:
            return 'Clear-sky surface UV spectral flux (355-360 nm)'

        if table2Version == 214 and indicatorOfParameter == 42:
            return 'Clear-sky surface UV spectral flux (350-355 nm)'

        if table2Version == 214 and indicatorOfParameter == 41:
            return 'Clear-sky surface UV spectral flux (345-350 nm)'

        if table2Version == 214 and indicatorOfParameter == 40:
            return 'Clear-sky surface UV spectral flux (340-345 nm)'

        if table2Version == 214 and indicatorOfParameter == 39:
            return 'Clear-sky surface UV spectral flux (335-340 nm)'

        if table2Version == 214 and indicatorOfParameter == 38:
            return 'Clear-sky surface UV spectral flux (330-335 nm)'

        if table2Version == 214 and indicatorOfParameter == 37:
            return 'Clear-sky surface UV spectral flux (325-330 nm)'

        if table2Version == 214 and indicatorOfParameter == 36:
            return 'Clear-sky surface UV spectral flux (320-325 nm)'

        if table2Version == 214 and indicatorOfParameter == 35:
            return 'Clear-sky surface UV spectral flux (315-320 nm)'

        if table2Version == 214 and indicatorOfParameter == 34:
            return 'Clear-sky surface UV spectral flux (310-315 nm)'

        if table2Version == 214 and indicatorOfParameter == 33:
            return 'Clear-sky surface UV spectral flux (305-310 nm)'

        if table2Version == 214 and indicatorOfParameter == 32:
            return 'Clear-sky surface UV spectral flux (300-305 nm)'

        if table2Version == 214 and indicatorOfParameter == 31:
            return 'Clear-sky surface UV spectral flux (295-300 nm)'

        if table2Version == 214 and indicatorOfParameter == 30:
            return 'Clear-sky surface UV spectral flux (290-295 nm)'

        if table2Version == 214 and indicatorOfParameter == 29:
            return 'Clear-sky surface UV spectral flux (285-290 nm)'

        if table2Version == 214 and indicatorOfParameter == 28:
            return 'Clear-sky surface UV spectral flux (280-285 nm)'

        if table2Version == 214 and indicatorOfParameter == 27:
            return 'Total surface UV spectral flux (395-400 nm)'

        if table2Version == 214 and indicatorOfParameter == 26:
            return 'Total surface UV spectral flux (390-395 nm)'

        if table2Version == 214 and indicatorOfParameter == 25:
            return 'Total surface UV spectral flux (385-390 nm)'

        if table2Version == 214 and indicatorOfParameter == 24:
            return 'Total surface UV spectral flux (380-385 nm)'

        if table2Version == 214 and indicatorOfParameter == 23:
            return 'Total surface UV spectral flux (375-380 nm)'

        if table2Version == 214 and indicatorOfParameter == 22:
            return 'Total surface UV spectral flux (370-375 nm)'

        if table2Version == 214 and indicatorOfParameter == 21:
            return 'Total surface UV spectral flux (365-370 nm)'

        if table2Version == 214 and indicatorOfParameter == 20:
            return 'Total surface UV spectral flux (360-365 nm)'

        if table2Version == 214 and indicatorOfParameter == 19:
            return 'Total surface UV spectral flux (355-360 nm)'

        if table2Version == 214 and indicatorOfParameter == 18:
            return 'Total surface UV spectral flux (350-355 nm)'

        if table2Version == 214 and indicatorOfParameter == 17:
            return 'Total surface UV spectral flux (345-350 nm)'

        if table2Version == 214 and indicatorOfParameter == 16:
            return 'Total surface UV spectral flux (340-345 nm)'

        if table2Version == 214 and indicatorOfParameter == 15:
            return 'Total surface UV spectral flux (335-340 nm)'

        if table2Version == 214 and indicatorOfParameter == 14:
            return 'Total surface UV spectral flux (330-335 nm)'

        if table2Version == 214 and indicatorOfParameter == 13:
            return 'Total surface UV spectral flux (325-330 nm)'

        if table2Version == 214 and indicatorOfParameter == 12:
            return 'Total surface UV spectral flux (320-325 nm)'

        if table2Version == 214 and indicatorOfParameter == 11:
            return 'Total surface UV spectral flux (315-320 nm)'

        if table2Version == 214 and indicatorOfParameter == 10:
            return 'Total surface UV spectral flux (310-315 nm)'

        if table2Version == 214 and indicatorOfParameter == 9:
            return 'Total surface UV spectral flux (305-310 nm)'

        if table2Version == 214 and indicatorOfParameter == 8:
            return 'Total surface UV spectral flux (300-305 nm)'

        if table2Version == 214 and indicatorOfParameter == 7:
            return 'Total surface UV spectral flux (295-300 nm)'

        if table2Version == 214 and indicatorOfParameter == 6:
            return 'Total surface UV spectral flux (290-295 nm)'

        if table2Version == 214 and indicatorOfParameter == 5:
            return 'Total surface UV spectral flux (285-290 nm)'

        if table2Version == 214 and indicatorOfParameter == 4:
            return 'Total surface UV spectral flux (280-285 nm)'

        if table2Version == 214 and indicatorOfParameter == 3:
            return 'UV biologically effective dose clear-sky'

        if table2Version == 214 and indicatorOfParameter == 2:
            return 'UV biologically effective dose'

        if table2Version == 214 and indicatorOfParameter == 1:
            return 'Cosine of solar zenith angle'

        if table2Version == 213 and indicatorOfParameter == 150:
            return 'Random pattern 50 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 149:
            return 'Random pattern 49 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 148:
            return 'Random pattern 48 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 147:
            return 'Random pattern 47 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 146:
            return 'Random pattern 46 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 145:
            return 'Random pattern 45 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 144:
            return 'Random pattern 44 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 143:
            return 'Random pattern 43 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 142:
            return 'Random pattern 42 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 141:
            return 'Random pattern 41 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 140:
            return 'Random pattern 40 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 139:
            return 'Random pattern 39 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 138:
            return 'Random pattern 38 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 137:
            return 'Random pattern 37 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 136:
            return 'Random pattern 36 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 135:
            return 'Random pattern 35 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 134:
            return 'Random pattern 34 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 133:
            return 'Random pattern 33 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 132:
            return 'Random pattern 32 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 131:
            return 'Random pattern 31 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 130:
            return 'Random pattern 30 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 129:
            return 'Random pattern 29 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 128:
            return 'Random pattern 28 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 127:
            return 'Random pattern 27 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 126:
            return 'Random pattern 26 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 125:
            return 'Random pattern 25 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 124:
            return 'Random pattern 24 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 123:
            return 'Random pattern 23 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 122:
            return 'Random pattern 22 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 121:
            return 'Random pattern 21 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 120:
            return 'Random pattern 20 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 119:
            return 'Random pattern 19 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 118:
            return 'Random pattern 18 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 117:
            return 'Random pattern 17 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 116:
            return 'Random pattern 16 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 115:
            return 'Random pattern 15 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 114:
            return 'Random pattern 14 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 113:
            return 'Random pattern 13 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 112:
            return 'Random pattern 12 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 111:
            return 'Random pattern 11 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 110:
            return 'Random pattern 10 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 109:
            return 'Random pattern 9 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 108:
            return 'Random pattern 8 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 107:
            return 'Random pattern 7 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 106:
            return 'Random pattern 6 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 105:
            return 'Random pattern 5 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 104:
            return 'Random pattern 4 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 103:
            return 'Random pattern 3 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 102:
            return 'Random pattern 2 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 101:
            return 'Random pattern 1 for SPP scheme'

        if table2Version == 213 and indicatorOfParameter == 5:
            return 'Random pattern 5 for sppt'

        if table2Version == 213 and indicatorOfParameter == 4:
            return 'Random pattern 4 for sppt'

        if table2Version == 213 and indicatorOfParameter == 3:
            return 'Random pattern 3 for sppt'

        if table2Version == 213 and indicatorOfParameter == 2:
            return 'Random pattern 2 for sppt'

        if table2Version == 213 and indicatorOfParameter == 1:
            return 'Random pattern 1 for sppt'

        if table2Version == 212 and indicatorOfParameter == 255:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 254:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 253:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 252:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 251:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 250:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 249:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 248:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 247:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 246:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 245:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 244:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 243:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 242:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 241:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 240:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 239:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 238:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 237:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 236:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 235:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 234:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 233:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 232:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 231:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 230:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 229:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 228:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 227:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 226:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 225:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 224:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 223:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 222:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 221:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 220:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 219:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 218:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 217:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 216:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 215:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 214:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 213:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 212:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 211:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 210:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 209:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 208:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 207:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 206:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 205:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 204:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 203:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 202:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 201:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 200:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 199:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 198:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 197:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 196:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 195:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 194:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 193:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 192:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 191:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 190:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 189:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 188:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 187:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 186:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 185:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 184:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 183:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 182:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 181:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 180:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 179:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 178:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 177:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 176:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 175:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 174:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 173:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 172:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 171:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 170:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 169:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 168:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 167:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 166:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 165:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 164:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 163:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 162:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 161:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 160:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 159:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 158:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 157:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 156:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 155:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 154:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 153:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 152:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 151:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 150:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 149:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 148:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 147:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 146:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 145:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 144:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 143:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 142:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 141:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 140:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 139:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 138:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 137:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 136:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 135:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 134:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 133:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 132:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 131:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 130:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 129:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 128:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 127:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 126:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 125:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 124:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 123:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 122:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 121:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 120:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 119:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 118:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 117:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 116:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 115:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 114:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 113:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 112:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 111:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 110:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 109:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 108:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 107:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 106:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 105:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 104:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 103:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 102:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 101:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 100:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 99:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 98:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 97:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 96:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 95:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 94:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 93:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 92:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 91:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 90:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 89:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 88:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 87:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 86:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 85:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 84:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 83:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 82:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 81:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 80:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 79:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 78:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 77:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 76:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 75:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 74:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 73:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 72:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 71:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 70:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 69:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 68:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 67:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 66:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 65:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 64:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 63:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 62:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 61:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 60:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 59:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 58:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 57:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 56:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 55:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 54:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 53:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 52:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 51:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 50:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 49:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 48:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 47:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 46:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 45:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 44:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 43:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 42:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 41:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 40:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 39:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 38:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 37:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 36:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 35:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 34:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 33:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 32:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 31:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 30:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 29:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 28:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 27:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 26:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 25:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 24:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 23:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 22:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 21:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 20:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 19:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 18:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 17:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 16:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 15:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 14:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 13:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 12:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 11:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 10:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 9:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 8:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 7:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 6:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 5:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 4:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 3:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 2:
            return 'Experimental product'

        if table2Version == 212 and indicatorOfParameter == 1:
            return 'Experimental product'

        if table2Version == 211 and indicatorOfParameter == 120:
            return 'Altitude of plume top'

        if table2Version == 211 and indicatorOfParameter == 119:
            return 'Altitude of emitter'

        if table2Version == 211 and indicatorOfParameter == 118:
            return 'Wildfire Flux of Ethane (C2H6)'

        if table2Version == 211 and indicatorOfParameter == 56:
            return 'Experimental product'

        if table2Version == 211 and indicatorOfParameter == 55:
            return 'Experimental product'

        if table2Version == 211 and indicatorOfParameter == 45:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 4'

        if table2Version == 211 and indicatorOfParameter == 44:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 3'

        if table2Version == 211 and indicatorOfParameter == 43:
            return 'DMS surface emission'

        if table2Version == 211 and indicatorOfParameter == 30:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 2'

        if table2Version == 211 and indicatorOfParameter == 29:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 1'

        if table2Version == 211 and indicatorOfParameter == 28:
            return 'SO4 aerosol precursor mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 15:
            return 'Aerosol type 15 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 14:
            return 'Aerosol type 14 mass mixing ratio'

        if table2Version == 211 and indicatorOfParameter == 13:
            return 'Aerosol type 13 mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 251:
            return 'Ammonium aerosol optical depth at 550 nm'

        if table2Version == 210 and indicatorOfParameter == 250:
            return 'Nitrate aerosol optical depth at 550 nm'

        if table2Version == 210 and indicatorOfParameter == 249:
            return 'Ammonium aerosol mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 248:
            return 'Nitrate coarse mode aerosol mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 247:
            return 'Nitrate fine mode aerosol mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 246:
            return 'Profile of total aerosol dry absorption coefficient'

        if table2Version == 210 and indicatorOfParameter == 245:
            return 'Profile of total aerosol dry extinction coefficient'

        if table2Version == 210 and indicatorOfParameter == 244:
            return 'Volcanic ash optical depth at 550 nm'

        if table2Version == 210 and indicatorOfParameter == 243:
            return 'Volcanic sulphate aerosol optical depth at 550 nm'

        if table2Version == 210 and indicatorOfParameter == 242:
            return 'Altitude of plume bottom'

        if table2Version == 210 and indicatorOfParameter == 241:
            return 'Wildfire Flux of Heptane (C7H16)'

        if table2Version == 210 and indicatorOfParameter == 240:
            return 'Wildfire Flux of Hexanes (C6H14)'

        if table2Version == 210 and indicatorOfParameter == 239:
            return 'Wildfire Flux of Pentanes (C5H12)'

        if table2Version == 210 and indicatorOfParameter == 238:
            return 'Wildfire Flux of Butanes (C4H10)'

        if table2Version == 210 and indicatorOfParameter == 237:
            return 'Wildfire Flux of Octene (C8H16)'

        if table2Version == 210 and indicatorOfParameter == 236:
            return 'Wildfire Flux of Hexene (C6H12)'

        if table2Version == 210 and indicatorOfParameter == 235:
            return 'Wildfire Flux of Pentenes (C5H10)'

        if table2Version == 210 and indicatorOfParameter == 234:
            return 'Wildfire Flux of Butenes (C4H8)'

        if table2Version == 210 and indicatorOfParameter == 233:
            return 'Wildfire Flux of Xylene (C8H10)'

        if table2Version == 210 and indicatorOfParameter == 232:
            return 'Wildfire Flux of Benzene (C6H6)'

        if table2Version == 210 and indicatorOfParameter == 231:
            return 'Wildfire Flux of Toluene (C7H8)'

        if table2Version == 210 and indicatorOfParameter == 230:
            return 'Total aerosol optical depth at 2130 nm'

        if table2Version == 210 and indicatorOfParameter == 229:
            return 'Total aerosol optical depth at 1640 nm'

        if table2Version == 210 and indicatorOfParameter == 228:
            return 'Total aerosol optical depth at 1064 nm'

        if table2Version == 210 and indicatorOfParameter == 227:
            return 'Total aerosol optical depth at 1020 nm'

        if table2Version == 210 and indicatorOfParameter == 226:
            return 'Total aerosol optical depth at 858 nm'

        if table2Version == 210 and indicatorOfParameter == 225:
            return 'Total aerosol optical depth at 800 nm'

        if table2Version == 210 and indicatorOfParameter == 224:
            return 'Total aerosol optical depth at 645 nm'

        if table2Version == 210 and indicatorOfParameter == 223:
            return 'Total aerosol optical depth at 532 nm'

        if table2Version == 210 and indicatorOfParameter == 222:
            return 'Total aerosol optical depth at 500 nm'

        if table2Version == 210 and indicatorOfParameter == 221:
            return 'Total aerosol optical depth at 440 nm'

        if table2Version == 210 and indicatorOfParameter == 220:
            return 'Total aerosol optical depth at 400 nm'

        if table2Version == 210 and indicatorOfParameter == 219:
            return 'Total aerosol optical depth at 380 nm'

        if table2Version == 210 and indicatorOfParameter == 218:
            return 'Total aerosol optical depth at 355 nm'

        if table2Version == 210 and indicatorOfParameter == 217:
            return 'Total aerosol optical depth at 340 nm'

        if table2Version == 210 and indicatorOfParameter == 197:
            return 'Near IR albedo for diffuse radiation, geometric component '

        if table2Version == 210 and indicatorOfParameter == 196:
            return 'Near IR albedo for diffuse radiation, volumetric component '

        if table2Version == 210 and indicatorOfParameter == 195:
            return 'Near IR albedo for diffuse radiation, isotropic component '

        if table2Version == 210 and indicatorOfParameter == 194:
            return 'UV visible albedo for diffuse radiation, geometric component '

        if table2Version == 210 and indicatorOfParameter == 193:
            return 'UV visible albedo for diffuse radiation, volumetric component '

        if table2Version == 210 and indicatorOfParameter == 192:
            return 'UV visible albedo for diffuse radiation, isotropic component '

        if table2Version == 210 and indicatorOfParameter == 191:
            return 'Near IR albedo for direct radiation, geometric component '

        if table2Version == 210 and indicatorOfParameter == 190:
            return 'Near IR albedo for direct radiation, volumetric component'

        if table2Version == 210 and indicatorOfParameter == 189:
            return 'Near IR albedo for direct radiation, isotropic component '

        if table2Version == 210 and indicatorOfParameter == 188:
            return 'UV visible albedo for direct radiation, geometric component '

        if table2Version == 210 and indicatorOfParameter == 187:
            return 'UV visible albedo for direct radiation, volumetric component '

        if table2Version == 210 and indicatorOfParameter == 186:
            return 'UV visible albedo for direct radiation, isotropic component '

        if table2Version == 210 and indicatorOfParameter == 120:
            return 'Altitude of plume top'

        if table2Version == 210 and indicatorOfParameter == 119:
            return 'Mean altitude of maximum injection'

        if table2Version == 210 and indicatorOfParameter == 118:
            return 'Wildfire Flux of Ethane (C2H6)'

        if table2Version == 210 and indicatorOfParameter == 79:
            return 'Wildfire viewing angle of observation'

        if table2Version == 210 and indicatorOfParameter == 74:
            return 'Particulate matter d < 10 um'

        if table2Version == 210 and indicatorOfParameter == 73:
            return 'Particulate matter d < 2.5 um'

        if table2Version == 210 and indicatorOfParameter == 72:
            return 'Particulate matter d < 1 um'

        if table2Version == 210 and indicatorOfParameter == 60:
            return 'Injection height (from IS4FIRES)'

        if table2Version == 210 and indicatorOfParameter == 59:
            return 'Secondary organic precursor mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 58:
            return 'Monoterpene precursor mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 57:
            return 'Mixing ration of organic carbon aerosol, nucleation mode'

        if table2Version == 210 and indicatorOfParameter == 56:
            return 'Experimental product'

        if table2Version == 210 and indicatorOfParameter == 55:
            return 'Experimental product'

        if table2Version == 210 and indicatorOfParameter == 45:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 4'

        if table2Version == 210 and indicatorOfParameter == 44:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 3'

        if table2Version == 210 and indicatorOfParameter == 43:
            return 'DMS surface emission'

        if table2Version == 210 and indicatorOfParameter == 30:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 2'

        if table2Version == 210 and indicatorOfParameter == 29:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 1'

        if table2Version == 210 and indicatorOfParameter == 28:
            return 'SO4 aerosol precursor mass mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 15:
            return 'Volcanic SO2 precursor mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 14:
            return 'Volcanic sulphate aerosol mixing ratio'

        if table2Version == 210 and indicatorOfParameter == 13:
            return 'Volcanic ash aerosol mixing ratio'

        if table2Version == 174 and indicatorOfParameter == 249:
            return 'Total cloud amount in lw radiation'

        if table2Version == 174 and indicatorOfParameter == 248:
            return 'Total cloud amount - random overlap'

        if table2Version == 174 and indicatorOfParameter == 240:
            return 'Large scale snowfall rate'

        if table2Version == 174 and indicatorOfParameter == 239:
            return 'Convective snowfall rate'

        if table2Version == 174 and indicatorOfParameter == 186:
            return 'Very low cloud amount'

        if table2Version == 174 and indicatorOfParameter == 143:
            return 'Convective rainfall rate'

        if table2Version == 174 and indicatorOfParameter == 142:
            return 'Large scale rainfall rate'

        if table2Version == 174 and indicatorOfParameter == 137:
            return 'Total column water vapour'

        if table2Version == 174 and indicatorOfParameter == 117:
            return 'Short wave radiation flux at top of atmosphere'

        if table2Version == 174 and indicatorOfParameter == 116:
            return 'Short wave radiation flux at surface'

        if table2Version == 174 and indicatorOfParameter == 97:
            return 'Sea ice snow thickness'

        if table2Version == 174 and indicatorOfParameter == 96:
            return '2 metre specific humidity'

        if table2Version == 174 and indicatorOfParameter == 52:
            return 'Relative humidity at 1.5m'

        if table2Version == 174 and indicatorOfParameter == 51:
            return 'Maximum temperature at 1.5m since previous post-processing'

        if table2Version == 174 and indicatorOfParameter == 50:
            return 'Minimum temperature at 1.5m since previous post-processing'

        if table2Version == 174 and indicatorOfParameter == 25:
            return 'Visibility at 1.5m'

        if table2Version == 174 and indicatorOfParameter == 13:
            return 'Clear-sky (II) up surface sw flux'

        if table2Version == 174 and indicatorOfParameter == 10:
            return 'Clear-sky (II) down surface sw flux'

        if table2Version == 173 and indicatorOfParameter == 9:
            return 'Mean sub-surface runoff rate anomaly'

        if table2Version == 173 and indicatorOfParameter == 8:
            return 'Mean surface runoff rate anomaly'

        if table2Version == 172 and indicatorOfParameter == 9:
            return 'Mean sub-surface runoff rate'

        if table2Version == 172 and indicatorOfParameter == 8:
            return 'Mean surface runoff rate'

        if table2Version == 171 and indicatorOfParameter == 122:
            return 'Minimum temperature at 2 metres in the last 6 hours anomaly'

        if table2Version == 171 and indicatorOfParameter == 121:
            return 'Maximum temperature at 2 metres in the last 6 hours anomaly'

        if table2Version == 171 and indicatorOfParameter == 25:
            return 'Lake ice depth anomaly'

        if table2Version == 171 and indicatorOfParameter == 24:
            return 'Lake mix-layer temperature anomaly'

        if table2Version == 171 and indicatorOfParameter == 7:
            return '100 metre V wind component anomaly'

        if table2Version == 171 and indicatorOfParameter == 6:
            return '100 metre U wind component anomaly'

        if table2Version == 170 and indicatorOfParameter == 3:
            return 'Standardised precipitation index valid in the last 12 months'

        if table2Version == 170 and indicatorOfParameter == 2:
            return 'Standardised precipitation index valid in the last 6 months'

        if table2Version == 170 and indicatorOfParameter == 1:
            return 'Standardised precipitation index valid in the last 3 months'

        if table2Version == 162 and indicatorOfParameter == 141:
            return 'q-tendency from shallow convection'

        if table2Version == 162 and indicatorOfParameter == 140:
            return 'T-tendency from shallow convection'

        if table2Version == 162 and indicatorOfParameter == 139:
            return 'V-tendency from shallow convection'

        if table2Version == 162 and indicatorOfParameter == 138:
            return 'U-tendency from shallow convection'

        if table2Version == 162 and indicatorOfParameter == 137:
            return 'Ice Precip flux from cloud scheme (stratiform)'

        if table2Version == 162 and indicatorOfParameter == 136:
            return 'Liquid Precip flux from cloud scheme (stratiform)'

        if table2Version == 162 and indicatorOfParameter == 135:
            return 'qi-tendency from cloud scheme'

        if table2Version == 162 and indicatorOfParameter == 134:
            return 'ql-tendency from cloud scheme'

        if table2Version == 162 and indicatorOfParameter == 133:
            return 'q-tendency from cloud scheme'

        if table2Version == 162 and indicatorOfParameter == 132:
            return 'T-tendency from cloud scheme'

        if table2Version == 162 and indicatorOfParameter == 131:
            return 'Ice Precipitation flux from convection'

        if table2Version == 162 and indicatorOfParameter == 130:
            return 'Liquid Precipitation flux from convection'

        if table2Version == 162 and indicatorOfParameter == 129:
            return 'q-tendency from convection (deep+shallow)'

        if table2Version == 162 and indicatorOfParameter == 128:
            return 'T-tendency from convection (deep+shallow)'

        if table2Version == 162 and indicatorOfParameter == 127:
            return 'V-tendency from convection (deep+shallow)'

        if table2Version == 162 and indicatorOfParameter == 126:
            return 'U-tendency from convection (deep+shallow)'

        if table2Version == 162 and indicatorOfParameter == 125:
            return 'T-tendency from subgrid orography'

        if table2Version == 162 and indicatorOfParameter == 124:
            return 'V-tendency from subgrid orography'

        if table2Version == 162 and indicatorOfParameter == 123:
            return 'U-tendency from subgrid orography'

        if table2Version == 162 and indicatorOfParameter == 122:
            return 'q-tendency from turbulent diffusion'

        if table2Version == 162 and indicatorOfParameter == 121:
            return 'T-tendency from turbulent diffusion + subgrid orography'

        if table2Version == 162 and indicatorOfParameter == 120:
            return 'V-tendency from turbulent diffusion + subgrid orography'

        if table2Version == 162 and indicatorOfParameter == 119:
            return 'U-tendency from turbulent diffusion + subgrid orography'

        if table2Version == 162 and indicatorOfParameter == 118:
            return 'T-tendency from radiation'

        if table2Version == 162 and indicatorOfParameter == 117:
            return 'q-tendency from dynamics'

        if table2Version == 162 and indicatorOfParameter == 116:
            return 'T-tendency from dynamics'

        if table2Version == 162 and indicatorOfParameter == 115:
            return 'V-tendency from dynamics'

        if table2Version == 162 and indicatorOfParameter == 114:
            return 'U-tendency from dynamics'

        if table2Version == 162 and indicatorOfParameter == 92:
            return 'Vertical integral of mass tendency'

        if table2Version == 162 and indicatorOfParameter == 91:
            return 'Vertical integral of northward cloud frozen water flux '

        if table2Version == 162 and indicatorOfParameter == 90:
            return 'Vertical integral of eastward cloud frozen water flux'

        if table2Version == 162 and indicatorOfParameter == 89:
            return 'Vertical integral of northward cloud liquid water flux'

        if table2Version == 162 and indicatorOfParameter == 88:
            return 'Vertical integral of eastward cloud liquid water flux'

        if table2Version == 162 and indicatorOfParameter == 80:
            return 'Vertical integral of divergence of cloud frozen water flux'

        if table2Version == 162 and indicatorOfParameter == 79:
            return 'Vertical integral of divergence of cloud liquid water flux'

        if table2Version == 162 and indicatorOfParameter == 45:
            return 'Water vapour flux'

        if table2Version == 151 and indicatorOfParameter == 193:
            return 'Reserved'

        if table2Version == 140 and indicatorOfParameter == 214:
            return 'Normalized stress into ocean'

        if table2Version == 140 and indicatorOfParameter == 213:
            return 'Turbulent Langmuir number'

        if table2Version == 140 and indicatorOfParameter == 212:
            return 'Normalized energy flux into ocean'

        if table2Version == 140 and indicatorOfParameter == 211:
            return 'Normalized energy flux into waves'

        if table2Version == 140 and indicatorOfParameter == 210:
            return 'Mean square wave strain in sea ice'

        if table2Version == 140 and indicatorOfParameter == 209:
            return 'Air density over the oceans'

        if table2Version == 140 and indicatorOfParameter == 208:
            return 'Free convective velocity over the oceans'

        if table2Version == 140 and indicatorOfParameter == 207:
            return 'Wave Spectral Skewness'

        if table2Version == 140 and indicatorOfParameter == 129:
            return 'Mean wave period of third swell partition'

        if table2Version == 140 and indicatorOfParameter == 128:
            return 'Mean wave direction of third swell partition'

        if table2Version == 140 and indicatorOfParameter == 127:
            return 'Significant wave height of third swell partition'

        if table2Version == 140 and indicatorOfParameter == 126:
            return 'Mean wave period of second swell partition'

        if table2Version == 140 and indicatorOfParameter == 125:
            return 'Mean wave direction of second swell partition'

        if table2Version == 140 and indicatorOfParameter == 124:
            return 'Significant wave height of second swell partition'

        if table2Version == 140 and indicatorOfParameter == 123:
            return 'Mean wave period of first swell partition'

        if table2Version == 140 and indicatorOfParameter == 122:
            return 'Mean wave direction of first swell partition'

        if table2Version == 140 and indicatorOfParameter == 121:
            return 'Significant wave height of first swell partition'

        if table2Version == 140 and indicatorOfParameter == 120:
            return 'Significant wave height of all waves with period larger than 10s'

        if table2Version == 140 and indicatorOfParameter == 119:
            return 'Significant wave height of all waves with periods within the inclusive range from 25 to 30 seconds'

        if table2Version == 140 and indicatorOfParameter == 118:
            return 'Significant wave height of all waves with periods within the inclusive range from 21 to 25 seconds'

        if table2Version == 140 and indicatorOfParameter == 117:
            return 'Significant wave height of all waves with periods within the inclusive range from 17 to 21 seconds'

        if table2Version == 140 and indicatorOfParameter == 116:
            return 'Significant wave height of all waves with periods within the inclusive range from 14 to 17 seconds'

        if table2Version == 140 and indicatorOfParameter == 115:
            return 'Significant wave height of all waves with periods within the inclusive range from 12 to 14 seconds'

        if table2Version == 140 and indicatorOfParameter == 114:
            return 'Significant wave height of all waves with periods within the inclusive range from 10 to 12 seconds'

        if table2Version == 140 and indicatorOfParameter == 113:
            return 'Wave energy flux mean direction'

        if table2Version == 140 and indicatorOfParameter == 112:
            return 'Wave energy flux magnitude'

        if table2Version == 140 and indicatorOfParameter == 111:
            return 'Wave frequency width of third swell partition'

        if table2Version == 140 and indicatorOfParameter == 110:
            return 'Wave directional width of third swell partition'

        if table2Version == 140 and indicatorOfParameter == 109:
            return 'Wave frequency width of second swell partition'

        if table2Version == 140 and indicatorOfParameter == 108:
            return 'Wave directional width of second swell partition'

        if table2Version == 140 and indicatorOfParameter == 107:
            return 'Wave frequency width of first swell partition'

        if table2Version == 140 and indicatorOfParameter == 106:
            return 'Wave directional width of first swell partition'

        if table2Version == 140 and indicatorOfParameter == 105:
            return 'Wave turbulent energy flux into ocean'

        if table2Version == 140 and indicatorOfParameter == 104:
            return 'V-component of surface momentum flux into ocean'

        if table2Version == 140 and indicatorOfParameter == 103:
            return 'U-component of surface momentum flux into ocean'

        if table2Version == 140 and indicatorOfParameter == 102:
            return 'V-component of atmospheric surface momentum flux'

        if table2Version == 140 and indicatorOfParameter == 101:
            return 'U-component of atmospheric surface momentum flux'

        if table2Version == 140 and indicatorOfParameter == 100:
            return 'Number of events in freak waves statistics'

        if table2Version == 140 and indicatorOfParameter == 99:
            return 'Ratio of wave angular and frequency width'

        if table2Version == 140 and indicatorOfParameter == 98:
            return 'Wave induced mean sea level correction'

        if table2Version == 140 and indicatorOfParameter == 84:
            return 'Wave experimental parameter 5'

        if table2Version == 140 and indicatorOfParameter == 83:
            return 'Wave experimental parameter 4'

        if table2Version == 140 and indicatorOfParameter == 82:
            return 'Wave experimental parameter 3'

        if table2Version == 140 and indicatorOfParameter == 81:
            return 'Wave experimental parameter 2'

        if table2Version == 140 and indicatorOfParameter == 80:
            return 'Wave experimental parameter 1'

        if table2Version == 132 and indicatorOfParameter == 216:
            return 'Maximum of significant wave height index'

        if table2Version == 132 and indicatorOfParameter == 59:
            return 'Convective available potential energy index'

        if table2Version == 132 and indicatorOfParameter == 45:
            return 'Water vapour flux index'

        if table2Version == 132 and indicatorOfParameter == 44:
            return 'Convective available potential energy shear index'

        if table2Version == 131 and indicatorOfParameter == 100:
            return '10 metre wind gust of at least 10 m/s'

        if table2Version == 131 and indicatorOfParameter == 99:
            return 'Total precipitation of at least 50 mm'

        if table2Version == 131 and indicatorOfParameter == 98:
            return 'Total precipitation of at least 25 mm'

        if table2Version == 131 and indicatorOfParameter == 97:
            return 'Probability anomaly of a tropical depression'

        if table2Version == 131 and indicatorOfParameter == 96:
            return 'Probability anomaly of a hurricane'

        if table2Version == 131 and indicatorOfParameter == 95:
            return 'Probability anomaly of a tropical storm'

        if table2Version == 131 and indicatorOfParameter == 94:
            return 'Climatological probability of a tropical depression'

        if table2Version == 131 and indicatorOfParameter == 93:
            return 'Climatological probability of a hurricane'

        if table2Version == 131 and indicatorOfParameter == 92:
            return 'Climatological probability of a tropical storm'

        if table2Version == 131 and indicatorOfParameter == 91:
            return 'Probability of a tropical depression'

        if table2Version == 131 and indicatorOfParameter == 90:
            return 'Probability of a hurricane'

        if table2Version == 131 and indicatorOfParameter == 89:
            return 'Probability of a tropical storm'

        if table2Version == 200 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 200 and indicatorOfParameter == 254:
            return 'Adiabatic tendency of meridional wind difference'

        if table2Version == 200 and indicatorOfParameter == 253:
            return 'Adiabatic tendency of zonal wind difference'

        if table2Version == 200 and indicatorOfParameter == 252:
            return 'Adiabatic tendency of humidity difference'

        if table2Version == 200 and indicatorOfParameter == 251:
            return 'Adiabatic tendency of temperature difference'

        if table2Version == 200 and indicatorOfParameter == 250:
            return 'Ice age difference'

        if table2Version == 200 and indicatorOfParameter == 249:
            return 'Accumulated ice water tendency difference'

        if table2Version == 200 and indicatorOfParameter == 248:
            return 'Cloud cover difference'

        if table2Version == 200 and indicatorOfParameter == 247:
            return 'Specific cloud ice water content difference'

        if table2Version == 200 and indicatorOfParameter == 246:
            return 'Specific cloud liquid water content difference'

        if table2Version == 200 and indicatorOfParameter == 245:
            return 'Forecast logarithm of surface roughness for heat difference'

        if table2Version == 200 and indicatorOfParameter == 244:
            return 'Forecast surface roughness difference'

        if table2Version == 200 and indicatorOfParameter == 243:
            return 'Forecast albedo difference'

        if table2Version == 200 and indicatorOfParameter == 242:
            return 'Accumulated liquid water tendency difference'

        if table2Version == 200 and indicatorOfParameter == 241:
            return 'Accumulated cloud fraction tendency difference'

        if table2Version == 200 and indicatorOfParameter == 240:
            return 'Large scale snowfall difference'

        if table2Version == 200 and indicatorOfParameter == 239:
            return 'Convective snowfall difference'

        if table2Version == 200 and indicatorOfParameter == 238:
            return 'Temperature of snow layer difference'

        if table2Version == 200 and indicatorOfParameter == 237:
            return 'Soil wetness level 4 difference'

        if table2Version == 200 and indicatorOfParameter == 236:
            return 'Soil temperature level 4 difference'

        if table2Version == 200 and indicatorOfParameter == 235:
            return 'Skin temperature difference'

        if table2Version == 200 and indicatorOfParameter == 234:
            return 'Logarithm of surface roughness length for heat difference'

        if table2Version == 200 and indicatorOfParameter == 233:
            return 'Apparent surface humidity difference'

        if table2Version == 200 and indicatorOfParameter == 232:
            return 'Instantaneous moisture flux difference'

        if table2Version == 200 and indicatorOfParameter == 231:
            return 'Instantaneous surface heat flux difference'

        if table2Version == 200 and indicatorOfParameter == 230:
            return 'Instantaneous Y surface stress difference'

        if table2Version == 200 and indicatorOfParameter == 229:
            return 'Instantaneous X surface stress difference'

        if table2Version == 200 and indicatorOfParameter == 228:
            return 'Total precipitation difference'

        if table2Version == 200 and indicatorOfParameter == 227:
            return 'Change from removal of negative humidity difference'

        if table2Version == 200 and indicatorOfParameter == 226:
            return 'Humidity tendency by large-scale condensation difference'

        if table2Version == 200 and indicatorOfParameter == 225:
            return 'Humidity tendency by cumulus convection difference'

        if table2Version == 200 and indicatorOfParameter == 224:
            return 'Vertical diffusion of humidity difference'

        if table2Version == 200 and indicatorOfParameter == 223:
            return 'Convective tendency of meridional wind difference'

        if table2Version == 200 and indicatorOfParameter == 222:
            return 'Convective tendency of zonal wind difference'

        if table2Version == 200 and indicatorOfParameter == 221:
            return 'North-South gravity wave drag tendency difference'

        if table2Version == 200 and indicatorOfParameter == 220:
            return 'East-West gravity wave drag tendency difference'

        if table2Version == 200 and indicatorOfParameter == 219:
            return 'Vertical diffusion of meridional wind difference'

        if table2Version == 200 and indicatorOfParameter == 218:
            return 'Vertical diffusion of zonal wind difference'

        if table2Version == 200 and indicatorOfParameter == 217:
            return 'Diabatic heating large-scale condensation difference'

        if table2Version == 200 and indicatorOfParameter == 216:
            return 'Diabatic heating by cumulus convection difference'

        if table2Version == 200 and indicatorOfParameter == 215:
            return 'Diabatic heating by vertical diffusion difference'

        if table2Version == 200 and indicatorOfParameter == 214:
            return 'Diabatic heating by radiation difference'

        if table2Version == 200 and indicatorOfParameter == 212:
            return 'TOA incident solar radiation difference'

        if table2Version == 200 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky difference'

        if table2Version == 200 and indicatorOfParameter == 210:
            return 'Surface net solar radiation, clear sky difference'

        if table2Version == 200 and indicatorOfParameter == 209:
            return 'Top net thermal radiation, clear sky difference'

        if table2Version == 200 and indicatorOfParameter == 208:
            return 'Top net solar radiation, clear sky difference'

        if table2Version == 200 and indicatorOfParameter == 207:
            return '10 metre wind speed difference'

        if table2Version == 200 and indicatorOfParameter == 206:
            return 'Total column ozone difference'

        if table2Version == 200 and indicatorOfParameter == 205:
            return 'Runoff difference'

        if table2Version == 200 and indicatorOfParameter == 204:
            return 'Precipitation analysis weights difference'

        if table2Version == 200 and indicatorOfParameter == 203:
            return 'Ozone mass mixing ratio difference'

        if table2Version == 200 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres since previous post-processing difference'

        if table2Version == 200 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres since previous post-processing difference'

        if table2Version == 200 and indicatorOfParameter == 200:
            return 'Variance of sub-gridscale orography difference'

        if table2Version == 200 and indicatorOfParameter == 199:
            return 'Vegetation fraction difference'

        if table2Version == 200 and indicatorOfParameter == 198:
            return 'Skin reservoir content difference'

        if table2Version == 200 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation difference'

        if table2Version == 200 and indicatorOfParameter == 196:
            return 'Meridional component of gravity wave stress difference'

        if table2Version == 200 and indicatorOfParameter == 195:
            return 'Longitudinal component of gravity wave stress difference'

        if table2Version == 200 and indicatorOfParameter == 194:
            return 'Brightness temperature difference'

        if table2Version == 200 and indicatorOfParameter == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance difference'

        if table2Version == 200 and indicatorOfParameter == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance difference'

        if table2Version == 200 and indicatorOfParameter == 191:
            return 'North-South component of sub-gridscale orographic variance difference'

        if table2Version == 200 and indicatorOfParameter == 190:
            return 'East-West component of sub-gridscale orographic variance difference'

        if table2Version == 200 and indicatorOfParameter == 189:
            return 'Sunshine duration difference'

        if table2Version == 200 and indicatorOfParameter == 188:
            return 'High cloud cover difference'

        if table2Version == 200 and indicatorOfParameter == 187:
            return 'Medium cloud cover difference'

        if table2Version == 200 and indicatorOfParameter == 186:
            return 'Low cloud cover difference'

        if table2Version == 200 and indicatorOfParameter == 185:
            return 'Convective cloud cover difference'

        if table2Version == 200 and indicatorOfParameter == 184:
            return 'Soil wetness level 3 difference'

        if table2Version == 200 and indicatorOfParameter == 183:
            return 'Soil temperature level 3 difference'

        if table2Version == 200 and indicatorOfParameter == 182:
            return 'Evaporation difference'

        if table2Version == 200 and indicatorOfParameter == 181:
            return 'North-South surface stress difference'

        if table2Version == 200 and indicatorOfParameter == 180:
            return 'East-West surface stress difference'

        if table2Version == 200 and indicatorOfParameter == 179:
            return 'Top net thermal radiation difference'

        if table2Version == 200 and indicatorOfParameter == 178:
            return 'Top net solar radiation difference'

        if table2Version == 200 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation difference'

        if table2Version == 200 and indicatorOfParameter == 176:
            return 'Surface net solar radiation difference'

        if table2Version == 200 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards difference'

        if table2Version == 200 and indicatorOfParameter == 174:
            return 'Albedo difference'

        if table2Version == 200 and indicatorOfParameter == 173:
            return 'Surface roughness difference'

        if table2Version == 200 and indicatorOfParameter == 172:
            return 'Land-sea mask difference'

        if table2Version == 200 and indicatorOfParameter == 171:
            return 'Soil wetness level 2 difference'

        if table2Version == 200 and indicatorOfParameter == 170:
            return 'Soil temperature level 2 difference'

        if table2Version == 200 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards difference'

        if table2Version == 200 and indicatorOfParameter == 167:
            return '2 metre temperature difference'

        if table2Version == 200 and indicatorOfParameter == 166:
            return '10 metre V wind component difference'

        if table2Version == 200 and indicatorOfParameter == 165:
            return '10 metre U wind component difference'

        if table2Version == 200 and indicatorOfParameter == 164:
            return 'Total cloud cover difference'

        if table2Version == 200 and indicatorOfParameter == 163:
            return 'Slope of sub-gridscale orography difference'

        if table2Version == 200 and indicatorOfParameter == 162:
            return 'Angle of sub-gridscale orography difference'

        if table2Version == 200 and indicatorOfParameter == 161:
            return 'Anisotropy of sub-gridscale orography difference'

        if table2Version == 200 and indicatorOfParameter == 160:
            return 'Standard deviation of orography difference'

        if table2Version == 200 and indicatorOfParameter == 159:
            return 'Boundary layer height difference'

        if table2Version == 200 and indicatorOfParameter == 158:
            return 'Tendency of surface pressure difference'

        if table2Version == 200 and indicatorOfParameter == 157:
            return 'Relative humidity difference'

        if table2Version == 200 and indicatorOfParameter == 156:
            return 'Height difference'

        if table2Version == 200 and indicatorOfParameter == 155:
            return 'Divergence difference'

        if table2Version == 200 and indicatorOfParameter == 154:
            return 'Long-wave heating rate difference'

        if table2Version == 200 and indicatorOfParameter == 153:
            return 'Short-wave heating rate difference'

        if table2Version == 200 and indicatorOfParameter == 152:
            return 'Logarithm of surface pressure difference'

        if table2Version == 200 and indicatorOfParameter == 151:
            return 'Mean sea level pressure difference'

        if table2Version == 200 and indicatorOfParameter == 150:
            return 'Top net radiation difference'

        if table2Version == 200 and indicatorOfParameter == 149:
            return 'Surface net radiation difference'

        if table2Version == 200 and indicatorOfParameter == 148:
            return 'Charnock difference'

        if table2Version == 200 and indicatorOfParameter == 147:
            return 'Surface latent heat flux difference'

        if table2Version == 200 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux difference'

        if table2Version == 200 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation difference'

        if table2Version == 200 and indicatorOfParameter == 144:
            return 'Snowfall (convective + stratiform) difference'

        if table2Version == 200 and indicatorOfParameter == 143:
            return 'Convective precipitation difference'

        if table2Version == 200 and indicatorOfParameter == 142:
            return 'Stratiform precipitation (Large-scale precipitation) difference'

        if table2Version == 200 and indicatorOfParameter == 141:
            return 'Snow depth difference'

        if table2Version == 200 and indicatorOfParameter == 140:
            return 'Soil wetness level 1 difference'

        if table2Version == 200 and indicatorOfParameter == 139:
            return 'Soil temperature level 1 difference'

        if table2Version == 200 and indicatorOfParameter == 138:
            return 'Vorticity (relative) difference'

        if table2Version == 200 and indicatorOfParameter == 137:
            return 'Total column water vapour difference'

        if table2Version == 200 and indicatorOfParameter == 136:
            return 'Total column water difference'

        if table2Version == 200 and indicatorOfParameter == 135:
            return 'Vertical velocity (pressure) difference'

        if table2Version == 200 and indicatorOfParameter == 134:
            return 'Surface pressure difference'

        if table2Version == 200 and indicatorOfParameter == 133:
            return 'Specific humidity difference'

        if table2Version == 200 and indicatorOfParameter == 132:
            return 'V component of wind difference'

        if table2Version == 200 and indicatorOfParameter == 131:
            return 'U component of wind difference'

        if table2Version == 200 and indicatorOfParameter == 130:
            return 'Temperature difference'

        if table2Version == 200 and indicatorOfParameter == 129:
            return 'Geopotential difference'

        if table2Version == 200 and indicatorOfParameter == 128:
            return 'Budget values difference'

        if table2Version == 200 and indicatorOfParameter == 127:
            return 'Atmospheric tide difference'

        if table2Version == 200 and indicatorOfParameter == 126:
            return 'Generic parameter for sensitive area prediction'

        if table2Version == 200 and indicatorOfParameter == 125:
            return 'Vertically integrated total energy'

        if table2Version == 200 and indicatorOfParameter == 123:
            return '10 metre wind gust in the last 6 hours difference'

        if table2Version == 200 and indicatorOfParameter == 122:
            return 'Minimum temperature at 2 metres difference'

        if table2Version == 200 and indicatorOfParameter == 121:
            return 'Maximum temperature at 2 metres difference'

        if table2Version == 200 and indicatorOfParameter == 120:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 119:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 118:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 117:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 116:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 115:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 114:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 113:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 112:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 111:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 110:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 109:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 108:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 107:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 106:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 105:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 104:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 103:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 102:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 101:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 100:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 99:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 98:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 97:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 96:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 95:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 94:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 93:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 92:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 91:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 90:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 89:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 88:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 87:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 86:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 85:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 84:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 83:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 82:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 81:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 80:
            return 'Experimental product'

        if table2Version == 200 and indicatorOfParameter == 79:
            return 'Total column ice water'

        if table2Version == 200 and indicatorOfParameter == 78:
            return 'Total column liquid water'

        if table2Version == 200 and indicatorOfParameter == 71:
            return 'Biome cover, high vegetation'

        if table2Version == 200 and indicatorOfParameter == 70:
            return 'Biome cover, low vegetation'

        if table2Version == 200 and indicatorOfParameter == 69:
            return 'Minimum stomatal resistance, high vegetation'

        if table2Version == 200 and indicatorOfParameter == 68:
            return 'Minimum stomatal resistance, low vegetation'

        if table2Version == 200 and indicatorOfParameter == 67:
            return 'Leaf area index, high vegetation'

        if table2Version == 200 and indicatorOfParameter == 66:
            return 'Leaf area index, low vegetation'

        if table2Version == 200 and indicatorOfParameter == 65:
            return 'Skin temperature difference'

        if table2Version == 200 and indicatorOfParameter == 64:
            return 'Finish time for skin temperature difference'

        if table2Version == 200 and indicatorOfParameter == 63:
            return 'Start time for skin temperature difference'

        if table2Version == 200 and indicatorOfParameter == 62:
            return 'Observation count difference'

        if table2Version == 200 and indicatorOfParameter == 61:
            return 'Total precipitation from observations difference'

        if table2Version == 200 and indicatorOfParameter == 60:
            return 'Potential vorticity difference'

        if table2Version == 200 and indicatorOfParameter == 59:
            return 'Convective available potential energy difference'

        if table2Version == 200 and indicatorOfParameter == 58:
            return 'Photosynthetically active radiation at the surface difference'

        if table2Version == 200 and indicatorOfParameter == 57:
            return 'Downward UV radiation at the surface difference'

        if table2Version == 200 and indicatorOfParameter == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours difference'

        if table2Version == 200 and indicatorOfParameter == 55:
            return 'Mean 2 metre temperature in the last 24 hours difference'

        if table2Version == 200 and indicatorOfParameter == 54:
            return 'Pressure difference'

        if table2Version == 200 and indicatorOfParameter == 53:
            return 'Montgomery potential difference'

        if table2Version == 200 and indicatorOfParameter == 52:
            return 'Minimum 2 metre temperature difference'

        if table2Version == 200 and indicatorOfParameter == 51:
            return 'Maximum 2 metre temperature difference'

        if table2Version == 200 and indicatorOfParameter == 50:
            return 'Large-scale precipitation fraction difference'

        if table2Version == 200 and indicatorOfParameter == 49:
            return '10 metre wind gust difference'

        if table2Version == 200 and indicatorOfParameter == 48:
            return 'Magnitude of turbulent surface stress difference'

        if table2Version == 200 and indicatorOfParameter == 47:
            return 'Direct solar radiation difference'

        if table2Version == 200 and indicatorOfParameter == 46:
            return 'Solar duration difference'

        if table2Version == 200 and indicatorOfParameter == 45:
            return 'Snowmelt difference'

        if table2Version == 200 and indicatorOfParameter == 44:
            return 'Snow evaporation difference'

        if table2Version == 200 and indicatorOfParameter == 43:
            return 'Soil type difference'

        if table2Version == 200 and indicatorOfParameter == 42:
            return 'Volumetric soil water layer 4 difference'

        if table2Version == 200 and indicatorOfParameter == 41:
            return 'Volumetric soil water layer 3 difference'

        if table2Version == 200 and indicatorOfParameter == 40:
            return 'Volumetric soil water layer 2 difference'

        if table2Version == 200 and indicatorOfParameter == 39:
            return 'Volumetric soil water layer 1 difference'

        if table2Version == 200 and indicatorOfParameter == 38:
            return 'Ice surface temperature layer 4 difference'

        if table2Version == 200 and indicatorOfParameter == 37:
            return 'Ice surface temperature layer 3 difference'

        if table2Version == 200 and indicatorOfParameter == 36:
            return 'Ice surface temperature layer 2 difference'

        if table2Version == 200 and indicatorOfParameter == 35:
            return 'Ice surface temperature layer 1 difference'

        if table2Version == 200 and indicatorOfParameter == 34:
            return 'Sea surface temperature difference'

        if table2Version == 200 and indicatorOfParameter == 33:
            return 'Snow density difference'

        if table2Version == 200 and indicatorOfParameter == 32:
            return 'Snow albedo difference'

        if table2Version == 200 and indicatorOfParameter == 31:
            return 'Sea-ice cover difference'

        if table2Version == 200 and indicatorOfParameter == 30:
            return 'Type of high vegetation difference'

        if table2Version == 200 and indicatorOfParameter == 29:
            return 'Type of low vegetation difference'

        if table2Version == 200 and indicatorOfParameter == 28:
            return 'High vegetation cover difference'

        if table2Version == 200 and indicatorOfParameter == 27:
            return 'Low vegetation cover difference'

        if table2Version == 200 and indicatorOfParameter == 26:
            return 'Lake cover difference'

        if table2Version == 200 and indicatorOfParameter == 25:
            return 'Reserved for future unbalanced components'

        if table2Version == 200 and indicatorOfParameter == 24:
            return 'Reserved for future unbalanced components'

        if table2Version == 200 and indicatorOfParameter == 23:
            return 'Unbalanced component of divergence difference'

        if table2Version == 200 and indicatorOfParameter == 22:
            return 'Unbalanced component of logarithm of surface pressure difference'

        if table2Version == 200 and indicatorOfParameter == 21:
            return 'Unbalanced component of temperature difference'

        if table2Version == 200 and indicatorOfParameter == 14:
            return 'V component of rotational wind difference'

        if table2Version == 200 and indicatorOfParameter == 13:
            return 'U component of rotational wind difference'

        if table2Version == 200 and indicatorOfParameter == 12:
            return 'V component of divergent wind difference'

        if table2Version == 200 and indicatorOfParameter == 11:
            return 'U component of divergent wind difference'

        if table2Version == 200 and indicatorOfParameter == 5:
            return 'Saturated equivalent potential temperature difference'

        if table2Version == 200 and indicatorOfParameter == 4:
            return 'Equivalent potential temperature difference'

        if table2Version == 200 and indicatorOfParameter == 3:
            return 'Potential temperature difference'

        if table2Version == 200 and indicatorOfParameter == 2:
            return 'Velocity potential difference'

        if table2Version == 200 and indicatorOfParameter == 1:
            return 'Stream function difference'

        if table2Version == 190 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 180 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 170 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 160 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 132 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 130 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 128 and indicatorOfParameter == 255:
            return 'Indicates a missing value'

        if table2Version == 128 and indicatorOfParameter == 254:
            return 'Adiabatic tendency of meridional wind'

        if table2Version == 128 and indicatorOfParameter == 253:
            return 'Adiabatic tendency of zonal wind'

        if table2Version == 128 and indicatorOfParameter == 252:
            return 'Adiabatic tendency of humidity'

        if table2Version == 128 and indicatorOfParameter == 251:
            return 'Adiabatic tendency of temperature'

        if table2Version == 128 and indicatorOfParameter == 250:
            return 'Ice age'

        if table2Version == 128 and indicatorOfParameter == 249:
            return 'Accumulated ice water tendency'

        if table2Version == 128 and indicatorOfParameter == 248:
            return 'Fraction of cloud cover'

        if table2Version == 128 and indicatorOfParameter == 247:
            return 'Specific cloud ice water content'

        if table2Version == 128 and indicatorOfParameter == 246:
            return 'Specific cloud liquid water content'

        if table2Version == 160 and indicatorOfParameter == 245:
            return 'Forecast logarithm of surface roughness for heat'

        if table2Version == 128 and indicatorOfParameter == 245:
            return 'Forecast logarithm of surface roughness for heat'

        if table2Version == 160 and indicatorOfParameter == 244:
            return 'Forecast surface roughness'

        if table2Version == 128 and indicatorOfParameter == 244:
            return 'Forecast surface roughness'

        if table2Version == 128 and indicatorOfParameter == 243:
            return 'Forecast albedo'

        if table2Version == 128 and indicatorOfParameter == 242:
            return 'Accumulated liquid water tendency'

        if table2Version == 128 and indicatorOfParameter == 241:
            return 'Accumulated cloud fraction tendency'

        if table2Version == 128 and indicatorOfParameter == 240:
            return 'Large-scale snowfall'

        if table2Version == 128 and indicatorOfParameter == 239:
            return 'Convective snowfall'

        if table2Version == 160 and indicatorOfParameter == 238:
            return 'Temperature of snow layer'

        if table2Version == 128 and indicatorOfParameter == 238:
            return 'Temperature of snow layer'

        if table2Version == 160 and indicatorOfParameter == 237:
            return 'Soil wetness level 4'

        if table2Version == 128 and indicatorOfParameter == 237:
            return 'Soil wetness level 4'

        if table2Version == 160 and indicatorOfParameter == 236:
            return 'Soil temperature level 4'

        if table2Version == 128 and indicatorOfParameter == 236:
            return 'Soil temperature level 4'

        if table2Version == 160 and indicatorOfParameter == 235:
            return 'Skin temperature'

        if table2Version == 128 and indicatorOfParameter == 235:
            return 'Skin temperature'

        if table2Version == 160 and indicatorOfParameter == 234:
            return 'Logarithm of surface roughness length for heat'

        if table2Version == 128 and indicatorOfParameter == 234:
            return 'Logarithm of surface roughness length for heat'

        if table2Version == 160 and indicatorOfParameter == 233:
            return 'Apparent surface humidity'

        if table2Version == 128 and indicatorOfParameter == 233:
            return 'Apparent surface humidity'

        if table2Version == 160 and indicatorOfParameter == 232:
            return 'Instantaneous moisture flux'

        if table2Version == 128 and indicatorOfParameter == 232:
            return 'Instantaneous moisture flux'

        if table2Version == 128 and indicatorOfParameter == 231:
            return 'Instantaneous surface sensible heat flux'

        if table2Version == 160 and indicatorOfParameter == 230:
            return 'Instantaneous northward turbulent surface stress'

        if table2Version == 128 and indicatorOfParameter == 230:
            return 'Instantaneous northward turbulent surface stress'

        if table2Version == 160 and indicatorOfParameter == 229:
            return 'Instantaneous eastward turbulent surface stress'

        if table2Version == 128 and indicatorOfParameter == 229:
            return 'Instantaneous eastward turbulent surface stress'

        if table2Version == 190 and indicatorOfParameter == 228:
            return 'Total precipitation'

        if table2Version == 170 and indicatorOfParameter == 228:
            return 'Total precipitation'

        if table2Version == 160 and indicatorOfParameter == 228:
            return 'Total precipitation'

        if table2Version == 128 and indicatorOfParameter == 228:
            return 'Total precipitation'

        if table2Version == 130 and indicatorOfParameter == 227:
            return 'Tendency due to removal of negative humidity'

        if table2Version == 128 and indicatorOfParameter == 227:
            return 'Tendency due to removal of negative humidity'

        if table2Version == 128 and indicatorOfParameter == 226:
            return 'Humidity tendency by large-scale condensation'

        if table2Version == 128 and indicatorOfParameter == 225:
            return 'Humidity tendency by cumulus convection'

        if table2Version == 128 and indicatorOfParameter == 224:
            return 'Vertical diffusion of humidity'

        if table2Version == 130 and indicatorOfParameter == 223:
            return 'Convective tendency of meridional wind'

        if table2Version == 128 and indicatorOfParameter == 223:
            return 'Convective tendency of meridional wind'

        if table2Version == 130 and indicatorOfParameter == 222:
            return 'Convective tendency of zonal wind'

        if table2Version == 128 and indicatorOfParameter == 222:
            return 'Convective tendency of zonal wind'

        if table2Version == 128 and indicatorOfParameter == 221:
            return 'North-South gravity wave drag tendency'

        if table2Version == 128 and indicatorOfParameter == 220:
            return 'East-West gravity wave drag tendency'

        if table2Version == 128 and indicatorOfParameter == 219:
            return 'Vertical diffusion of meridional wind'

        if table2Version == 128 and indicatorOfParameter == 218:
            return 'Vertical diffusion of zonal wind'

        if table2Version == 128 and indicatorOfParameter == 217:
            return 'Diabatic heating large-scale condensation'

        if table2Version == 128 and indicatorOfParameter == 216:
            return 'Diabatic heating by cumulus convection'

        if table2Version == 128 and indicatorOfParameter == 215:
            return 'Diabatic heating by vertical diffusion'

        if table2Version == 128 and indicatorOfParameter == 214:
            return 'Diabatic heating by radiation'

        if table2Version == 128 and indicatorOfParameter == 213:
            return 'Vertically integrated moisture divergence'

        if table2Version == 128 and indicatorOfParameter == 212:
            return 'TOA incident solar radiation'

        if table2Version == 128 and indicatorOfParameter == 211:
            return 'Surface net thermal radiation, clear sky'

        if table2Version == 128 and indicatorOfParameter == 210:
            return 'Surface net solar radiation, clear sky'

        if table2Version == 128 and indicatorOfParameter == 209:
            return 'Top net thermal radiation, clear sky'

        if table2Version == 128 and indicatorOfParameter == 208:
            return 'Top net solar radiation, clear sky'

        if table2Version == 128 and indicatorOfParameter == 207:
            return '10 metre wind speed'

        if table2Version == 128 and indicatorOfParameter == 206:
            return 'Total column ozone'

        if table2Version == 180 and indicatorOfParameter == 205:
            return 'Runoff'

        if table2Version == 128 and indicatorOfParameter == 205:
            return 'Runoff'

        if table2Version == 160 and indicatorOfParameter == 204:
            return 'Precipitation analysis weights'

        if table2Version == 128 and indicatorOfParameter == 204:
            return 'Precipitation analysis weights'

        if table2Version == 128 and indicatorOfParameter == 203:
            return 'Ozone mass mixing ratio'

        if table2Version == 190 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres since previous post-processing'

        if table2Version == 170 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres since previous post-processing'

        if table2Version == 128 and indicatorOfParameter == 202:
            return 'Minimum temperature at 2 metres since previous post-processing'

        if table2Version == 190 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres since previous post-processing'

        if table2Version == 170 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres since previous post-processing'

        if table2Version == 128 and indicatorOfParameter == 201:
            return 'Maximum temperature at 2 metres since previous post-processing'

        if table2Version == 160 and indicatorOfParameter == 200:
            return 'Variance of sub-gridscale orography'

        if table2Version == 128 and indicatorOfParameter == 200:
            return 'Variance of sub-gridscale orography'

        if table2Version == 128 and indicatorOfParameter == 199:
            return 'Vegetation fraction'

        if table2Version == 128 and indicatorOfParameter == 198:
            return 'Skin reservoir content'

        if table2Version == 160 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation'

        if table2Version == 128 and indicatorOfParameter == 197:
            return 'Gravity wave dissipation'

        if table2Version == 160 and indicatorOfParameter == 196:
            return 'Northward gravity wave surface stress'

        if table2Version == 128 and indicatorOfParameter == 196:
            return 'Northward gravity wave surface stress'

        if table2Version == 160 and indicatorOfParameter == 195:
            return 'Eastward gravity wave surface stress'

        if table2Version == 128 and indicatorOfParameter == 195:
            return 'Eastward gravity wave surface stress'

        if table2Version == 128 and indicatorOfParameter == 194:
            return 'Brightness temperature'

        if table2Version == 160 and indicatorOfParameter == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance'

        if table2Version == 128 and indicatorOfParameter == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance'

        if table2Version == 160 and indicatorOfParameter == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance'

        if table2Version == 128 and indicatorOfParameter == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance'

        if table2Version == 160 and indicatorOfParameter == 191:
            return 'North-South component of sub-gridscale orographic variance'

        if table2Version == 128 and indicatorOfParameter == 191:
            return 'North-South component of sub-gridscale orographic variance'

        if table2Version == 160 and indicatorOfParameter == 190:
            return 'East-West component of sub-gridscale orographic variance'

        if table2Version == 128 and indicatorOfParameter == 190:
            return 'East-West component of sub-gridscale orographic variance'

        if table2Version == 128 and indicatorOfParameter == 189:
            return 'Sunshine duration'

        if table2Version == 160 and indicatorOfParameter == 188:
            return 'High cloud cover'

        if table2Version == 128 and indicatorOfParameter == 188:
            return 'High cloud cover'

        if table2Version == 160 and indicatorOfParameter == 187:
            return 'Medium cloud cover'

        if table2Version == 128 and indicatorOfParameter == 187:
            return 'Medium cloud cover'

        if table2Version == 160 and indicatorOfParameter == 186:
            return 'Low cloud cover'

        if table2Version == 128 and indicatorOfParameter == 186:
            return 'Low cloud cover'

        if table2Version == 170 and indicatorOfParameter == 185:
            return 'Convective cloud cover'

        if table2Version == 160 and indicatorOfParameter == 185:
            return 'Convective cloud cover'

        if table2Version == 128 and indicatorOfParameter == 185:
            return 'Convective cloud cover'

        if table2Version == 170 and indicatorOfParameter == 184:
            return 'Soil wetness level 3'

        if table2Version == 128 and indicatorOfParameter == 184:
            return 'Soil wetness level 3'

        if table2Version == 160 and indicatorOfParameter == 183:
            return 'Soil temperature level 3'

        if table2Version == 128 and indicatorOfParameter == 183:
            return 'Soil temperature level 3'

        if table2Version == 190 and indicatorOfParameter == 182:
            return 'Evaporation'

        if table2Version == 180 and indicatorOfParameter == 182:
            return 'Evaporation'

        if table2Version == 170 and indicatorOfParameter == 182:
            return 'Evaporation'

        if table2Version == 128 and indicatorOfParameter == 182:
            return 'Evaporation'

        if table2Version == 180 and indicatorOfParameter == 181:
            return 'Northward turbulent surface stress'

        if table2Version == 170 and indicatorOfParameter == 181:
            return 'Northward turbulent surface stress'

        if table2Version == 128 and indicatorOfParameter == 181:
            return 'Northward turbulent surface stress'

        if table2Version == 180 and indicatorOfParameter == 180:
            return 'Eastward turbulent surface stress'

        if table2Version == 170 and indicatorOfParameter == 180:
            return 'Eastward turbulent surface stress'

        if table2Version == 128 and indicatorOfParameter == 180:
            return 'Eastward turbulent surface stress'

        if table2Version == 190 and indicatorOfParameter == 179:
            return 'Top net thermal radiation'

        if table2Version == 160 and indicatorOfParameter == 179:
            return 'Top net thermal radiation'

        if table2Version == 128 and indicatorOfParameter == 179:
            return 'Top net thermal radiation'

        if table2Version == 190 and indicatorOfParameter == 178:
            return 'Top net solar radiation'

        if table2Version == 160 and indicatorOfParameter == 178:
            return 'Top net solar radiation'

        if table2Version == 128 and indicatorOfParameter == 178:
            return 'Top net solar radiation'

        if table2Version == 190 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation'

        if table2Version == 170 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation'

        if table2Version == 160 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation'

        if table2Version == 128 and indicatorOfParameter == 177:
            return 'Surface net thermal radiation'

        if table2Version == 190 and indicatorOfParameter == 176:
            return 'Surface net solar radiation'

        if table2Version == 170 and indicatorOfParameter == 176:
            return 'Surface net solar radiation'

        if table2Version == 160 and indicatorOfParameter == 176:
            return 'Surface net solar radiation'

        if table2Version == 128 and indicatorOfParameter == 176:
            return 'Surface net solar radiation'

        if table2Version == 190 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards'

        if table2Version == 128 and indicatorOfParameter == 175:
            return 'Surface thermal radiation downwards'

        if table2Version == 190 and indicatorOfParameter == 174:
            return 'Albedo'

        if table2Version == 160 and indicatorOfParameter == 174:
            return 'Albedo'

        if table2Version == 128 and indicatorOfParameter == 174:
            return 'Albedo'

        if table2Version == 160 and indicatorOfParameter == 173:
            return 'Surface roughness'

        if table2Version == 128 and indicatorOfParameter == 173:
            return 'Surface roughness'

        if table2Version == 190 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 180 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 175 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 174 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 171 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 160 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 128 and indicatorOfParameter == 172:
            return 'Land-sea mask'

        if table2Version == 128 and indicatorOfParameter == 171:
            return 'Soil wetness level 2'

        if table2Version == 160 and indicatorOfParameter == 170:
            return 'Soil temperature level 2'

        if table2Version == 128 and indicatorOfParameter == 170:
            return 'Soil temperature level 2'

        if table2Version == 190 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards'

        if table2Version == 128 and indicatorOfParameter == 169:
            return 'Surface solar radiation downwards'

        if table2Version == 190 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature'

        if table2Version == 180 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature'

        if table2Version == 160 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature'

        if table2Version == 128 and indicatorOfParameter == 168:
            return '2 metre dewpoint temperature'

        if table2Version == 190 and indicatorOfParameter == 167:
            return '2 metre temperature'

        if table2Version == 180 and indicatorOfParameter == 167:
            return '2 metre temperature'

        if table2Version == 160 and indicatorOfParameter == 167:
            return '2 metre temperature'

        if table2Version == 128 and indicatorOfParameter == 167:
            return '2 metre temperature'

        if table2Version == 190 and indicatorOfParameter == 166:
            return '10 metre V wind component'

        if table2Version == 180 and indicatorOfParameter == 166:
            return '10 metre V wind component'

        if table2Version == 160 and indicatorOfParameter == 166:
            return '10 metre V wind component'

        if table2Version == 128 and indicatorOfParameter == 166:
            return '10 metre V wind component'

        if table2Version == 190 and indicatorOfParameter == 165:
            return '10 metre U wind component'

        if table2Version == 180 and indicatorOfParameter == 165:
            return '10 metre U wind component'

        if table2Version == 160 and indicatorOfParameter == 165:
            return '10 metre U wind component'

        if table2Version == 128 and indicatorOfParameter == 165:
            return '10 metre U wind component'

        if table2Version == 190 and indicatorOfParameter == 164:
            return 'Total cloud cover'

        if table2Version == 180 and indicatorOfParameter == 164:
            return 'Total cloud cover'

        if table2Version == 170 and indicatorOfParameter == 164:
            return 'Total cloud cover'

        if table2Version == 160 and indicatorOfParameter == 164:
            return 'Total cloud cover'

        if table2Version == 128 and indicatorOfParameter == 164:
            return 'Total cloud cover'

        if table2Version == 128 and indicatorOfParameter == 163:
            return 'Slope of sub-gridscale orography'

        if table2Version == 128 and indicatorOfParameter == 162:
            return 'Angle of sub-gridscale orography'

        if table2Version == 128 and indicatorOfParameter == 161:
            return 'Anisotropy of sub-gridscale orography'

        if table2Version == 128 and indicatorOfParameter == 160:
            return 'Standard deviation of orography'

        if table2Version == 128 and indicatorOfParameter == 159:
            return 'Boundary layer height'

        if table2Version == 160 and indicatorOfParameter == 158:
            return 'Tendency of surface pressure'

        if table2Version == 128 and indicatorOfParameter == 158:
            return 'Tendency of surface pressure'

        if table2Version == 190 and indicatorOfParameter == 157:
            return 'Relative humidity'

        if table2Version == 170 and indicatorOfParameter == 157:
            return 'Relative humidity'

        if table2Version == 128 and indicatorOfParameter == 157:
            return 'Relative humidity'

        if table2Version == 128 and indicatorOfParameter == 156:
            return 'Geopotential Height'

        if table2Version == 190 and indicatorOfParameter == 155:
            return 'Divergence'

        if table2Version == 180 and indicatorOfParameter == 155:
            return 'Divergence'

        if table2Version == 170 and indicatorOfParameter == 155:
            return 'Divergence'

        if table2Version == 160 and indicatorOfParameter == 155:
            return 'Divergence'

        if table2Version == 128 and indicatorOfParameter == 155:
            return 'Divergence'

        if table2Version == 128 and indicatorOfParameter == 154:
            return 'Long-wave heating rate'

        if table2Version == 128 and indicatorOfParameter == 153:
            return 'Short-wave heating rate'

        if table2Version == 160 and indicatorOfParameter == 152:
            return 'Logarithm of surface pressure'

        if table2Version == 128 and indicatorOfParameter == 152:
            return 'Logarithm of surface pressure'

        if table2Version == 190 and indicatorOfParameter == 151:
            return 'Mean sea level pressure'

        if table2Version == 180 and indicatorOfParameter == 151:
            return 'Mean sea level pressure'

        if table2Version == 170 and indicatorOfParameter == 151:
            return 'Mean sea level pressure'

        if table2Version == 160 and indicatorOfParameter == 151:
            return 'Mean sea level pressure'

        if table2Version == 128 and indicatorOfParameter == 151:
            return 'Mean sea level pressure'

        if table2Version == 128 and indicatorOfParameter == 150:
            return 'Top net radiation'

        if table2Version == 128 and indicatorOfParameter == 149:
            return 'Surface net radiation'

        if table2Version == 128 and indicatorOfParameter == 148:
            return 'Charnock'

        if table2Version == 190 and indicatorOfParameter == 147:
            return 'Surface latent heat flux'

        if table2Version == 180 and indicatorOfParameter == 147:
            return 'Surface latent heat flux'

        if table2Version == 170 and indicatorOfParameter == 147:
            return 'Surface latent heat flux'

        if table2Version == 160 and indicatorOfParameter == 147:
            return 'Surface latent heat flux'

        if table2Version == 128 and indicatorOfParameter == 147:
            return 'Surface latent heat flux'

        if table2Version == 190 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux'

        if table2Version == 180 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux'

        if table2Version == 170 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux'

        if table2Version == 160 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux'

        if table2Version == 128 and indicatorOfParameter == 146:
            return 'Surface sensible heat flux'

        if table2Version == 160 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation'

        if table2Version == 128 and indicatorOfParameter == 145:
            return 'Boundary layer dissipation'

        if table2Version == 180 and indicatorOfParameter == 144:
            return 'Snowfall'

        if table2Version == 128 and indicatorOfParameter == 144:
            return 'Snowfall'

        if table2Version == 180 and indicatorOfParameter == 143:
            return 'Convective precipitation'

        if table2Version == 170 and indicatorOfParameter == 143:
            return 'Convective precipitation'

        if table2Version == 128 and indicatorOfParameter == 143:
            return 'Convective precipitation'

        if table2Version == 180 and indicatorOfParameter == 142:
            return 'Large-scale precipitation'

        if table2Version == 170 and indicatorOfParameter == 142:
            return 'Large-scale precipitation'

        if table2Version == 128 and indicatorOfParameter == 142:
            return 'Large-scale precipitation'

        if table2Version == 180 and indicatorOfParameter == 141:
            return 'Snow depth'

        if table2Version == 170 and indicatorOfParameter == 141:
            return 'Snow depth'

        if table2Version == 128 and indicatorOfParameter == 141:
            return 'Snow depth'

        if table2Version == 170 and indicatorOfParameter == 140:
            return 'Soil wetness level 1'

        if table2Version == 128 and indicatorOfParameter == 140:
            return 'Soil wetness level 1'

        if table2Version == 190 and indicatorOfParameter == 139:
            return 'Soil temperature level 1'

        if table2Version == 170 and indicatorOfParameter == 139:
            return 'Soil temperature level 1'

        if table2Version == 160 and indicatorOfParameter == 139:
            return 'Soil temperature level 1'

        if table2Version == 128 and indicatorOfParameter == 139:
            return 'Soil temperature level 1'

        if table2Version == 190 and indicatorOfParameter == 138:
            return 'Vorticity (relative)'

        if table2Version == 180 and indicatorOfParameter == 138:
            return 'Vorticity (relative)'

        if table2Version == 170 and indicatorOfParameter == 138:
            return 'Vorticity (relative)'

        if table2Version == 160 and indicatorOfParameter == 138:
            return 'Vorticity (relative)'

        if table2Version == 128 and indicatorOfParameter == 138:
            return 'Vorticity (relative)'

        if table2Version == 180 and indicatorOfParameter == 137:
            return 'Total column water vapour'

        if table2Version == 128 and indicatorOfParameter == 137:
            return 'Total column water vapour'

        if table2Version == 160 and indicatorOfParameter == 136:
            return 'Total column water'

        if table2Version == 128 and indicatorOfParameter == 136:
            return 'Total column water'

        if table2Version == 170 and indicatorOfParameter == 135:
            return 'Vertical velocity'

        if table2Version == 128 and indicatorOfParameter == 135:
            return 'Vertical velocity'

        if table2Version == 190 and indicatorOfParameter == 134:
            return 'Surface pressure'

        if table2Version == 180 and indicatorOfParameter == 134:
            return 'Surface pressure'

        if table2Version == 162 and indicatorOfParameter == 52:
            return 'Surface pressure'

        if table2Version == 160 and indicatorOfParameter == 134:
            return 'Surface pressure'

        if table2Version == 128 and indicatorOfParameter == 134:
            return 'Surface pressure'

        if table2Version == 190 and indicatorOfParameter == 133:
            return 'Specific humidity'

        if table2Version == 180 and indicatorOfParameter == 133:
            return 'Specific humidity'

        if table2Version == 170 and indicatorOfParameter == 133:
            return 'Specific humidity'

        if table2Version == 160 and indicatorOfParameter == 133:
            return 'Specific humidity'

        if table2Version == 128 and indicatorOfParameter == 133:
            return 'Specific humidity'

        if table2Version == 190 and indicatorOfParameter == 132:
            return 'V component of wind'

        if table2Version == 180 and indicatorOfParameter == 132:
            return 'V component of wind'

        if table2Version == 170 and indicatorOfParameter == 132:
            return 'V component of wind'

        if table2Version == 160 and indicatorOfParameter == 132:
            return 'V component of wind'

        if table2Version == 128 and indicatorOfParameter == 132:
            return 'V component of wind'

        if table2Version == 190 and indicatorOfParameter == 131:
            return 'U component of wind'

        if table2Version == 180 and indicatorOfParameter == 131:
            return 'U component of wind'

        if table2Version == 170 and indicatorOfParameter == 131:
            return 'U component of wind'

        if table2Version == 160 and indicatorOfParameter == 131:
            return 'U component of wind'

        if table2Version == 128 and indicatorOfParameter == 131:
            return 'U component of wind'

        if table2Version == 190 and indicatorOfParameter == 130:
            return 'Temperature'

        if table2Version == 180 and indicatorOfParameter == 130:
            return 'Temperature'

        if table2Version == 170 and indicatorOfParameter == 130:
            return 'Temperature'

        if table2Version == 160 and indicatorOfParameter == 130:
            return 'Temperature'

        if table2Version == 128 and indicatorOfParameter == 130:
            return 'Temperature'

        if table2Version == 190 and indicatorOfParameter == 129:
            return 'Geopotential'

        if table2Version == 180 and indicatorOfParameter == 129:
            return 'Geopotential'

        if table2Version == 170 and indicatorOfParameter == 129:
            return 'Geopotential'

        if table2Version == 160 and indicatorOfParameter == 129:
            return 'Geopotential'

        if table2Version == 128 and indicatorOfParameter == 129:
            return 'Geopotential'

        if table2Version == 160 and indicatorOfParameter == 128:
            return 'Budget values'

        if table2Version == 128 and indicatorOfParameter == 128:
            return 'Budget values'

        if table2Version == 160 and indicatorOfParameter == 127:
            return 'Atmospheric tide'

        if table2Version == 128 and indicatorOfParameter == 127:
            return 'Atmospheric tide'

        if table2Version == 128 and indicatorOfParameter == 126:
            return 'Generic parameter for sensitive area prediction'

        if table2Version == 128 and indicatorOfParameter == 125:
            return 'Vertically integrated total energy'

        if table2Version == 128 and indicatorOfParameter == 124:
            return 'Surface emissivity'

        if table2Version == 128 and indicatorOfParameter == 123:
            return '10 metre wind gust in the last 6 hours'

        if table2Version == 128 and indicatorOfParameter == 122:
            return 'Minimum temperature at 2 metres in the last 6 hours'

        if table2Version == 128 and indicatorOfParameter == 121:
            return 'Maximum temperature at 2 metres in the last 6 hours'

        if table2Version == 128 and indicatorOfParameter == 120:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 119:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 118:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 117:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 116:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 115:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 114:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 113:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 112:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 111:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 110:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 109:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 108:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 107:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 106:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 105:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 104:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 103:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 102:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 101:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 100:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 99:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 98:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 97:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 96:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 95:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 94:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 93:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 92:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 91:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 90:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 89:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 88:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 87:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 86:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 85:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 84:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 83:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 82:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 81:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 80:
            return 'Experimental product'

        if table2Version == 128 and indicatorOfParameter == 79:
            return 'Total column cloud ice water'

        if table2Version == 128 and indicatorOfParameter == 78:
            return 'Total column cloud liquid water'

        if table2Version == 128 and indicatorOfParameter == 77:
            return 'Eta-coordinate vertical velocity'

        if table2Version == 128 and indicatorOfParameter == 76:
            return 'Specific snow water content'

        if table2Version == 128 and indicatorOfParameter == 75:
            return 'Specific rain water content'

        if table2Version == 128 and indicatorOfParameter == 74:
            return 'Standard deviation of filtered subgrid orography'

        if table2Version == 128 and indicatorOfParameter == 73:
            return 'Instantaneous surface thermal radiation downwards'

        if table2Version == 128 and indicatorOfParameter == 72:
            return 'Instantaneous surface solar radiation downwards'

        if table2Version == 128 and indicatorOfParameter == 71:
            return 'Biome cover, high vegetation'

        if table2Version == 128 and indicatorOfParameter == 70:
            return 'Biome cover, low vegetation'

        if table2Version == 128 and indicatorOfParameter == 69:
            return 'Minimum stomatal resistance, high vegetation'

        if table2Version == 128 and indicatorOfParameter == 68:
            return 'Minimum stomatal resistance, low vegetation'

        if table2Version == 128 and indicatorOfParameter == 67:
            return 'Leaf area index, high vegetation'

        if table2Version == 128 and indicatorOfParameter == 66:
            return 'Leaf area index, low vegetation'

        if table2Version == 128 and indicatorOfParameter == 65:
            return 'Skin temperature difference'

        if table2Version == 128 and indicatorOfParameter == 64:
            return 'Finish time for skin temperature difference'

        if table2Version == 128 and indicatorOfParameter == 63:
            return 'Start time for skin temperature difference'

        if table2Version == 128 and indicatorOfParameter == 62:
            return 'Observation count'

        if table2Version == 128 and indicatorOfParameter == 60:
            return 'Potential vorticity'

        if table2Version == 128 and indicatorOfParameter == 59:
            return 'Convective available potential energy'

        if table2Version == 128 and indicatorOfParameter == 58:
            return 'Photosynthetically active radiation at the surface'

        if table2Version == 128 and indicatorOfParameter == 57:
            return 'Downward UV radiation at the surface'

        if table2Version == 128 and indicatorOfParameter == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours'

        if table2Version == 128 and indicatorOfParameter == 55:
            return 'Mean temperature at 2 metres in the last 24 hours'

        if table2Version == 128 and indicatorOfParameter == 54:
            return 'Pressure'

        if table2Version == 128 and indicatorOfParameter == 53:
            return 'Montgomery potential'

        if table2Version == 128 and indicatorOfParameter == 52:
            return 'Minimum temperature at 2 metres in the last 24 hours'

        if table2Version == 128 and indicatorOfParameter == 51:
            return 'Maximum temperature at 2 metres in the last 24 hours'

        if table2Version == 128 and indicatorOfParameter == 50:
            return 'Large-scale precipitation fraction'

        if table2Version == 128 and indicatorOfParameter == 49:
            return '10 metre wind gust since previous post-processing'

        if table2Version == 128 and indicatorOfParameter == 48:
            return 'Magnitude of turbulent surface stress'

        if table2Version == 128 and indicatorOfParameter == 47:
            return 'Direct solar radiation'

        if table2Version == 128 and indicatorOfParameter == 46:
            return 'Solar duration'

        if table2Version == 128 and indicatorOfParameter == 45:
            return 'Snowmelt'

        if table2Version == 128 and indicatorOfParameter == 44:
            return 'Snow evaporation'

        if table2Version == 128 and indicatorOfParameter == 43:
            return 'Soil type'

        if table2Version == 128 and indicatorOfParameter == 42:
            return 'Volumetric soil water layer 4'

        if table2Version == 128 and indicatorOfParameter == 41:
            return 'Volumetric soil water layer 3'

        if table2Version == 128 and indicatorOfParameter == 40:
            return 'Volumetric soil water layer 2'

        if table2Version == 128 and indicatorOfParameter == 39:
            return 'Volumetric soil water layer 1'

        if table2Version == 128 and indicatorOfParameter == 38:
            return 'Ice temperature layer 4'

        if table2Version == 128 and indicatorOfParameter == 37:
            return 'Ice temperature layer 3'

        if table2Version == 128 and indicatorOfParameter == 36:
            return 'Ice temperature layer 2'

        if table2Version == 128 and indicatorOfParameter == 35:
            return 'Ice temperature layer 1'

        if table2Version == 128 and indicatorOfParameter == 34:
            return 'Sea surface temperature'

        if table2Version == 128 and indicatorOfParameter == 33:
            return 'Snow density'

        if table2Version == 128 and indicatorOfParameter == 32:
            return 'Snow albedo'

        if table2Version == 128 and indicatorOfParameter == 31:
            return 'Sea ice area fraction'

        if table2Version == 128 and indicatorOfParameter == 30:
            return 'Type of high vegetation'

        if table2Version == 128 and indicatorOfParameter == 29:
            return 'Type of low vegetation'

        if table2Version == 128 and indicatorOfParameter == 28:
            return 'High vegetation cover'

        if table2Version == 128 and indicatorOfParameter == 27:
            return 'Low vegetation cover'

        if table2Version == 128 and indicatorOfParameter == 26:
            return 'Lake cover'

        if table2Version == 128 and indicatorOfParameter == 25:
            return 'Reserved for future unbalanced components'

        if table2Version == 128 and indicatorOfParameter == 24:
            return 'Reserved for future unbalanced components'

        if table2Version == 128 and indicatorOfParameter == 23:
            return 'Unbalanced component of divergence'

        if table2Version == 128 and indicatorOfParameter == 22:
            return 'Unbalanced component of logarithm of surface pressure'

        if table2Version == 128 and indicatorOfParameter == 21:
            return 'Unbalanced component of temperature'

        if table2Version == 128 and indicatorOfParameter == 20:
            return 'Clear sky surface photosynthetically active radiation'

        if table2Version == 128 and indicatorOfParameter == 19:
            return 'Clear sky surface UV'

        if table2Version == 128 and indicatorOfParameter == 18:
            return 'Near IR albedo for diffuse radiation'

        if table2Version == 128 and indicatorOfParameter == 17:
            return 'Near IR albedo for direct radiation'

        if table2Version == 128 and indicatorOfParameter == 16:
            return 'UV visible albedo for diffuse radiation'

        if table2Version == 128 and indicatorOfParameter == 15:
            return 'UV visible albedo for direct radiation'

        if table2Version == 128 and indicatorOfParameter == 14:
            return 'V component of rotational wind'

        if table2Version == 128 and indicatorOfParameter == 13:
            return 'U component of rotational wind'

        if table2Version == 128 and indicatorOfParameter == 12:
            return 'V component of divergent wind'

        if table2Version == 128 and indicatorOfParameter == 11:
            return 'U component of divergent wind'

        if table2Version == 128 and indicatorOfParameter == 10:
            return 'Wind speed'

        if table2Version == 128 and indicatorOfParameter == 9:
            return 'Sub-surface runoff'

        if table2Version == 128 and indicatorOfParameter == 8:
            return 'Surface runoff'

        if table2Version == 128 and indicatorOfParameter == 7:
            return 'Soil clay fraction'

        if table2Version == 128 and indicatorOfParameter == 6:
            return 'Soil sand fraction'

        if table2Version == 128 and indicatorOfParameter == 5:
            return 'Saturated equivalent potential temperature'

        if table2Version == 128 and indicatorOfParameter == 4:
            return 'Equivalent potential temperature'

        if table2Version == 128 and indicatorOfParameter == 3:
            return 'Potential temperature'

        if table2Version == 128 and indicatorOfParameter == 2:
            return 'Velocity potential'

        if table2Version == 128 and indicatorOfParameter == 1:
            return 'Stream function'

        if table2Version == 131 and indicatorOfParameter == 88:
            return 'Total precipitation of at least 300 mm'

        if table2Version == 131 and indicatorOfParameter == 87:
            return 'Total precipitation of at least 200 mm'

        if table2Version == 131 and indicatorOfParameter == 86:
            return 'Total precipitation of at least 150 mm'

        if table2Version == 131 and indicatorOfParameter == 85:
            return 'Total precipitation of at least 100 mm'

        if table2Version == 131 and indicatorOfParameter == 84:
            return 'Total precipitation of at least 80 mm'

        if table2Version == 131 and indicatorOfParameter == 83:
            return 'Total precipitation of at least 60 mm'

        if table2Version == 131 and indicatorOfParameter == 82:
            return 'Total precipitation of at least 40 mm'

        if table2Version == 131 and indicatorOfParameter == 63:
            return 'Total precipitation of at least 20 mm'

        if table2Version == 131 and indicatorOfParameter == 62:
            return 'Total precipitation of at least 10 mm'

        if table2Version == 131 and indicatorOfParameter == 61:
            return 'Total precipitation of at least 5 mm'

        if table2Version == 131 and indicatorOfParameter == 60:
            return 'Total precipitation of at least 1 mm'

    return wrapped
