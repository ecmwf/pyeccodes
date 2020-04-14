def load(h):
    return ({'abbr': 0, 'code': 0, 'title': 'Ozone O3'},
            {'abbr': 1, 'code': 1, 'title': 'Water vapour H2O'},
            {'abbr': 2, 'code': 2, 'title': 'Methane CH4'},
            {'abbr': 3, 'code': 3, 'title': 'Carbon dioxide CO2'},
            {'abbr': 4, 'code': 4, 'title': 'Carbon monoxide CO'},
            {'abbr': 5, 'code': 5, 'title': 'Nitrogen dioxide NO2'},
            {'abbr': 6, 'code': 6, 'title': 'Nitrous oxide N2O'},
            {'abbr': 7, 'code': 7, 'title': 'Formaldehyde HCHO'},
            {'abbr': 8, 'code': 8, 'title': 'Sulphur dioxide SO2'},
            {'abbr': 9, 'code': 9, 'title': 'Ammonia NH3'},
            {'abbr': 10, 'code': 10, 'title': 'Ammonium NH4'},
            {'abbr': 11, 'code': 11, 'title': 'Nitrogen monoxide NO'},
            {'abbr': 12, 'code': 12, 'title': 'Atomic oxygen O'},
            {'abbr': 13, 'code': 13, 'title': 'Nitrate radical NO3'},
            {'abbr': 14, 'code': 14, 'title': 'Hydroperoxyl radical HO2'},
            {'abbr': 15, 'code': 15, 'title': 'Dinitrogen pentoxide N2O5'},
            {'abbr': 16, 'code': 16, 'title': 'Nitrous acid HONO'},
            {'abbr': 17, 'code': 17, 'title': 'Nitric acid HNO3'},
            {'abbr': 18, 'code': 18, 'title': 'Peroxynitric acid HO2NO2'},
            {'abbr': 19, 'code': 19, 'title': 'Hydrogen peroxide H2O2'},
            {'abbr': 20, 'code': 20, 'title': 'Molecular hydrogen H2'},
            {'abbr': 21, 'code': 21, 'title': 'Atomic nitrogen N'},
            {'abbr': 22, 'code': 22, 'title': 'Sulphate SO42-'},
            {'abbr': 23, 'code': 23, 'title': 'Radon Rn'},
            {'abbr': 24, 'code': 24, 'title': 'Elemental mercury Hg(0)'},
            {'abbr': 25, 'code': 25, 'title': 'Divalent mercury Hg2+'},
            {'abbr': 26, 'code': 26, 'title': 'Atomic chlorine Cl'},
            {'abbr': 27, 'code': 27, 'title': 'Chlorine monoxide ClO'},
            {'abbr': 28, 'code': 28, 'title': 'Dichlorine peroxide Cl2O2'},
            {'abbr': 29, 'code': 29, 'title': 'Hypochlorous acid HClO'},
            {'abbr': 30, 'code': 30, 'title': 'Chlorine nitrate ClONO2'},
            {'abbr': 31, 'code': 31, 'title': 'Chlorine dioxide ClO2'},
            {'abbr': 32, 'code': 32, 'title': 'Atomic bromine Br'},
            {'abbr': 33, 'code': 33, 'title': 'Bromine monoxide BrO'},
            {'abbr': 34, 'code': 34, 'title': 'Bromine chloride BrCl'},
            {'abbr': 35, 'code': 35, 'title': 'Hydrogen bromide HBr'},
            {'abbr': 36, 'code': 36, 'title': 'Hypobromous acid HBrO'},
            {'abbr': 37, 'code': 37, 'title': 'Bromine nitrate BrONO2'},
            {'abbr': 38, 'code': 38, 'title': 'Oxygen O2'},
            {'abbr': 10000, 'code': 10000, 'title': 'Hydroxyl radical OH'},
            {'abbr': 10001, 'code': 10001, 'title': 'Methyl peroxy radical CH3O2'},
            {'abbr': 10002, 'code': 10002, 'title': 'Methyl hydroperoxide CH3O2H'},
            {'abbr': 10004, 'code': 10004, 'title': 'Methanol CH3OH'},
            {'abbr': 10005, 'code': 10005, 'title': 'Formic acid CH3OOH'},
            {'abbr': 10006, 'code': 10006, 'title': 'Hydrogen cyanide HCN'},
            {'abbr': 10007, 'code': 10007, 'title': 'Aceto nitrile CH3CN'},
            {'abbr': 10008, 'code': 10008, 'title': 'Ethane C2H6'},
            {'abbr': 10009, 'code': 10009, 'title': 'Ethene (= Ethylene) C2H4'},
            {'abbr': 10010, 'code': 10010, 'title': 'Ethyne (= Acetylene) C2H2'},
            {'abbr': 10011, 'code': 10011, 'title': 'Ethanol C2H5OH'},
            {'abbr': 10012, 'code': 10012, 'title': 'Acetic acid C2H5OOH'},
            {'abbr': 10013, 'code': 10013, 'title': 'Peroxyacetyl nitrate CH3C(O)OONO2'},
            {'abbr': 10014, 'code': 10014, 'title': 'Propane C3H8'},
            {'abbr': 10015, 'code': 10015, 'title': 'Propene C3H6'},
            {'abbr': 10016, 'code': 10016, 'title': 'Butanes C4H10'},
            {'abbr': 10017, 'code': 10017, 'title': 'Isoprene C5H10'},
            {'abbr': 10018, 'code': 10018, 'title': 'Alpha pinene C10H16'},
            {'abbr': 10019, 'code': 10019, 'title': 'Beta pinene C10H16'},
            {'abbr': 10020, 'code': 10020, 'title': 'Limonene C10H16'},
            {'abbr': 10021, 'code': 10021, 'title': 'Benzene C6H6'},
            {'abbr': 10022, 'code': 10022, 'title': 'Toluene C7H8'},
            {'abbr': 10023, 'code': 10023, 'title': 'Xylene C8H10'},
            {'abbr': 10500,
             'code': 10500,
             'title': 'Dimethyl sulphide CH3SCH3',
             'units': 'DMS'},
            {'abbr': 20001, 'code': 20001, 'title': 'Hydrogen chloride'},
            {'abbr': 20002, 'code': 20002, 'title': 'CFC-11'},
            {'abbr': 20003, 'code': 20003, 'title': 'CFC-12'},
            {'abbr': 20004, 'code': 20004, 'title': 'CFC-113'},
            {'abbr': 20005, 'code': 20005, 'title': 'CFC-113a'},
            {'abbr': 20006, 'code': 20006, 'title': 'CFC-114'},
            {'abbr': 20007, 'code': 20007, 'title': 'CFC-115'},
            {'abbr': 20008, 'code': 20008, 'title': 'HCFC-22'},
            {'abbr': 20009, 'code': 20009, 'title': 'HCFC-141b'},
            {'abbr': 20010, 'code': 20010, 'title': 'HCFC-142b'},
            {'abbr': 20011, 'code': 20011, 'title': 'Halon-1202'},
            {'abbr': 20012, 'code': 20012, 'title': 'Halon-1211'},
            {'abbr': 20013, 'code': 20013, 'title': 'Halon-1301'},
            {'abbr': 20014, 'code': 20014, 'title': 'Halon-2402'},
            {'abbr': 20015, 'code': 20015, 'title': 'Methyl chloride', 'units': 'HCC-40'},
            {'abbr': 20016,
             'code': 20016,
             'title': 'Carbon tetrachloride',
             'units': 'HCC-10'},
            {'abbr': 20017, 'code': 20017, 'title': 'HCC-140a CH3CCl3'},
            {'abbr': 20018, 'code': 20018, 'title': 'Methyl bromide', 'units': 'HBC-40B1'},
            {'abbr': 20019,
             'code': 20019,
             'title': 'Hexachlorocyclohexane',
             'units': 'HCH'},
            {'abbr': 20020, 'code': 20020, 'title': 'Alpha hexachlorocyclohexane'},
            {'abbr': 20021,
             'code': 20021,
             'title': 'Hexachlorobiphenyl',
             'units': 'PCB-153'},
            {'abbr': 30000,
             'code': 30000,
             'title': 'Radioactive pollutant',
             'units': 'tracer, defined by originating centre'},
            {'abbr': 30010, 'code': 30010, 'title': 'Hydrogen H-3'},
            {'abbr': 30011, 'code': 30011, 'title': 'Hydrogen organic bounded H-3o'},
            {'abbr': 30012, 'code': 30012, 'title': 'Hydrogen inorganic H-3a'},
            {'abbr': 30013, 'code': 30013, 'title': 'Beryllium 7 Be-7'},
            {'abbr': 30014, 'code': 30014, 'title': 'Beryllium 10 Be-10'},
            {'abbr': 30015, 'code': 30015, 'title': 'Carbon 14 C-14'},
            {'abbr': 30016, 'code': 30016, 'title': 'Carbon 14 CO2 C-14CO2'},
            {'abbr': 30017, 'code': 30017, 'title': 'Carbon 14 other gases C-14og'},
            {'abbr': 30018, 'code': 30018, 'title': 'Nitrogen 13 N-13'},
            {'abbr': 30019, 'code': 30019, 'title': 'Nitrogen 16 N-16'},
            {'abbr': 30020, 'code': 30020, 'title': 'Fluorine 18 F-18'},
            {'abbr': 30021, 'code': 30021, 'title': 'Sodium 22 Na-22'},
            {'abbr': 30022, 'code': 30022, 'title': 'Phosphate 32 P-32'},
            {'abbr': 30023, 'code': 30023, 'title': 'Phosphate 33 P-33'},
            {'abbr': 30024, 'code': 30024, 'title': 'Sulphur 35 S-35'},
            {'abbr': 30025, 'code': 30025, 'title': 'Chlorine 36 Cl-36'},
            {'abbr': 30026, 'code': 30026, 'title': 'Potassium 40 K-40'},
            {'abbr': 30027, 'code': 30027, 'title': 'Argon 41 Ar-41'},
            {'abbr': 30028, 'code': 30028, 'title': 'Calcium 41 Ca-41'},
            {'abbr': 30029, 'code': 30029, 'title': 'Calcium 45 Ca-45'},
            {'abbr': 30030, 'code': 30030, 'title': 'Titanium 44 Ti-44'},
            {'abbr': 30031, 'code': 30031, 'title': 'Scandium 46 Sc-46'},
            {'abbr': 30032, 'code': 30032, 'title': 'Vanadium 48 V-48'},
            {'abbr': 30033, 'code': 30033, 'title': 'Vanadium 49 V-49'},
            {'abbr': 30034, 'code': 30034, 'title': 'Chrome 51 Cr-51'},
            {'abbr': 30035, 'code': 30035, 'title': 'Manganese 52 Mn-52'},
            {'abbr': 30036, 'code': 30036, 'title': 'Manganese 54 Mn-54'},
            {'abbr': 30037, 'code': 30037, 'title': 'Iron 55 Fe-55'},
            {'abbr': 30038, 'code': 30038, 'title': 'Iron 59 Fe-59'},
            {'abbr': 30039, 'code': 30039, 'title': 'Cobalt 56 Co-56'},
            {'abbr': 30040, 'code': 30040, 'title': 'Cobalt 57 Co-57'},
            {'abbr': 30041, 'code': 30041, 'title': 'Cobalt 58 Co-58'},
            {'abbr': 30042, 'code': 30042, 'title': 'Cobalt 60 Co-60'},
            {'abbr': 30043, 'code': 30043, 'title': 'Nickel 59 Ni-59'},
            {'abbr': 30044, 'code': 30044, 'title': 'Nickel 63 Ni-63'},
            {'abbr': 30045, 'code': 30045, 'title': 'Zinc 65 Zn-65'},
            {'abbr': 30046, 'code': 30046, 'title': 'Gallium 67 Ga-67'},
            {'abbr': 30047, 'code': 30047, 'title': 'Gallium 68 Ga-68'},
            {'abbr': 30048, 'code': 30048, 'title': 'Germanium 68 Ge-68'},
            {'abbr': 30049, 'code': 30049, 'title': 'Germanium 69 Ge-69'},
            {'abbr': 30050, 'code': 30050, 'title': 'Arsenic 73 As-73'},
            {'abbr': 30051, 'code': 30051, 'title': 'Selenium 75 Se-75'},
            {'abbr': 30052, 'code': 30052, 'title': 'Selenium 79 Se-79'},
            {'abbr': 30053, 'code': 30053, 'title': 'Rubidium 81 Rb-81'},
            {'abbr': 30054, 'code': 30054, 'title': 'Rubidium 83 Rb-83'},
            {'abbr': 30055, 'code': 30055, 'title': 'Rubidium 84 Rb-84'},
            {'abbr': 30056, 'code': 30056, 'title': 'Rubidium 86 Rb-86'},
            {'abbr': 30057, 'code': 30057, 'title': 'Rubidium 87 Rb-87'},
            {'abbr': 30058, 'code': 30058, 'title': 'Rubidium 88 Rb-88'},
            {'abbr': 30059, 'code': 30059, 'title': 'Krypton 85 Kr-85'},
            {'abbr': 30060, 'code': 30060, 'title': 'Krypton 85 metastable Kr-85m'},
            {'abbr': 30061, 'code': 30061, 'title': 'Krypton 87 Kr-87'},
            {'abbr': 30062, 'code': 30062, 'title': 'Krypton 88 Kr-88'},
            {'abbr': 30063, 'code': 30063, 'title': 'Krypton 89 Kr-89'},
            {'abbr': 30064, 'code': 30064, 'title': 'Strontium 85 Sr-85'},
            {'abbr': 30065, 'code': 30065, 'title': 'Strontium 89 Sr-89'},
            {'abbr': 30066, 'code': 30066, 'title': 'Strontium 89/90 Sr-8990'},
            {'abbr': 30067, 'code': 30067, 'title': 'Strontium 90 Sr-90'},
            {'abbr': 30068, 'code': 30068, 'title': 'Strontium 91 Sr-91'},
            {'abbr': 30069, 'code': 30069, 'title': 'Strontium 92 Sr-92'},
            {'abbr': 30070, 'code': 30070, 'title': 'Yttrium 87 Y-87'},
            {'abbr': 30071, 'code': 30071, 'title': 'Yttrium 88 Y-88'},
            {'abbr': 30072, 'code': 30072, 'title': 'Yttrium 90 Y-90'},
            {'abbr': 30073, 'code': 30073, 'title': 'Yttrium 91 Y-91'},
            {'abbr': 30074, 'code': 30074, 'title': 'Yttrium 91 metastable Y-91m'},
            {'abbr': 30075, 'code': 30075, 'title': 'Yttrium 92 Y-92'},
            {'abbr': 30076, 'code': 30076, 'title': 'Yttrium 93 Y-93'},
            {'abbr': 30077, 'code': 30077, 'title': 'Zirconium 89 Zr-89'},
            {'abbr': 30078, 'code': 30078, 'title': 'Zirconium 93 Zr-93'},
            {'abbr': 30079, 'code': 30079, 'title': 'Zirconium 95 Zr-95'},
            {'abbr': 30080, 'code': 30080, 'title': 'Zirconium 97 Zr-97'},
            {'abbr': 30081, 'code': 30081, 'title': 'Niobium 93 metastable Nb-93m'},
            {'abbr': 30082, 'code': 30082, 'title': 'Niobium 94 Nb-94'},
            {'abbr': 30083, 'code': 30083, 'title': 'Niobium 95 Nb-95'},
            {'abbr': 30084, 'code': 30084, 'title': 'Niobium 95 metastable Nb-95m'},
            {'abbr': 30085, 'code': 30085, 'title': 'Niobium 97 Nb-97'},
            {'abbr': 30086, 'code': 30086, 'title': 'Niobium 97 metastable Nb-97m'},
            {'abbr': 30087, 'code': 30087, 'title': 'Molybdenum 93 Mo-93'},
            {'abbr': 30088, 'code': 30088, 'title': 'Molybdenum 99 Mo-99'},
            {'abbr': 30089, 'code': 30089, 'title': 'Technetium 95 metastable Tc-95m'},
            {'abbr': 30090, 'code': 30090, 'title': 'Technetium 96 Tc-96'},
            {'abbr': 30091, 'code': 30091, 'title': 'Technetium 99 Tc-99'},
            {'abbr': 30092, 'code': 30092, 'title': 'Technetium 99 metastable Tc-99m'},
            {'abbr': 30093, 'code': 30093, 'title': 'Rhodium 99 Rh-99'},
            {'abbr': 30094, 'code': 30094, 'title': 'Rhodium 101 Rh-101'},
            {'abbr': 30095, 'code': 30095, 'title': 'Rhodium 102 metastable Rh-102m'},
            {'abbr': 30096, 'code': 30096, 'title': 'Rhodium 103 metastable Rh-103m'},
            {'abbr': 30097, 'code': 30097, 'title': 'Rhodium 105 Rh-105'},
            {'abbr': 30098, 'code': 30098, 'title': 'Rhodium 106 Rh-106'},
            {'abbr': 30099, 'code': 30099, 'title': 'Palladium 100 Pd-100'},
            {'abbr': 30100, 'code': 30100, 'title': 'Palladium 103 Pd-103'},
            {'abbr': 30101, 'code': 30101, 'title': 'Palladium 107 Pd-107'},
            {'abbr': 30102, 'code': 30102, 'title': 'Ruthenium 103 Ru-103'},
            {'abbr': 30103, 'code': 30103, 'title': 'Ruthenium 105 Ru-105'},
            {'abbr': 30104, 'code': 30104, 'title': 'Ruthenium 106 Ru-106'},
            {'abbr': 30105, 'code': 30105, 'title': 'Silver 108 metastable Ag-108m'},
            {'abbr': 30106, 'code': 30106, 'title': 'Silver 110 metastable Ag-110m'},
            {'abbr': 30107, 'code': 30107, 'title': 'Cadmium 109 Cd-109'},
            {'abbr': 30108, 'code': 30108, 'title': 'Cadmium 113 metastable Cd-113m'},
            {'abbr': 30109, 'code': 30109, 'title': 'Cadmium 115 metastable Cd-115m'},
            {'abbr': 30110, 'code': 30110, 'title': 'Indium 114 metastable In-114m'},
            {'abbr': 30111, 'code': 30111, 'title': 'Tin 113 Sn-113'},
            {'abbr': 30112, 'code': 30112, 'title': 'Tin 119 metastable Sn-119m'},
            {'abbr': 30113, 'code': 30113, 'title': 'Tin 121 metastable Sn-121m'},
            {'abbr': 30114, 'code': 30114, 'title': 'Tin 122 Sn-122'},
            {'abbr': 30115, 'code': 30115, 'title': 'Tin 123 Sn-123'},
            {'abbr': 30116, 'code': 30116, 'title': 'Tin 126 Sn-126'},
            {'abbr': 30117, 'code': 30117, 'title': 'Antimony 124 Sb-124'},
            {'abbr': 30118, 'code': 30118, 'title': 'Antimony 125 Sb-125'},
            {'abbr': 30119, 'code': 30119, 'title': 'Antimony 126 Sb-126'},
            {'abbr': 30120, 'code': 30120, 'title': 'Antimony 127 Sb-127'},
            {'abbr': 30121, 'code': 30121, 'title': 'Antimony 129 Sb-129'},
            {'abbr': 30122, 'code': 30122, 'title': 'Tellurium 123 metastable Te-123m'},
            {'abbr': 30123, 'code': 30123, 'title': 'Tellurium 125 metastable Te-125m'},
            {'abbr': 30124, 'code': 30124, 'title': 'Tellurium 127 Te-127'},
            {'abbr': 30125, 'code': 30125, 'title': 'Tellurium 127 metastable Te-127m'},
            {'abbr': 30126, 'code': 30126, 'title': 'Tellurium 129 Te-129'},
            {'abbr': 30127, 'code': 30127, 'title': 'Tellurium 129 metastable Te-129m'},
            {'abbr': 30128, 'code': 30128, 'title': 'Tellurium 131 metastable Te-131m'},
            {'abbr': 30129, 'code': 30129, 'title': 'Tellurium 132 Te-132'},
            {'abbr': 30130, 'code': 30130, 'title': 'Iodine 123 I-123'},
            {'abbr': 30131, 'code': 30131, 'title': 'Iodine 124 I-124'},
            {'abbr': 30132, 'code': 30132, 'title': 'Iodine 125 I-125'},
            {'abbr': 30133, 'code': 30133, 'title': 'Iodine 126 I-126'},
            {'abbr': 30134, 'code': 30134, 'title': 'Iodine 129 I-129'},
            {'abbr': 30135,
             'code': 30135,
             'title': 'Iodine 129 elementary gaseous I-129g'},
            {'abbr': 30136, 'code': 30136, 'title': 'Iodine 129 organic bounded I-129o'},
            {'abbr': 30137, 'code': 30137, 'title': 'Iodine 131 I-131'},
            {'abbr': 30138,
             'code': 30138,
             'title': 'Iodine 131 elementary gaseous I-131g'},
            {'abbr': 30139, 'code': 30139, 'title': 'Iodine 131 organic bounded I-131o'},
            {'abbr': 30140,
             'code': 30140,
             'title': 'Iodine 131 gaseous elementary and organic bounded I-131go'},
            {'abbr': 30141, 'code': 30141, 'title': 'Iodine 131 aerosol I-131a'},
            {'abbr': 30142, 'code': 30142, 'title': 'Iodine 132 I-132'},
            {'abbr': 30143,
             'code': 30143,
             'title': 'Iodine 132 elementary gaseous I-132g'},
            {'abbr': 30144, 'code': 30144, 'title': 'Iodine 132 organic bounded I-132o'},
            {'abbr': 30145,
             'code': 30145,
             'title': 'Iodine 132 gaseous elementary and organic bounded I-132go'},
            {'abbr': 30146, 'code': 30146, 'title': 'Iodine 132 aerosol I-132a'},
            {'abbr': 30147, 'code': 30147, 'title': 'Iodine 133 I-133'},
            {'abbr': 30148,
             'code': 30148,
             'title': 'Iodine 133 elementary gaseous I-133g'},
            {'abbr': 30149, 'code': 30149, 'title': 'Iodine 133 organic bounded I-133o'},
            {'abbr': 30150,
             'code': 30150,
             'title': 'Iodine 133 gaseous elementary and organic bounded I-133go'},
            {'abbr': 30151, 'code': 30151, 'title': 'Iodine 133 aerosol I-133a'},
            {'abbr': 30152, 'code': 30152, 'title': 'Iodine 134 I-134'},
            {'abbr': 30153,
             'code': 30153,
             'title': 'Iodine 134 elementary gaseous I-134g'},
            {'abbr': 30154, 'code': 30154, 'title': 'Iodine 134 organic bounded I-134o'},
            {'abbr': 30155, 'code': 30155, 'title': 'Iodine 135 I-135'},
            {'abbr': 30156,
             'code': 30156,
             'title': 'Iodine 135 elementary gaseous I-135g'},
            {'abbr': 30157, 'code': 30157, 'title': 'Iodine 135 organic bounded I-135o'},
            {'abbr': 30158,
             'code': 30158,
             'title': 'Iodine 135 gaseous elementary and organic bounded I-135go'},
            {'abbr': 30159, 'code': 30159, 'title': 'Iodine 135 aerosol I-135a'},
            {'abbr': 30160, 'code': 30160, 'title': 'Xenon 131 metastable Xe-131m'},
            {'abbr': 30161, 'code': 30161, 'title': 'Xenon 133 Xe-133'},
            {'abbr': 30162, 'code': 30162, 'title': 'Xenon 133 metastable Xe-133m'},
            {'abbr': 30163, 'code': 30163, 'title': 'Xenon 135 Xe-135'},
            {'abbr': 30164, 'code': 30164, 'title': 'Xenon 135 metastable Xe-135m'},
            {'abbr': 30165, 'code': 30165, 'title': 'Xenon 137 Xe-137'},
            {'abbr': 30166, 'code': 30166, 'title': 'Xenon 138 Xe-138'},
            {'abbr': 30167,
             'code': 30167,
             'title': 'Xenon sum of all Xenon isotopes Xe-sum'},
            {'abbr': 30168, 'code': 30168, 'title': 'Caesium 131 Cs-131'},
            {'abbr': 30169, 'code': 30169, 'title': 'Caesium 134 Cs-134'},
            {'abbr': 30170, 'code': 30170, 'title': 'Caesium 135 Cs-135'},
            {'abbr': 30171, 'code': 30171, 'title': 'Caesium 136 Cs-136'},
            {'abbr': 30172, 'code': 30172, 'title': 'Caesium 137 Cs-137'},
            {'abbr': 30173, 'code': 30173, 'title': 'Barium 133 Ba-133'},
            {'abbr': 30174, 'code': 30174, 'title': 'Barium 137 metastable Ba-137m'},
            {'abbr': 30175, 'code': 30175, 'title': 'Barium 140 Ba-140'},
            {'abbr': 30176, 'code': 30176, 'title': 'Cerium 139 Ce-139'},
            {'abbr': 30177, 'code': 30177, 'title': 'Cerium 141 Ce-141'},
            {'abbr': 30178, 'code': 30178, 'title': 'Cerium 143 Ce-143'},
            {'abbr': 30179, 'code': 30179, 'title': 'Cerium 144 Ce-144'},
            {'abbr': 30180, 'code': 30180, 'title': 'Lanthanum 140 La-140'},
            {'abbr': 30181, 'code': 30181, 'title': 'Lanthanum 141 La-141'},
            {'abbr': 30182, 'code': 30182, 'title': 'Praseodymium 143 Pr-143'},
            {'abbr': 30183, 'code': 30183, 'title': 'Praseodymium 144 Pr-144'},
            {'abbr': 30184, 'code': 30184, 'title': 'Praseodymium 144 metastable Pr-144m'},
            {'abbr': 30185, 'code': 30185, 'title': 'Samarium 145 Sm-145'},
            {'abbr': 30186, 'code': 30186, 'title': 'Samarium 147 Sm-147'},
            {'abbr': 30187, 'code': 30187, 'title': 'Samarium 151 Sm-151'},
            {'abbr': 30188, 'code': 30188, 'title': 'Neodymium 147 Nd-147'},
            {'abbr': 30189, 'code': 30189, 'title': 'Promethium 146 Pm-146'},
            {'abbr': 30190, 'code': 30190, 'title': 'Promethium 147 Pm-147'},
            {'abbr': 30191, 'code': 30191, 'title': 'Promethium 151 Pm-151'},
            {'abbr': 30192, 'code': 30192, 'title': 'Europium 152 Eu-152'},
            {'abbr': 30193, 'code': 30193, 'title': 'Europium 154 Eu-154'},
            {'abbr': 30194, 'code': 30194, 'title': 'Europium 155 Eu-155'},
            {'abbr': 30195, 'code': 30195, 'title': 'Gadolinium 153 Gd-153'},
            {'abbr': 30196, 'code': 30196, 'title': 'Terbium 160 Tb-160'},
            {'abbr': 30197, 'code': 30197, 'title': 'Holmium 166 metastable Ho-166m'},
            {'abbr': 30198, 'code': 30198, 'title': 'Thulium 170 Tm-170'},
            {'abbr': 30199, 'code': 30199, 'title': 'Ytterbium 169 Yb-169'},
            {'abbr': 30200, 'code': 30200, 'title': 'Hafnium 175 Hf-175'},
            {'abbr': 30201, 'code': 30201, 'title': 'Hafnium 181 Hf-181'},
            {'abbr': 30202, 'code': 30202, 'title': 'Tantalum 179 Ta-179'},
            {'abbr': 30203, 'code': 30203, 'title': 'Tantalum 182 Ta-182'},
            {'abbr': 30204, 'code': 30204, 'title': 'Rhenium 184 Re-184'},
            {'abbr': 30205, 'code': 30205, 'title': 'Iridium 192 Ir-192'},
            {'abbr': 30206, 'code': 30206, 'title': 'Mercury 203 Hg-203'},
            {'abbr': 30207, 'code': 30207, 'title': 'Thallium 204 Tl-204'},
            {'abbr': 30208, 'code': 30208, 'title': 'Thallium 207 Tl-207'},
            {'abbr': 30209, 'code': 30209, 'title': 'Thallium 208 Tl-208'},
            {'abbr': 30210, 'code': 30210, 'title': 'Thallium 209 Tl-209'},
            {'abbr': 30211, 'code': 30211, 'title': 'Bismuth 205 Bi-205'},
            {'abbr': 30212, 'code': 30212, 'title': 'Bismuth 207 Bi-207'},
            {'abbr': 30213, 'code': 30213, 'title': 'Bismuth 210 Bi-210'},
            {'abbr': 30214, 'code': 30214, 'title': 'Bismuth 211 Bi-211'},
            {'abbr': 30215, 'code': 30215, 'title': 'Bismuth 212 Bi-212'},
            {'abbr': 30216, 'code': 30216, 'title': 'Bismuth 213 Bi-213'},
            {'abbr': 30217, 'code': 30217, 'title': 'Bismuth 214 Bi-214'},
            {'abbr': 30218, 'code': 30218, 'title': 'Polonium 208 Po-208'},
            {'abbr': 30219, 'code': 30219, 'title': 'Polonium 210 Po-210'},
            {'abbr': 30220, 'code': 30220, 'title': 'Polonium 212 Po-212'},
            {'abbr': 30221, 'code': 30221, 'title': 'Polonium 213 Po-213'},
            {'abbr': 30222, 'code': 30222, 'title': 'Polonium 214 Po-214'},
            {'abbr': 30223, 'code': 30223, 'title': 'Polonium 215 Po-215'},
            {'abbr': 30224, 'code': 30224, 'title': 'Polonium 216 Po-216'},
            {'abbr': 30225, 'code': 30225, 'title': 'Polonium 218 Po-218'},
            {'abbr': 30226, 'code': 30226, 'title': 'Lead 209 Pb-209'},
            {'abbr': 30227, 'code': 30227, 'title': 'Lead 210 Pb-210'},
            {'abbr': 30228, 'code': 30228, 'title': 'Lead 211 Pb-211'},
            {'abbr': 30229, 'code': 30229, 'title': 'Lead 212 Pb-212'},
            {'abbr': 30230, 'code': 30230, 'title': 'Lead 214 Pb-214'},
            {'abbr': 30231, 'code': 30231, 'title': 'Astatine 217 At-217'},
            {'abbr': 30232, 'code': 30232, 'title': 'Radon 219 Rn-219'},
            {'abbr': 30233, 'code': 30233, 'title': 'Radon 220 Rn-220'},
            {'abbr': 30234, 'code': 30234, 'title': 'Radon 222 Rn-222'},
            {'abbr': 30235, 'code': 30235, 'title': 'Francium 221 Fr-221'},
            {'abbr': 30236, 'code': 30236, 'title': 'Francium 223 Fr-223'},
            {'abbr': 30237, 'code': 30237, 'title': 'Radium 223 Ra-223'},
            {'abbr': 30238, 'code': 30238, 'title': 'Radium 224 Ra-224'},
            {'abbr': 30239, 'code': 30239, 'title': 'Radium 225 Ra-225'},
            {'abbr': 30240, 'code': 30240, 'title': 'Radium 226 Ra-226'},
            {'abbr': 30241, 'code': 30241, 'title': 'Radium 228 Ra-228'},
            {'abbr': 30242, 'code': 30242, 'title': 'Actinium 225 Ac-225'},
            {'abbr': 30243, 'code': 30243, 'title': 'Actinium 227 Ac-227'},
            {'abbr': 30244, 'code': 30244, 'title': 'Actinium 228 Ac-228'},
            {'abbr': 30245, 'code': 30245, 'title': 'Thorium 227 Th-227'},
            {'abbr': 30246, 'code': 30246, 'title': 'Thorium 228 Th-228'},
            {'abbr': 30247, 'code': 30247, 'title': 'Thorium 229 Th-229'},
            {'abbr': 30248, 'code': 30248, 'title': 'Thorium 230 Th-230'},
            {'abbr': 30249, 'code': 30249, 'title': 'Thorium 231 Th-231'},
            {'abbr': 30250, 'code': 30250, 'title': 'Thorium 232 Th-232'},
            {'abbr': 30251, 'code': 30251, 'title': 'Thorium 234 Th-234'},
            {'abbr': 30252, 'code': 30252, 'title': 'Protactinium 231 Pa-231'},
            {'abbr': 30253, 'code': 30253, 'title': 'Protactinium 233 Pa-233'},
            {'abbr': 30254, 'code': 30254, 'title': 'Protactinium 234 metastable Pa-234m'},
            {'abbr': 30255, 'code': 30255, 'title': 'Uranium 232 U-232'},
            {'abbr': 30256, 'code': 30256, 'title': 'Uranium 233 U-233'},
            {'abbr': 30257, 'code': 30257, 'title': 'Uranium 234 U-234'},
            {'abbr': 30258, 'code': 30258, 'title': 'Uranium 235 U-235'},
            {'abbr': 30259, 'code': 30259, 'title': 'Uranium 236 U-236'},
            {'abbr': 30260, 'code': 30260, 'title': 'Uranium 237 U-237'},
            {'abbr': 30261, 'code': 30261, 'title': 'Uranium 238 U-238'},
            {'abbr': 30262, 'code': 30262, 'title': 'Plutonium 236 Pu-236'},
            {'abbr': 30263, 'code': 30263, 'title': 'Plutonium 238 Pu-238'},
            {'abbr': 30264, 'code': 30264, 'title': 'Plutonium 239 Pu-239'},
            {'abbr': 30265, 'code': 30265, 'title': 'Plutonium 240 Pu-240'},
            {'abbr': 30266, 'code': 30266, 'title': 'Plutonium 241 Pu-241'},
            {'abbr': 30267, 'code': 30267, 'title': 'Plutonium 242 Pu-242'},
            {'abbr': 30268, 'code': 30268, 'title': 'Plutonium 244 Pu-244'},
            {'abbr': 30269, 'code': 30269, 'title': 'Neptunium 237 Np-237'},
            {'abbr': 30270, 'code': 30270, 'title': 'Neptunium 238 Np-238'},
            {'abbr': 30271, 'code': 30271, 'title': 'Neptunium 239 Np-239'},
            {'abbr': 30272, 'code': 30272, 'title': 'Americium 241 Am-241'},
            {'abbr': 30273, 'code': 30273, 'title': 'Americium 242 Am-242'},
            {'abbr': 30274, 'code': 30274, 'title': 'Americium 242 metastable Am-242m'},
            {'abbr': 30275, 'code': 30275, 'title': 'Americium 243 Am-243'},
            {'abbr': 30276, 'code': 30276, 'title': 'Curium 242 Cm-242'},
            {'abbr': 30277, 'code': 30277, 'title': 'Curium 243 Cm-243'},
            {'abbr': 30278, 'code': 30278, 'title': 'Curium 244 Cm-244'},
            {'abbr': 30279, 'code': 30279, 'title': 'Curium 245 Cm-245'},
            {'abbr': 30280, 'code': 30280, 'title': 'Curium 246 Cm-246'},
            {'abbr': 30281, 'code': 30281, 'title': 'Curium 247 Cm-247'},
            {'abbr': 30282, 'code': 30282, 'title': 'Curium 248 Cm-248'},
            {'abbr': 30283, 'code': 30283, 'title': 'Curium 243/244 Cm-243244'},
            {'abbr': 30284,
             'code': 30284,
             'title': 'Plutonium 238/Americium 241 Pu-238Am-241'},
            {'abbr': 30285, 'code': 30285, 'title': 'Plutonium 239/240 Pu-239240'},
            {'abbr': 30286, 'code': 30286, 'title': 'Berkelium 249 Bk-249'},
            {'abbr': 30287, 'code': 30287, 'title': 'Californium 249 Cf-249'},
            {'abbr': 30288, 'code': 30288, 'title': 'Californium 250 Cf-250'},
            {'abbr': 30289, 'code': 30289, 'title': 'Californium 252 Cf-252'},
            {'abbr': 30290, 'code': 30290, 'title': 'Sum aerosol particulates SumAer'},
            {'abbr': 30291, 'code': 30291, 'title': 'Sum Iodine SumIod'},
            {'abbr': 30292, 'code': 30292, 'title': 'Sum noble gas SumNG'},
            {'abbr': 30293, 'code': 30293, 'title': 'Activation gas ActGas'},
            {'abbr': 30294, 'code': 30294, 'title': 'Cs-137 Equivalent EquCs137'},
            {'abbr': 60000, 'code': 60000, 'title': 'HOx radical', 'units': 'OH+HO2'},
            {'abbr': 60001,
             'code': 60001,
             'title': 'Total inorganic and organic peroxy radicals',
             'units': 'HO2 + RO2'},
            {'abbr': 60002, 'code': 60002, 'title': 'Passive Ozone'},
            {'abbr': 60003, 'code': 60003, 'title': 'NOx expressed as nitrogen NOx'},
            {'abbr': 60004,
             'code': 60004,
             'title': 'All nitrogen oxides (NOy) expressed as nitrogen NOy'},
            {'abbr': 60005, 'code': 60005, 'title': 'Total inorganic chlorine Clx'},
            {'abbr': 60006, 'code': 60006, 'title': 'Total inorganic bromine Brx'},
            {'abbr': 60007,
             'code': 60007,
             'title': 'Total inorganic chlorine except HCl, ClONO2: ClOx'},
            {'abbr': 60008,
             'code': 60008,
             'title': 'Total inorganic bromine except HBr, BrONO2: BrOx'},
            {'abbr': 60009, 'code': 60009, 'title': 'Lumped alkanes'},
            {'abbr': 60010, 'code': 60010, 'title': 'Lumped alkenes'},
            {'abbr': 60011, 'code': 60011, 'title': 'Lumped aromatic compounds'},
            {'abbr': 60012, 'code': 60012, 'title': 'Lumped terpenes'},
            {'abbr': 60013,
             'code': 60013,
             'title': 'Non-methane volatile organic compounds expressed as carbon'},
            {'abbr': 60014,
             'code': 60014,
             'title': 'Anthropogenic non-methane volatile organic compounds expressed as '
                      'carbon'},
            {'abbr': 60015,
             'code': 60015,
             'title': 'Biogenic non-methane volatile organic compounds expressed as '
                      'carbon'},
            {'abbr': 60016, 'code': 60016, 'title': 'Lumped oxygenated hydrocarbons'},
            {'abbr': 60017,
             'code': 60017,
             'title': 'NOx expressed as nitrogen dioxide',
             'units': 'NO2'},
            {'abbr': 62000, 'code': 62000, 'title': 'Total aerosol'},
            {'abbr': 62001, 'code': 62001, 'title': 'Dust dry'},
            {'abbr': 62002, 'code': 62002, 'title': 'Water in ambient'},
            {'abbr': 62003, 'code': 62003, 'title': 'Ammonium dry'},
            {'abbr': 62004, 'code': 62004, 'title': 'Nitrate dry'},
            {'abbr': 62005, 'code': 62005, 'title': 'Nitric acid trihydrate'},
            {'abbr': 62006, 'code': 62006, 'title': 'Sulphate dry'},
            {'abbr': 62007, 'code': 62007, 'title': 'Mercury dry'},
            {'abbr': 62008, 'code': 62008, 'title': 'Sea salt dry'},
            {'abbr': 62009, 'code': 62009, 'title': 'Black carbon dry'},
            {'abbr': 62010, 'code': 62010, 'title': 'Particulate organic matter dry'},
            {'abbr': 62011,
             'code': 62011,
             'title': 'Primary particulate organic matter dry'},
            {'abbr': 62012,
             'code': 62012,
             'title': 'Secondary particulate organic matter dry'},
            {'abbr': 62013, 'code': 62013, 'title': 'Black carbon hydrophilic dry'},
            {'abbr': 62014, 'code': 62014, 'title': 'Black carbon hydrophobic dry'},
            {'abbr': 62015,
             'code': 62015,
             'title': 'Particulate organic matter hydrophilic dry'},
            {'abbr': 62016,
             'code': 62016,
             'title': 'Particulate organic matter hydrophobic dry'},
            {'abbr': 62017, 'code': 62017, 'title': 'Nitrate hydrophilic dry'},
            {'abbr': 62018, 'code': 62018, 'title': 'Nitrate hydrophobic dry'},
            {'abbr': 62020, 'code': 62020, 'title': 'Smoke - high absorption'},
            {'abbr': 62021, 'code': 62021, 'title': 'Smoke - low absorption'},
            {'abbr': 62022, 'code': 62022, 'title': 'Aerosol - high absorption'},
            {'abbr': 62023, 'code': 62023, 'title': 'Aerosol - low absorption'},
            {'abbr': 62025, 'code': 62025, 'title': 'Volcanic ash'},
            {'abbr': 62026, 'code': 62026, 'title': 'Particulate matter', 'units': 'PM'},
            {'abbr': 62100, 'code': 62100, 'title': 'Alnus (Alder) pollen'},
            {'abbr': 62101, 'code': 62101, 'title': 'Betula (Birch) pollen'},
            {'abbr': 62102, 'code': 62102, 'title': 'Castanea (Chestnut) pollen'},
            {'abbr': 62103, 'code': 62103, 'title': 'Carpinus (Hornbeam) pollen'},
            {'abbr': 62104, 'code': 62104, 'title': 'Corylus (Hazel) pollen'},
            {'abbr': 62105, 'code': 62105, 'title': 'Fagus (Beech) pollen'},
            {'abbr': 62106, 'code': 62106, 'title': 'Fraxinus (Ash) pollen'},
            {'abbr': 62107, 'code': 62107, 'title': 'Pinus (Pine) pollen'},
            {'abbr': 62108, 'code': 62108, 'title': 'Platanus (Plane) pollen'},
            {'abbr': 62109, 'code': 62109, 'title': 'Populus (Cottonwood, Poplar) pollen'},
            {'abbr': 62110, 'code': 62110, 'title': 'Quercus (Oak) pollen'},
            {'abbr': 62111, 'code': 62111, 'title': 'Salix (Willow) pollen'},
            {'abbr': 62112, 'code': 62112, 'title': 'Taxus (Yew) pollen'},
            {'abbr': 62113, 'code': 62113, 'title': 'Tilia (Lime, Linden) pollen'},
            {'abbr': 62114, 'code': 62114, 'title': 'Ulmus (Elm) pollen'},
            {'abbr': 62200,
             'code': 62200,
             'title': 'Ambrosia (Ragweed, Burr-ragweed ) pollen'},
            {'abbr': 62201,
             'code': 62201,
             'title': 'Artemisia (Sagebrush, Wormwood, Mugwort) pollen'},
            {'abbr': 62202,
             'code': 62202,
             'title': 'Brassica (Rape, Broccoli, Brussels Sprouts, Cabbage, Cauliflower, '
                      'Collards, Kale, Kohlrabi, Mustard, Rutabaga) pollen'},
            {'abbr': 62203, 'code': 62203, 'title': 'Plantago (Plantain) pollen'},
            {'abbr': 62204, 'code': 62204, 'title': 'Rumex (Dock, Sorrel) pollen'},
            {'abbr': 62205, 'code': 62205, 'title': 'Urtica (Nettle) pollen'},
            {'abbr': 62300, 'code': 62300, 'title': 'Poaceae (Grass family) pollen'},
            {'abbr': 65535, 'code': 65535, 'title': 'Missing'})
