import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 228228

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2:
            return 228171

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == 1 and scaleFactorOfFirstFixedSurface == 0:
            return 228170

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228164

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 228144

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 228141

        is_tigge = h.get_l('is_tigge')

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and scaleFactorOfFirstFixedSurface == 0 and is_tigge == 1:
            return 228139

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 228139

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1 and is_tigge == 1:
            return 228039

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 228039

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 228002

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 228001

        productDefinitionTemplateNumber = h.get_l('productDefinitionTemplateNumber')
        probabilityType = h.get_l('probabilityType')
        scaleFactorOfLowerLimit = h.get_l('scaleFactorOfLowerLimit')
        scaledValueOfLowerLimit = h.get_l('scaledValueOfLowerLimit')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and productDefinitionTemplateNumber == 9 and scaledValueOfFirstFixedSurface == 10 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfLowerLimit == 20 and typeOfFirstFixedSurface == 103:
            return 131071

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and productDefinitionTemplateNumber == 9 and scaledValueOfFirstFixedSurface == 10 and probabilityType == 3 and scaleFactorOfFirstFixedSurface == 0 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 15 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 131070

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 3126

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 3120

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 3119

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 3117

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 3111

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 3109

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 3106

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 3105

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 3104

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 3103

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 3102

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16:
            return 3099

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 3098

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 3097

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 3096

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 3095

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 3094

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 3093

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 3092

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 3089

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 3088

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 3086

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 3077

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 3070

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 3069

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 3068

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 3067

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 3063

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 3060

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 3059

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 3056

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 3054

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 3050

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 3049

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 3046

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 3045

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 3042

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 3041

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 3038

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 3037

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 3030

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 3029

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 3028

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 3027

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 3026

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 3025

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 3024

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 3023

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 3022

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6:
            return 3021

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 3020

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 3019

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 3017

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 3016

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 3015

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 3009

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 3008

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 3005

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2:
            return 3003

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 260509

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 260241

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 260240

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 260239

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 260238

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 260237

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 260236

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 260235

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 260234

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 260233

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 260232

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 260231

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return 260230

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return 260229

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return 260228

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return 260227

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 8:
            return 260226

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 260225

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 260224

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 260223

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 260222

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 260221

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 260220

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 260219

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 260218

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 260217

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 260216

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 260215

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 260214

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 260213

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 260212

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 260211

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 260210

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 260209

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 260208

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 260207

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 260206

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 260205

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 260204

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 260203

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 260202

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 260201

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 260200

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 260199

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 260198

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 260197

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 260196

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 260195

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 19:
            return 260194

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 260193

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 260192

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 260191

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 260190

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 260189

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 260188

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return 260187

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 260186

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 260185

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 260184

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 260183

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 260182

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5:
            return 260181

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 260180

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 260179

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return 260178

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return 260177

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 260176

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 260175

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 260174

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return 260173

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 260172

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 260171

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 260170

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 260169

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 260168

        if discipline == 0 and parameterCategory == 190 and parameterNumber == 0:
            return 260167

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 260166

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 260165

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 260164

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 260163

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 260162

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return 260161

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 260160

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 260159

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 260158

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 260157

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 260156

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 260155

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 260154

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 260153

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 260152

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 260151

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 260150

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 260149

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 260148

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 260147

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 260146

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 260145

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 260144

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 260143

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 260142

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 260141

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 260140

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 260139

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5:
            return 260138

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 260137

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 260136

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 260135

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 260134

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 260133

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 260132

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0:
            return 260130

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 260129

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 260128

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 260127

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 260126

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 260125

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 260124

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 260123

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 260122

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 260121

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 260120

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24:
            return 260119

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 260118

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 260117

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 260116

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 260115

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 260114

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 260113

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 260112

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 260111

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return 260110

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 260109

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 260108

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 260107

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 260106

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 260105

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 260104

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 260103

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 260102

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 260101

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 260100

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5:
            return 260099

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 260098

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 260097

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 260096

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 260095

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 260094

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50:
            return 260093

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 260092

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 260091

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10:
            return 260090

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9:
            return 260089

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8:
            return 260088

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 260087

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 260086

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 260085

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return 260084

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 260083

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 260082

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 260081

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return 260080

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 260079

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 260078

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 260077

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 260076

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6:
            return 260075

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 260074

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 260073

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 260072

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 260071

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 260070

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 260069

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 260068

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 260067

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 260066

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22:
            return 260065

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 260064

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18:
            return 260063

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17:
            return 260062

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 260061

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 260060

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66:
            return 260059

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65:
            return 260058

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 260057

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 260056

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 260055

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 260054

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 57:
            return 260053

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 260052

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 260051

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54:
            return 260050

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 260049

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 260048

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 260047

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 260046

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 260045

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 260044

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 260043

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 260042

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 260041

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 260040

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 260039

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 260038

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 260037

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 260036

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 260035

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 38:
            return 260034

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37:
            return 260033

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 260032

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 260031

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 260030

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 260029

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 260028

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 260027

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 260026

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 260025

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 260024

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return 260023

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 260022

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 260021

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 260020

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 260019

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 260018

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 260017

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 260016

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 260015

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 260014

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 260013

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 260012

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 260011

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 260010

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 260009

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 260008

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 260007

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 260006

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 260005

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 260004

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11:
            return 260003

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10:
            return 260002

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 235

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 207

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 194

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 189

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 179

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 177

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 176

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 173

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 172

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 168

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 167

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 166

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 165

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 157

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 156

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 155

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 101:
            return 151

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 147

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 146

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 145

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 138

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 136

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 135

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 134

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 133

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 132

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 131

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 130

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 129

        is_uerra = h.get_l('is_uerra')
        indicatorOfUnitForTimeRange = h.get_l('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get_l('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 122

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 121

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 60

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 59

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 54

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 3

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 2

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 1

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and scaleFactorOfLowerLimit == 0 and scaledValueOfLowerLimit == 20 and typeOfStatisticalProcessing == 1 and probabilityType == 3:
            return 131063

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and probabilityType == 3 and scaledValueOfLowerLimit == 10 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and productDefinitionTemplateNumber == 9:
            return 131062

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 228247

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103:
            return 228246

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 174098

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 34:
            return 174008

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 21 and typeOfSecondFixedSurface == 160 and typeOfFirstFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 151175

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfFirstFixedSurface == 20 and typeOfSecondFixedSurface == 255 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 29315:
            return 151163

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 151145

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3 and typeOfFirstFixedSurface == 160:
            return 151132

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 160:
            return 151131

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 140232

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 140231

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 140230

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 140229

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 140221

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 3031

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 3014

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 3012

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 300012

        if discipline == 20 and parameterCategory == 2 and parameterNumber == 0:
            return 261013

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 9:
            return 261012

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 8:
            return 261011

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 7:
            return 261010

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 6:
            return 261009

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 5:
            return 261008

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 4:
            return 261007

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 3:
            return 261006

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 2:
            return 261005

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 1:
            return 261004

        if discipline == 20 and parameterCategory == 1 and parameterNumber == 0:
            return 261003

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 1:
            return 261002

        if discipline == 20 and parameterCategory == 0 and parameterNumber == 0:
            return 261001

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 23:
            return 260556

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 22:
            return 260555

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 21:
            return 260554

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 20:
            return 260553

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 19:
            return 260552

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17:
            return 260551

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16:
            return 260550

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 11:
            return 260546

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 10:
            return 260545

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 9:
            return 260544

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 8:
            return 260543

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 7:
            return 260542

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 6:
            return 260541

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 5:
            return 260540

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 9:
            return 260539

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 8:
            return 260538

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 7:
            return 260537

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 6:
            return 260536

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 5:
            return 260535

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 4:
            return 260534

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 3:
            return 260533

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2:
            return 260532

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1:
            return 260531

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 0:
            return 260530

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15:
            return 260511

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14:
            return 260510

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16 and typeOfFirstFixedSurface == 177 and typeOfStatisticalProcessing == 1:
            return 260430

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 260428

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 260427

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 260423

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 27:
            return 260367

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 16:
            return 260365

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 26:
            return 260364

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 8:
            return 260363

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 53:
            return 260362

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 52:
            return 260361

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18:
            return 260360

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 28:
            return 260291

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 29:
            return 260290

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 121:
            return 260289

        is_efas = h.get_l('is_efas')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1 and is_efas == 1:
            return 260268

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and is_efas == 1:
            return 260267

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and is_uerra == 0:
            return 260266

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and is_uerra == 0 and typeOfStatisticalProcessing == 1 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 260265

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 260264

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 14:
            return 260263

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 13:
            return 260262

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 260260

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 260259

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79:
            return 260258

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 260257

        if discipline == 2 and parameterCategory == 4 and parameterNumber == 2:
            return 260256

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 260255

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0:
            return 260242

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 9:
            return 240029

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 8:
            return 240028

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 25:
            return 240026

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 24 and indicatorOfUnitForTimeRange == 1:
            return 240024

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 240023

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 15:
            return 240022

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 14:
            return 240021

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 13:
            return 240020

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 24:
            return 240018

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 3:
            return 240017

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 240016

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 12:
            return 240015

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 11:
            return 240014

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 7:
            return 240013

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 10:
            return 240012

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 13:
            return 240011

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and typeOfStatisticalProcessing == 0:
            return 235014

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 0:
            return 235013

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 30 and typeOfStatisticalProcessing == 0:
            return 235012

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 29 and typeOfStatisticalProcessing == 0:
            return 235011

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 28 and typeOfStatisticalProcessing == 0:
            return 235010

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 27 and typeOfStatisticalProcessing == 0:
            return 235009

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 40 and typeOfStatisticalProcessing == 0:
            return 235008

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 39 and typeOfStatisticalProcessing == 0:
            return 235007

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 108 and typeOfStatisticalProcessing == 0:
            return 235006

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 26 and typeOfStatisticalProcessing == 0:
            return 235005

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 25 and typeOfStatisticalProcessing == 0:
            return 235004

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 24 and typeOfStatisticalProcessing == 0:
            return 235003

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 235002

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 22 and typeOfStatisticalProcessing == 0:
            return 235001

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 100 and typeOfFirstFixedSurface == 103:
            return 228249

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200:
            return 228241

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200:
            return 228240

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200:
            return 228239

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 33:
            return 228205

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 228143

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == 1:
            return 228096

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1:
            return 228095

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == 1:
            return 228087

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and scaleFactorOfSecondFixedSurface == 1:
            return 228086

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 228060

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 3 and indicatorOfUnitForTimeRange == 1:
            return 228059

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfSecondFixedSurface == 8 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1:
            return 228058

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 3 and typeOfFirstFixedSurface == 1 and indicatorOfUnitForTimeRange == 1 and typeOfSecondFixedSurface == 8:
            return 228057

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 120:
            return 228056

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 119:
            return 228055

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 118:
            return 228054

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 1 and indicatorOfUnitForTimeRange == 1:
            return 228053

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 2 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228052

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and lengthOfTimeRange == 1 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228051

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfSecondFixedSurface == 8:
            return 228050

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27:
            return 228046

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 228037

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 19 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1:
            return 228036

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and lengthOfTimeRange == 6 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8:
            return 228035

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 37:
            return 228034

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 36:
            return 228033

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 19:
            return 228032

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return 228031

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 93:
            return 228030

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and is_uerra == 0 and typeOfStatisticalProcessing == 2 and lengthOfTimeRange == 3 and indicatorOfUnitForTimeRange == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 228028

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 27315 and scaleFactorOfFirstFixedSurface == 2:
            return 228024

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 20 and scaledValueOfFirstFixedSurface == 26315 and scaleFactorOfFirstFixedSurface == 2:
            return 228020

        aerosolType = h.get_l('aerosolType')
        is_aerosol = h.get_l('is_aerosol')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1 and aerosolType == 62003 and is_aerosol == 1:
            return 215211

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 10 and aerosolType == 62003 and is_aerosol == 1:
            return 215209

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 9 and aerosolType == 62003 and is_aerosol == 1:
            return 215208

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 11 and aerosolType == 62003 and is_aerosol == 1:
            return 215207

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 6 and aerosolType == 62003 and is_aerosol == 1:
            return 215206

        typeOfWavelengthInterval = h.get_l('typeOfWavelengthInterval')
        scaleFactorOfFirstWavelength = h.get_l('scaleFactorOfFirstWavelength')
        scaledValueOfFirstWavelength = h.get_l('scaledValueOfFirstWavelength')
        typeOfSizeInterval = h.get_l('typeOfSizeInterval')
        is_aerosol_optical = h.get_l('is_aerosol_optical')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55 and typeOfSizeInterval == 255 and aerosolType == 62003 and is_aerosol_optical == 1:
            return 210251

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfSizeInterval == 255 and aerosolType == 62004 and is_aerosol_optical == 1 and typeOfWavelengthInterval == 11 and scaleFactorOfFirstWavelength == 8 and scaledValueOfFirstWavelength == 55:
            return 210250

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and aerosolType == 62003 and is_aerosol == 1:
            return 210249

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14 and typeOfSecondFixedSurface == 255 and scaleFactorOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 169 and scaledValueOfFirstFixedSurface == 1:
            return 151225

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 3 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 255 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 151219

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 15 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 151127

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 18 and typeOfFirstFixedSurface == 160 and typeOfSecondFixedSurface == 160 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfSecondFixedSurface == 300 and scaleFactorOfSecondFixedSurface == 0:
            return 151126

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == -2 and probabilityType == 0 and scaleFactorOfLowerLimit == 0:
            return 133098

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == -15 and probabilityType == 0 and scaleFactorOfLowerLimit == 1:
            return 133097

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and probabilityType == 0 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == -1:
            return 133096

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == 2 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9:
            return 133095

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == 15 and probabilityType == 3 and scaleFactorOfLowerLimit == 1:
            return 133094

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 10 and scaledValueOfLowerLimit == 1 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9:
            return 133093

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 2 and scaledValueOfLowerLimit == 10:
            return 131100

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 50 and probabilityType == 3:
            return 131099

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 25 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1:
            return 131098

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 5:
            return 3075

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 4:
            return 3074

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 3:
            return 3073

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 3066

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 3062

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 32:
            return 248

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 84:
            return 247

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 83:
            return 246

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 211

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 210

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 203

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 3:
            return 202

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfStatisticalProcessing == 2 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 201

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 37:
            return 181

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 38:
            return 180

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 175

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 169

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 32:
            return 77

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 86:
            return 76

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 85:
            return 75

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfStatisticalProcessing == 2 and is_uerra == 1:
            return 49

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0:
            return 43

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 34

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 33

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 31

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 45:
            return 23

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 31:
            return 22

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 28:
            return 21

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and is_uerra == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 200:
            return 10

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 100:
            return 10

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 10

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 3 and scaleFactorOfLowerLimit == -2 and probabilityType == 3 and typeOfStatisticalProcessing == 1 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1:
            return 131088

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 200 and probabilityType == 3 and scaleFactorOfLowerLimit == 0:
            return 131087

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 150 and probabilityType == 3:
            return 131086

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 100 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1:
            return 131085

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 80 and probabilityType == 3 and scaleFactorOfLowerLimit == 0:
            return 131084

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 60 and probabilityType == 3 and typeOfFirstFixedSurface == 1 and scaleFactorOfLowerLimit == 0:
            return 131083

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 40 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9:
            return 131082

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and productDefinitionTemplateNumber == 9 and typeOfStatisticalProcessing == 1 and scaledValueOfLowerLimit == 5 and probabilityType == 3 and scaleFactorOfLowerLimit == 0:
            return 131061

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and scaledValueOfLowerLimit == 1 and probabilityType == 3 and scaleFactorOfLowerLimit == 0 and productDefinitionTemplateNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 131060

    return wrapped
