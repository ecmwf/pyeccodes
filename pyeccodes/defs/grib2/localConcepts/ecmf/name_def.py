import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 254:
            return 'ASCAT second soil moisture CDF matching parameter'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 253:
            return 'ASCAT first soil moisture CDF matching parameter'

        localTablesVersion = h.get_l('localTablesVersion')

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 'U-tendency from non-orographic wave drag'

        if localTablesVersion == 228 and discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 'V-tendency from non-orographic wave drag'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 101:
            return 'Wildfire radiative power maximum'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 117:
            return 'Wildfire Flux of Dimethyl Sulfide (DMS) (C2H6S)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 116:
            return 'Wildfire Flux of Ammonia (NH3)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 115:
            return 'Wildfire Flux of Acetone (C3H6O)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 114:
            return 'Wildfire Flux of Acetaldehyde (C2H4O)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 113:
            return 'Wildfire Flux of Formaldehyde (CH2O)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 112:
            return 'Wildfire Flux of Higher Alkanes (CnH2n+2, C>=4)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 111:
            return 'Wildfire Flux of Higher Alkenes (CnH2n, C>=4)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 110:
            return 'Wildfire Flux of Toluene_lump (C7H8+ C6H6 + C8H10)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 109:
            return 'Wildfire Flux of Terpenes (C5H8)n'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 108:
            return 'Wildfire Flux of Isoprene (C5H8)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 107:
            return 'Wildfire Flux of Propene (C3H6)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 106:
            return 'Wildfire Flux of Ethene (C2H4)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 105:
            return 'Wildfire Flux of Propane (C3H8)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 104:
            return 'Wildfire Flux of Ethanol (C2H5OH)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 103:
            return 'Wildfire Flux of Methanol (CH3OH)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 102:
            return 'Wildfire flux of Sulfur Dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 101:
            return 'Wildfire radiative power maximum'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 216:
            return 'V-component stokes drift'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 215:
            return 'U-component stokes drift'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 228:
            return 'Total precipitation significance'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 167:
            return '2 metre temperature significance'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 151:
            return 'Mean sea level pressure significance'

        if discipline == 192 and parameterCategory == 234 and parameterNumber == 139:
            return 'Surface temperature significance'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 132:
            return 'Neutral wind at 10 m v-component'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 131:
            return 'Neutral wind at 10 m u-component'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 19:
            return 'Trapping layer top height'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 18:
            return 'Trapping layer base height'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 17:
            return 'Duct base height'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 16:
            return 'Mean vertical gradient of refractivity inside trapping layer'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 15:
            return 'Minimum vertical gradient of refractivity inside trapping layer'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 14:
            return 'Lake ice depth'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 13:
            return 'Lake ice temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 12:
            return 'Lake shape factor'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 11:
            return 'Lake total layer temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 10:
            return 'Lake bottom temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 9:
            return 'Lake mix-layer depth'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 8:
            return 'Lake mix-layer temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 7:
            return 'Lake depth'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 6:
            return 'Mean total cloud cover'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 5:
            return 'Mean of 10 metre wind speed'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 4:
            return 'Mean temperature at 2 metres'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 3:
            return 'Friction velocity'

        if discipline == 192 and parameterCategory == 220 and parameterNumber == 228:
            return 'Total precipitation observation count'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 216:
            return 'Total Aerosol Optical Depth at 1240nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 215:
            return 'Total Aerosol Optical Depth at 865nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 214:
            return 'Total Aerosol Optical Depth at 670nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 213:
            return 'Total Aerosol Optical Depth at 469nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 212:
            return 'Sulphate Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 211:
            return 'Black Carbon Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 210:
            return 'Organic Matter Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 209:
            return 'Dust Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 208:
            return 'Sea Salt Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 207:
            return 'Total Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 206:
            return 'GEMS Total column ozone'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 203:
            return 'GEMS Ozone'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 185:
            return 'Anthropogenic Emissions of Sulphur Hexafluoride'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 184:
            return 'Total column Sulphur Hexafluoride'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 183:
            return 'Total column Radon'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 182:
            return 'Sulphur Hexafluoride'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 181:
            return 'Radon'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 166:
            return 'Surface flux reactive tracer 10'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 165:
            return 'Surface flux reactive tracer 9'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 164:
            return 'Surface flux reactive tracer 8'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 163:
            return 'Surface flux reactive tracer 7'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 162:
            return 'Surface flux reactive tracer 6'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 161:
            return 'Surface flux reactive tracer 5'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 160:
            return 'Surface flux reactive tracer 4'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 159:
            return 'Surface flux reactive tracer 3'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 158:
            return 'Surface flux reactive tracer 2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 157:
            return 'Surface flux reactive tracer 1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 156:
            return 'Surface flux GEMS Ozone'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 155:
            return 'Surface flux Formaldehyde'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 154:
            return 'Surface flux Carbon monoxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 153:
            return 'Surface flux Sulphur dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 152:
            return 'Surface flux Nitrogen dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 151:
            return 'Surface flux Nitrogen oxides'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 150:
            return 'Total column GRG tracer 10'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 149:
            return 'Reactive tracer 10 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 148:
            return 'Total column GRG tracer 9'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 147:
            return 'Reactive tracer 9 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 146:
            return 'Total column GRG tracer 8'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 145:
            return 'Reactive tracer 8 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 144:
            return 'Total column GRG tracer 7'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 143:
            return 'Reactive tracer 7 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 142:
            return 'Total column GRG tracer 6'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 141:
            return 'Reactive tracer 6 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 140:
            return 'Total column GRG tracer 5'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 139:
            return 'Reactive tracer 5 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 138:
            return 'Total column GRG tracer 4'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 137:
            return 'Reactive tracer 4 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 136:
            return 'Total column GRG tracer 3'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 135:
            return 'Reactive tracer 3 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 134:
            return 'Total column GRG tracer 2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 133:
            return 'Reactive tracer 2 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 132:
            return 'Total column GRG tracer 1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 131:
            return 'Reactive tracer 1 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 130:
            return 'Total Column Nitrogen Oxides'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 129:
            return 'Nitrogen Oxides'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 128:
            return 'Total column Formaldehyde'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 127:
            return 'Total column Carbon monoxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 126:
            return 'Total column Sulphur dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 125:
            return 'Total column Nitrogen dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 124:
            return 'Formaldehyde'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 123:
            return 'Carbon monoxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 122:
            return 'Sulphur dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 121:
            return 'Nitrogen dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 100:
            return 'Wildfire combustion rate'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 99:
            return 'Wildfire radiative power'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 98:
            return 'Wildfire observed area'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 97:
            return 'Wildfire fraction of area observed'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 96:
            return 'Wildfire Fuel Load: Carbon per unit area'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 95:
            return 'Wildfire Combustion Completeness'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 94:
            return 'Wildfire vegetation map index'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 93:
            return 'Wildfire fraction of C4 plants'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 92:
            return 'Wildfire overall flux of burnt Carbon'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 71:
            return 'Methane loss rate due to radical hydroxyl (OH)'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 70:
            return 'Methane Surface Fluxes'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 69:
            return 'Anthropogenic emissions of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 68:
            return 'Natural biosphere flux of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 67:
            return 'Ocean flux of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 66:
            return 'Total column Nitrous oxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 65:
            return 'Total column Methane'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 64:
            return 'Total column Carbon Dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 63:
            return 'Nitrous oxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 62:
            return 'Methane'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 61:
            return 'Carbon Dioxide'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 54:
            return 'Soil clay content'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 53:
            return 'Lifting threshold speed'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 52:
            return 'Dust emission potential'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 51:
            return 'Aerosol large mode optical depth'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 50:
            return 'Aerosol small mode optical depth'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 49:
            return 'Aerosol precursor optical depth'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 48:
            return 'Aerosol large mode mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 47:
            return 'Aerosol small mode mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 46:
            return 'Aerosol precursor mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 42:
            return 'Aerosol type 12 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 41:
            return 'Aerosol type 11 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 40:
            return 'Aerosol type 10 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 39:
            return 'Aerosol type 9 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 38:
            return 'Aerosol type 8 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 37:
            return 'Aerosol type 7 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 36:
            return 'Aerosol type 6 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 35:
            return 'Aerosol type 5 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 34:
            return 'Aerosol type 4 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 33:
            return 'Aerosol type 3 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 32:
            return 'Aerosol type 2 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 31:
            return 'Aerosol type 1 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 27:
            return 'Aerosol type 12 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 26:
            return 'Aerosol type 11 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 25:
            return 'Aerosol type 10 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 24:
            return 'Aerosol type 9 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 23:
            return 'Aerosol type 8 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 22:
            return 'Aerosol type 7 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 21:
            return 'Aerosol type 6 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 20:
            return 'Aerosol type 5 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 19:
            return 'Aerosol type 4 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 18:
            return 'Aerosol type 3 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 17:
            return 'Aerosol type 2 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 16:
            return 'Aerosol type 1 source/gain accumulated'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 12:
            return 'Aerosol type 12 mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 11:
            return 'Sulphate Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 10:
            return 'Hydrophobic Black Carbon Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 9:
            return 'Hydrophilic Black Carbon Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 8:
            return 'Hydrophobic Organic Matter Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 7:
            return 'Hydrophilic Organic Matter Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 6:
            return 'Dust Aerosol (0.9 - 20 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 5:
            return 'Dust Aerosol (0.55 - 0.9 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 4:
            return 'Dust Aerosol (0.03 - 0.55 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 3:
            return 'Sea Salt Aerosol (5 - 20 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 2:
            return 'Sea Salt Aerosol (0.5 - 5 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 1:
            return 'Sea Salt Aerosol (0.03 - 0.5 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 216:
            return 'Total Aerosol Optical Depth at 1240nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 215:
            return 'Total Aerosol Optical Depth at 865nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 214:
            return 'Total Aerosol Optical Depth at 670nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 213:
            return 'Total Aerosol Optical Depth at 469nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 212:
            return 'Sulphate Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 211:
            return 'Black Carbon Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 210:
            return 'Organic Matter Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 209:
            return 'Dust Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 208:
            return 'Sea Salt Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 207:
            return 'Total Aerosol Optical Depth at 550nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 206:
            return 'GEMS Total column ozone'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 203:
            return 'GEMS Ozone'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 185:
            return 'Anthropogenic Emissions of Sulphur Hexafluoride'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 184:
            return 'Total column Sulphur Hexafluoride'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 183:
            return 'Total column Radon'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 182:
            return 'Sulphur Hexafluoride'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 181:
            return 'Radon'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 166:
            return 'Surface flux reactive tracer 10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 165:
            return 'Surface flux reactive tracer 9'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 164:
            return 'Surface flux reactive tracer 8'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 163:
            return 'Surface flux reactive tracer 7'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 162:
            return 'Surface flux reactive tracer 6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 161:
            return 'Surface flux reactive tracer 5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 160:
            return 'Surface flux reactive tracer 4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 159:
            return 'Surface flux reactive tracer 3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 158:
            return 'Surface flux reactive tracer 2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 157:
            return 'Surface flux reactive tracer 1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 156:
            return 'Surface flux GEMS Ozone'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 155:
            return 'Surface flux Formaldehyde'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 154:
            return 'Surface flux Carbon monoxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 153:
            return 'Surface flux Sulphur dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 152:
            return 'Surface flux Nitrogen dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 151:
            return 'Surface flux Nitrogen oxides'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 150:
            return 'Total column GRG tracer 10'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 149:
            return 'Reactive tracer 10 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 148:
            return 'Total column GRG tracer 9'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 147:
            return 'Reactive tracer 9 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 146:
            return 'Total column GRG tracer 8'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 145:
            return 'Reactive tracer 8 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 144:
            return 'Total column GRG tracer 7'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 143:
            return 'Reactive tracer 7 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 142:
            return 'Total column GRG tracer 6'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 141:
            return 'Reactive tracer 6 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 140:
            return 'Total column GRG tracer 5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 139:
            return 'Reactive tracer 5 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 138:
            return 'Total column GRG tracer 4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 137:
            return 'Reactive tracer 4 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 136:
            return 'Total column GRG tracer 3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 135:
            return 'Reactive tracer 3 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 134:
            return 'Total column GRG tracer 2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 133:
            return 'Reactive tracer 2 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 132:
            return 'Total column GRG tracer 1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 131:
            return 'Reactive tracer 1 mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 130:
            return 'Total Column Nitrogen Oxides'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 129:
            return 'Nitrogen Oxides'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 128:
            return 'Total column Formaldehyde'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 127:
            return 'Total column Carbon monoxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 126:
            return 'Total column Sulphur dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 125:
            return 'Total column Nitrogen dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 124:
            return 'Formaldehyde'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 123:
            return 'Carbon monoxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 122:
            return 'Sulphur dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 121:
            return 'Nitrogen dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 100:
            return 'Wildfire combustion rate'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 99:
            return 'Wildfire radiative power'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 98:
            return 'Number of positive FRP pixels per grid cell'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 97:
            return 'Wildfire fraction of area observed'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 96:
            return 'Wildfire Fuel Load: Carbon per unit area'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 95:
            return 'Wildfire Combustion Completeness'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 94:
            return 'Wildfire vegetation map index'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 93:
            return 'Wildfire fraction of C4 plants'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 92:
            return 'Wildfire overall flux of burnt Carbon'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 91:
            return 'Wildfire flux of Black Carbon'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 90:
            return 'Wildfire flux of Organic Carbon'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 89:
            return 'Wildfire flux of Total Carbon in Aerosols'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 88:
            return 'Wildfire flux of Total Particulate Matter'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 87:
            return 'Wildfire flux of Particulate Matter PM2.5'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 86:
            return 'Wildfire flux of Nitrous Oxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 85:
            return 'Wildfire flux of Nitrogen Oxides NOx'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 84:
            return 'Wildfire flux of Hydrogen'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 83:
            return 'Wildfire flux of Non-Methane Hydro-Carbons'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 82:
            return 'Wildfire flux of Methane'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 81:
            return 'Wildfire flux of Carbon Monoxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 80:
            return 'Wildfire flux of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 71:
            return 'Methane loss rate due to radical hydroxyl (OH)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 70:
            return 'Methane Surface Fluxes'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 69:
            return 'Anthropogenic emissions of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 68:
            return 'Natural biosphere flux of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 67:
            return 'Ocean flux of Carbon Dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 66:
            return 'Total column Nitrous oxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 65:
            return 'CH4 column-mean molar fraction'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 64:
            return 'CO2 column-mean molar fraction'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 63:
            return 'Nitrous oxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 62:
            return 'Methane'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 61:
            return 'Carbon Dioxide'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 54:
            return 'Soil clay content'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 53:
            return 'Lifting threshold speed'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 52:
            return 'Dust emission potential'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 51:
            return 'Aerosol large mode optical depth'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 50:
            return 'Aerosol small mode optical depth'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 49:
            return 'Aerosol precursor optical depth'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 48:
            return 'Aerosol large mode mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 47:
            return 'Aerosol small mode mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 46:
            return 'Aerosol precursor mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 42:
            return 'Aerosol type 12 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 41:
            return 'Aerosol type 11 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 40:
            return 'Aerosol type 10 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 39:
            return 'Aerosol type 9 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 38:
            return 'Aerosol type 8 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 37:
            return 'Aerosol type 7 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 36:
            return 'Aerosol type 6 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 35:
            return 'Aerosol type 5 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 34:
            return 'Aerosol type 4 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 33:
            return 'Aerosol type 3 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 32:
            return 'Aerosol type 2 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 31:
            return 'Aerosol type 1 sink/loss accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 27:
            return 'Aerosol type 12 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 26:
            return 'Aerosol type 11 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 25:
            return 'Aerosol type 10 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 24:
            return 'Aerosol type 9 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 23:
            return 'Aerosol type 8 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 22:
            return 'Aerosol type 7 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 21:
            return 'Aerosol type 6 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 20:
            return 'Aerosol type 5 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 19:
            return 'Aerosol type 4 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 18:
            return 'Aerosol type 3 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 17:
            return 'Aerosol type 2 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 16:
            return 'Aerosol type 1 source/gain accumulated'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 12:
            return 'SO2 precursor mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 11:
            return 'Sulphate Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 10:
            return 'Hydrophobic Black Carbon Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 9:
            return 'Hydrophilic Black Carbon Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 8:
            return 'Hydrophobic Organic Matter Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 7:
            return 'Hydrophilic Organic Matter Aerosol Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 6:
            return 'Dust Aerosol (0.9 - 20 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 5:
            return 'Dust Aerosol (0.55 - 0.9 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 4:
            return 'Dust Aerosol (0.03 - 0.55 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 3:
            return 'Sea Salt Aerosol (5 - 20 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 2:
            return 'Sea Salt Aerosol (0.5 - 5 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 1:
            return 'Sea Salt Aerosol (0.03 - 0.5 um) Mixing Ratio'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 241:
            return 'convective available potential energy'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 215:
            return 'ice surface temperature'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 203:
            return 'snow temperature'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 200:
            return 'water content of interception store'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 187:
            return 'Maximum wind velocity'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 150:
            return 'coefficient of horizontal diffusion'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 139:
            return 'deviation of pressure from reference value'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 113:
            return 'surface precipitation amount, rain, convective'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 112:
            return 'surface precipitation rate, snow, convective'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 111:
            return 'surface precipitation rate, rain, convective'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 102:
            return 'surface precipitation amount, rain, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 101:
            return 'surface precipitation rate, snow, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 100:
            return 'surface precipitation rate, rain, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 99:
            return 'spec. content of precip. particles'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 85:
            return 'height of snow-fall limit'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 84:
            return 'height of 0 degree Celsius isotherm above msl'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 83:
            return 'dry convection top index'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 82:
            return 'top of dry convection (above msl)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 81:
            return 'convective divergence tendency'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 80:
            return 'convective vorticity tendency'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 79:
            return 'convective momentum tendency (Y-component)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 78:
            return 'convective momentum tendency (X-component)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 77:
            return 'convective tendency of total water'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 76:
            return 'convective tendency of total heat'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 75:
            return 'convective tendency of specific humidity'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 74:
            return 'convective temperature tendency'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 73:
            return 'convection top index'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 72:
            return 'convection base index'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 71:
            return 'KO-index'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 70:
            return 'convective layers (00...77)  (BKE)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 69:
            return 'cloud top, convective clouds (above msl)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 68:
            return 'cloud base, convective clouds (above msl)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 67:
            return 'entrainment parameter, convection'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 66:
            return 'Updraft velocity, convection'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 65:
            return 'convective mass flux'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 64:
            return 'cloud ice content, conv clouds, vert integrated'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 63:
            return 'specific cloud ice content, convective clouds'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 62:
            return 'cloud water content, conv clouds, vert integrated'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 61:
            return 'specific cloud water content, convective clouds'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 60:
            return 'cloud cover, convective cirrus'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 56:
            return 'fog'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 55:
            return 'fog (0..8)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 54:
            return 'total cloud cover (0..8)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 53:
            return 'cloud cover CL (0..8)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 52:
            return 'cloud cover CM (0..8)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 51:
            return 'cloud cover CH (0..8)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 50:
            return 'cloud covers CH_CM_CL (000...888)'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 42:
            return 'vert. integral of divergence of tot. water content'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 41:
            return 'total column water'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 38:
            return 'specific snow content, gs, vert. integrated'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 37:
            return 'specific rainwater content, gs, vert. integrated'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 36:
            return 'specific snow content, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 35:
            return 'specific rainwater content, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 34:
            return 'cloud ice content, grid scale, vert integrated'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 33:
            return 'specific cloud ice content, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 32:
            return 'cloud water content, grid scale, vert integrated'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 31:
            return 'specific cloud water content'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 30:
            return 'cloud cover, grid scale'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 29:
            return 'fractional cloud cover'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 17:
            return 'soil heat flux, bottom of layer'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 16:
            return 'soil heat flux, surface'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 15:
            return 'total radiative heating rate'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 14:
            return 'longwave radiative heating rate'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 13:
            return 'shortwave radiative heating rate'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 12:
            return 'upw longw radiant flux density, cloudy part'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 11:
            return 'downw longw radiant flux density, cloudfree part'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 10:
            return 'upw shortw radiant flux density, cloudy part'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 9:
            return 'downw shortw radiant flux density, cloudfree part'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 8:
            return 'total net radiative flux density'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 7:
            return 'net longwave flux'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 6:
            return 'net shortwave flux'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 5:
            return 'downwd photosynthetic active radiant flux density'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 4:
            return 'upward longwave radiant flux density'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 3:
            return 'downward longwave radiant flux density'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 2:
            return 'upward shortwave radiant flux density'

        if discipline == 192 and parameterCategory == 201 and parameterNumber == 1:
            return 'downward shortwave radiant flux density'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 168:
            return '2 metre dewpoint temperature difference'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 229:
            return 'Total soil moisture'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 173:
            return 'Roughness length'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 171:
            return 'Wilting point'

        if discipline == 192 and parameterCategory == 190 and parameterNumber == 170:
            return 'Field capacity'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 179:
            return 'Top net thermal radiation'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 178:
            return 'Top net solar radiation'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 177:
            return 'Surface net thermal radiation'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 176:
            return 'Surface net solar radiation'

        if discipline == 192 and parameterCategory == 180 and parameterNumber == 149:
            return 'Total soil wetness'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 236:
            return 'Soil temperature layer 4'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 202:
            return '1.5m temperature - minimum in the last 24 hours'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 201:
            return '1.5m temperature - maximum in the last 24 hours'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 183:
            return 'Soil temperature layer 3'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 175:
            return 'Average salinity in upper 293.4m'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 170:
            return 'Soil temperature layer 2'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 168:
            return '1.5m dewpoint temperature'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 167:
            return '1.5m temperature'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 164:
            return 'Average potential temperature in upper 293.4m'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 139:
            return 'Soil temperature layer 1'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 111:
            return 'Ocean mean ice depth'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 110:
            return 'Ocean ice concentration'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 90:
            return 'Top outgoing solar radiation'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 89:
            return 'Top incoming solar radiation'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 88:
            return '1.5m dewpoint temperature over land'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 87:
            return '1.5m temperature over land'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 86:
            return '10m V wind over land'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 85:
            return '10m U wind over land'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 83:
            return 'Net primary productivity'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 55:
            return '1.5m temperature - mean in the last 24 hours'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 49:
            return '10m wind gust in the last 24 hours'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 42:
            return 'Volumetric soil water layer 4'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 41:
            return 'Volumetric soil water layer 3'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 40:
            return 'Volumetric soil water layer 2'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 39:
            return 'Volumetric soil water layer 1'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 34:
            return 'Open-sea surface temperature'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 31:
            return 'Fraction of sea-ice in sea'

        if discipline == 192 and parameterCategory == 175 and parameterNumber == 6:
            return 'Total soil moisture'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 236:
            return 'Soil temperature layer 4'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 202:
            return '1.5m temperature - minimum in the last 24 hours'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 201:
            return '1.5m temperature - maximum in the last 24 hours'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 183:
            return 'Soil temperature layer 3'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 175:
            return 'Average salinity in upper 293.4m'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 170:
            return 'Soil temperature layer 2'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 168:
            return '1.5m dewpoint temperature'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 167:
            return '1.5m temperature'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 164:
            return 'Average potential temperature in upper 293.4m'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 139:
            return 'Soil temperature layer 1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 111:
            return 'Ocean mean ice depth'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 110:
            return 'Ocean ice concentration'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 99:
            return 'Liquid water potential temperature'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 95:
            return '1.5m specific humidity'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 94:
            return 'Mean sea surface temperature'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 90:
            return 'Top outgoing solar radiation'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 89:
            return 'Top incoming solar radiation'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 88:
            return '1.5m dewpoint temperature over land'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 87:
            return '1.5m temperature over land'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 86:
            return '10m V wind over land'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 85:
            return '10m U wind over land'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 83:
            return 'Net primary productivity'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 55:
            return '1.5m temperature - mean in the last 24 hours'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 49:
            return '10 metre wind gust in the last 24 hours'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 42:
            return 'Volumetric soil water layer 4'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 41:
            return 'Volumetric soil water layer 3'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 40:
            return 'Volumetric soil water layer 2'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 39:
            return 'Volumetric soil water layer 1'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 34:
            return 'Open-sea surface temperature'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 31:
            return 'Fraction of sea-ice in sea'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 9:
            return 'Sub-surface runoff'

        if discipline == 192 and parameterCategory == 174 and parameterNumber == 6:
            return 'Total soil moisture'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 240:
            return 'Large scale snowfall anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 239:
            return 'Convective snowfall anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 228:
            return 'Total precipitation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 212:
            return 'Solar insolation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 211:
            return 'Surface net thermal radiation, clear sky anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 210:
            return 'Surface net solar radiation, clear sky anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 209:
            return 'Top net thermal radiation, clear sky anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 208:
            return 'Top net solar radiation, clear sky anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 205:
            return 'Runoff anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 197:
            return 'Gravity wave dissipation anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 196:
            return 'Meridional component of gravity wave stress anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 195:
            return 'Longitudinal component of gravity wave stress anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 189:
            return 'Sunshine duration anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 182:
            return 'Evaporation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 181:
            return 'North-South surface stress anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 180:
            return 'East-West surface stress anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 179:
            return 'Top thermal radiation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 178:
            return 'Top solar radiation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 177:
            return 'Surface thermal radiation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 176:
            return 'Surface solar radiation anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 175:
            return 'Surface thermal radiation downwards anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 169:
            return 'Surface solar radiation downwards anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 154:
            return 'Long-wave heating rate anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 153:
            return 'Short-wave heating rate anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 149:
            return 'Surface net radiation anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 147:
            return 'Surface latent heat flux anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 146:
            return 'Surface sensible heat flux anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 145:
            return 'Boundary layer dissipation anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 144:
            return 'Snowfall (convective + stratiform) anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 143:
            return 'Mean convective precipitation rate anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 142:
            return 'Stratiform precipitation (Large-scale precipitation) anomalous rate of accumulation'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 50:
            return 'Large-scale precipitation fraction anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 48:
            return 'Magnitude of turbulent surface stress anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 45:
            return 'Snowmelt anomaly'

        if discipline == 192 and parameterCategory == 173 and parameterNumber == 44:
            return 'Snow evaporation anomaly'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 240:
            return 'Large scale snowfall'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 239:
            return 'Convective snowfall'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 228:
            return 'Mean total precipitation rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 212:
            return 'Solar insolation rate of accumulation'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 211:
            return 'Surface net thermal radiation, clear sky'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 210:
            return 'Surface net solar radiation, clear sky'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 209:
            return 'Top net thermal radiation, clear sky'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 208:
            return 'Top net solar radiation, clear sky'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 205:
            return 'Mean runoff rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 197:
            return 'Gravity wave dissipation'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 196:
            return 'Meridional component of gravity wave stress'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 195:
            return 'Longitudinal component of gravity wave stress'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 189:
            return 'Mean sunshine duration rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 182:
            return 'Evaporation'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 181:
            return 'North-South surface stress rate of accumulation'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 180:
            return 'East-West surface stress rate of accumulation'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 179:
            return 'Mean top net thermal radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 178:
            return 'Mean top net solar radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 177:
            return 'Mean surface net thermal radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 176:
            return 'Mean surface net solar radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 175:
            return 'Mean surface downward thermal radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 169:
            return 'Mean surface downward solar radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 154:
            return 'Mean long-wave heating rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 153:
            return 'Mean short-wave heating rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 149:
            return 'Mean surface net radiation flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 147:
            return 'Mean surface latent heat flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 146:
            return 'Mean surface sensible heat flux'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 145:
            return 'Boundary layer dissipation'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 144:
            return 'Mean total snowfall rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 143:
            return 'Mean convective precipitation rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 142:
            return 'Mean large-scale precipitation rate'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 50:
            return 'Mean large-scale precipitation fraction'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 48:
            return 'Magnitude of turbulent surface stress'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 45:
            return 'Snowmelt'

        if discipline == 192 and parameterCategory == 172 and parameterNumber == 44:
            return 'Snow evaporation'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 254:
            return 'Adiabatic tendency of meridional wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 253:
            return 'Adiabatic tendency of zonal wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 252:
            return 'Adiabatic tendency of humidity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 251:
            return 'Adiabatic tendency of temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 250:
            return 'Ice age anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 249:
            return 'Accumulated ice water tendency anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 248:
            return 'Cloud cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 247:
            return 'Cloud ice water content anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 246:
            return 'Cloud liquid water content anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 245:
            return 'Forecast logarithm of surface roughness for heat anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 244:
            return 'Forecast surface roughness anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 243:
            return 'Forecast albedo anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 242:
            return 'Accumulated liquid water tendency anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 241:
            return 'Accumulated cloud fraction tendency anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 240:
            return 'Large scale snowfall anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 239:
            return 'Convective snowfall anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 238:
            return 'Temperature of snow layer anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 237:
            return 'Soil wetness level 4 anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 236:
            return 'Soil temperature level 4 anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 235:
            return 'Skin temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 234:
            return 'Logarithm of surface roughness length for heat anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 233:
            return 'Apparent surface humidity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 232:
            return 'Instantaneous moisture flux anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 231:
            return 'Instantaneous surface heat flux anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 230:
            return 'Instantaneous Y surface stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 229:
            return 'Instantaneous X surface stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 228:
            return 'Total precipitation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 227:
            return 'Change from removal of negative humidity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 226:
            return 'Humidity tendency by large-scale condensation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 225:
            return 'Humidity tendency by cumulus convection anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 224:
            return 'Vertical diffusion of humidity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 223:
            return 'Convective tendency of meridional wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 222:
            return 'Convective tendency of zonal wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 221:
            return 'North-South gravity wave drag tendency anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 220:
            return 'East-West gravity wave drag tendency anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 219:
            return 'Vertical diffusion of meridional wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 218:
            return 'Vertical diffusion of zonal wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 217:
            return 'Diabatic heating by large-scale condensation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 216:
            return 'Diabatic heating by cumulus convection anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 215:
            return 'Diabatic heating by vertical diffusion anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 214:
            return 'Diabatic heating by radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 212:
            return 'Solar insolation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 211:
            return 'Surface net thermal radiation, clear sky anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 210:
            return 'Surface net solar radiation clear sky anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 209:
            return 'Top net thermal radiation clear sky anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 208:
            return 'Top net solar radiation clear sky anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 207:
            return '10 metre wind speed anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 206:
            return 'Total column ozone anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 205:
            return 'Runoff anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 204:
            return 'Precipitation analysis weights anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 203:
            return 'Ozone mass mixing ratio anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 202:
            return 'Minimum temperature at 2 metres anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 201:
            return 'Maximum temperature at 2 metres anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 200:
            return 'Variance of sub-gridscale orography anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 199:
            return 'Vegetation fraction anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 198:
            return 'Skin reservoir content anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 197:
            return 'Gravity wave dissipation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 196:
            return 'Meridional component of gravity wave stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 195:
            return 'Longitudinal component of gravity wave stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 194:
            return 'Brightness temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 191:
            return 'North-South component of sub-gridscale orographic variance anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 190:
            return 'East-West component of sub-gridscale orographic variance anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 189:
            return 'Sunshine duration anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 188:
            return 'High cloud cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 187:
            return 'Medium cloud cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 186:
            return 'Low cloud cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 185:
            return 'Convective cloud cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 184:
            return 'Soil wetness anomaly level 3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 183:
            return 'Soil temperature anomaly level 3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 182:
            return 'Evaporation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 181:
            return 'North-South surface stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 180:
            return 'East-West surface stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 179:
            return 'Top net thermal radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 178:
            return 'Top net solar radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 177:
            return 'Surface net thermal radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 176:
            return 'Surface net solar radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 175:
            return 'Surface thermal radiation downwards anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 174:
            return 'Albedo anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 173:
            return 'Surface roughness anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 171:
            return 'Soil wetness anomaly level 2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 170:
            return 'Soil temperature anomaly level 2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 169:
            return 'Surface solar radiation downwards anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 168:
            return '2 metre dewpoint temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 167:
            return '2 metre temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 166:
            return '10 metre V wind component anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 165:
            return '10 metre U wind component anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 164:
            return 'Total cloud cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 163:
            return 'Slope of sub-gridscale orography anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 162:
            return 'Angle of sub-gridscale orography anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 161:
            return 'Anisotropy of sub-gridscale orography anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 160:
            return 'Standard deviation of orography anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 159:
            return 'Boundary layer height anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 158:
            return 'Tendency of surface pressure anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 157:
            return 'Relative humidity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 156:
            return 'Height anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 155:
            return 'Relative divergence anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 154:
            return 'Long-wave heating rate anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 153:
            return 'Short-wave heating rate anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 152:
            return 'Logarithm of surface pressure anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 151:
            return 'Mean sea level pressure anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 150:
            return 'Top net radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 149:
            return 'Surface net radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 148:
            return 'Charnock anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 147:
            return 'Surface latent heat flux anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 146:
            return 'Surface sensible heat flux anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 145:
            return 'Boundary layer dissipation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 144:
            return 'Snowfall (convective + stratiform) anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 143:
            return 'Convective precipitation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 142:
            return 'Stratiform precipitation (Large-scale precipitation) anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 141:
            return 'Snow depth anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 140:
            return 'Soil wetness anomaly level 1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 139:
            return 'Soil temperature anomaly level 1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 138:
            return 'Relative vorticity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 137:
            return 'Total column water vapour anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 136:
            return 'Total column water anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 135:
            return 'Vertical velocity (pressure) anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 134:
            return 'Surface pressure anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 133:
            return 'Specific humidity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 132:
            return 'V component of wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 131:
            return 'U component of wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 130:
            return 'Temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 129:
            return 'Geopotential anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 128:
            return 'Budget values anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 127:
            return 'Atmospheric tide anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 126:
            return 'Generic parameter for sensitive area prediction'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 125:
            return 'Vertically integrated total energy anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 79:
            return 'Total column ice water anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 78:
            return 'Total column liquid water anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 65:
            return 'Skin temperature difference anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 64:
            return 'Finish time for skin temperature difference anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 63:
            return 'Start time for skin temperature difference anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 62:
            return 'Observation count anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 61:
            return 'Total precipitation from observations anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 60:
            return 'Potential vorticity anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 59:
            return 'Convective available potential energy anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 58:
            return 'Photosynthetically active radiation at the surface anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 57:
            return 'Downward UV radiation at the surface anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 55:
            return 'Mean 2 metre temperature in the last 24 hours anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 54:
            return 'Pressure anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 53:
            return 'Montgomery potential anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 52:
            return 'Minimum 2 metre temperature in the last 24 hours anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 51:
            return 'Maximum 2 metre temperature in the last 24 hours anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 50:
            return 'Large-scale precipitation fraction anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 49:
            return '10 metre wind gust anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 48:
            return 'Magnitude of turbulent surface stress anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 47:
            return 'Direct solar radiation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 46:
            return 'Solar duration anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 45:
            return 'Snowmelt anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 44:
            return 'Snow evaporation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 43:
            return 'Soil type anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 42:
            return 'Volumetric soil water anomaly layer 4'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 41:
            return 'Volumetric soil water anomaly layer 3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 40:
            return 'Volumetric soil water anomaly layer 2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 39:
            return 'Volumetric soil water anomaly layer 1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 38:
            return 'Ice surface temperature anomaly layer 4'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 37:
            return 'Ice surface temperature anomaly layer 3'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 36:
            return 'Ice surface temperature anomaly layer 2'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 35:
            return 'Ice surface temperature anomaly layer 1'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 34:
            return 'Sea surface temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 33:
            return 'Snow density anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 32:
            return 'Snow albedo anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 31:
            return 'Sea-ice cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 30:
            return 'Type of high vegetation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 29:
            return 'Type of low vegetation anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 28:
            return 'High vegetation cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 27:
            return 'Low vegetation cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 26:
            return 'Lake cover anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 23:
            return 'Unbalanced component of divergence anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 22:
            return 'Unbalanced component of logarithm of surface pressure anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 21:
            return 'Unbalanced component of temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 14:
            return 'V component of rotational wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 13:
            return 'U component of rotational wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 12:
            return 'V component of divergent wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 11:
            return 'U component of divergent wind anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 5:
            return 'Saturated equivalent potential temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 4:
            return 'Equivalent potential temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 3:
            return 'Potential temperature anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 2:
            return 'Velocity potential anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 1:
            return 'Stream function anomaly'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 179:
            return 'Top net thermal radiation'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 171:
            return 'Soil wetness level 2'

        if discipline == 192 and parameterCategory == 170 and parameterNumber == 149:
            return 'Total soil moisture'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 233:
            return 'Variance of ozone'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 232:
            return 'Covariance of omega/ozone'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 231:
            return 'Covariance of v component/ozone'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 230:
            return 'Covariance of u component/ozone'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 229:
            return 'Variance of relative humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 227:
            return 'Variance of surface pressure'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 226:
            return 'Variance of omega'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 225:
            return 'Covariance of omega/v component'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 224:
            return 'Covariance of omega/u component'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 223:
            return 'Covariance of omega/specific humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 222:
            return 'Covariance of omega/temperature'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 221:
            return 'Covariance of omega/geopotential'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 220:
            return 'Variance of v component'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 219:
            return 'Covariance of v component/u component'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 218:
            return 'Covariance of v component/specific humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 217:
            return 'Covariance of v component/temperature'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 216:
            return 'Covariance of v component/geopotential'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 215:
            return 'Variance of u component'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 214:
            return 'Covariance of u component/specific humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 213:
            return 'Covariance of u component/temperature'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 212:
            return 'Covariance of u component/geopotential'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 211:
            return 'Variance of specific humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 210:
            return 'Covariance of temperature/specific humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 209:
            return 'Covariance of geopotential/specific humidity'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 208:
            return 'Variance of temperature'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 207:
            return 'Covariance of geopotential/temperature'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 206:
            return 'Variance of geopotential'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 113:
            return 'Tendency of v component due to physics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 112:
            return 'Tendency of u component due to physics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 111:
            return 'Tendency of specific humidity due to physics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 110:
            return 'Tendency of temperature due to physics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 109:
            return 'Turbulent diffusion coefficient for heat'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 108:
            return 'Total precipitation flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 107:
            return 'Downdraught detrainment rate'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 106:
            return 'Updraught detrainment rate'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 105:
            return 'Downdraught mass flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 104:
            return 'Updraught mass flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 103:
            return 'Tendency of clear sky long wave radiation'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 102:
            return 'Tendency of clear sky short wave radiation'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 101:
            return 'Tendency of long wave radiation'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 100:
            return 'Tendency of short wave radiation'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 87:
            return 'Vertical integral of divergence of ozone flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 86:
            return 'Vertical integral of divergence of total energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 85:
            return 'Vertical integral of divergence of geopotential flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 84:
            return 'Vertical integral of divergence of moisture flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 83:
            return 'Vertical integral of divergence of thermal energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 82:
            return 'Vertical integral of divergence of kinetic energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 81:
            return 'Vertical integral of divergence of mass flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 78:
            return 'Vertical integral of northward ozone flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 77:
            return 'Vertical integral of eastward ozone flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 76:
            return 'Vertical integral of northward total energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 75:
            return 'Vertical integral of eastward total energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 74:
            return 'Vertical integral of northward geopotential flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 73:
            return 'Vertical integral of eastward geopotential flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 72:
            return 'Vertical integral of northward water vapour flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 71:
            return 'Vertical integral of eastward water vapour flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 70:
            return 'Vertical integral of northward heat flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 69:
            return 'Vertical integral of eastward heat flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 68:
            return 'Vertical integral of northward kinetic energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 67:
            return 'Vertical integral of eastward kinetic energy flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 66:
            return 'Vertical integral of northward mass flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 65:
            return 'Vertical integral of eastward mass flux'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 64:
            return 'Vertical integral of energy conversion'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 63:
            return 'Vertical integral of total energy'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 62:
            return 'Vertical integral of potential+internal+latent energy'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 61:
            return 'Vertical integral of potential+internal energy'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 60:
            return 'Vertical integral of thermal energy'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 59:
            return 'Vertical integral of kinetic energy'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 58:
            return 'Vertical integral of ozone'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 57:
            return 'Vertical integral of cloud frozen water'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 56:
            return 'Vertical integral of cloud liquid water'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 55:
            return 'Vertical integral of water vapour'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 54:
            return 'Vertical integral of temperature'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 53:
            return 'Vertical integral of mass of atmosphere'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 51:
            return 'Surface geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 254:
            return 'Heaviside beta function'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 249:
            return 'Gravity wave dissipation flux'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 247:
            return 'Momentum flux'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 246:
            return '10 metre wind speed'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 243:
            return 'Forecast albedo'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 242:
            return 'Cloud cover'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 241:
            return 'Cloud liquid water content'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 240:
            return 'Large scale snowfall'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 239:
            return 'Convective snowfall'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 231:
            return 'Instantaneous surface heat flux'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 226:
            return 'Standard deviation of vertical velocity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 225:
            return 'Covariance of W component and V component'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 224:
            return 'Covariance of W component and U component'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 223:
            return 'Covariance of W component and specific humidity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 222:
            return 'Covariance of W component and temperature'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 221:
            return 'Covariance of W component and geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 220:
            return 'Standard deviation of V component'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 219:
            return 'Covariance of V component and U component'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 218:
            return 'Covariance of V component and specific humidity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 217:
            return 'Covariance of V component and temperature'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 216:
            return 'Covariance of V component and geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 215:
            return 'Standard deviation of U velocity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 214:
            return 'Covariance of U component and specific humidity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 213:
            return 'Covariance of U component and temperature'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 212:
            return 'Covariance of U component and geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 211:
            return 'Standard deviation of specific humidity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 210:
            return 'Covariance of specific humidity and temperature'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 209:
            return 'Covariance of specific humidity and geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 208:
            return 'Standard deviation of temperature'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 207:
            return 'Covariance of temperature and geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 206:
            return 'Standard deviation of geopotential'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 205:
            return 'Runoff'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 202:
            return 'Minimum temperature at 2 metres during averaging time'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 201:
            return 'Maximum temperature at 2 metres during averaging time'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 199:
            return 'Percentage of vegetation'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 198:
            return 'Skin reservoir content'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 184:
            return 'Soil wetness level 3'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 182:
            return 'Evaporation'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 181:
            return 'North-South surface stress'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 180:
            return 'East-West surface stress'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 171:
            return 'Soil wetness level 2'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 157:
            return 'Relative humidity'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 156:
            return 'Height'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 144:
            return 'Snowfall'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 143:
            return 'Convective precipitation'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 142:
            return 'Large-scale precipitation'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 140:
            return 'Soil wetness level 1'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 137:
            return 'Precipitable water content'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 135:
            return 'vertical velocity (pressure)'

        if discipline == 192 and parameterCategory == 160 and parameterNumber == 49:
            return '10 metre wind gust during averaging time'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 212:
            return 'Bias in salinity (applied)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 211:
            return 'Bias in temperature(applied)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 210:
            return 'FG bias in pressure'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 209:
            return 'Applied bias in pressure'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 208:
            return 'First guess bias in salinity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 207:
            return 'First guess bias in temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 206:
            return 'Estimated salinity bias from relaxation'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 205:
            return 'Estimated temperature bias from relaxation'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 204:
            return 'Bias in the meridional pressure gradient (applied)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 203:
            return 'Bias in the zonal pressure gradient (applied)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 202:
            return 'Salinity increment from relaxation term'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 201:
            return 'Temperature increment from relaxation term'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 200:
            return 'Estimated salinity bias from assimilation'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 199:
            return 'Estimated temperature bias from assimilation'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 194:
            return 'Salinity background error'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 192:
            return 'Background Salinity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 191:
            return 'Salinity analysis error'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 190:
            return 'Salinity increment (from salinity data)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 188:
            return 'Meridional Velocity increment (from balance operator)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 187:
            return 'Zonal Velocity increment (from balance operator)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 186:
            return 'Estimated Bias in Salinity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 185:
            return 'Estimated Bias in Temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 184:
            return 'Salinity increment'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 183:
            return 'Analysed salinity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 182:
            return 'Potential temperature background error'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 181:
            return 'Analysed potential temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 180:
            return 'Background potential temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 179:
            return 'Potential temperature analysis error'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 178:
            return 'Potential temperature increment'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 177:
            return 'Layer Thickness at vector points'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 176:
            return 'Layer Thickness at scalar points'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 174:
            return 'Depth of salinity maximum'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 173:
            return 'Salinity maximum'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 172:
            return 'Depth of the velocity maximum'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 171:
            return 'U velocity maximum'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 170:
            return 'Vertically integrated meridional heat transport'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 169:
            return 'Vertically integrated zonal heat transport'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 168:
            return 'Vertically integrated meridional volume transport'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 167:
            return 'Vertically integrated zonal volume transport'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 166:
            return 'Vertically Integrated meridional velocity (previous time step)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 165:
            return 'Vertically integrated zonal velocity (previous time step)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 164:
            return 'Average potential temperature in the upper 300m'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 162:
            return 'Heat flux correction'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 161:
            return 'Diagnosed sea surface temperature error'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 160:
            return 'Specified surface heat flux'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 159:
            return 'Specified sea surface temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 158:
            return 'Precipitation - evaporation'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 157:
            return 'Absorbed solar radiation'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 156:
            return 'Net surface heat flux'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 155:
            return 'Turbulent kinetic energy input'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 154:
            return 'Surface downward northward stress'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 153:
            return 'Surface downward eastward stress'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 152:
            return 'Divergence of wind stress'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 151:
            return 'Curl of Wind Stress'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 150:
            return 'Steric height'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 149:
            return 'Bottom Pressure (equivalent height)'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 148:
            return 'Mixed layer depth'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 147:
            return 'Ocean barotropic stream function'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 146:
            return 'Sea level previous timestep'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 144:
            return 'VV product'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 143:
            return 'UU product'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 142:
            return 'VT product'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 141:
            return 'UT product'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 140:
            return 'UV product'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 139:
            return 'Richardson number'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 138:
            return 'Sea water sigma theta'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 137:
            return 'Bottom level Depth'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 136:
            return 'Vertical diffusivity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 135:
            return 'Vertical viscosity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 134:
            return 'Modulus of strain rate tensor'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 133:
            return 'Upward sea water velocity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 130:
            return 'Sea water practical salinity'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 129:
            return 'Sea water potential temperature'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 128:
            return 'In situ Temperature'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 183:
            return 'Observed heat flux'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 182:
            return 'Observed sea surface temperature'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 181:
            return 'Heat flux correction'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 180:
            return 'Diagnosed sea surface temperature error'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 173:
            return 'P-E'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 172:
            return 'Surface solar radiation'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 171:
            return 'Net surface heat flux'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 170:
            return 'Turbulent kinetic energy input'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 169:
            return 'V stress'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 168:
            return 'U stress'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 155:
            return 'Depth'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 154:
            return 'Mixed layer depth'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 153:
            return 'Barotropic stream function'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 152:
            return 'Sea level'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 148:
            return 'VV - V~V~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 147:
            return 'UU - U~U~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 146:
            return 'VT - V~T~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 145:
            return 'UT - U~T~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 144:
            return 'UV - U~V~'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 143:
            return 'V*V product'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 142:
            return 'U*U product'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 141:
            return 'V*T product'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 140:
            return 'U*T product'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 139:
            return 'U*V product'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 137:
            return 'Richardson number'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 135:
            return 'Ocean W wind component'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 134:
            return 'Ocean V wind component'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 133:
            return 'Ocean U wind component'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 131:
            return 'Ocean potential density'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 130:
            return 'Ocean salinity'

        if discipline == 192 and parameterCategory == 150 and parameterNumber == 129:
            return 'Ocean potential temperature'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 254:
            return 'Wave spectral peakedness'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 253:
            return 'Benjamin-Feir index'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 252:
            return 'Wave spectral kurtosis'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 251:
            return '2D wave spectra (single)'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 250:
            return '2D wave spectra (multiple)'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 249:
            return '10 metre wind direction'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 248:
            return 'Altimeter range relative correction'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 247:
            return 'Altimeter corrected wave height'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 246:
            return 'Altimeter wave height'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 245:
            return '10 metre wind speed'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 244:
            return 'Mean square slope of waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 243:
            return 'Standard deviation of 10 metre wind speed'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 242:
            return 'Mean wind direction'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 241:
            return 'Mean of 10 metre wind speed'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 240:
            return 'Standard deviation wave height'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 239:
            return 'Mean period of total swell'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 238:
            return 'Mean direction of total swell'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 237:
            return 'Significant height of total swell'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 'Mean period of wind waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 235:
            return 'Mean direction of wind waves'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 'Significant height of wind waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 233:
            return 'Coefficient of drag with waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 231:
            return 'Peak wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 'Peak wave period'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 228:
            return 'Wave spectral directional width for swell'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 227:
            return 'Mean wave period based on second moment for swell'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 226:
            return 'Mean wave period based on first moment for swell'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 225:
            return 'Wave spectral directional width for wind waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 224:
            return 'Mean wave period based on second moment for wind waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 223:
            return 'Mean wave period based on first moment for wind waves'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 222:
            return 'Wave spectral directional width'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 221:
            return 'Mean zero-crossing wave period'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 'Mean zero-crossing wave period'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 220:
            return 'Mean wave period based on first moment'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 219:
            return 'Model bathymetry'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 218:
            return 'Maximum individual wave height'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 217:
            return 'Period corresponding to maximum individual wave height'

        if discipline == 192 and parameterCategory == 140 and parameterNumber == 200:
            return 'Maximum of significant wave height'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 92:
            return 'Low Cloud Cover probability greater than 99%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 91:
            return 'Low Cloud Cover probability greater than 90%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 90:
            return 'Low Cloud Cover probability greater than 80%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 89:
            return 'Low Cloud Cover probability greater than 70%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 88:
            return 'Low Cloud Cover probability greater than 60%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 87:
            return 'Low Cloud Cover probability greater than 50%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 86:
            return 'Low Cloud Cover probability greater than 40%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 85:
            return 'Low Cloud Cover probability greater than 30%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 84:
            return 'Low Cloud Cover probability greater than 20%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 83:
            return 'Low Cloud Cover probability greater than 10%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 82:
            return 'Medium Cloud Cover probability greater than 99%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 81:
            return 'Medium Cloud Cover probability greater than 90%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 80:
            return 'Medium Cloud Cover probability greater than 80%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 79:
            return 'Medium Cloud Cover probability greater than 70%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 78:
            return 'Medium Cloud Cover probability greater than 60%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 77:
            return 'Medium Cloud Cover probability greater than 50%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 76:
            return 'Medium Cloud Cover probability greater than 40%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 75:
            return 'Medium Cloud Cover probability greater than 30%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 74:
            return 'Medium Cloud Cover probability greater than 20%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 73:
            return 'Medium Cloud Cover probability greater than 10%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 72:
            return 'High Cloud Cover probability greater than 99%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 71:
            return 'High Cloud Cover probability greater than 90%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 70:
            return 'High Cloud Cover probability greater than 80%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 69:
            return 'High Cloud Cover probability greater than 70%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 68:
            return 'High Cloud Cover probability greater than 60%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 67:
            return 'High Cloud Cover probability greater than 50%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 66:
            return 'High Cloud Cover probability greater than 40%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 65:
            return 'High Cloud Cover probability greater than 30%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 64:
            return 'High Cloud Cover probability greater than 20%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 63:
            return 'High Cloud Cover probability greater than 10%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 62:
            return 'Total Cloud Cover probability greater than 99%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 61:
            return 'Total Cloud Cover probability greater than 90%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 60:
            return 'Total Cloud Cover probability greater than 80%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 59:
            return 'Total Cloud Cover probability greater than 70%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 58:
            return 'Total Cloud Cover probability greater than 60%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 57:
            return 'Total Cloud Cover probability greater than 50%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 56:
            return 'Total Cloud Cover probability greater than 40%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 55:
            return 'Total Cloud Cover probability greater than 30%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 54:
            return 'Total Cloud Cover probability greater than 20%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 53:
            return 'Total Cloud Cover probability greater than 10%'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 52:
            return 'Snowfall probability of at least 300 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 51:
            return 'Snowfall probability of at least 200 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 50:
            return 'Snowfall probability of at least 150 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 49:
            return 'Snowfall probability of at least 100 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 48:
            return 'Snowfall probability of at least 80 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 47:
            return 'Snowfall probability of at least 60 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 46:
            return 'Snowfall probability of at least 40 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 45:
            return 'Snowfall probability of at least 20 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 44:
            return 'Snowfall probability of at least 10 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 43:
            return 'Snowfall probability of at least 5 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 42:
            return 'Snowfall probability of at least 1 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 41:
            return 'Total precipitation probability of at least 300 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 40:
            return 'Total precipitation probability of at least 200 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 39:
            return 'Total precipitation probability of at least 150 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 38:
            return 'Total precipitation probability of at least 100 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 37:
            return 'Total precipitation probability of at least 80 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 36:
            return 'Total precipitation probability of at least 60 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 35:
            return 'Total precipitation probability of at least 40 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 34:
            return 'Total precipitation probability of at least 20 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 33:
            return 'Total precipitation probability of at least 10 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 32:
            return 'Total precipitation probability of at least 5 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 31:
            return 'Total precipitation probability of at least 1 mm'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 30:
            return '10 metre wind gust probability of at least 100 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 29:
            return '10 metre wind gust probability of at least 75 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 28:
            return '10 metre wind gust probability of at least 50 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 27:
            return '10 metre wind gust probability of at least 35 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 26:
            return '10 metre wind gust probability of at least 20 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 25:
            return '10 metre wind speed probability of at least 50 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 24:
            return '10 metre wind speed probability of at least 35 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 23:
            return '10 metre wind speed probability of at least 20 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 22:
            return '10 metre wind speed probability of at least 15 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 21:
            return '10 metre wind speed probability of at least 10 m/s'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 20:
            return 'Maximum 2 metre temperature probability greater than 45 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 19:
            return 'Maximum 2 metre temperature probability greater than 40 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 18:
            return 'Maximum 2 metre temperature probability greater than 35 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 17:
            return 'Maximum 2 metre temperature probability greater than 30 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 16:
            return 'Maximum 2 metre temperature probability greater than 25 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 15:
            return 'Minimum 2 metre temperature probability less than 10 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 14:
            return 'Minimum 2 metre temperature probability less than 5 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 13:
            return 'Minimum 2 metre temperature probability less than 0 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 12:
            return 'Minimum 2 metre temperature probability less than -5 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 11:
            return 'Minimum 2 metre temperature probability less than -10 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 10:
            return '2m temperature probability greater than 45 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 9:
            return '2m temperature probability greater than 40 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 8:
            return '2m temperature probability greater than 35 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 7:
            return '2m temperature probability greater than 30 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 6:
            return '2m temperature probability greater than 25 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 5:
            return '2m temperature probability less than 10 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 4:
            return '2m temperature probability less than 5 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 3:
            return '2m temperature probability less than 0 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 2:
            return '2m temperature probability less than -5 C'

        if discipline == 192 and parameterCategory == 133 and parameterNumber == 1:
            return '2m temperature probability less than -10 C'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 232:
            return 'Mean wave period probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 229:
            return 'Significant wave height probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 228:
            return 'Total precipitation probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 202:
            return 'Minimum 2 metre temperature probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 201:
            return 'Maximum 2 metre temperature probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 167:
            return '2 metre temperature probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 165:
            return '10 metre speed probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 164:
            return 'Total cloud cover probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 151:
            return 'Mean sea level pressure probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 144:
            return 'Snowfall (convective + stratiform) probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 139:
            return 'Soil temperature level 1 probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 130:
            return 'Temperature anomaly probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 129:
            return 'Geopotential probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 81:
            return 'Mean wave period of at least 15 s'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 80:
            return 'Mean wave period of at least 12 s'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 79:
            return 'Mean wave period of at least 10 s'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 78:
            return 'Mean wave period of at least 8 s'

        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        probabilityType = h.get_l('probabilityType')

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaledValueOfLowerLimit == 8 and typeOfFirstFixedSurface == 101 and productDefinitionTemplateNumber == 5 and scaleFactorOfLowerLimit == 0 and probabilityType == 3:
            return 'Significant wave height of at least 8 m'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 6 and productDefinitionTemplateNumber == 5 and typeOfFirstFixedSurface == 101 and probabilityType == 3:
            return 'Significant wave height of at least 6 m'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and probabilityType == 3 and typeOfFirstFixedSurface == 101 and productDefinitionTemplateNumber == 5 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 4:
            return 'Significant wave height of at least 4 m'

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 5 and scaledValueOfLowerLimit == 2 and typeOfFirstFixedSurface == 101 and probabilityType == 3:
            return 'Significant wave height of at least 2 m'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 73:
            return '2 metre temperature less than 273.15 K'

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfLowerLimit == 25 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 103 and probabilityType == 3:
            return '10 metre wind gust of at least 25 m/s'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 69:
            return '10 metre Wind speed of at least 15 m/s'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 68:
            return '10 metre Wind speed of at least 10 m/s'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 67:
            return 'Total precipitation rate of at least 5 mm/day'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 66:
            return 'Total precipitation rate of at least 3 mm/day'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 65:
            return 'Total precipitation rate less than 1 mm/day'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 64:
            return 'Total precipitation less than 0.1 mm'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 59:
            return 'Convective available potential energy probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 49:
            return '10 metre wind gust probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 25:
            return 'Temperature anomaly greater than +8 K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 24:
            return 'Temperature anomaly greater than +4 K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 23:
            return 'Temperature anomaly less than -4 K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 22:
            return 'Temperature anomaly less than -8 K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 21:
            return 'Temperature anomaly of at least +2 K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 20:
            return 'Temperature anomaly less than -2 K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 18:
            return 'Whiting index probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 17:
            return 'Showalter index probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 16:
            return 'Height of snowfall limit probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 15:
            return 'Height of 0 degree isotherm probability'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 10:
            return 'Mean sea level pressure anomaly of at least 0 Pa'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 9:
            return 'Surface temperature anomaly of at least 0K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 8:
            return 'Total precipitation anomaly of at least 0 mm'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 7:
            return 'Total precipitation anomaly of at least 10 mm'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 6:
            return 'Total precipitation anomaly of at least 20 mm'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 5:
            return '2m temperature anomaly of at most -2K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 4:
            return '2m temperature anomaly of at most -1K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 3:
            return '2m temperature anomaly of at least 0K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 2:
            return '2m temperature anomaly of at least +1K'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 1:
            return '2m temperature anomaly of at least +2K'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 232:
            return 'Mean vertical velocity'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 231:
            return 'Adiabatic tendency of meridional wind'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 230:
            return 'Adiabatic tendency of zonal wind'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 229:
            return 'Adiabatic tendency of humidity'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 228:
            return 'Adiabatic tendency of temperature'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 226:
            return 'Humidity tendency by large-scale condensation'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 225:
            return 'Humidity tendency by cumulus convection'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 224:
            return 'Vertical diffusion of humidity'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 221:
            return 'North-South gravity wave drag'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 220:
            return 'East-West gravity wave drag'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 219:
            return 'Vertical diffusion of meridional wind'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 218:
            return 'Vertical diffusion of zonal wind'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 217:
            return 'Diabatic heating by large-scale condensation'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 216:
            return 'Diabatic heating by cumulus convection'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 215:
            return 'Diabatic heating by vertical diffusion'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 214:
            return 'Diabatic heating by radiation'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 213:
            return 'Cloud fraction'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 212:
            return 'Cloud liquid water'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 211:
            return 'Top thermal radiation upward, clear sky'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 210:
            return 'Top solar radiation upward, clear sky'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 209:
            return 'Top thermal radiation upward'

        if discipline == 192 and parameterCategory == 130 and parameterNumber == 208:
            return 'Top solar radiation upward'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 254:
            return 'Adiabatic tendency of meridional wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 253:
            return 'Adiabatic tendency of zonal wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 252:
            return 'Adiabatic tendency of humidity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 251:
            return 'Adiabatic tendency of temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 250:
            return 'Ice age gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 249:
            return 'Accumulated ice water tendency gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 248:
            return 'Cloud cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 247:
            return 'Specific cloud ice water content gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 246:
            return 'Specific cloud liquid water content gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 245:
            return 'Forecast logarithm of surface roughness for heat gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 244:
            return 'Forecast surface roughness gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 243:
            return 'Forecast albedo gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 242:
            return 'Accumulated liquid water tendency gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 241:
            return 'Accumulated cloud fraction tendency gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 240:
            return 'Large scale snowfall gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 239:
            return 'Convective snowfall gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 238:
            return 'Temperature of snow layer gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 237:
            return 'Soil wetness level 4 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 236:
            return 'Soil temperature level 4 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 235:
            return 'Skin temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 234:
            return 'Logarithm of surface roughness length for heat gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 233:
            return 'Apparent surface humidity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 232:
            return 'Instantaneous moisture flux gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 231:
            return 'Instantaneous surface heat flux gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 230:
            return 'Instantaneous Y surface stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 229:
            return 'Instantaneous X surface stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 228:
            return 'Total precipitation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 227:
            return 'Change from removal of negative humidity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 226:
            return 'Humidity tendency by large-scale condensation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 225:
            return 'Humidity tendency by cumulus convection gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 224:
            return 'Vertical diffusion of humidity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 223:
            return 'Convective tendency of meridional wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 222:
            return 'Convective tendency of zonal wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 221:
            return 'North-South gravity wave drag tendency gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 220:
            return 'East-West gravity wave drag tendency gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 219:
            return 'Vertical diffusion of meridional wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 218:
            return 'Vertical diffusion of zonal wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 217:
            return 'Diabatic heating large-scale condensation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 216:
            return 'Diabatic heating by cumulus convection gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 215:
            return 'Diabatic heating by vertical diffusion gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 214:
            return 'Diabatic heating by radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 212:
            return 'TOA incident solar radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 211:
            return 'Surface net thermal radiation, clear sky gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 210:
            return 'Surface net solar radiation, clear sky gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 209:
            return 'Top net thermal radiation, clear sky gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 208:
            return 'Top net solar radiation, clear sky gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 207:
            return '10 metre wind speed gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 206:
            return 'Total column ozone gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 205:
            return 'Runoff gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 204:
            return 'Precipitation analysis weights gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 203:
            return 'Ozone mass mixing ratio gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 202:
            return 'Minimum temperature at 2 metres since previous post-processing gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 201:
            return 'Maximum temperature at 2 metres since previous post-processing gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 200:
            return 'Variance of sub-gridscale orography gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 199:
            return 'Vegetation fraction gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 198:
            return 'Skin reservoir content gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 197:
            return 'Gravity wave dissipation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 196:
            return 'Meridional component of gravity wave stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 195:
            return 'Longitudinal component of gravity wave stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 194:
            return 'Brightness temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 191:
            return 'North-South component of sub-gridscale orographic variance gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 190:
            return 'East-West component of sub-gridscale orographic variance gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 189:
            return 'Sunshine duration gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 188:
            return 'High cloud cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 187:
            return 'Medium cloud cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 186:
            return 'Low cloud cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 185:
            return 'Convective cloud cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 184:
            return 'Soil wetness level 3 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 183:
            return 'Soil temperature level 3 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 182:
            return 'Evaporation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 181:
            return 'North-South surface stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 180:
            return 'East-West surface stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 179:
            return 'Top net thermal radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 178:
            return 'Top net solar radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 177:
            return 'Surface net thermal radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 176:
            return 'Surface net solar radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 175:
            return 'Surface thermal radiation downwards gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 174:
            return 'Albedo gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 173:
            return 'Surface roughness gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 172:
            return 'Land-sea mask gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 171:
            return 'Soil wetness level 2 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 170:
            return 'Soil temperature level 2 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 169:
            return 'Surface solar radiation downwards gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 168:
            return '2 metre dewpoint temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 167:
            return '2 metre temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 166:
            return '10 metre V wind component gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 165:
            return '10 metre U wind component gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 164:
            return 'Total cloud cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 163:
            return 'Slope of sub-gridscale orography gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 162:
            return 'Angle of sub-gridscale orography gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 161:
            return 'Anisotropy of sub-gridscale orography gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 160:
            return 'Standard deviation of orography gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 159:
            return 'Boundary layer height gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 158:
            return 'Tendency of surface pressure gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 157:
            return 'Relative humidity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 156:
            return 'Height gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 155:
            return 'Divergence gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 154:
            return 'Long-wave heating rate gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 153:
            return 'Short-wave heating rate gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 152:
            return 'Logarithm of surface pressure gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 151:
            return 'Mean sea level pressure gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 150:
            return 'Top net radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 149:
            return 'Surface net radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 148:
            return 'Charnock gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 147:
            return 'Surface latent heat flux gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 146:
            return 'Surface sensible heat flux gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 145:
            return 'Boundary layer dissipation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 144:
            return 'Snowfall (convective + stratiform) gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 143:
            return 'Convective precipitation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 142:
            return 'Stratiform precipitation (Large-scale precipitation) gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 141:
            return 'Snow depth gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 140:
            return 'Soil wetness level 1 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 139:
            return 'Soil temperature level 1 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 138:
            return 'Vorticity (relative) gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 137:
            return 'Total column water vapour gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 136:
            return 'Total column water gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 135:
            return 'vertical velocity (pressure) gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 134:
            return 'Surface pressure gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 133:
            return 'Specific humidity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 132:
            return 'V component of wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 131:
            return 'U component of wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 130:
            return 'Temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 129:
            return 'Geopotential gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 128:
            return 'Budget values gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 127:
            return 'Atmospheric tide gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 126:
            return 'Generic parameter for sensitive area prediction'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 125:
            return 'Vertically integrated total energy'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 123:
            return '10 metre wind gust in the last 6 hours gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 122:
            return 'Minimum temperature at 2 metres gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 121:
            return 'Maximum temperature at 2 metres gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 120:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 119:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 118:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 117:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 116:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 115:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 114:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 113:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 112:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 111:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 110:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 109:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 108:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 107:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 106:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 105:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 104:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 103:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 102:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 101:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 100:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 99:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 98:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 97:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 96:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 95:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 94:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 93:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 92:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 91:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 90:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 89:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 88:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 87:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 86:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 85:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 84:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 83:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 82:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 81:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 80:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 79:
            return 'Total column ice water'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 78:
            return 'Total column liquid water'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 71:
            return 'Biome cover, high vegetation'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 70:
            return 'Biome cover, low vegetation'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 69:
            return 'Minimum stomatal resistance, high vegetation'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 68:
            return 'Minimum stomatal resistance, low vegetation'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 67:
            return 'Leaf area index, high vegetation'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 66:
            return 'Leaf area index, low vegetation'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 65:
            return 'Skin temperature difference'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 64:
            return 'Finish time for skin temperature difference'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 63:
            return 'Start time for skin temperature difference'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 62:
            return 'Observation count gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 61:
            return 'Total precipitation from observations gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 60:
            return 'Potential vorticity gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 59:
            return 'Convective available potential energy gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 58:
            return 'Photosynthetically active radiation at the surface gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 57:
            return 'Downward UV radiation at the surface gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 55:
            return 'Mean 2 metre temperature in the last 24 hours gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 54:
            return 'Pressure gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 53:
            return 'Montgomery potential gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 52:
            return 'Minimum 2 metre temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 51:
            return 'Maximum 2 metre temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 50:
            return 'Large-scale precipitation fraction gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 49:
            return '10 metre wind gust gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 48:
            return 'Magnitude of turbulent surface stress gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 47:
            return 'Direct solar radiation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 46:
            return 'Solar duration gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 45:
            return 'Snowmelt gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 44:
            return 'Snow evaporation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 43:
            return 'Soil type gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 42:
            return 'Volumetric soil water layer 4 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 41:
            return 'Volumetric soil water layer 3 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 40:
            return 'Volumetric soil water layer 2 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 39:
            return 'Volumetric soil water layer 1 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 38:
            return 'Ice surface temperature layer 4 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 37:
            return 'Ice surface temperature layer 3 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 36:
            return 'Ice surface temperature layer 2 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 35:
            return 'Ice surface temperature layer 1 gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 34:
            return 'Sea surface temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 33:
            return 'Snow density gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 32:
            return 'Snow albedo gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 31:
            return 'Sea-ice cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 30:
            return 'Type of high vegetation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 29:
            return 'Type of low vegetation gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 28:
            return 'High vegetation cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 27:
            return 'Low vegetation cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 26:
            return 'Lake cover gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 25:
            return 'Reserved for future unbalanced components'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 24:
            return 'Reserved for future unbalanced components'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 23:
            return 'Unbalanced component of divergence gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 22:
            return 'Unbalanced component of logarithm of surface pressure gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 21:
            return 'Unbalanced component of temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 14:
            return 'V component of rotational wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 13:
            return 'U component of rotational wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 12:
            return 'V component of divergent wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 11:
            return 'U component of divergent wind gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 5:
            return 'Saturated equivalent potential temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 4:
            return 'Equivalent potential temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 3:
            return 'Potential temperature gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 2:
            return 'Velocity potential gradient'

        if discipline == 192 and parameterCategory == 129 and parameterNumber == 1:
            return 'Stream function gradient'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 255:
            return 'Surface long wave-effective total cloudiness'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 252:
            return 'Irrigation'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 251:
            return 'Potential evaporation'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 250:
            return 'Irrigation fraction'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 248:
            return 'Surface short wave-effective total cloudiness'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 130:
            return 'Surface thermal radiation downward clear-sky'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 129:
            return 'Surface solar radiation downward clear-sky'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 103:
            return 'Evaporation from vegetation transpiration'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 102:
            return 'Evaporation from open water surfaces excluding oceans'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 101:
            return 'Evaporation from bare soil'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 100:
            return 'Evaporation from the top of canopy'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 94:
            return 'Ice temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 93:
            return 'Volumetric soil moisture'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 92:
            return 'Soil texture fraction'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 91:
            return 'Canopy cover fraction'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 90:
            return 'Total column snow water'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 89:
            return 'Total column rain water'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 'Flux of Carbon Dioxide Ecosystem Respiration'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 'Flux of Carbon Dioxide Gross Primary Production'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 'Flux of Carbon Dioxide Net Ecosystem Exchange'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 'Accumulated Carbon Dioxide Ecosystem Respiration'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 'Accumulated Carbon Dioxide Gross Primary Production'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 'Accumulated Carbon Dioxide Net Ecosystem Exchange'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 'Rec coefficient from Biogenic Flux Adjustment System'

        if localTablesVersion == 1 and discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 'GPP coefficient from Biogenic Flux Adjustment System'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 60:
            return 'Averaged cloud-to-ground lightning flash density in the last 6 hours'

        lengthOfTimeRange = h.get_l('lengthOfTimeRange')
        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 6 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Averaged cloud-to-ground lightning flash density in the last 6 hours'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 59:
            return 'Averaged cloud-to-ground lightning flash density in the last 3 hours'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and lengthOfTimeRange == 3 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 'Averaged cloud-to-ground lightning flash density in the last 3 hours'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 58:
            return 'Averaged total lightning flash density in the last 6 hours'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6:
            return 'Averaged total lightning flash density in the last 6 hours'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 57:
            return 'Averaged total lightning flash density in the last 3 hours'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8:
            return 'Averaged total lightning flash density in the last 3 hours'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 53:
            return 'Averaged cloud-to-ground lightning flash density in the last hour'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1 and typeOfSecondFixedSurface == 8:
            return 'Averaged cloud-to-ground lightning flash density in the last hour'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 52:
            return 'Instantaneous cloud-to-ground lightning flash density'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 'Instantaneous cloud-to-ground lightning flash density'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 51:
            return 'Averaged total lightning flash density in the last hour'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and lengthOfTimeRange == 1:
            return 'Averaged total lightning flash density in the last hour'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 50:
            return 'Instantaneous total lightning flash density'

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Instantaneous total lightning flash density'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 48:
            return 'Height of one-degree wet-bulb temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 47:
            return 'Height of zero-degree wet-bulb temperature'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 43:
            return 'Soil wetness index in layer 4'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 42:
            return 'Soil wetness index in layer 3'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 41:
            return 'Soil wetness index in layer 2'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 40:
            return 'Soil wetness index in layer 1'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 28:
            return '10 metre wind gust in the last 3 hours'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and indicatorOfUnitForTimeRange == 1 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 3 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 'Minimum temperature at 2 metres in the last 3 hours'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and lengthOfTimeRange == 3 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1:
            return 'Maximum temperature at 2 metres in the last 3 hours'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 25:
            return 'Horizontal visibility'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 23:
            return 'Cloud base height'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 22:
            return 'Clear-sky direct solar radiation at surface'

        if discipline == 192 and parameterCategory == 228 and parameterNumber == 21:
            return 'Total sky direct solar radiation at surface'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 206:
            return 'Dry deposition velocity of stratospheric aerosol'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 205:
            return 'Dry deposition velocity of ground state oxygen atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 204:
            return 'Dry deposition velocity of excited oxygen atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 203:
            return 'Dry deposition velocity of oxygen atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 202:
            return 'Dry deposition velocity of hydrogen fluoride'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 201:
            return 'Dry deposition velocity of formyl radical'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 200:
            return 'Dry deposition velocity of hydrogen chloride'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 199:
            return 'Dry deposition velocity of hydrogen'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 198:
            return 'Dry deposition velocity of asymmetric chlorine dioxide radical'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 197:
            return 'Dry deposition velocity of tribromomethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 196:
            return 'Dry deposition velocity of methoxy radical'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 195:
            return 'Dry deposition velocity of dibromomethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 194:
            return 'Dry deposition velocity of bromine nitrate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 193:
            return 'Dry deposition velocity of bromine monochloride'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 192:
            return 'Dry deposition velocity of bromine'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 191:
            return 'Dry deposition velocity of bromine atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 190:
            return 'Dry deposition velocity of carbonyl sulfide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 189:
            return 'Dry deposition velocity of sulfur trioxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 188:
            return 'Dry deposition velocity of condensable gas type 2b'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 187:
            return 'Dry deposition velocity of condensable gas type 2a'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 186:
            return 'Dry deposition velocity of condensable gas type 1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 185:
            return 'Dry deposition velocity of secondary organic aerosol type 2b'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 184:
            return 'Dry deposition velocity of secondary organic aerosol type 2a'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 183:
            return 'Dry deposition velocity of secondary organic aerosol type 1'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 182:
            return 'Dry deposition velocity of aromatic-ho from csl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 181:
            return 'Dry deposition velocity of ammonium nitrate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 180:
            return 'Dry deposition velocity of aromatic-ho from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 179:
            return 'Dry deposition velocity of aromatic-ho from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 178:
            return 'Dry deposition velocity of methyl group'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 177:
            return 'Dry deposition velocity of hydrogen atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 176:
            return 'Dry deposition velocity of bromine monoxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 175:
            return 'Dry deposition velocity of chlorine atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 174:
            return 'Dry deposition velocity of chlorine monoxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 173:
            return 'Dry deposition velocity of nitrogen atom'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 172:
            return 'Dry deposition velocity of c10h18o3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 171:
            return 'Dry deposition velocity of bromine family'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 170:
            return 'Dry deposition velocity of c10h16(oh)(oo)'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 169:
            return 'Dry deposition velocity of chlorine family'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 168:
            return 'Dry deposition velocity of all nitrogen oxides'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 167:
            return 'Dry deposition velocity of c7h10o6'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 166:
            return 'Dry deposition velocity of hydrogensulfide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 165:
            return 'Dry deposition velocity of c7h10o5'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 164:
            return 'Dry deposition velocity of c7h9o5'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 163:
            return 'Dry deposition velocity of dimethyl sulfoxyde'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 162:
            return 'Dry deposition velocity of lumped aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 161:
            return 'Dry deposition velocity of hoch2c(ooh)(ch3)ch=ch2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 160:
            return 'Dry deposition velocity of hoch2c(ooh)(ch3)chchoh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 159:
            return 'Dry deposition velocity of bromine oxides'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 158:
            return 'Dry deposition velocity of chlorine oxides'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 157:
            return 'Dry deposition velocity of c3 organic nitrate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 156:
            return 'Dry deposition velocity of ch2chc(ch3)(oo)ch2ono2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 155:
            return 'Dry deposition velocity of oxides'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 154:
            return 'Dry deposition velocity of trop sulfuric acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 153:
            return 'Dry deposition velocity of c5h6o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 152:
            return 'Dry deposition velocity of hoch2c(ch3)=chcho'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 151:
            return 'Dry deposition velocity of no3-alkenes adduct reacting via decomposition'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 150:
            return 'Dry deposition velocity of c5h11ooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 149:
            return 'Dry deposition velocity of no3-alkenes adduct reacting to form carbonitrates'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 148:
            return 'Dry deposition velocity of c5h11o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 147:
            return 'Dry deposition velocity of peroxy radical from ketones'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 146:
            return 'Dry deposition velocity of unsaturated acyl peroxy radical'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 145:
            return 'Dry deposition velocity of unsaturated pans'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 144:
            return 'Dry deposition velocity of peroxy radical from cresol'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 143:
            return 'Dry deposition velocity of h3c(o)ch(ooh)ch2oh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 142:
            return 'Dry deposition velocity of peroxy radical from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 141:
            return 'Dry deposition velocity of ch3c(o)ch(oo)ch2oh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 140:
            return 'Dry deposition velocity of peroxy radical from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 139:
            return 'Dry deposition velocity of phenoxy radical'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 138:
            return 'Dry deposition velocity of methylvinylketone'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 137:
            return 'Dry deposition velocity of peroxy radical from d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 136:
            return 'Dry deposition velocity of ch2=c(ch3)co3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 135:
            return 'Dry deposition velocity of peroxy radical from a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 134:
            return 'Dry deposition velocity of ch3coch(ooh)ch3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 133:
            return 'Dry deposition velocity of peroxy radical from c5h8'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 132:
            return 'Dry deposition velocity of ch3coch(oo)ch3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 131:
            return 'Dry deposition velocity of peroxy radical from internal alkenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 130:
            return 'Dry deposition velocity of c4h9o3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 129:
            return 'Dry deposition velocity of peroxy radical from terminal alkenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 128:
            return 'Dry deposition velocity of c4h8o'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 127:
            return 'Dry deposition velocity of peroxy radical from c2h4'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 126:
            return 'Dry deposition velocity of lumped alkanes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 125:
            return 'Dry deposition velocity of peroxy radical from hc8'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 124:
            return 'Dry deposition velocity of lumped alkenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 123:
            return 'Dry deposition velocity of peroxy radical from hc5'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 122:
            return 'Dry deposition velocity of peroxy radical from hc3'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 121:
            return 'Dry deposition velocity of peroxy radical from c2h6'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 120:
            return 'Dry deposition velocity of ch3coch2o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 119:
            return 'Dry deposition velocity of peroxyacetic acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 118:
            return 'Dry deposition velocity of hydroxyacetone'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 117:
            return 'Dry deposition velocity of higher organic peroxides'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 116:
            return 'Dry deposition velocity of c3h6ohooh'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 115:
            return 'Dry deposition velocity of c3h6oho2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 114:
            return 'Dry deposition velocity of isopropyl hydroperoxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 113:
            return 'Dry deposition velocity of hydroxy ketone'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 112:
            return 'Dry deposition velocity of isopropyldioxidanyl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 111:
            return 'Dry deposition velocity of unsaturated hydroxy dicarbonyl'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 110:
            return 'Dry deposition velocity of methacrolein'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 109:
            return 'Dry deposition velocity of unsaturated dicarbonyls'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 108:
            return 'Dry deposition velocity of hoch2ch2o'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 107:
            return 'Dry deposition velocity of glyoxal'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 106:
            return 'Dry deposition velocity of hoch2ch2o2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 105:
            return 'Dry deposition velocity of ketones'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 104:
            return 'Dry deposition velocity of peracetic acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 103:
            return 'Dry deposition velocity of acetaldehyde and higher'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 102:
            return 'Dry deposition velocity of cresol'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 101:
            return 'Dry deposition velocity of glycolaldehyde'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 100:
            return 'Dry deposition velocity of xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 99:
            return 'Dry deposition velocity of toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 98:
            return 'Dry deposition velocity of acetaldehyde'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 97:
            return 'Dry deposition velocity of d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 96:
            return 'Dry deposition velocity of acetic acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 95:
            return 'Dry deposition velocity of a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 94:
            return 'Dry deposition velocity of ethyl hydroperoxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 93:
            return 'Dry deposition velocity of butadiene'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 92:
            return 'Dry deposition velocity of ethylperoxy radical'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 91:
            return 'Dry deposition velocity of internal alkenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 90:
            return 'Dry deposition velocity of terminal alkenes'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 89:
            return 'Dry deposition velocity of alkanes high oh rate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 88:
            return 'Dry deposition velocity of alkanes med oh rate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 87:
            return 'Dry deposition velocity of alkanes low oh rate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 86:
            return 'Dry deposition velocity of nitrous acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 85:
            return 'Dry deposition velocity of sulfuric acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 84:
            return 'Dry deposition velocity of cbrf2cbrf2'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 83:
            return 'Dry deposition velocity of trifluorobromomethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 82:
            return 'Dry deposition velocity of bromochlorodifluoromethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 81:
            return 'Dry deposition velocity of dibromodifluoromethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 80:
            return 'Dry deposition velocity of methyl bromide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 79:
            return 'Dry deposition velocity of chlorodifluoromethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 78:
            return 'Dry deposition velocity of methyl chloride'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 77:
            return 'Dry deposition velocity of methyl chloroform'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 76:
            return 'Dry deposition velocity of tetrachloromethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 75:
            return 'Dry deposition velocity of chloropentafluoroethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 74:
            return 'Dry deposition velocity of dichlorotetrafluoroethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 73:
            return 'Dry deposition velocity of trichlorotrifluoroethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 72:
            return 'Dry deposition velocity of dichlorodifluoromethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 71:
            return 'Dry deposition velocity of trichlorofluoromethane'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 70:
            return 'Dry deposition velocity of hypobromous acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 69:
            return 'Dry deposition velocity of dichlorine dioxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 68:
            return 'Dry deposition velocity of hydrogen bromide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 67:
            return 'Dry deposition velocity of nitryl chloride'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 66:
            return 'Dry deposition velocity of chlorine'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 65:
            return 'Dry deposition velocity of hypochlorous acid'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 64:
            return 'Dry deposition velocity of chlorine nitrate'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 63:
            return 'Dry deposition velocity of chlorine dioxide'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 62:
            return 'Dry deposition velocity of singlet delta oxygen'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 61:
            return 'Dry deposition velocity of singlet oxygen'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 60:
            return 'Dry deposition velocity of oxygen'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 59:
            return 'Dry deposition velocity of water vapour (chemistry)'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 58:
            return 'Dry deposition velocity of nitrous oxide (chemistry)'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 57:
            return 'Dry deposition velocity of carbon dioxide (chemistry)'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 56:
            return 'Nitrogen oxides Transp deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 55:
            return 'HYPROPO2 deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 54:
            return 'IC3H7O2 deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 53:
            return 'Acetone product deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 52:
            return 'Acetone deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 51:
            return 'Nitrate deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 50:
            return 'Methacrolein MVK  deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 49:
            return 'Terpenes deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 48:
            return 'Propene deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 47:
            return 'Propane deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 46:
            return 'Ethanol deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 45:
            return 'Ethane deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 44:
            return 'Methacrylic acid deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 43:
            return 'Formic acid deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 42:
            return 'Methanol deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 41:
            return 'Polar stratospheric cloud deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 40:
            return 'Amine deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 39:
            return 'NO to alkyl nitrate operator deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 38:
            return 'NO to NO2 operator deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 37:
            return 'PAR budget corrector deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 36:
            return 'Organic ethers deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 35:
            return 'Peroxy acetyl radical deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 34:
            return 'Pernitric acid deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 33:
            return 'Dinitrogen pentoxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 32:
            return 'Nitrate radical deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 31:
            return 'Nitrogen dioxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 30:
            return 'Hydroxyl radical deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 29:
            return 'Methylperoxy radical deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 28:
            return 'Hydroperoxy radical deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 27:
            return 'Nitrogen monoxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 26:
            return 'Lead deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 25:
            return 'Radon deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 24:
            return 'Stratospheric ozone deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 23:
            return 'Methyl glyoxal deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 22:
            return 'Methane sulfonic acid deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 21:
            return 'Ammonium deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 20:
            return 'Sulfate deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 19:
            return 'Ammonia deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 18:
            return 'Dimethyl sulfide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 17:
            return 'Sulfur dioxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 16:
            return 'Isoprene deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 15:
            return 'Organic nitrates deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 14:
            return 'Peroxides deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 13:
            return 'Peroxyacetyl nitrate deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 12:
            return 'Aldehydes deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 11:
            return 'Olefins deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 10:
            return 'Ethene deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 9:
            return 'Paraffins deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 8:
            return 'Formaldehyde deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 7:
            return 'Methyl peroxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 6:
            return 'Nitric acid deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 5:
            return 'Carbon monoxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 4:
            return 'Methane deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 3:
            return 'Hydrogen peroxide deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 2:
            return 'Nitrogen oxides deposition velocity'

        if discipline == 192 and parameterCategory == 221 and parameterNumber == 1:
            return 'Ozone deposition velocity'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 220:
            return 'Wildfire flux of acetonitrile'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 219:
            return 'Wildfire flux of hydrogen cyanide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 218:
            return 'Wildfire flux of alkanes high oh rate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 217:
            return 'Wildfire flux of alkanes med oh rate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 216:
            return 'Wildfire flux of  alkanes low oh rate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 215:
            return 'Wildfire flux of  terminal alkenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 214:
            return 'Wildfire flux of d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 213:
            return 'Wildfire flux of xylene more reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 212:
            return 'Wildfire flux of  toluene less reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 211:
            return 'Wildfire flux of f a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 210:
            return 'Wildfire flux of ketones'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 209:
            return 'Wildfire flux of aldehydes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 208:
            return 'Wildfire flux of olefines'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 207:
            return 'Wildfire flux of paraffins'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 206:
            return 'Emissions of stratospheric aerosol'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 205:
            return 'Emissions of ground state oxygen atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 204:
            return 'Emissions of excited oxygen atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 203:
            return 'Emissions of oxygen atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 202:
            return 'Emissions of hydrogen fluoride'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 201:
            return 'Emissions of formyl radical'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 200:
            return 'Emissions of hydrogen chloride'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 199:
            return 'Emissions of hydrogen'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 198:
            return 'Emissions of asymmetric chlorine dioxide radical'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 197:
            return 'Emissions of tribromomethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 196:
            return 'Emissions of methoxy radical'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 195:
            return 'Emissions of dibromomethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 194:
            return 'Emissions of bromine nitrate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 193:
            return 'Emissions of bromine monochloride'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 192:
            return 'Emissions of bromine'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 191:
            return 'Emissions of bromine atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 190:
            return 'Emissions of carbonyl sulfide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 189:
            return 'Emissions of sulfur trioxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 188:
            return 'Emissions of condensable gas type 2b'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 187:
            return 'Emissions of condensable gas type 2a'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 186:
            return 'Emissions of condensable gas type 1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 185:
            return 'Emissions of secondary organic aerosol type 2b'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 184:
            return 'Emissions of secondary organic aerosol type 2a'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 183:
            return 'Emissions of secondary organic aerosol type 1'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 182:
            return 'Emissions of aromatic-ho from csl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 181:
            return 'Emissions of ammonium nitrate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 180:
            return 'Emissions of aromatic-ho from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 179:
            return 'Emissions of aromatic-ho from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 178:
            return 'Emissions of methyl group'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 177:
            return 'Emissions of hydrogen atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 176:
            return 'Emissions of bromine monoxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 175:
            return 'Emissions of chlorine atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 174:
            return 'Emissions of chlorine monoxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 173:
            return 'Emissions of nitrogen atom'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 172:
            return 'Emissions of c10h18o3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 171:
            return 'Emissions of bromine family'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 170:
            return 'Emissions of c10h16(oh)(oo)'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 169:
            return 'Emissions of chlorine family'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 168:
            return 'Emissions of all nitrogen oxides'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 167:
            return 'Emissions of c7h10o6'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 166:
            return 'Emissions of hydrogensulfide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 165:
            return 'Emissions of c7h10o5'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 164:
            return 'Emissions of c7h9o5'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 163:
            return 'Emissions of dimethyl sulfoxyde'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 162:
            return 'Emissions of lumped aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 161:
            return 'Emissions of hoch2c(ooh)(ch3)ch=ch2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 160:
            return 'Emissions of hoch2c(ooh)(ch3)chchoh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 159:
            return 'Emissions of bromine oxides'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 158:
            return 'Emissions of chlorine oxides'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 157:
            return 'Emissions of c3 organic nitrate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 156:
            return 'Emissions of ch2chc(ch3)(oo)ch2ono2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 155:
            return 'Emissions of oxides'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 154:
            return 'Emissions of trop sulfuric acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 153:
            return 'Emissions of c5h6o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 152:
            return 'Emissions of hoch2c(ch3)=chcho'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 151:
            return 'Emissions of no3-alkenes adduct reacting via decomposition'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 150:
            return 'Emissions of c5h11ooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 149:
            return 'Emissions of no3-alkenes adduct reacting to form carbonitrates'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 148:
            return 'Emissions of c5h11o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 147:
            return 'Emissions of peroxy radical from ketones'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 146:
            return 'Emissions of unsaturated acyl peroxy radical'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 145:
            return 'Emissions of unsaturated pans'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 144:
            return 'Emissions of peroxy radical from cresol'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 143:
            return 'Emissions of h3c(o)ch(ooh)ch2oh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 142:
            return 'Emissions of peroxy radical from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 141:
            return 'Emissions of ch3c(o)ch(oo)ch2oh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 140:
            return 'Emissions of peroxy radical from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 139:
            return 'Emissions of phenoxy radical'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 138:
            return 'Emissions of methylvinylketone'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 137:
            return 'Emissions of peroxy radical from d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 136:
            return 'Emissions of ch2=c(ch3)co3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 135:
            return 'Emissions of peroxy radical from a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 134:
            return 'Emissions of ch3coch(ooh)ch3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 133:
            return 'Emissions of peroxy radical from c5h8'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 132:
            return 'Emissions of ch3coch(oo)ch3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 131:
            return 'Emissions of peroxy radical from internal alkenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 130:
            return 'Emissions of c4h9o3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 129:
            return 'Emissions of peroxy radical from terminal alkenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 128:
            return 'Emissions of c4h8o'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 127:
            return 'Emissions of peroxy radical from c2h4'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 126:
            return 'Emissions of lumped alkanes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 125:
            return 'Emissions of peroxy radical from hc8'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 124:
            return 'Emissions of lumped alkenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 123:
            return 'Emissions of peroxy radical from hc5'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 122:
            return 'Emissions of peroxy radical from hc3'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 121:
            return 'Emissions of peroxy radical from c2h6'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 120:
            return 'Emissions of ch3coch2o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 119:
            return 'Emissions of peroxyacetic acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 118:
            return 'Emissions of hydroxyacetone'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 117:
            return 'Emissions of higher organic peroxides'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 116:
            return 'Emissions of c3h6ohooh'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 115:
            return 'Emissions of c3h6oho2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 114:
            return 'Emissions of isopropyl hydroperoxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 113:
            return 'Emissions of hydroxy ketone'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 112:
            return 'Emissions of isopropyldioxidanyl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 111:
            return 'Emissions of unsaturated hydroxy dicarbonyl'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 110:
            return 'Emissions of methacrolein'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 109:
            return 'Emissions of unsaturated dicarbonyls'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 108:
            return 'Emissions of hoch2ch2o'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 107:
            return 'Emissions of glyoxal'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 106:
            return 'Emissions of hoch2ch2o2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 105:
            return 'Emissions of ketones'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 104:
            return 'Emissions of peracetic acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 103:
            return 'Emissions of acetaldehyde and higher'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 102:
            return 'Emissions of cresol'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 101:
            return 'Emissions of glycolaldehyde'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 100:
            return 'Emissions of xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 99:
            return 'Emissions of toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 98:
            return 'Emissions of acetaldehyde'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 97:
            return 'Emissions of d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 96:
            return 'Emissions of acetic acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 95:
            return 'Emissions of a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 94:
            return 'Emissions of ethyl hydroperoxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 93:
            return 'Emissions of butadiene'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 92:
            return 'Emissions of ethylperoxy radical'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 91:
            return 'Emissions of internal alkenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 90:
            return 'Emissions of terminal alkenes'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 89:
            return 'Emissions of alkanes high oh rate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 88:
            return 'Emissions of alkanes med oh rate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 87:
            return 'Emissions of alkanes low oh rate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 86:
            return 'Emissions of nitrous acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 85:
            return 'Emissions of sulfuric acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 84:
            return 'Emissions of cbrf2cbrf2'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 83:
            return 'Emissions of trifluorobromomethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 82:
            return 'Emissions of bromochlorodifluoromethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 81:
            return 'Emissions of dibromodifluoromethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 80:
            return 'Emissions of methyl bromide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 79:
            return 'Emissions of chlorodifluoromethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 78:
            return 'Emissions of methyl chloride'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 77:
            return 'Emissions of methyl chloroform'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 76:
            return 'Emissions of tetrachloromethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 75:
            return 'Emissions of chloropentafluoroethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 74:
            return 'Emissions of dichlorotetrafluoroethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 73:
            return 'Emissions of trichlorotrifluoroethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 72:
            return 'Emissions of dichlorodifluoromethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 71:
            return 'Emissions of trichlorofluoromethane'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 70:
            return 'Emissions of hypobromous acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 69:
            return 'Emissions of dichlorine dioxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 68:
            return 'Emissions of hydrogen bromide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 67:
            return 'Emissions of nitryl chloride'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 66:
            return 'Emissions of chlorine'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 65:
            return 'Emissions of hypochlorous acid'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 64:
            return 'Emissions of chlorine nitrate'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 63:
            return 'Emissions of chlorine dioxide'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 62:
            return 'Emissions of singlet delta oxygen'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 61:
            return 'Emissions of singlet oxygen'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 60:
            return 'Emissions of oxygen'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 59:
            return 'Emissions of water vapour (chemistry)'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 58:
            return 'Emissions of nitrous oxide (chemistry)'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 57:
            return 'Emissions of carbon dioxide (chemistry)'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 56:
            return 'Nitrogen oxides Transp emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 55:
            return 'HYPROPO2 emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 54:
            return 'IC3H7O2 emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 53:
            return 'Acetone product emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 52:
            return 'Acetone emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 51:
            return 'Nitrate emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 50:
            return 'Methacrolein MVK  emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 49:
            return 'Terpenes emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 48:
            return 'Propene emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 47:
            return 'Propane emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 46:
            return 'Ethanol emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 45:
            return 'Ethane emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 44:
            return 'Methacrylic acid emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 43:
            return 'Formic acid emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 42:
            return 'Methanol emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 41:
            return 'Polar stratospheric cloud emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 40:
            return 'Amine emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 39:
            return 'NO to alkyl nitrate operator emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 38:
            return 'NO to NO2 operator emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 37:
            return 'PAR budget corrector emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 36:
            return 'Organic ethers emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 35:
            return 'Peroxy acetyl radical emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 34:
            return 'Pernitric acid emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 33:
            return 'Dinitrogen pentoxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 32:
            return 'Nitrate radical emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 31:
            return 'Nitrogen dioxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 30:
            return 'Hydroxyl radical emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 29:
            return 'Methylperoxy radical emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 28:
            return 'Hydroperoxy radical emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 27:
            return 'Nitrogen monoxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 26:
            return 'Lead emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 25:
            return 'Radon emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 24:
            return 'Stratospheric ozone emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 23:
            return 'Methyl glyoxal emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 22:
            return 'Methane sulfonic acid emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 21:
            return 'Ammonium emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 20:
            return 'Sulfate emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 19:
            return 'Ammonia emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 18:
            return 'Dimethyl sulfide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 17:
            return 'Sulfur dioxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 16:
            return 'Isoprene emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 15:
            return 'Organic nitrates emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 14:
            return 'Peroxides emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 13:
            return 'Peroxyacetyl nitrate emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 12:
            return 'Aldehydes emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 11:
            return 'Olefins emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 10:
            return 'Ethene emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 9:
            return 'Paraffins emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 8:
            return 'Formaldehyde emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 7:
            return 'Methyl peroxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 6:
            return 'Nitric acid emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 5:
            return 'Carbon monoxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 4:
            return 'Methane emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 3:
            return 'Hydrogen peroxide emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 2:
            return 'Nitrogen oxides emissions'

        if discipline == 192 and parameterCategory == 219 and parameterNumber == 1:
            return 'Ozone emissions'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 206:
            return 'Total column of stratospheric aerosol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 205:
            return 'Total column of ground state oxygen atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 204:
            return 'Total column of excited oxygen atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 203:
            return 'Total column of oxygen atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 202:
            return 'Total column of hydrogen fluoride'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 201:
            return 'Total column of formyl radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 200:
            return 'Total column of hydrogen chloride'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 199:
            return 'Total column of hydrogen'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 198:
            return 'Total column of asymmetric chlorine dioxide radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 197:
            return 'Total column of tribromomethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 196:
            return 'Total column of methoxy radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 195:
            return 'Total column of dibromomethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 194:
            return 'Total column of bromine nitrate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 193:
            return 'Total column of bromine monochloride'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 192:
            return 'Total column of bromine'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 191:
            return 'Total column of bromine atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 190:
            return 'Total column of carbonyl sulfide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 189:
            return 'Total column of sulfur trioxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 188:
            return 'Total column of condensable gas type 2b'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 187:
            return 'Total column of condensable gas type 2a'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 186:
            return 'Total column of condensable gas type 1'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 185:
            return 'Total column of secondary organic aerosol type 2b'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 184:
            return 'Total column of secondary organic aerosol type 2a'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 183:
            return 'Total column of secondary organic aerosol type 1'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 182:
            return 'Total column of aromatic-ho from csl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 181:
            return 'Total column of ammonium nitrate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 180:
            return 'Total column of aromatic-ho from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 179:
            return 'Total column of aromatic-ho from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 178:
            return 'Total column of methyl group'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 177:
            return 'Total column of hydrogen atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 176:
            return 'Total column of bromine monoxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 175:
            return 'Total column of chlorine atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 174:
            return 'Total column of chlorine monoxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 173:
            return 'Total column of nitrogen atom'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 172:
            return 'Total column of c10h18o3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 171:
            return 'Total column of bromine family'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 170:
            return 'Total column of c10h16(oh)(oo)'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 169:
            return 'Total column of chlorine family'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 168:
            return 'Total column of all nitrogen oxides'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 167:
            return 'Total column of c7h10o6'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 166:
            return 'Total column of hydrogensulfide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 165:
            return 'Total column of c7h10o5'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 164:
            return 'Total column of c7h9o5'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 163:
            return 'Total column of dimethyl sulfoxyde'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 162:
            return 'Total column of lumped aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 161:
            return 'Total column of hoch2c(ooh)(ch3)ch=ch2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 160:
            return 'Total column of hoch2c(ooh)(ch3)chchoh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 159:
            return 'Total column of bromine oxides'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 158:
            return 'Total column of chlorine oxides'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 157:
            return 'Total column of c3 organic nitrate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 156:
            return 'Total column of ch2chc(ch3)(oo)ch2ono2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 155:
            return 'Total column of oxides'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 154:
            return 'Total column of trop sulfuric acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 153:
            return 'Total column of c5h6o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 152:
            return 'Total column of hoch2c(ch3)=chcho'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 151:
            return 'Total column of no3-alkenes adduct reacting via decomposition'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 150:
            return 'Total column of c5h11ooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 149:
            return 'Total column of no3-alkenes adduct reacting to form carbonitrates'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 148:
            return 'Total column of c5h11o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 147:
            return 'Total column of peroxy radical from ketones'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 146:
            return 'Total column of unsaturated acyl peroxy radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 145:
            return 'Total column of unsaturated pans'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 144:
            return 'Total column of peroxy radical from cresol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 143:
            return 'Total column of h3c(o)ch(ooh)ch2oh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 142:
            return 'Total column of peroxy radical from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 141:
            return 'Total column of ch3c(o)ch(oo)ch2oh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 140:
            return 'Total column of peroxy radical from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 139:
            return 'Total column of phenoxy radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 138:
            return 'Total column of methylvinylketone'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 137:
            return 'Total column of peroxy radical from d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 136:
            return 'Total column of ch2=c(ch3)co3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 135:
            return 'Total column of peroxy radical from a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 134:
            return 'Total column of ch3coch(ooh)ch3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 133:
            return 'Total column of peroxy radical from c5h8'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 132:
            return 'Total column of ch3coch(oo)ch3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 131:
            return 'Total column of peroxy radical from internal alkenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 130:
            return 'Total column of c4h9o3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 129:
            return 'Total column of peroxy radical from terminal alkenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 128:
            return 'Total column of c4h8o'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 127:
            return 'Total column of peroxy radical from c2h4'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 126:
            return 'Total column of lumped alkanes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 125:
            return 'Total column of peroxy radical from hc8'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 124:
            return 'Total column of lumped alkenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 123:
            return 'Total column of peroxy radical from hc5'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 122:
            return 'Total column of peroxy radical from hc3'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 121:
            return 'Total column of peroxy radical from c2h6'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 120:
            return 'Total column of ch3coch2o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 119:
            return 'Total column of peroxyacetic acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 118:
            return 'Total column of hydroxyacetone'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 117:
            return 'Total column of higher organic peroxides'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 116:
            return 'Total column of c3h6ohooh'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 115:
            return 'Total column of c3h6oho2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 114:
            return 'Total column of isopropyl hydroperoxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 113:
            return 'Total column of hydroxy ketone'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 112:
            return 'Total column of isopropyldioxidanyl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 111:
            return 'Total column of unsaturated hydroxy dicarbonyl'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 110:
            return 'Total column of methacrolein'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 109:
            return 'Total column of unsaturated dicarbonyls'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 108:
            return 'Total column of hoch2ch2o'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 107:
            return 'Total column of glyoxal'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 106:
            return 'Total column of hoch2ch2o2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 105:
            return 'Total column of ketones'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 104:
            return 'Total column of peracetic acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 103:
            return 'Total column of acetaldehyde and higher'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 102:
            return 'Total column of cresol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 101:
            return 'Total column of glycolaldehyde'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 100:
            return 'Total column of xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 99:
            return 'Total column of toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 98:
            return 'Total column of acetaldehyde'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 97:
            return 'Total column of d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 96:
            return 'Total column of acetic acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 95:
            return 'Total column of a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 94:
            return 'Total column of ethyl hydroperoxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 93:
            return 'Total column of butadiene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 92:
            return 'Total column of ethylperoxy radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 91:
            return 'Total column of internal alkenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 90:
            return 'Total column of terminal alkenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 89:
            return 'Total column of alkanes high oh rate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 88:
            return 'Total column of alkanes med oh rate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 87:
            return 'Total column of alkanes low oh rate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 86:
            return 'Total column of nitrous acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 85:
            return 'Total column of sulfuric acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 84:
            return 'Total column of cbrf2cbrf2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 83:
            return 'Total column of trifluorobromomethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 82:
            return 'Total column of bromochlorodifluoromethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 81:
            return 'Total column of dibromodifluoromethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 80:
            return 'Total column of methyl bromide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 79:
            return 'Total column of chlorodifluoromethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 78:
            return 'Total column of methyl chloride'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 77:
            return 'Total column of methyl chloroform'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 76:
            return 'Total column of tetrachloromethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 75:
            return 'Total column of chloropentafluoroethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 74:
            return 'Total column of dichlorotetrafluoroethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 73:
            return 'Total column of trichlorotrifluoroethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 72:
            return 'Total column of dichlorodifluoromethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 71:
            return 'Total column of trichlorofluoromethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 70:
            return 'Total column of hypobromous acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 69:
            return 'Total column of dichlorine dioxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 68:
            return 'Total column of hydrogen bromide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 67:
            return 'Total column of nitryl chloride'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 66:
            return 'Total column of chlorine'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 65:
            return 'Total column of hypochlorous acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 64:
            return 'Total column of chlorine nitrate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 63:
            return 'Total column of chlorine dioxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 62:
            return 'Total column of singlet delta oxygen'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 61:
            return 'Total column of singlet oxygen'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 60:
            return 'Total column of oxygen'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 59:
            return 'Total column of water vapour (chemistry)'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 58:
            return 'Total column of nitrous oxide (chemistry)'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 57:
            return 'Total column of carbon dioxide (chemistry)'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 56:
            return 'Total column nitrogen oxides Transp'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 55:
            return 'Total column HYPROPO2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 54:
            return 'Total column IC3H7O2'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 53:
            return 'Total column acetone product'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 52:
            return 'Total column acetone'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 51:
            return 'Total column nitrate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 50:
            return 'Total column methacrolein MVK'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 49:
            return 'Total column terpenes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 48:
            return 'Total column propene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 47:
            return 'Total column propane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 46:
            return 'Total column ethanol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 45:
            return 'Total column  ethane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 44:
            return 'Total column  methacrylic acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 43:
            return 'Total column formic acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 42:
            return 'Total column methanol'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 41:
            return 'Total column  polar stratospheric cloud'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 40:
            return 'Total column amine'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 39:
            return 'Total column NO to alkyl nitrate operator'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 38:
            return 'Total column NO to NO2 operator'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 37:
            return 'Total column PAR budget corrector'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 36:
            return 'Total column  organic ethers'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 35:
            return 'Total column peroxy acetyl radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 34:
            return 'Total column pernitric acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 33:
            return 'Total column dinitrogen pentoxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 32:
            return 'Total column nitrate radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 30:
            return 'Total column hydroxyl radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 29:
            return 'Total column methylperoxy radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 28:
            return 'Total column hydroperoxy radical'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 27:
            return 'Total column nitrogen monoxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 26:
            return 'Total column  lead'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 24:
            return 'Total column stratospheric ozone'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 23:
            return 'Total column methyl glyoxal'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 22:
            return 'Total column  methane sulfonic acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 21:
            return 'Total column ammonium'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 20:
            return 'Total column  sulfate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 19:
            return 'Total column ammonia'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 18:
            return 'Total column dimethyl sulfide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 16:
            return 'Total column  isoprene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 15:
            return 'Total column organic nitrates'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 14:
            return 'Total column peroxides'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 13:
            return 'Total column  peroxyacetyl nitrate'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 12:
            return 'Total column aldehydes'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 11:
            return 'Total column olefins'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 10:
            return 'Total column ethene'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 9:
            return 'Total column paraffins'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 7:
            return 'Total column methyl peroxide'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 6:
            return 'Total column nitric acid'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 4:
            return 'Total column methane'

        if discipline == 192 and parameterCategory == 218 and parameterNumber == 3:
            return 'Total column hydrogen peroxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 206:
            return 'Stratospheric aerosol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 205:
            return 'Ground state oxygen atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 204:
            return 'Excited oxygen atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 203:
            return 'Oxygen atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 202:
            return 'Hydrogen fluoride'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 201:
            return 'Formyl radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 200:
            return 'Hydrogen chloride'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 199:
            return 'Hydrogen'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 198:
            return 'Asymmetric chlorine dioxide radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 197:
            return 'Tribromomethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 196:
            return 'Methoxy radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 195:
            return 'Dibromomethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 194:
            return 'Bromine nitrate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 193:
            return 'Bromine monochloride'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 192:
            return 'Bromine'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 191:
            return 'Bromine atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 190:
            return 'Carbonyl sulfide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 189:
            return 'Sulfur trioxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 188:
            return 'Condensable gas type 2b'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 187:
            return 'Condensable gas type 2a'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 186:
            return 'Condensable gas type 1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 185:
            return 'Secondary organic aerosol type 2b'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 184:
            return 'Secondary organic aerosol type 2a'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 183:
            return 'Secondary organic aerosol type 1'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 182:
            return 'Aromatic-ho from csl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 181:
            return 'Ammonium nitrate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 180:
            return 'Aromatic-ho from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 179:
            return 'Aromatic-ho from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 178:
            return 'Methyl group'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 177:
            return 'Hydrogen atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 176:
            return 'Bromine monoxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 175:
            return 'Chlorine atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 174:
            return 'Chlorine monoxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 173:
            return 'Nitrogen atom'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 172:
            return 'C10h18o3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 171:
            return 'Bromine family'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 170:
            return 'C10h16(oh)(oo)'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 169:
            return 'Chlorine family'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 168:
            return 'All nitrogen oxides'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 167:
            return 'C7h10o6'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 166:
            return 'Hydrogensulfide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 165:
            return 'C7h10o5'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 164:
            return 'C7h9o5'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 163:
            return 'Dimethyl sulfoxyde'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 162:
            return 'Lumped aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 161:
            return 'Hoch2c(ooh)(ch3)ch=ch2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 160:
            return 'Hoch2c(ooh)(ch3)chchoh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 159:
            return 'Bromine oxides'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 158:
            return 'Chlorine oxides'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 157:
            return 'C3 organic nitrate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 156:
            return 'Ch2chc(ch3)(oo)ch2ono2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 155:
            return 'Oxides'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 154:
            return 'Trop sulfuric acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 153:
            return 'C5h6o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 152:
            return 'Hoch2c(ch3)=chcho'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 151:
            return 'No3-alkenes adduct reacting via decomposition'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 150:
            return 'C5h11ooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 149:
            return 'No3-alkenes adduct reacting to form carbonitrates'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 148:
            return 'C5h11o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 147:
            return 'Peroxy radical from ketones'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 146:
            return 'Unsaturated acyl peroxy radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 145:
            return 'Unsaturated pans'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 144:
            return 'Peroxy radical from cresol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 143:
            return 'H3c(o)ch(ooh)ch2oh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 142:
            return 'Peroxy radical from xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 141:
            return 'Ch3c(o)ch(oo)ch2oh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 140:
            return 'Peroxy radical from toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 139:
            return 'Phenoxy radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 138:
            return 'Methylvinylketone'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 137:
            return 'Peroxy radical from d-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 136:
            return 'Ch2=c(ch3)co3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 135:
            return 'Peroxy radical from a-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 134:
            return 'Ch3coch(ooh)ch3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 133:
            return 'Peroxy radical from c5h8'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 132:
            return 'Ch3coch(oo)ch3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 131:
            return 'Peroxy radical from internal alkenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 130:
            return 'C4h9o3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 129:
            return 'Peroxy radical from terminal alkenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 128:
            return 'C4h8o'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 127:
            return 'Peroxy radical from c2h4'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 126:
            return 'Lumped alkanes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 125:
            return 'Peroxy radical from hc8'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 124:
            return 'Lumped alkenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 123:
            return 'Peroxy radical from hc5'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 122:
            return 'Peroxy radical from hc3'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 121:
            return 'Peroxy radical from c2h6'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 120:
            return 'Ch3coch2o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 119:
            return 'Peroxyacetic acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 118:
            return 'Hydroxyacetone'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 117:
            return 'Higher organic peroxides'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 116:
            return 'C3h6ohooh'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 115:
            return 'C3h6oho2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 114:
            return 'Isopropyl hydroperoxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 113:
            return 'Hydroxy ketone'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 112:
            return 'Isopropyldioxidanyl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 111:
            return 'Unsaturated hydroxy dicarbonyl'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 110:
            return 'Methacrolein'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 109:
            return 'Unsaturated dicarbonyls'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 108:
            return 'Hoch2ch2o'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 107:
            return 'Glyoxal'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 106:
            return 'Hoch2ch2o2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 105:
            return 'Ketones'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 104:
            return 'Peracetic acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 103:
            return 'Acetaldehyde and higher'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 102:
            return 'Cresol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 101:
            return 'Glycolaldehyde'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 100:
            return 'Xylene and more reactive aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 99:
            return 'Toluene and less reactive aromatics'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 98:
            return 'Acetaldehyde'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 97:
            return 'D-limonene cyclic diene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 96:
            return 'Acetic acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 95:
            return 'A-pinene cyclic terpenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 94:
            return 'Ethyl hydroperoxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 93:
            return 'Butadiene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 92:
            return 'Ethylperoxy radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 91:
            return 'Internal alkenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 90:
            return 'Terminal alkenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 89:
            return 'Alkanes high oh rate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 88:
            return 'Alkanes med oh rate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 87:
            return 'Alkanes low oh rate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 86:
            return 'Nitrous acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 85:
            return 'Sulfuric acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 84:
            return 'Cbrf2cbrf2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 83:
            return 'Trifluorobromomethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 82:
            return 'Bromochlorodifluoromethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 81:
            return 'Dibromodifluoromethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 80:
            return 'Methyl bromide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 79:
            return 'Chlorodifluoromethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 78:
            return 'Methyl chloride'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 77:
            return 'Methyl chloroform'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 76:
            return 'Tetrachloromethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 75:
            return 'Chloropentafluoroethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 74:
            return 'Dichlorotetrafluoroethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 73:
            return 'Trichlorotrifluoroethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 72:
            return 'Dichlorodifluoromethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 71:
            return 'Trichlorofluoromethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 70:
            return 'Hypobromous acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 69:
            return 'Dichlorine dioxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 68:
            return 'Hydrogen bromide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 67:
            return 'Nitryl chloride'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 66:
            return 'Chlorine'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 65:
            return 'Hypochlorous acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 64:
            return 'Chlorine nitrate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 63:
            return 'Chlorine dioxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 62:
            return 'Singlet delta oxygen'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 61:
            return 'Singlet oxygen'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 60:
            return 'Oxygen'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 59:
            return 'Water vapour (chemistry)'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 58:
            return 'Nitrous oxide (chemistry)'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 57:
            return 'Carbon dioxide (chemistry)'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 56:
            return 'Nitrogen oxides Transp'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 55:
            return 'HYPROPO2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 54:
            return 'IC3H7O2'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 53:
            return 'Acetone product'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 52:
            return 'Acetone'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 51:
            return 'Nitrate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 50:
            return 'Methacrolein MVK'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 49:
            return 'Terpenes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 48:
            return 'Propene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 47:
            return 'Propane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 46:
            return 'Ethanol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 45:
            return 'Ethane'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 44:
            return 'Methacrylic acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 43:
            return 'Formic acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 42:
            return 'Methanol'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 41:
            return 'Polar stratospheric cloud'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 40:
            return 'Amine'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 39:
            return 'NO to alkyl nitrate operator'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 38:
            return 'NO to NO2 operator'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 37:
            return 'PAR budget corrector'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 36:
            return 'Organic ethers'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 35:
            return 'Peroxy acetyl radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 34:
            return 'Pernitric acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 33:
            return 'Dinitrogen pentoxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 32:
            return 'Nitrate radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 30:
            return 'Hydroxyl radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 29:
            return 'Methylperoxy radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 28:
            return 'Hydroperoxy radical'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 27:
            return 'Nitrogen monoxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 26:
            return 'Lead'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 24:
            return 'Stratospheric ozone'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 23:
            return 'Methyl glyoxal'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 22:
            return 'Methane sulfonic acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 21:
            return 'Ammonium'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 20:
            return 'Sulfate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 19:
            return 'Ammonia'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 18:
            return 'Dimethyl sulfide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 16:
            return 'Isoprene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 15:
            return 'Organic nitrates'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 14:
            return 'Peroxides'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 13:
            return 'Peroxyacetyl nitrate'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 12:
            return 'Aldehydes'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 11:
            return 'Olefins'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 10:
            return 'Ethene'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 9:
            return 'Paraffins'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 7:
            return 'Methyl peroxide'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 6:
            return 'Nitric acid'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 4:
            return 'Methane (chemistry)'

        if discipline == 192 and parameterCategory == 217 and parameterNumber == 3:
            return 'Hydrogen peroxide'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 255:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 254:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 253:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 252:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 251:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 250:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 249:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 248:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 247:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 246:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 245:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 244:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 243:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 242:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 241:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 240:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 239:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 238:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 237:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 236:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 235:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 234:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 233:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 232:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 231:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 230:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 229:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 228:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 227:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 226:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 225:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 224:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 223:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 222:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 221:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 220:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 219:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 218:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 217:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 216:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 215:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 214:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 213:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 212:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 211:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 210:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 209:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 208:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 207:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 206:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 205:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 204:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 203:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 202:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 201:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 200:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 199:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 198:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 197:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 196:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 195:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 194:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 193:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 192:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 191:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 190:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 189:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 188:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 187:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 186:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 185:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 184:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 183:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 182:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 181:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 180:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 179:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 178:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 177:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 176:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 175:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 174:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 173:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 172:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 171:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 170:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 169:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 168:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 167:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 166:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 165:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 164:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 163:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 162:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 161:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 160:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 159:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 158:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 157:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 156:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 155:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 154:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 153:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 152:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 151:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 150:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 149:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 148:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 147:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 146:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 145:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 144:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 143:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 142:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 141:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 140:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 139:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 138:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 137:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 136:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 135:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 134:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 133:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 132:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 131:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 130:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 129:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 128:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 127:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 126:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 125:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 124:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 123:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 122:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 121:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 120:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 119:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 118:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 117:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 116:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 115:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 114:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 113:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 112:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 111:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 110:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 109:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 108:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 107:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 106:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 105:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 104:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 103:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 102:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 101:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 100:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 99:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 98:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 97:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 96:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 95:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 94:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 93:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 92:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 91:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 90:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 89:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 88:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 87:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 86:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 85:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 84:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 83:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 82:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 81:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 80:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 79:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 78:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 77:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 76:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 75:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 74:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 73:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 72:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 71:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 70:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 69:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 68:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 67:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 66:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 65:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 64:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 63:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 62:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 61:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 60:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 59:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 58:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 57:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 56:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 55:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 54:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 53:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 52:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 51:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 50:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 49:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 48:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 47:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 46:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 45:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 44:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 43:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 42:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 41:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 40:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 39:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 38:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 37:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 36:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 35:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 34:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 33:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 32:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 31:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 30:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 29:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 28:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 27:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 26:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 25:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 24:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 23:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 22:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 21:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 20:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 19:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 18:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 17:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 16:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 15:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 14:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 13:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 12:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 11:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 10:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 9:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 8:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 7:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 6:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 5:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 4:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 3:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 2:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 216 and parameterNumber == 1:
            return 'Experimental product'

        is_aerosol = h.get_l('is_aerosol')
        aerosolType = h.get_l('aerosolType')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and is_aerosol == 1 and aerosolType == 62003:
            return 'Negative fixer of ammonium aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and is_aerosol == 1 and aerosolType == 62003:
            return 'Source/gain of ammonium aerosol'

        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        is_aerosol_optical = h.get_l('is_aerosol_optical')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')
        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfWavelengthInterval == 11 and aerosolType == 65533 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and typeOfSizeInterval == 255 and scaledValueOfFirstWavelength == 55:
            return 'Coarse-mode nitrate aerosol optical depth at 550 nm'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and scaleFactorOfFirstWavelength == 8 and is_aerosol_optical == 1 and typeOfSizeInterval == 255 and scaledValueOfFirstWavelength == 55 and typeOfWavelengthInterval == 11 and aerosolType == 65534:
            return 'Fine-mode nitrate aerosol optical depth at 550 nm'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and aerosolType == 65533 and is_aerosol == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 'Vertically integrated mass of coarse-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and is_aerosol == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1 and aerosolType == 65534:
            return 'Vertically integrated mass of fine-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and is_aerosol == 1 and aerosolType == 65533:
            return 'Negative fixer of coarse-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and aerosolType == 65534 and is_aerosol == 1:
            return 'Negative fixer of fine-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and is_aerosol == 1 and aerosolType == 65533:
            return 'Wet deposition of coarse-mode nitrate aerosol by convective precipitation'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and is_aerosol == 1 and aerosolType == 65534:
            return 'Wet deposition of fine-mode nitrate aerosol by convective precipitation'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and is_aerosol == 1 and aerosolType == 65533:
            return 'Wet deposition of coarse-mode nitrate aerosol by large-scale precipitation'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and is_aerosol == 1 and aerosolType == 65534:
            return 'Wet deposition of fine-mode nitrate aerosol by large-scale precipitation'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and is_aerosol == 1 and aerosolType == 65533:
            return 'Sedimentation of coarse-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 65534 and is_aerosol == 1:
            return 'Sedimentation of fine-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65533 and is_aerosol == 1:
            return 'Dry deposition of coarse-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 65534 and is_aerosol == 1:
            return 'Dry deposition of fine-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65533 and is_aerosol == 1:
            return 'Source/gain of coarse-mode nitrate aerosol'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and aerosolType == 65534 and is_aerosol == 1:
            return 'Source/gain of fine-mode nitrate aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 188:
            return 'Aerosol backscatter coefficient at 1064 nm (from ground)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 187:
            return 'Aerosol backscatter coefficient at 532 nm (from ground)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 186:
            return 'Aerosol backscatter coefficient at 355 nm (from ground)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 185:
            return 'Aerosol backscatter coefficient at 1064 nm (from top of atmosphere)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 184:
            return 'Aerosol backscatter coefficient at 532 nm (from top of atmosphere)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 183:
            return 'Aerosol backscatter coefficient at 355 nm (from top of atmosphere)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 182:
            return 'Aerosol extinction coefficient at 1064 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 181:
            return 'Aerosol extinction coefficient at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 180:
            return 'Aerosol extinction coefficient at 355 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 179:
            return 'Asymmetry factor at 2130 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 178:
            return 'Single scattering albedo at 2130 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 177:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 2130 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 176:
            return 'Total absorption aerosol optical depth at 2130 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 175:
            return 'Sulphur dioxide optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 174:
            return 'Vertically integrated mass of sulphur dioxide'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 173:
            return 'Negative fixer of sulphur dioxide'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 172:
            return 'Wet deposition of sulphur dioxide by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 171:
            return 'Wet deposition of sulphur dioxide by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 170:
            return 'Sedimentation of sulphur dioxide'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 169:
            return 'Dry deposition of sulphur dioxide'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 168:
            return 'Source/gain of sulphur dioxide'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 167:
            return 'Asymmetry factor at 1640 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 166:
            return 'Asymmetry factor at 1240 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 165:
            return 'Asymmetry factor at 1064 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 164:
            return 'Asymmetry factor at 1020 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 163:
            return 'Asymmetry factor at 865 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 162:
            return 'Asymmetry factor at 858 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 161:
            return 'Asymmetry factor at 800 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 160:
            return 'Asymmetry factor at 670 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 159:
            return 'Asymmetry factor at 645 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 158:
            return 'Asymmetry factor at 550 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 157:
            return 'Asymmetry factor at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 156:
            return 'Asymmetry factor at 500 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 155:
            return 'Asymmetry factor at 469 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 154:
            return 'Asymmetry factor at 440 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 153:
            return 'Asymmetry factor at 400 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 152:
            return 'Asymmetry factor at 380 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 151:
            return 'Asymmetry factor at 355 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 150:
            return 'Asymmetry factor at 340 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 149:
            return 'Single scattering albedo at 1640 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 148:
            return 'Single scattering albedo at 1240 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 147:
            return 'Single scattering albedo at 1064 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 146:
            return 'Single scattering albedo at 1020 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 145:
            return 'Single scattering albedo at 865 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 144:
            return 'Single scattering albedo at 858 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 143:
            return 'Single scattering albedo at 800 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 142:
            return 'Single scattering albedo at 670 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 141:
            return 'Single scattering albedo at 645 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 140:
            return 'Single scattering albedo at 550 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 139:
            return 'Single scattering albedo at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 138:
            return 'Single scattering albedo at 500 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 137:
            return 'Single scattering albedo at 469 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 136:
            return 'Single scattering albedo at 440 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 135:
            return 'Single scattering albedo at 400 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 134:
            return 'Single scattering albedo at 380 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 133:
            return 'Single scattering albedo at 355 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 132:
            return 'Single scattering albedo at 340 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 131:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1640 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 130:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1240 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 129:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1064 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 128:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 1020 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 127:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 865 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 126:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 858 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 125:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 800 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 124:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 670 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 123:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 645 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 122:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 550 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 121:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 120:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 500 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 119:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 469 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 118:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 440 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 117:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 400 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 116:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 380 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 115:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 355 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 114:
            return 'Total fine mode (r < 0.5 um) aerosol optical depth at 340 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 113:
            return 'Total absorption aerosol optical depth at 1640 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 112:
            return 'Total absorption aerosol optical depth at 1240 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 111:
            return 'Total absorption aerosol optical depth at 1064 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 110:
            return 'Total absorption aerosol optical depth at 1020 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 109:
            return 'Total absorption aerosol optical depth at 865 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 108:
            return 'Total absorption aerosol optical depth at 858 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 107:
            return 'Total absorption aerosol optical depth at 800 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 106:
            return 'Total absorption aerosol optical depth at 670 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 105:
            return 'Total absorption aerosol optical depth at 645 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 104:
            return 'Total absorption aerosol optical depth at 550 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 103:
            return 'Total absorption aerosol optical depth at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 102:
            return 'Total absorption aerosol optical depth at 500 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 101:
            return 'Total absorption aerosol optical depth at 469 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 100:
            return 'Total absorption aerosol optical depth at 440 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 99:
            return 'Total absorption aerosol optical depth at 400 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 98:
            return 'Total absorption aerosol optical depth at 380 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 97:
            return 'Total absorption aerosol optical depth at 355 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 96:
            return 'Total absorption aerosol optical depth at 340 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 95:
            return 'Antropogenic (black carbon, organic matter, sulphate) aerosol optical thickness at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 94:
            return 'Natural (sea-salt and dust) aerosol optical thickness at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 93:
            return 'Total aerosol optical thickness at 532 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 92:
            return '10 metre wind gustiness dust emission potential'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 91:
            return '10 metre wind speed dust emission potential'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 90:
            return 'Effective (snow effect included) UV visible albedo for direct radiation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 89:
            return 'Accumulated total aerosol optical depth at 550 nm'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 88:
            return 'Sulphate aerosol optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 87:
            return 'Vertically integrated mass of sulphate aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 86:
            return 'Negative fixer of sulphate aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 85:
            return 'Wet deposition of sulphate aerosol by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 84:
            return 'Wet deposition of sulphate aerosol by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 83:
            return 'Sedimentation of sulphate aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 82:
            return 'Dry deposition of sulphate aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 81:
            return 'Source/gain of sulphate aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 80:
            return 'Hydrophilic black carbon aerosol optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 79:
            return 'Hydrophobic black carbon aerosol optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 78:
            return 'Vertically integrated mass of hydrophilic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 77:
            return 'Vertically integrated mass of hydrophobic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 76:
            return 'Negative fixer of hydrophilic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 75:
            return 'Negative fixer of hydrophobic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 74:
            return 'Wet deposition of hydrophilic black carbon aerosol by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 73:
            return 'Wet deposition of hydrophobic black carbon aerosol by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 72:
            return 'Wet deposition of hydrophilic black carbon aerosol by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 71:
            return 'Wet deposition of hydrophobic black carbon aerosol by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 70:
            return 'Sedimentation of hydrophilic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 69:
            return 'Sedimentation of hydrophobic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 68:
            return 'Dry deposition of hydrophilic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 67:
            return 'Dry deposition of hydrophobic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 66:
            return 'Source/gain of hydrophilic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 65:
            return 'Source/gain of hydrophobic black carbon aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 64:
            return 'Hydrophilic organic matter aerosol optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 63:
            return 'Hydrophobic organic matter aerosol optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 62:
            return 'Vertically integrated mass of hydrophilic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 61:
            return 'Vertically integrated mass of hydrophobic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 60:
            return 'Negative fixer of hydrophilic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 59:
            return 'Negative fixer of hydrophobic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 58:
            return 'Wet deposition of hydrophilic organic matter aerosol by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 57:
            return 'Wet deposition of hydrophobic organic matter aerosol by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 56:
            return 'Wet deposition of hydrophilic organic matter aerosol by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 55:
            return 'Wet deposition of hydrophobic organic matter aerosol by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 54:
            return 'Sedimentation of hydrophilic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 53:
            return 'Sedimentation of hydrophobic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 52:
            return 'Dry deposition of hydrophilic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 51:
            return 'Dry deposition of hydrophobic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 50:
            return 'Source/gain of hydrophilic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 49:
            return 'Source/gain of hydrophobic organic matter aerosol'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 48:
            return 'Dust aerosol (9 - 20 um) optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 47:
            return 'Dust aerosol (0.55 - 9 um) optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 46:
            return 'Dust aerosol (0.03 - 0.55 um) optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 45:
            return 'Vertically integrated mass of dust aerosol (9 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 44:
            return 'Vertically integrated mass of dust aerosol (0.55 - 9 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 43:
            return 'Vertically integrated mass of dust aerosol (0.03 - 0.55 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 42:
            return 'Negative fixer of dust aerosol (9 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 41:
            return 'Negative fixer of dust aerosol (0.55 - 9 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 40:
            return 'Negative fixer of dust aerosol (0.03 - 0.55 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 39:
            return 'Wet deposition of dust aerosol (9 - 20 um) by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 38:
            return 'Wet deposition of dust aerosol (0.55 - 9 um) by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 37:
            return 'Wet deposition of dust aerosol (0.03 - 0.55 um) by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 36:
            return 'Wet deposition of dust aerosol (9 - 20 um) by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 35:
            return 'Wet deposition of dust aerosol (0.55 - 9 um) by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 34:
            return 'Wet deposition of dust aerosol (0.03 - 0.55 um) by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 33:
            return 'Sedimentation of dust aerosol (9 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 32:
            return 'Sedimentation of dust aerosol (0.55 - 9 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 31:
            return 'Sedimentation of dust aerosol (0.03 - 0.55 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 30:
            return 'Dry deposition of dust aerosol (9 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 29:
            return 'Dry deposition of dust aerosol (0.55 - 9 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 28:
            return 'Dry deposition of dust aerosol (0.03 - 0.55 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 27:
            return 'Source/gain of dust aerosol (9 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 26:
            return 'Source/gain of dust aerosol (0.55 - 9 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 25:
            return 'Source/gain of dust aerosol (0.03 - 0.55 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 24:
            return 'Sea salt aerosol (5 - 20 um) optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 23:
            return 'Sea salt aerosol (0.5 - 5 um) optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 22:
            return 'Sea salt aerosol (0.03 - 0.5 um) optical depth'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 21:
            return 'Vertically integrated mass of sea salt aerosol (5 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 20:
            return 'Vertically integrated mass of sea salt aerosol (0.5 - 5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 19:
            return 'Vertically integrated mass of sea salt aerosol (0.03 - 0.5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 18:
            return 'Negative fixer of sea salt aerosol (5 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 17:
            return 'Negative fixer of sea salt aerosol (0.5 - 5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 16:
            return 'Negative fixer of sea salt aerosol (0.03 - 0.5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 15:
            return 'Wet deposition of sea salt aerosol (5 - 20 um) by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 14:
            return 'Wet deposition of sea salt aerosol (0.5 - 5 um) by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 13:
            return 'Wet deposition of sea salt aerosol (0.03 - 0.5 um) by convective precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 12:
            return 'Wet deposition of sea salt aerosol (5 - 20 um) by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 11:
            return 'Wet deposition of sea salt aerosol (0.5 - 5 um) by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 10:
            return 'Wet deposition of sea salt aerosol (0.03 - 0.5 um) by large-scale precipitation'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 9:
            return 'Sedimentation of sea salt aerosol (5 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 8:
            return 'Sedimentation of sea salt aerosol (0.5 - 5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 7:
            return 'Sedimentation of sea salt aerosol (0.03 - 0.5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 6:
            return 'Dry deposition of sea salt aerosol (5 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 5:
            return 'Dry deposition of sea salt aerosol (0.5 - 5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 4:
            return 'Dry deposition of sea salt aerosol (0.03 - 0.5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 3:
            return 'Source/gain of sea salt aerosol (5 - 20 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 2:
            return 'Source/gain of sea salt aerosol (0.5 - 5 um)'

        if discipline == 192 and parameterCategory == 215 and parameterNumber == 1:
            return 'Source/gain of sea salt aerosol (0.03 - 0.5 um)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 52:
            return 'Profile of optical thickness at 340 nm'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 51:
            return 'Clear-sky surface UV spectral flux (395-400 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 50:
            return 'Clear-sky surface UV spectral flux (390-395 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 49:
            return 'Clear-sky surface UV spectral flux (385-390 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 48:
            return 'Clear-sky surface UV spectral flux (380-385 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 47:
            return 'Clear-sky surface UV spectral flux (375-380 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 46:
            return 'Clear-sky surface UV spectral flux (370-375 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 45:
            return 'Clear-sky surface UV spectral flux (365-370 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 44:
            return 'Clear-sky surface UV spectral flux (360-365 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 43:
            return 'Clear-sky surface UV spectral flux (355-360 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 42:
            return 'Clear-sky surface UV spectral flux (350-355 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 41:
            return 'Clear-sky surface UV spectral flux (345-350 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 40:
            return 'Clear-sky surface UV spectral flux (340-345 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 39:
            return 'Clear-sky surface UV spectral flux (335-340 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 38:
            return 'Clear-sky surface UV spectral flux (330-335 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 37:
            return 'Clear-sky surface UV spectral flux (325-330 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 36:
            return 'Clear-sky surface UV spectral flux (320-325 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 35:
            return 'Clear-sky surface UV spectral flux (315-320 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 34:
            return 'Clear-sky surface UV spectral flux (310-315 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 33:
            return 'Clear-sky surface UV spectral flux (305-310 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 32:
            return 'Clear-sky surface UV spectral flux (300-305 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 31:
            return 'Clear-sky surface UV spectral flux (295-300 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 30:
            return 'Clear-sky surface UV spectral flux (290-295 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 29:
            return 'Clear-sky surface UV spectral flux (285-290 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 28:
            return 'Clear-sky surface UV spectral flux (280-285 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 27:
            return 'Total surface UV spectral flux (395-400 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 26:
            return 'Total surface UV spectral flux (390-395 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 25:
            return 'Total surface UV spectral flux (385-390 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 24:
            return 'Total surface UV spectral flux (380-385 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 23:
            return 'Total surface UV spectral flux (375-380 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 22:
            return 'Total surface UV spectral flux (370-375 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 21:
            return 'Total surface UV spectral flux (365-370 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 20:
            return 'Total surface UV spectral flux (360-365 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 19:
            return 'Total surface UV spectral flux (355-360 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 18:
            return 'Total surface UV spectral flux (350-355 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 17:
            return 'Total surface UV spectral flux (345-350 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 16:
            return 'Total surface UV spectral flux (340-345 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 15:
            return 'Total surface UV spectral flux (335-340 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 14:
            return 'Total surface UV spectral flux (330-335 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 13:
            return 'Total surface UV spectral flux (325-330 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 12:
            return 'Total surface UV spectral flux (320-325 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 11:
            return 'Total surface UV spectral flux (315-320 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 10:
            return 'Total surface UV spectral flux (310-315 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 9:
            return 'Total surface UV spectral flux (305-310 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 8:
            return 'Total surface UV spectral flux (300-305 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 7:
            return 'Total surface UV spectral flux (295-300 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 6:
            return 'Total surface UV spectral flux (290-295 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 5:
            return 'Total surface UV spectral flux (285-290 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 4:
            return 'Total surface UV spectral flux (280-285 nm)'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 3:
            return 'UV biologically effective dose clear-sky'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 2:
            return 'UV biologically effective dose'

        if discipline == 192 and parameterCategory == 214 and parameterNumber == 1:
            return 'Cosine of solar zenith angle'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 150:
            return 'Random pattern 50 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 149:
            return 'Random pattern 49 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 148:
            return 'Random pattern 48 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 147:
            return 'Random pattern 47 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 146:
            return 'Random pattern 46 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 145:
            return 'Random pattern 45 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 144:
            return 'Random pattern 44 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 143:
            return 'Random pattern 43 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 142:
            return 'Random pattern 42 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 141:
            return 'Random pattern 41 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 140:
            return 'Random pattern 40 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 139:
            return 'Random pattern 39 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 138:
            return 'Random pattern 38 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 137:
            return 'Random pattern 37 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 136:
            return 'Random pattern 36 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 135:
            return 'Random pattern 35 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 134:
            return 'Random pattern 34 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 133:
            return 'Random pattern 33 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 132:
            return 'Random pattern 32 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 131:
            return 'Random pattern 31 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 130:
            return 'Random pattern 30 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 129:
            return 'Random pattern 29 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 128:
            return 'Random pattern 28 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 127:
            return 'Random pattern 27 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 126:
            return 'Random pattern 26 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 125:
            return 'Random pattern 25 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 124:
            return 'Random pattern 24 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 123:
            return 'Random pattern 23 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 122:
            return 'Random pattern 22 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 121:
            return 'Random pattern 21 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 120:
            return 'Random pattern 20 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 119:
            return 'Random pattern 19 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 118:
            return 'Random pattern 18 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 117:
            return 'Random pattern 17 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 116:
            return 'Random pattern 16 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 115:
            return 'Random pattern 15 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 114:
            return 'Random pattern 14 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 113:
            return 'Random pattern 13 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 112:
            return 'Random pattern 12 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 111:
            return 'Random pattern 11 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 110:
            return 'Random pattern 10 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 109:
            return 'Random pattern 9 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 108:
            return 'Random pattern 8 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 107:
            return 'Random pattern 7 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 106:
            return 'Random pattern 6 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 105:
            return 'Random pattern 5 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 104:
            return 'Random pattern 4 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 103:
            return 'Random pattern 3 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 102:
            return 'Random pattern 2 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 101:
            return 'Random pattern 1 for SPP scheme'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 5:
            return 'Random pattern 5 for sppt'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 4:
            return 'Random pattern 4 for sppt'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 3:
            return 'Random pattern 3 for sppt'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 2:
            return 'Random pattern 2 for sppt'

        if discipline == 192 and parameterCategory == 213 and parameterNumber == 1:
            return 'Random pattern 1 for sppt'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 255:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 254:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 253:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 252:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 251:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 250:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 249:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 248:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 247:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 246:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 245:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 244:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 243:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 242:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 241:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 240:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 239:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 238:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 237:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 236:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 235:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 234:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 233:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 232:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 231:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 230:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 229:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 228:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 227:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 226:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 225:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 224:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 223:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 222:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 221:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 220:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 219:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 218:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 217:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 216:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 215:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 214:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 213:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 212:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 211:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 210:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 209:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 208:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 207:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 206:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 205:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 204:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 203:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 202:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 201:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 200:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 199:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 198:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 197:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 196:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 195:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 194:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 193:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 192:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 191:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 190:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 189:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 188:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 187:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 186:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 185:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 184:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 183:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 182:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 181:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 180:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 179:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 178:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 177:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 176:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 175:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 174:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 173:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 172:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 171:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 170:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 169:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 168:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 167:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 166:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 165:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 164:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 163:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 162:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 161:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 160:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 159:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 158:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 157:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 156:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 155:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 154:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 153:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 152:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 151:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 150:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 149:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 148:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 147:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 146:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 145:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 144:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 143:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 142:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 141:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 140:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 139:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 138:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 137:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 136:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 135:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 134:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 133:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 132:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 131:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 130:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 129:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 128:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 127:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 126:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 125:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 124:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 123:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 122:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 121:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 120:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 119:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 118:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 117:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 116:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 115:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 114:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 113:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 112:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 111:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 110:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 109:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 108:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 107:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 106:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 105:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 104:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 103:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 102:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 101:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 100:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 99:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 98:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 97:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 96:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 95:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 94:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 93:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 92:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 91:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 90:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 89:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 88:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 87:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 86:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 85:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 84:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 83:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 82:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 81:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 80:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 79:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 78:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 77:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 76:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 75:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 74:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 73:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 72:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 71:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 70:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 69:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 68:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 67:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 66:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 65:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 64:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 63:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 62:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 61:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 60:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 59:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 58:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 57:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 56:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 55:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 54:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 53:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 52:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 51:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 50:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 49:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 48:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 47:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 46:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 45:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 44:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 43:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 42:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 41:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 40:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 39:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 38:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 37:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 36:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 35:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 34:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 33:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 32:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 31:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 30:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 29:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 28:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 27:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 26:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 25:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 24:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 23:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 22:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 21:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 20:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 19:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 18:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 17:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 16:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 15:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 14:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 13:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 12:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 11:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 10:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 9:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 8:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 7:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 6:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 5:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 4:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 3:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 2:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 212 and parameterNumber == 1:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 120:
            return 'Altitude of plume top'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 119:
            return 'Altitude of emitter'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 56:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 55:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 45:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 4'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 44:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 3'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 43:
            return 'DMS surface emission'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 30:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 2'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 29:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 1'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 28:
            return 'SO4 aerosol precursor mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 15:
            return 'Aerosol type 15 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 14:
            return 'Aerosol type 14 mass mixing ratio'

        if discipline == 192 and parameterCategory == 211 and parameterNumber == 13:
            return 'Aerosol type 13 mass mixing ratio'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 65533 and is_aerosol == 1:
            return 'Nitrate coarse mode aerosol mass mixing ratio'

        if localTablesVersion == 1 and discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and is_aerosol == 1 and aerosolType == 65534:
            return 'Nitrate fine mode aerosol mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 246:
            return 'Profile of total aerosol dry absorption coefficient'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 245:
            return 'Profile of total aerosol dry extinction coefficient'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 244:
            return 'Volcanic ash optical depth at 550 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 243:
            return 'Volcanic sulphate aerosol optical depth at 550 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 242:
            return 'Altitude of plume bottom'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 241:
            return 'Wildfire Flux of Heptane (C7H16)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 240:
            return 'Wildfire Flux of Hexanes (C6H14)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 239:
            return 'Wildfire Flux of Pentanes (C5H12)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 238:
            return 'Wildfire Flux of Butanes (C4H10)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 237:
            return 'Wildfire Flux of Octene (C8H16)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 236:
            return 'Wildfire Flux of Hexene (C6H12)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 235:
            return 'Wildfire Flux of Pentenes (C5H10)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 234:
            return 'Wildfire Flux of Butenes (C4H8)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 233:
            return 'Wildfire Flux of Xylene (C8H10)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 232:
            return 'Wildfire Flux of Benzene (C6H6)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 231:
            return 'Wildfire Flux of Toluene (C7H8)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 230:
            return 'Total aerosol optical depth at 2130 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 229:
            return 'Total aerosol optical depth at 1640 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 228:
            return 'Total aerosol optical depth at 1064 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 227:
            return 'Total aerosol optical depth at 1020 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 226:
            return 'Total aerosol optical depth at 858 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 225:
            return 'Total aerosol optical depth at 800 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 224:
            return 'Total aerosol optical depth at 645 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 223:
            return 'Total aerosol optical depth at 532 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 222:
            return 'Total aerosol optical depth at 500 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 221:
            return 'Total aerosol optical depth at 440 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 220:
            return 'Total aerosol optical depth at 400 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 219:
            return 'Total aerosol optical depth at 380 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 218:
            return 'Total aerosol optical depth at 355 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 217:
            return 'Total aerosol optical depth at 340 nm'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 197:
            return 'Near IR albedo for diffuse radiation, geometric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 196:
            return 'Near IR albedo for diffuse radiation, volumetric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 195:
            return 'Near IR albedo for diffuse radiation, isotropic component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 194:
            return 'UV visible albedo for diffuse radiation, geometric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 193:
            return 'UV visible albedo for diffuse radiation, volumetric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 192:
            return 'UV visible albedo for diffuse radiation, isotropic component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 191:
            return 'Near IR albedo for direct radiation, geometric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 190:
            return 'Near IR albedo for direct radiation, volumetric component'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 189:
            return 'Near IR albedo for direct radiation, isotropic component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 188:
            return 'UV visible albedo for direct radiation, geometric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 187:
            return 'UV visible albedo for direct radiation, volumetric component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 186:
            return 'UV visible albedo for direct radiation, isotropic component '

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 179:
            return 'Wildfire night-time inverse variance of radiative power'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 177:
            return 'Wildfire day-time inverse variance of radiative power'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 169:
            return 'Wildfire night-time radiative power'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 167:
            return 'Wildfire day-time radiative power'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 120:
            return 'Altitude of plume top'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 119:
            return 'Mean altitude of maximum injection'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 118:
            return 'Wildfire Flux of Ethane (C2H6)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 79:
            return 'Wildfire viewing angle of observation'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 74:
            return 'Particulate matter d < 10 um'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 73:
            return 'Particulate matter d < 2.5 um'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 72:
            return 'Particulate matter d < 1 um'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 60:
            return 'Injection height (from IS4FIRES)'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 59:
            return 'Secondary organic precursor mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 58:
            return 'Monoterpene precursor mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 57:
            return 'Mixing ration of organic carbon aerosol, nucleation mode'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 56:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 55:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 45:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 4'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 44:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 3'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 43:
            return 'DMS surface emission'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 30:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 2'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 29:
            return 'Water vapour mixing ratio for hydrophilic aerosols in mode 1'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 28:
            return 'SO4 aerosol precursor mass mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 15:
            return 'Volcanic SO2 precursor mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 14:
            return 'Volcanic sulphate aerosol mixing ratio'

        if discipline == 192 and parameterCategory == 210 and parameterNumber == 13:
            return 'Volcanic ash aerosol mixing ratio'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 122:
            return 'Minimum temperature at 2 metres in the last 6 hours anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 121:
            return 'Maximum temperature at 2 metres in the last 6 hours anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 7:
            return '100 metre V wind component anomaly'

        if discipline == 192 and parameterCategory == 171 and parameterNumber == 6:
            return '100 metre U wind component anomaly'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 141:
            return 'q-tendency from shallow convection'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 140:
            return 'T-tendency from shallow convection'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 139:
            return 'V-tendency from shallow convection'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 138:
            return 'U-tendency from shallow convection'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 137:
            return 'Ice Precip flux from cloud scheme (stratiform)'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 136:
            return 'Liquid Precip flux from cloud scheme (stratiform)'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 135:
            return 'qi-tendency from cloud scheme'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 134:
            return 'ql-tendency from cloud scheme'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 133:
            return 'q-tendency from cloud scheme'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 132:
            return 'T-tendency from cloud scheme'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 131:
            return 'Ice Precipitation flux from convection'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 130:
            return 'Liquid Precipitation flux from convection'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 129:
            return 'q-tendency from convection (deep+shallow)'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 128:
            return 'T-tendency from convection (deep+shallow)'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 127:
            return 'V-tendency from convection (deep+shallow)'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 126:
            return 'U-tendency from convection (deep+shallow)'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 125:
            return 'T-tendency from subgrid orography'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 124:
            return 'V-tendency from subgrid orography'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 123:
            return 'U-tendency from subgrid orography'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 122:
            return 'q-tendency from turbulent diffusion'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 121:
            return 'T-tendency from turbulent diffusion + subgrid orography'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 120:
            return 'V-tendency from turbulent diffusion + subgrid orography'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 119:
            return 'U-tendency from turbulent diffusion + subgrid orography'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 118:
            return 'T-tendency from radiation'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 117:
            return 'q-tendency from dynamics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 116:
            return 'T-tendency from dynamics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 115:
            return 'V-tendency from dynamics'

        if discipline == 192 and parameterCategory == 162 and parameterNumber == 114:
            return 'U-tendency from dynamics'

        if discipline == 192 and parameterCategory == 151 and parameterNumber == 193:
            return 'Reserved'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 255:
            return 'Indicates a missing value'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 254:
            return 'Adiabatic tendency of meridional wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 253:
            return 'Adiabatic tendency of zonal wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 252:
            return 'Adiabatic tendency of humidity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 251:
            return 'Adiabatic tendency of temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 250:
            return 'Ice age difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 249:
            return 'Accumulated ice water tendency difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 248:
            return 'Cloud cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 247:
            return 'Specific cloud ice water content difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 246:
            return 'Specific cloud liquid water content difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 245:
            return 'Forecast logarithm of surface roughness for heat difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 244:
            return 'Forecast surface roughness difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 243:
            return 'Forecast albedo difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 242:
            return 'Accumulated liquid water tendency difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 241:
            return 'Accumulated cloud fraction tendency difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 240:
            return 'Large scale snowfall difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 239:
            return 'Convective snowfall difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 238:
            return 'Temperature of snow layer difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 237:
            return 'Soil wetness level 4 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 236:
            return 'Soil temperature level 4 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 235:
            return 'Skin temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 234:
            return 'Logarithm of surface roughness length for heat difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 233:
            return 'Apparent surface humidity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 232:
            return 'Instantaneous moisture flux difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 231:
            return 'Instantaneous surface heat flux difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 230:
            return 'Instantaneous Y surface stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 229:
            return 'Instantaneous X surface stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 228:
            return 'Total precipitation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 227:
            return 'Change from removal of negative humidity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 226:
            return 'Humidity tendency by large-scale condensation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 225:
            return 'Humidity tendency by cumulus convection difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 224:
            return 'Vertical diffusion of humidity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 223:
            return 'Convective tendency of meridional wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 222:
            return 'Convective tendency of zonal wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 221:
            return 'North-South gravity wave drag tendency difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 220:
            return 'East-West gravity wave drag tendency difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 219:
            return 'Vertical diffusion of meridional wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 218:
            return 'Vertical diffusion of zonal wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 217:
            return 'Diabatic heating large-scale condensation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 216:
            return 'Diabatic heating by cumulus convection difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 215:
            return 'Diabatic heating by vertical diffusion difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 214:
            return 'Diabatic heating by radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 212:
            return 'TOA incident solar radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 211:
            return 'Surface net thermal radiation, clear sky difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 210:
            return 'Surface net solar radiation, clear sky difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 209:
            return 'Top net thermal radiation, clear sky difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 208:
            return 'Top net solar radiation, clear sky difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 207:
            return '10 metre wind speed difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 206:
            return 'Total column ozone difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 205:
            return 'Runoff difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 204:
            return 'Precipitation analysis weights difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 203:
            return 'Ozone mass mixing ratio difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 202:
            return 'Minimum temperature at 2 metres since previous post-processing difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 201:
            return 'Maximum temperature at 2 metres since previous post-processing difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 200:
            return 'Variance of sub-gridscale orography difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 199:
            return 'Vegetation fraction difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 198:
            return 'Skin reservoir content difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 197:
            return 'Gravity wave dissipation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 196:
            return 'Meridional component of gravity wave stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 195:
            return 'Longitudinal component of gravity wave stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 194:
            return 'Brightness temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 191:
            return 'North-South component of sub-gridscale orographic variance difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 190:
            return 'East-West component of sub-gridscale orographic variance difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 189:
            return 'Sunshine duration difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 188:
            return 'High cloud cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 187:
            return 'Medium cloud cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 186:
            return 'Low cloud cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 185:
            return 'Convective cloud cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 184:
            return 'Soil wetness level 3 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 183:
            return 'Soil temperature level 3 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 182:
            return 'Evaporation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 181:
            return 'North-South surface stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 180:
            return 'East-West surface stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 179:
            return 'Top net thermal radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 178:
            return 'Top net solar radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 177:
            return 'Surface net thermal radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 176:
            return 'Surface net solar radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 175:
            return 'Surface thermal radiation downwards difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 174:
            return 'Albedo difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 173:
            return 'Surface roughness difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 172:
            return 'Land-sea mask difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 171:
            return 'Soil wetness level 2 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 170:
            return 'Soil temperature level 2 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 169:
            return 'Surface solar radiation downwards difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 167:
            return '2 metre temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 166:
            return '10 metre V wind component difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 165:
            return '10 metre U wind component difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 164:
            return 'Total cloud cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 163:
            return 'Slope of sub-gridscale orography difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 162:
            return 'Angle of sub-gridscale orography difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 161:
            return 'Anisotropy of sub-gridscale orography difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 160:
            return 'Standard deviation of orography difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 159:
            return 'Boundary layer height difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 158:
            return 'Tendency of surface pressure difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 157:
            return 'Relative humidity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 156:
            return 'Height difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 155:
            return 'Divergence difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 154:
            return 'Long-wave heating rate difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 153:
            return 'Short-wave heating rate difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 152:
            return 'Logarithm of surface pressure difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 151:
            return 'Mean sea level pressure difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 150:
            return 'Top net radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 149:
            return 'Surface net radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 148:
            return 'Charnock difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 147:
            return 'Surface latent heat flux difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 146:
            return 'Surface sensible heat flux difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 145:
            return 'Boundary layer dissipation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 144:
            return 'Snowfall (convective + stratiform) difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 143:
            return 'Convective precipitation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 142:
            return 'Stratiform precipitation (Large-scale precipitation) difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 141:
            return 'Snow depth difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 140:
            return 'Soil wetness level 1 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 139:
            return 'Soil temperature level 1 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 138:
            return 'Vorticity (relative) difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 137:
            return 'Total column water vapour difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 136:
            return 'Total column water difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 135:
            return 'Vertical velocity (pressure) difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 134:
            return 'Surface pressure difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 133:
            return 'Specific humidity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 132:
            return 'V component of wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 131:
            return 'U component of wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 130:
            return 'Temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 129:
            return 'Geopotential difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 128:
            return 'Budget values difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 127:
            return 'Atmospheric tide difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 126:
            return 'Generic parameter for sensitive area prediction'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 125:
            return 'Vertically integrated total energy'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 123:
            return '10 metre wind gust in the last 6 hours difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 122:
            return 'Minimum temperature at 2 metres difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 121:
            return 'Maximum temperature at 2 metres difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 120:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 119:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 118:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 117:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 116:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 115:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 114:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 113:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 112:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 111:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 110:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 109:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 108:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 107:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 106:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 105:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 104:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 103:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 102:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 101:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 100:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 99:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 98:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 97:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 96:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 95:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 94:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 93:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 92:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 91:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 90:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 89:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 88:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 87:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 86:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 85:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 84:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 83:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 82:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 81:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 80:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 79:
            return 'Total column ice water'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 78:
            return 'Total column liquid water'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 71:
            return 'Biome cover, high vegetation'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 70:
            return 'Biome cover, low vegetation'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 69:
            return 'Minimum stomatal resistance, high vegetation'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 68:
            return 'Minimum stomatal resistance, low vegetation'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 67:
            return 'Leaf area index, high vegetation'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 66:
            return 'Leaf area index, low vegetation'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 65:
            return 'Skin temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 64:
            return 'Finish time for skin temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 63:
            return 'Start time for skin temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 62:
            return 'Observation count difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 61:
            return 'Total precipitation from observations difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 60:
            return 'Potential vorticity difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 59:
            return 'Convective available potential energy difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 58:
            return 'Photosynthetically active radiation at the surface difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 57:
            return 'Downward UV radiation at the surface difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 55:
            return 'Mean 2 metre temperature in the last 24 hours difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 54:
            return 'Pressure difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 53:
            return 'Montgomery potential difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 52:
            return 'Minimum 2 metre temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 51:
            return 'Maximum 2 metre temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 50:
            return 'Large-scale precipitation fraction difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 49:
            return '10 metre wind gust difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 48:
            return 'Magnitude of turbulent surface stress difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 47:
            return 'Direct solar radiation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 46:
            return 'Solar duration difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 45:
            return 'Snowmelt difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 44:
            return 'Snow evaporation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 43:
            return 'Soil type difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 42:
            return 'Volumetric soil water layer 4 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 41:
            return 'Volumetric soil water layer 3 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 40:
            return 'Volumetric soil water layer 2 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 39:
            return 'Volumetric soil water layer 1 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 38:
            return 'Ice surface temperature layer 4 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 37:
            return 'Ice surface temperature layer 3 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 36:
            return 'Ice surface temperature layer 2 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 35:
            return 'Ice surface temperature layer 1 difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 34:
            return 'Sea surface temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 33:
            return 'Snow density difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 32:
            return 'Snow albedo difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 31:
            return 'Sea-ice cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 30:
            return 'Type of high vegetation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 29:
            return 'Type of low vegetation difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 28:
            return 'High vegetation cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 27:
            return 'Low vegetation cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 26:
            return 'Lake cover difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 25:
            return 'Reserved for future unbalanced components'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 24:
            return 'Reserved for future unbalanced components'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 23:
            return 'Unbalanced component of divergence difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 22:
            return 'Unbalanced component of logarithm of surface pressure difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 21:
            return 'Unbalanced component of temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 14:
            return 'V component of rotational wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 13:
            return 'U component of rotational wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 12:
            return 'V component of divergent wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 11:
            return 'U component of divergent wind difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 5:
            return 'Saturated equivalent potential temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 4:
            return 'Equivalent potential temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 3:
            return 'Potential temperature difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 2:
            return 'Velocity potential difference'

        if discipline == 192 and parameterCategory == 200 and parameterNumber == 1:
            return 'Stream function difference'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 254:
            return 'Adiabatic tendency of meridional wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 253:
            return 'Adiabatic tendency of zonal wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 252:
            return 'Adiabatic tendency of humidity'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 251:
            return 'Adiabatic tendency of temperature'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 250:
            return 'Ice age'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 249:
            return 'Accumulated ice water tendency'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 245:
            return 'Forecast logarithm of surface roughness for heat'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 244:
            return 'Forecast surface roughness'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 243:
            return 'Forecast albedo'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 242:
            return 'Accumulated liquid water tendency'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 241:
            return 'Accumulated cloud fraction tendency'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 240:
            return 'Large-scale snowfall'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 239:
            return 'Convective snowfall'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 238:
            return 'Temperature of snow layer'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 237:
            return 'Soil wetness level 4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 236:
            return 'Soil temperature level 4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 234:
            return 'Logarithm of surface roughness length for heat'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 233:
            return 'Apparent surface humidity'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 232:
            return 'Instantaneous moisture flux'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 231:
            return 'Instantaneous surface sensible heat flux'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 230:
            return 'Instantaneous northward turbulent surface stress'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 229:
            return 'Instantaneous eastward turbulent surface stress'

        unitsFactor = h.get_l('unitsFactor')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and unitsFactor == 1000:
            return 'Total precipitation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 227:
            return 'Tendency due to removal of negative humidity'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 226:
            return 'Humidity tendency by large-scale condensation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 225:
            return 'Humidity tendency by cumulus convection'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 224:
            return 'Vertical diffusion of humidity'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 223:
            return 'Convective tendency of meridional wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 222:
            return 'Convective tendency of zonal wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 221:
            return 'North-South gravity wave drag tendency'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 220:
            return 'East-West gravity wave drag tendency'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 219:
            return 'Vertical diffusion of meridional wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 218:
            return 'Vertical diffusion of zonal wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 217:
            return 'Diabatic heating large-scale condensation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 216:
            return 'Diabatic heating by cumulus convection'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 215:
            return 'Diabatic heating by vertical diffusion'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 214:
            return 'Diabatic heating by radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 213:
            return 'Vertically integrated moisture divergence'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 212:
            return 'TOA incident solar radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 209:
            return 'Top net thermal radiation, clear sky'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 208:
            return 'Top net solar radiation, clear sky'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 206:
            return 'Total column ozone'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 205:
            return 'Runoff'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 204:
            return 'Precipitation analysis weights'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 200:
            return 'Variance of sub-gridscale orography'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 199:
            return 'Vegetation fraction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 198:
            return 'Skin reservoir content'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 197:
            return 'Gravity wave dissipation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 196:
            return 'Northward gravity wave surface stress'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 195:
            return 'Eastward gravity wave surface stress'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 193:
            return 'North-East/South-West component of sub-gridscale orographic variance'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 192:
            return 'North-West/South-East component of sub-gridscale orographic variance'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 191:
            return 'North-South component of sub-gridscale orographic variance'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 190:
            return 'East-West component of sub-gridscale orographic variance'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 188:
            return 'High cloud cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 187:
            return 'Medium cloud cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 186:
            return 'Low cloud cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 185:
            return 'Convective cloud cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 184:
            return 'Soil wetness level 3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 183:
            return 'Soil temperature level 3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 182:
            return 'Evaporation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 178:
            return 'Top net solar radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 174:
            return 'Albedo'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 171:
            return 'Soil wetness level 2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 170:
            return 'Soil temperature level 2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 164:
            return 'Total cloud cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 163:
            return 'Slope of sub-gridscale orography'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 162:
            return 'Angle of sub-gridscale orography'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 161:
            return 'Anisotropy of sub-gridscale orography'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 160:
            return 'Standard deviation of orography'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 159:
            return 'Boundary layer height'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 158:
            return 'Tendency of surface pressure'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 154:
            return 'Long-wave heating rate'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 153:
            return 'Short-wave heating rate'

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25 and typeOfFirstFixedSurface == 105:
            return 'Logarithm of surface pressure'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 150:
            return 'Top net radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 149:
            return 'Surface net radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 148:
            return 'Charnock'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 144:
            return 'Snowfall'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10 and unitsFactor == 1000:
            return 'Convective precipitation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 142:
            return 'Large-scale precipitation'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and unitsFactor == 1000:
            return 'Snow depth'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 140:
            return 'Soil wetness level 1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 139:
            return 'Soil temperature level 1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 137:
            return 'Total column water vapour'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 128:
            return 'Budget values'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 127:
            return 'Atmospheric tide'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 126:
            return 'Generic parameter for sensitive area prediction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 125:
            return 'Vertically integrated total energy'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 124:
            return 'Surface emissivity'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 123:
            return '10 metre wind gust in the last 6 hours'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 120:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 119:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 118:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 117:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 116:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 115:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 114:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 113:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 112:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 111:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 110:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 109:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 108:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 107:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 106:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 105:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 104:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 103:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 102:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 101:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 100:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 99:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 98:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 97:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 96:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 95:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 94:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 93:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 92:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 91:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 90:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 89:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 88:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 87:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 86:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 85:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 84:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 83:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 82:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 81:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 80:
            return 'Experimental product'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 79:
            return 'Total column cloud ice water'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 78:
            return 'Total column cloud liquid water'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 74:
            return 'Standard deviation of filtered subgrid orography'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 73:
            return 'Instantaneous surface thermal radiation downwards'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 72:
            return 'Instantaneous surface solar radiation downwards'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 71:
            return 'Biome cover, high vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 70:
            return 'Biome cover, low vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 69:
            return 'Minimum stomatal resistance, high vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 68:
            return 'Minimum stomatal resistance, low vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 67:
            return 'Leaf area index, high vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 66:
            return 'Leaf area index, low vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 65:
            return 'Skin temperature difference'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 64:
            return 'Finish time for skin temperature difference'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 63:
            return 'Start time for skin temperature difference'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 62:
            return 'Observation count'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 58:
            return 'Photosynthetically active radiation at the surface'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 57:
            return 'Downward UV radiation at the surface'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 56:
            return 'Mean 2 metre dewpoint temperature in the last 24 hours'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 55:
            return 'Mean temperature at 2 metres in the last 24 hours'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 53:
            return 'Montgomery potential'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 24 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 'Minimum temperature at 2 metres in the last 24 hours'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and lengthOfTimeRange == 24 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 'Maximum temperature at 2 metres in the last 24 hours'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 50:
            return 'Large-scale precipitation fraction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 48:
            return 'Magnitude of turbulent surface stress'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 47:
            return 'Direct solar radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 46:
            return 'Solar duration'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 45:
            return 'Snowmelt'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 44:
            return 'Snow evaporation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 42:
            return 'Volumetric soil water layer 4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 41:
            return 'Volumetric soil water layer 3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 40:
            return 'Volumetric soil water layer 2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 39:
            return 'Volumetric soil water layer 1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 38:
            return 'Ice temperature layer 4'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 37:
            return 'Ice temperature layer 3'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 36:
            return 'Ice temperature layer 2'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 35:
            return 'Ice temperature layer 1'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 32:
            return 'Snow albedo'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 30:
            return 'Type of high vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 29:
            return 'Type of low vegetation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 28:
            return 'High vegetation cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 27:
            return 'Low vegetation cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 26:
            return 'Lake cover'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 25:
            return 'Reserved for future unbalanced components'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 24:
            return 'Reserved for future unbalanced components'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 23:
            return 'Unbalanced component of divergence'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 22:
            return 'Unbalanced component of logarithm of surface pressure'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 21:
            return 'Unbalanced component of temperature'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 20:
            return 'Clear sky surface photosynthetically active radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 19:
            return 'Clear sky surface UV'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 18:
            return 'Near IR albedo for diffuse radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 17:
            return 'Near IR albedo for direct radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 16:
            return 'UV visible albedo for diffuse radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 15:
            return 'UV visible albedo for direct radiation'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 14:
            return 'V component of rotational wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 13:
            return 'U component of rotational wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 12:
            return 'V component of divergent wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 11:
            return 'U component of divergent wind'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 9:
            return 'Sub-surface runoff'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 8:
            return 'Surface runoff'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 7:
            return 'Soil clay fraction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 6:
            return 'Soil sand fraction'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 5:
            return 'Saturated equivalent potential temperature'

        if discipline == 192 and parameterCategory == 128 and parameterNumber == 4:
            return 'Equivalent potential temperature'

        if discipline == 192 and parameterCategory == 131 and parameterNumber == 85:
            return 'Total precipitation of at least 100 mm'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 100 and productDefinitionTemplateNumber == 9:
            return 'Total precipitation of at least 100 mm'

    return wrapped
