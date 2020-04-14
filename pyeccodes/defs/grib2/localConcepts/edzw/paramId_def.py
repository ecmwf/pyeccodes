import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 235:
            return 503426

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 199:
            return 503425

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 235:
            return 503424

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26 and typeOfStatisticalProcessing == 2:
            return 503423

        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 25:
            return 503422

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 25:
            return 503421

        constituentType = h.get_l('constituentType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62101:
            return 503420

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62200:
            return 503419

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62200:
            return 503418

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62200:
            return 503417

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62200:
            return 503416

        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 503415

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 503414

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62200:
            return 503413

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62200:
            return 503412

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 503411

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62200:
            return 503410

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62200:
            return 503409

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62200:
            return 503408

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62200:
            return 503407

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62200:
            return 503406

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62200:
            return 503405

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62300:
            return 503404

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62300:
            return 503403

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62300:
            return 503402

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62300:
            return 503401

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 503400

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 503399

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62300:
            return 503398

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62300:
            return 503397

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 503396

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62300:
            return 503395

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62300:
            return 503394

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62300:
            return 503393

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62300:
            return 503392

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62300:
            return 503391

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62300:
            return 503390

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62100:
            return 503389

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62100:
            return 503388

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62100:
            return 503387

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 199 and constituentType == 62100:
            return 503386

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 503385

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 503384

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62100:
            return 503383

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62100:
            return 503382

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 503381

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62100:
            return 503380

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62100:
            return 503379

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62100:
            return 503378

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62100:
            return 503377

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62100:
            return 503376

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62100:
            return 503375

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 202 and constituentType == 62101:
            return 503374

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 201 and constituentType == 62101:
            return 503373

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 200 and constituentType == 62101:
            return 503372

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 198 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 503371

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 197 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 503370

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 196 and constituentType == 62101:
            return 503369

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and constituentType == 62101:
            return 503368

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 195 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 503367

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 194 and constituentType == 62101:
            return 503366

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and typeOfStatisticalProcessing == 11 and constituentType == 62101:
            return 503365

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 193 and constituentType == 62101:
            return 503364

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 192 and constituentType == 62101:
            return 503363

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfGeneratingProcess == 9 and constituentType == 62101:
            return 503362

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 59 and constituentType == 62101:
            return 503360

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 198:
            return 503359

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 234:
            return 503358

        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 503357

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 205 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 503356

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 503355

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503354

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503353

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfSecondFixedSurface == 181 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503352

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 4:
            return 503351

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 503350

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 503349

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192 and typeOfStatisticalProcessing == 2:
            return 503348

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5:
            return 503347

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 5 and typeOfGeneratingProcess == 8:
            return 503346

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 503345

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 81 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 20 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 26315:
            return 503344

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 207 and typeOfStatisticalProcessing == 2:
            return 503343

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 206 and typeOfStatisticalProcessing == 2:
            return 503342

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 15 and typeOfStatisticalProcessing == 2:
            return 503341

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 23:
            return 503340

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 203:
            return 503339

        modeNumber = h.get_l('modeNumber')
        typeOfDistributionFunction = h.get_l('typeOfDistributionFunction')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 503338

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 503337

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 503336

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 8:
            return 503335

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 8:
            return 503334

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 3 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 8:
            return 503333

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 24:
            return 503332

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62001:
            return 503331

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 22 and constituentType == 62025:
            return 503330

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62001:
            return 503328

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 21 and constituentType == 62025:
            return 503327

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 17 and typeOfFirstFixedSurface == 10:
            return 503326

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 1:
            return 503325

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 99:
            return 503324

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 39:
            return 503323

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 38:
            return 503322

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 98:
            return 503321

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 97:
            return 503320

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 96:
            return 503319

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 107:
            return 503318

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 106:
            return 503317

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 105:
            return 503316

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 103:
            return 503315

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 102:
            return 503314

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 101:
            return 503313

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 104:
            return 503312

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 100:
            return 503311

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 116:
            return 503310

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 113:
            return 503309

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 110:
            return 503308

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 503307

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 503306

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfFirstFixedSurface == 8:
            return 503305

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 26:
            return 503304

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52:
            return 503303

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 2:
            return 503302

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 3:
            return 503301

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 1:
            return 503300

        if discipline == 0 and parameterCategory == 199 and parameterNumber == 0:
            return 503299

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 4:
            return 503296

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 4:
            return 503295

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 4:
            return 503294

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 4:
            return 503293

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 234:
            return 503292

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 197:
            return 503287

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 196:
            return 503286

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 2:
            return 503285

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 1:
            return 503284

        if discipline == 0 and parameterCategory == 198 and parameterNumber == 0:
            return 503283

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192 and typeOfFirstFixedSurface == 10:
            return 503282

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102:
            return 503280

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and constituentType == 62025:
            return 503279

        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 20000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10000 and constituentType == 62025:
            return 503278

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 38500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 20000 and constituentType == 62025:
            return 503277

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 70000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 38500 and constituentType == 62025:
            return 503276

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 24000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 9100 and constituentType == 62025:
            return 503275

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 70000 and constituentType == 62025:
            return 503274

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 46500 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 24000 and constituentType == 62025:
            return 503273

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 15:
            return 503270

        aerosolType = h.get_l('aerosolType')

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62008:
            return 503269

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62001:
            return 503268

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and aerosolType == 62025:
            return 503267

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 62 and constituentType == 62025:
            return 503266

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 1 and typeOfFirstFixedSurface == 10 and constituentType == 62025:
            return 503265

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 61 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 101325 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 46500 and constituentType == 62025:
            return 503263

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 0 and constituentType == 62025:
            return 503262

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30102:
            return 503261

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30175:
            return 503260

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30139:
            return 503259

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30138:
            return 503258

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30161:
            return 503257

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30079:
            return 503256

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30129:
            return 503255

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30141:
            return 503254

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 14 and constituentType == 30172:
            return 503253

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 503252

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 503251

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 503250

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 503249

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 503248

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62008 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 503247

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 503246

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 503245

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 503244

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 503243

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 503242

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62001 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 503241

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 503240

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 503239

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 60 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 503238

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 7:
            return 503237

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 7:
            return 503236

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 7:
            return 503235

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 6 and typeOfDistributionFunction == 1:
            return 503234

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 5 and typeOfDistributionFunction == 1:
            return 503233

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 4 and typeOfDistributionFunction == 1:
            return 503232

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 3 and typeOfDistributionFunction == 1:
            return 503231

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 2 and typeOfDistributionFunction == 1:
            return 503230

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 2 and constituentType == 62025 and modeNumber == 1 and typeOfDistributionFunction == 1:
            return 503229

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 202:
            return 503228

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 201:
            return 503227

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 28:
            return 503226

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 27:
            return 503223

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 26:
            return 503222

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 42:
            return 503221

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 41:
            return 503220

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 21:
            return 503219

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 194:
            return 503218

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503217

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503216

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 27:
            return 503215

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 3:
            return 503214

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503213

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503212

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6:
            return 503211

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503210

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 199:
            return 503209

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 198:
            return 503208

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 2:
            return 503207

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 1:
            return 503206

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 233:
            return 503205

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10 and typeOfFirstFixedSurface == 10:
            return 503204

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 12:
            return 503203

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 11:
            return 503202

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 10:
            return 503201

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 9:
            return 503200

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 8:
            return 503199

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 7:
            return 503198

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 13:
            return 503197

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 17:
            return 503196

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 94:
            return 503195

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 197 and typeOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 3:
            return 503194

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503193

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 2:
            return 503192

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 503191

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 2 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 503190

        if discipline == 215 and parameterCategory == 5 and parameterNumber == 1 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 503189

        if discipline == 215 and parameterCategory == 19 and parameterNumber == 0:
            return 503188

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 194:
            return 503187

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 5:
            return 503186

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 6:
            return 503185

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 5:
            return 503184

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 4:
            return 503183

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 3:
            return 503182

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 2:
            return 503181

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 1:
            return 503180

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 205:
            return 503179

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 204:
            return 503178

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 203:
            return 503177

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 202:
            return 503176

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 503175

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 503174

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 44:
            return 503173

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503172

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 195:
            return 503171

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503170

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 7:
            return 503169

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 503168

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 205 and typeOfStatisticalProcessing == 11 and typeOfFirstFixedSurface == 1:
            return 503167

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 43:
            return 503166

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 503165

        if discipline == 215 and parameterCategory == 2 and parameterNumber == 0:
            return 503164

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 194 and typeOfFirstFixedSurface == 10:
            return 503163

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 232:
            return 503162

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 231:
            return 503161

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 233:
            return 503160

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 232:
            return 503159

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 29:
            return 503158

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 231:
            return 503157

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 230:
            return 503156

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfSecondFixedSurface == 192 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 3000:
            return 503155

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 16:
            return 503154

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 197:
            return 503153

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 196:
            return 503152

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 195:
            return 503151

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 194:
            return 503150

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 201:
            return 503149

        if discipline == 215 and parameterCategory == 7 and parameterNumber == 0:
            return 503148

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 229:
            return 503147

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 196:
            return 503146

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 503145

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 230 and typeOfStatisticalProcessing == 1:
            return 503143

        if discipline == 0 and parameterCategory == 17 and parameterNumber == 192:
            return 503142

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 228:
            return 503137

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 503136

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 503135

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 503134

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 31:
            return 503133

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 30:
            return 503132

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73 and typeOfStatisticalProcessing == 1:
            return 503130

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 227:
            return 503128

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 204:
            return 503127

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 203:
            return 503126

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 226:
            return 503125

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 225:
            return 503124

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 224:
            return 503123

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 223:
            return 503122

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 222:
            return 503121

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 221:
            return 503120

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 219:
            return 503119

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 218:
            return 503118

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 217:
            return 503117

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 229:
            return 503116

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 228:
            return 503115

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 14:
            return 503114

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 13:
            return 503113

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 12:
            return 503112

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 11:
            return 503111

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 10:
            return 503110

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 9:
            return 503109

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 73:
            return 503108

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 72:
            return 503107

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 71:
            return 503106

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 20:
            return 503097

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 201:
            return 503096

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 23:
            return 503095

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 24:
            return 503094

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 44:
            return 503093

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 43:
            return 503092

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 45:
            return 503091

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 33:
            return 503090

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 30:
            return 503089

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 27:
            return 503088

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 32:
            return 503087

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 29:
            return 503086

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 26:
            return 503085

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 19:
            return 503084

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 16:
            return 503083

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 17:
            return 503082

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 14:
            return 503081

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 35:
            return 503080

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 200 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 503079

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 220:
            return 503078

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0:
            return 503076

        numberOfGridInReference = h.get_l('numberOfGridInReference')

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and numberOfGridInReference == 2 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 503075

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 193:
            return 503074

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 197 and typeOfStatisticalProcessing == 1:
            return 503073

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 196 and typeOfStatisticalProcessing == 1:
            return 503072

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 195 and typeOfStatisticalProcessing == 1:
            return 503071

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 194 and typeOfStatisticalProcessing == 1:
            return 503070

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 193 and typeOfStatisticalProcessing == 1:
            return 503069

        if discipline == 0 and parameterCategory == 16 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 503068

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfGeneratingProcess == 1:
            return 503066

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0 and typeOfGeneratingProcess == 1:
            return 503065

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 503064

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 503063

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 503062

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 503061

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 216:
            return 503060

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 215:
            return 503059

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 214:
            return 503058

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 213:
            return 503057

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 212:
            return 503056

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 211:
            return 503055

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 198:
            return 503054

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 197:
            return 503053

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 196:
            return 503052

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 195:
            return 503050

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 227:
            return 503049

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 17:
            return 503048

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 36:
            return 503047

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 4:
            return 503039

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 16:
            return 503038

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 26 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 2 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 503028

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 2:
            return 503025

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 19:
            return 503024

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7:
            return 503023

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 6:
            return 503022

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 5:
            return 503021

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 0:
            return 503020

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 12:
            return 503019

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 7:
            return 503017

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 6:
            return 503016

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 5:
            return 503015

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 4:
            return 503014

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 3:
            return 503013

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 2:
            return 503012

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 3:
            return 503011

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 3:
            return 502969

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 1:
            return 502968

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 1:
            return 502967

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 0:
            return 502966

        if discipline == 10 and parameterCategory == 4 and parameterNumber == 2:
            return 502965

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 10:
            return 502964

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 2:
            return 502963

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 7:
            return 502962

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 5:
            return 502961

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 3:
            return 502960

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 3:
            return 502959

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 2:
            return 502958

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 11:
            return 502955

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 7:
            return 502954

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 6:
            return 502953

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 9:
            return 502952

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 8:
            return 502951

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 9:
            return 502950

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 0:
            return 502949

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 8:
            return 502948

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 7:
            return 502947

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 0:
            return 502946

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 5:
            return 502945

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 4:
            return 502944

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 7:
            return 502943

        if discipline == 10 and parameterCategory == 191 and parameterNumber == 0:
            return 502942

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 1:
            return 502941

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 13:
            return 502940

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 11:
            return 502939

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 10:
            return 502938

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 13:
            return 502937

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 12:
            return 502936

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 11:
            return 502935

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 10:
            return 502934

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 9:
            return 502933

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 7:
            return 502932

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 6:
            return 502931

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 5:
            return 502930

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 4:
            return 502929

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 3:
            return 502928

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 1:
            return 502927

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 0:
            return 502926

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 16:
            return 502924

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 15:
            return 502923

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 14:
            return 502922

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 13:
            return 502921

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 12:
            return 502920

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 11:
            return 502919

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 10:
            return 502900

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 9:
            return 502899

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 8:
            return 502898

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 7:
            return 502897

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 6:
            return 502896

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 5:
            return 502895

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 4:
            return 502894

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 3:
            return 502893

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 2:
            return 502892

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 1:
            return 502891

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 27:
            return 502890

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 25:
            return 502889

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 24:
            return 502888

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 23:
            return 502887

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 21:
            return 502886

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 20:
            return 502885

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 18:
            return 502883

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 15:
            return 502882

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 14:
            return 502881

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 12:
            return 502880

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 11:
            return 502879

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 10:
            return 502878

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 9:
            return 502877

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 8:
            return 502876

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 6:
            return 502875

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 2:
            return 502874

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 1:
            return 502873

        if discipline == 1 and parameterCategory == 1 and parameterNumber == 0:
            return 502872

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 6:
            return 502871

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 5:
            return 502870

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 4:
            return 502869

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 3:
            return 502868

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 2:
            return 502867

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 1:
            return 502866

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 0:
            return 502865

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 0:
            return 502864

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 23:
            return 502862

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 22:
            return 502861

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 21:
            return 502860

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 25:
            return 502859

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 20:
            return 502858

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 17:
            return 502857

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 16:
            return 502856

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 15:
            return 502855

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 14:
            return 502854

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 13:
            return 502853

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 12:
            return 502852

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 10:
            return 502851

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 9:
            return 502850

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 8:
            return 502849

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 6:
            return 502848

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 5:
            return 502847

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 4:
            return 502846

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 8:
            return 502845

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 7:
            return 502844

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 6:
            return 502843

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 5:
            return 502802

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 4:
            return 502801

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 3:
            return 502800

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 2:
            return 502799

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 1:
            return 502798

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 0:
            return 502797

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 5 and typeOfStatisticalProcessing == 1:
            return 502796

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 4:
            return 502795

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 3:
            return 502794

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 2:
            return 502793

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 0:
            return 502792

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 0:
            return 502791

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 11:
            return 502790

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 10:
            return 502789

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 9:
            return 502788

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 5:
            return 502787

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 4:
            return 502786

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 2:
            return 502785

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 23:
            return 502783

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 21:
            return 502782

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 20:
            return 502781

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 19:
            return 502780

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 18:
            return 502779

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 17:
            return 502778

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 16:
            return 502777

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 15:
            return 502776

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 12:
            return 502775

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 11:
            return 502774

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 10:
            return 502773

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 9:
            return 502772

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 8:
            return 502771

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 7:
            return 502770

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 6:
            return 502769

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 0:
            return 502768

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 6:
            return 502767

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 4:
            return 502766

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 3:
            return 502765

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 1:
            return 502764

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 0:
            return 502763

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 12:
            return 502762

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 11:
            return 502761

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 7:
            return 502760

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 1:
            return 502759

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 19:
            return 502758

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18:
            return 502757

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 17:
            return 502756

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 16:
            return 502755

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 15:
            return 502754

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 14:
            return 502753

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 13:
            return 502752

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 14:
            return 502751

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 12:
            return 502749

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 28:
            return 502748

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 27:
            return 502747

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 26:
            return 502746

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 24:
            return 502745

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 23:
            return 502744

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 21:
            return 502743

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 68:
            return 502742

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 67:
            return 502741

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 13:
            return 502740

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 59:
            return 502739

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 58:
            return 502738

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 53:
            return 502737

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 50:
            return 502735

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 49:
            return 502734

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 48:
            return 502733

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 47:
            return 502732

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 44:
            return 502731

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 43:
            return 502730

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 41:
            return 502729

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 40:
            return 502728

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 39:
            return 502727

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 36:
            return 502725

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 35:
            return 502724

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 34:
            return 502723

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 33:
            return 502722

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 31:
            return 502721

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 30:
            return 502720

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 29:
            return 502719

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 28:
            return 502718

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 27:
            return 502717

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 23:
            return 502715

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 21:
            return 502714

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 20:
            return 502713

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 19:
            return 502712

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 18:
            return 502711

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 17:
            return 502710

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 15:
            return 502709

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 14:
            return 502708

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 12:
            return 502707

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 9:
            return 502706

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 51:
            return 502705

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 12:
            return 502703

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 4:
            return 502702

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 502701

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 20:
            return 502700

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 2:
            return 502693

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 16:
            return 502425

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 15:
            return 502424

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 1:
            return 502397

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 226:
            return 502354

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 225:
            return 502353

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 224:
            return 502352

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 1:
            return 502349

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 502348

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223:
            return 502347

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 223 and typeOfStatisticalProcessing == 0:
            return 502346

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222:
            return 502345

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 222 and typeOfStatisticalProcessing == 0:
            return 502344

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 80000:
            return 502343

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 80000 and typeOfFirstFixedSurface == 100 and scaledValueOfFirstFixedSurface == 40000:
            return 502342

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == 0 and scaledValueOfSecondFixedSurface == 40000 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 0:
            return 502341

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 42:
            return 502340

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 502339

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 17 and typeOfFirstFixedSurface == 1:
            return 502336

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 5:
            return 502335

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 4:
            return 502334

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 12:
            return 502333

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 210 and typeOfFirstFixedSurface == 114:
            return 502332

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 114:
            return 502331

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 114:
            return 502330

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 114:
            return 502329

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 114:
            return 502328

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 502327

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 8:
            return 502323

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 502322

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 502321

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 502320

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 502319

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 502318

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 502317

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 29:
            return 502316

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 28:
            return 502315

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 2:
            return 502314

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 2:
            return 502313

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 3:
            return 502312

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 3:
            return 502311

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and numberOfGridInReference == 1:
            return 502310

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and numberOfGridInReference == 1:
            return 502309

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18:
            return 502308

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 18 and typeOfStatisticalProcessing == 0:
            return 502307

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500905

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 254:
            return 500904

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 253:
            return 500903

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 252:
            return 500902

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 251:
            return 500901

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 250:
            return 500900

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 249:
            return 500899

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 248:
            return 500898

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 247:
            return 500897

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 246:
            return 500896

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 245:
            return 500895

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 244:
            return 500894

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 243:
            return 500893

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 242:
            return 500892

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 241:
            return 500891

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 240:
            return 500890

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 239:
            return 500889

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 238:
            return 500888

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 237:
            return 500887

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 236:
            return 500886

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 235:
            return 500885

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 234:
            return 500884

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 233:
            return 500883

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 232:
            return 500882

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 231:
            return 500881

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 230:
            return 500880

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 229:
            return 500879

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 228:
            return 500878

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 227:
            return 500877

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 226:
            return 500876

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 225:
            return 500875

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 224:
            return 500874

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 223:
            return 500873

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 222:
            return 500872

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 221:
            return 500871

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 220:
            return 500870

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 219:
            return 500869

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 218:
            return 500868

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 217:
            return 500867

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 216:
            return 500866

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 215:
            return 500865

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 214:
            return 500864

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 213:
            return 500863

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 212:
            return 500862

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 211:
            return 500861

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 210:
            return 500860

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 209:
            return 500859

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 208:
            return 500858

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 207:
            return 500857

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 206:
            return 500856

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 205:
            return 500855

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 204:
            return 500854

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 203:
            return 500853

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 202:
            return 500852

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 201:
            return 500851

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 200:
            return 500850

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 199:
            return 500849

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 198:
            return 500848

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 197:
            return 500847

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 196:
            return 500846

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 195:
            return 500845

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 194:
            return 500844

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 193:
            return 500843

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 192:
            return 500842

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 191:
            return 500841

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 190:
            return 500840

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 189:
            return 500839

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 188:
            return 500838

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 187:
            return 500837

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 186:
            return 500836

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 185:
            return 500835

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 184:
            return 500834

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 183:
            return 500833

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 182:
            return 500832

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 181:
            return 500831

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 180:
            return 500830

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 179:
            return 500829

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 178:
            return 500828

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 177:
            return 500827

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 176:
            return 500826

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 175:
            return 500825

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 174:
            return 500824

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 173:
            return 500823

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 172:
            return 500822

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 171:
            return 500821

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 170:
            return 500820

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 169:
            return 500819

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 168:
            return 500818

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 167:
            return 500817

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 166:
            return 500816

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 165:
            return 500815

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 164:
            return 500814

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 163:
            return 500813

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 162:
            return 500812

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 161:
            return 500811

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 160:
            return 500810

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 159:
            return 500809

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 158:
            return 500808

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 157:
            return 500807

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 156:
            return 500806

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 155:
            return 500805

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 154:
            return 500804

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 153:
            return 500803

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 152:
            return 500802

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 151:
            return 500801

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 150:
            return 500800

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 149:
            return 500799

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 148:
            return 500798

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 147:
            return 500797

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 146:
            return 500796

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 145:
            return 500795

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 144:
            return 500794

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 143:
            return 500793

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 142:
            return 500792

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 141:
            return 500791

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 140:
            return 500790

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 139:
            return 500789

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 138:
            return 500788

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 137:
            return 500787

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 136:
            return 500786

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 135:
            return 500785

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 134:
            return 500784

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 133:
            return 500783

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 132:
            return 500782

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 131:
            return 500781

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 130:
            return 500780

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 129:
            return 500779

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 128:
            return 500778

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 127:
            return 500777

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 126:
            return 500776

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 125:
            return 500775

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 124:
            return 500774

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 123:
            return 500773

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 122:
            return 500772

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 121:
            return 500771

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 120:
            return 500770

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 119:
            return 500769

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 118:
            return 500768

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 117:
            return 500767

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 116:
            return 500766

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 115:
            return 500765

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 114:
            return 500764

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 113:
            return 500763

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 112:
            return 500762

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 111:
            return 500761

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 110:
            return 500760

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 109:
            return 500759

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 108:
            return 500758

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 107:
            return 500757

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 106:
            return 500756

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 105:
            return 500755

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 104:
            return 500754

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 103:
            return 500753

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 102:
            return 500752

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 101:
            return 500751

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 100:
            return 500750

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 99:
            return 500749

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 98:
            return 500748

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 97:
            return 500747

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 96:
            return 500746

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 95:
            return 500745

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 94:
            return 500744

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 93:
            return 500743

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 92:
            return 500742

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 91:
            return 500741

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 90:
            return 500740

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 89:
            return 500739

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 88:
            return 500738

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 87:
            return 500737

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 86:
            return 500736

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 85:
            return 500735

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 84:
            return 500734

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 83:
            return 500733

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 82:
            return 500732

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 81:
            return 500731

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 80:
            return 500730

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 79:
            return 500729

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 78:
            return 500728

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 77:
            return 500727

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 76:
            return 500726

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 75:
            return 500725

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 74:
            return 500724

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 73:
            return 500723

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 72:
            return 500722

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 71:
            return 500721

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 70:
            return 500720

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 69:
            return 500719

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 68:
            return 500718

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 67:
            return 500717

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 66:
            return 500716

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 65:
            return 500715

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 64:
            return 500714

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 63:
            return 500713

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 62:
            return 500712

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 61:
            return 500711

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 60:
            return 500710

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 59:
            return 500709

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 58:
            return 500708

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 57:
            return 500707

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 56:
            return 500706

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 55:
            return 500705

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 54:
            return 500704

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 53:
            return 500703

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 52:
            return 500702

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 51:
            return 500701

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 50:
            return 500700

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 49:
            return 500699

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 48:
            return 500698

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 47:
            return 500697

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 46:
            return 500696

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 45:
            return 500695

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 44:
            return 500694

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 43:
            return 500693

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 42:
            return 500692

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 41:
            return 500691

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 40:
            return 500690

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 39:
            return 500689

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 38:
            return 500688

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 37:
            return 500687

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 36:
            return 500686

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 35:
            return 500685

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 34:
            return 500684

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 33:
            return 500683

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 32:
            return 500682

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 31:
            return 500681

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 30:
            return 500680

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 29:
            return 500679

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 28:
            return 500678

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 27:
            return 500677

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 26:
            return 500676

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 25:
            return 500675

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 24:
            return 500674

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 23:
            return 500673

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 22:
            return 500672

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 21:
            return 500671

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 20:
            return 500670

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 19:
            return 500669

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 18:
            return 500668

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 17:
            return 500667

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 16:
            return 500666

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 15:
            return 500665

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 14:
            return 500664

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 13:
            return 500663

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 12:
            return 500662

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 11:
            return 500661

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 10:
            return 500660

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 9:
            return 500659

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 8:
            return 500658

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 7:
            return 500657

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 6:
            return 500656

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 5:
            return 500655

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 4:
            return 500654

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 3:
            return 500652

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 2:
            return 500651

        if discipline == 0 and parameterCategory == 254 and parameterNumber == 1:
            return 500650

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 252:
            return 500649

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 251:
            return 500648

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 74:
            return 500647

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 73:
            return 500646

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 72:
            return 500645

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 35:
            return 500644

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 34:
            return 500643

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 8:
            return 500642

        if discipline == 0 and parameterCategory == 197 and parameterNumber == 33:
            return 500640

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 197:
            return 500639

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 200:
            return 500638

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 218:
            return 500637

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 219:
            return 500636

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 221:
            return 500635

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 220:
            return 500634

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 14 and typeOfGeneratingProcess == 5:
            return 500633

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 13 and typeOfGeneratingProcess == 5:
            return 500632

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 12 and typeOfGeneratingProcess == 5:
            return 500631

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500630

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 10 and typeOfGeneratingProcess == 5:
            return 500629

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 9 and typeOfGeneratingProcess == 5:
            return 500628

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 8 and typeOfGeneratingProcess == 5:
            return 500627

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 7 and typeOfGeneratingProcess == 5:
            return 500626

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 6 and typeOfGeneratingProcess == 5:
            return 500625

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 5 and typeOfGeneratingProcess == 5:
            return 500624

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 4 and typeOfGeneratingProcess == 5:
            return 500623

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 3 and typeOfGeneratingProcess == 5:
            return 500622

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 2 and typeOfGeneratingProcess == 5:
            return 500621

        if discipline == 0 and parameterCategory == 196 and parameterNumber == 1 and typeOfGeneratingProcess == 5:
            return 500620

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 5:
            return 500619

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfGeneratingProcess == 5:
            return 500618

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500617

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500616

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500615

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500614

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500613

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500612

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfGeneratingProcess == 5:
            return 500611

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfGeneratingProcess == 5:
            return 500610

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfGeneratingProcess == 5:
            return 500609

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfGeneratingProcess == 5:
            return 500608

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500607

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500606

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500605

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500604

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500603

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500602

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500601

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfGeneratingProcess == 5:
            return 500600

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 1:
            return 500599

        if discipline == 10 and parameterCategory == 1 and parameterNumber == 0:
            return 500598

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 15:
            return 500597

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 35:
            return 500596

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 34:
            return 500595

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 26:
            return 500594

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 3:
            return 500593

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 209 and typeOfStatisticalProcessing == 1:
            return 500591

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 3:
            return 500590

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 16 and typeOfStatisticalProcessing == 1:
            return 500588

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 217:
            return 500586

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 216:
            return 500585

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 33 and typeOfStatisticalProcessing == 1:
            return 500584

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 1:
            return 500583

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 1:
            return 500582

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 50 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 7:
            return 500581

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 7 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 500580

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 500579

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198 and typeOfGeneratingProcess == 6:
            return 500578

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197 and typeOfGeneratingProcess == 6:
            return 500577

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 198 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 6:
            return 500576

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 195:
            return 500575

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 25:
            return 500574

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 192:
            return 500573

        if discipline == 1 and parameterCategory == 0 and parameterNumber == 192:
            return 500572

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 202:
            return 500570

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 13:
            return 500569

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5:
            return 500568

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 22:
            return 500567

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 21:
            return 500566

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 20:
            return 500565

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 19:
            return 500564

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 18:
            return 500563

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 17:
            return 500562

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 16:
            return 500560

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 15:
            return 500559

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 14:
            return 500558

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 13:
            return 500557

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 12:
            return 500556

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 11:
            return 500555

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 10:
            return 500554

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 9:
            return 500553

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 8:
            return 500552

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 7:
            return 500551

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 23:
            return 500550

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 22:
            return 500549

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 19:
            return 500548

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 4:
            return 500547

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 11:
            return 500546

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 10:
            return 500545

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14:
            return 500544

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 12:
            return 500543

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 199:
            return 500542

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 198:
            return 500541

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 192:
            return 500540

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 2:
            return 500539

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 192:
            return 500538

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 209:
            return 500531

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 0:
            return 500530

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 0:
            return 500529

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 208 and typeOfGeneratingProcess == 2:
            return 500528

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 207 and typeOfGeneratingProcess == 2:
            return 500527

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 0:
            return 500526

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 0:
            return 500525

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 0:
            return 500524

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 0:
            return 500523

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 0:
            return 500522

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 0:
            return 500521

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 0:
            return 500520

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 0:
            return 500519

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 0:
            return 500518

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 0:
            return 500517

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 0:
            return 500516

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 0:
            return 500515

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 206 and typeOfGeneratingProcess == 2:
            return 500514

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 205 and typeOfGeneratingProcess == 2:
            return 500513

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 204 and typeOfGeneratingProcess == 2:
            return 500512

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 203 and typeOfGeneratingProcess == 2:
            return 500511

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 202 and typeOfGeneratingProcess == 2:
            return 500510

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 201 and typeOfGeneratingProcess == 2:
            return 500509

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 200 and typeOfGeneratingProcess == 2:
            return 500508

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 199 and typeOfGeneratingProcess == 2:
            return 500507

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 198 and typeOfGeneratingProcess == 2:
            return 500506

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 197 and typeOfGeneratingProcess == 2:
            return 500505

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 196 and typeOfGeneratingProcess == 2:
            return 500504

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 195 and typeOfGeneratingProcess == 2:
            return 500503

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 165 and typeOfFirstFixedSurface == 162:
            return 500502

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 165:
            return 500501

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 10 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 166:
            return 500500

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 500499

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 162:
            return 500498

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 166 and typeOfFirstFixedSurface == 1:
            return 500497

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 1 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 500496

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 4 and typeOfFirstFixedSurface == 164:
            return 500495

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 3 and typeOfSecondFixedSurface == 164 and typeOfFirstFixedSurface == 162:
            return 500494

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 11 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 500493

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 33:
            return 500492

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 0 and typeOfSecondFixedSurface == 162 and typeOfFirstFixedSurface == 1:
            return 500491

        if discipline == 1 and parameterCategory == 2 and parameterNumber == 2:
            return 500490

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500489

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500488

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500487

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500486

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 8 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500482

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 199 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500481

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 198 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500480

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 2:
            return 500479

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 3:
            return 500478

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 500477

        if discipline == 10 and parameterCategory == 3 and parameterNumber == 0:
            return 500475

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 13:
            return 500474

        if discipline == 0 and parameterCategory == 192 and parameterNumber == 1:
            return 500473

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 201:
            return 500472

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 194 and typeOfStatisticalProcessing == 2:
            return 500471

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 0 and typeOfStatisticalProcessing == 1:
            return 500469

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 50 and typeOfStatisticalProcessing == 2:
            return 500468

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 197:
            return 500467

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 196:
            return 500466

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 195:
            return 500465

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 236 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 500464

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 232 and typeOfStatisticalProcessing == 3 and typeOfGeneratingProcess == 5:
            return 500463

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 213 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500462

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 212 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500461

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 199 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500460

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 198 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500459

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 197 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500458

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 191 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500457

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 139 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500456

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 138 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500455

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 137 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500454

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 136 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500453

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 134 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500452

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 132 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500451

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 77 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500450

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 75 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500449

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 74 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500448

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 72 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500447

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 71 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500446

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 70 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500445

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 69 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500444

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 32 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500443

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 29 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500442

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 26 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500441

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 17 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500440

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 14 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500439

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 3 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500438

        if discipline == 0 and parameterCategory == 195 and parameterNumber == 1 and typeOfStatisticalProcessing == 2 and typeOfGeneratingProcess == 5:
            return 500437

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500436

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500434

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500433

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500432

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500431

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500430

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500429

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500428

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500425

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500424

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500423

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500422

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500421

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 500420

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8 and typeOfGeneratingProcess == 1:
            return 500419

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 1:
            return 500418

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 1:
            return 500417

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 1:
            return 500416

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 1:
            return 500412

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500411

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500410

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500409

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500408

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 1:
            return 500404

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 4:
            return 500401

        satelliteSeries = h.get_l('satelliteSeries')
        satelliteNumber = h.get_l('satelliteNumber')
        instrumentType = h.get_l('instrumentType')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500400

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 500399

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500398

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500397

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500396

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 500395

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 83333:
            return 500394

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500393

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1250000:
            return 500392

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1666666:
            return 500391

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 625000:
            return 500390

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 2000000:
            return 500389

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 198:
            return 500388

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 500387

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 198:
            return 500386

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 500385

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 500384

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 500383

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 197:
            return 500382

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and typeOfGeneratingProcess == 197:
            return 500381

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800 and typeOfGeneratingProcess == 197:
            return 500380

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfGeneratingProcess == 197:
            return 500379

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfGeneratingProcess == 197:
            return 500378

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 500377

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197:
            return 500376

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 500375

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 500374

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 500373

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 197:
            return 500372

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500371

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 500370

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500369

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500368

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500367

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 500366

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 500365

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500364

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500363

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 500362

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500361

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500360

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500359

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 500358

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 500357

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500356

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500355

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 500354

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500353

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500352

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 500351

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 500350

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500349

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500348

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500347

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290:
            return 500346

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500345

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500344

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500343

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 500342

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 500341

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500340

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 500339

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 500338

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 500337

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 500336

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 500335

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 500334

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 156250:
            return 500333

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205 and scaledValueOfCentralWaveNumber == 86956:
            return 500332

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500331

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500330

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500329

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500328

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 500327

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 500326

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 500325

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 500324

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500323

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500322

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500321

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500320

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500319

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500318

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500317

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500316

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500315

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500314

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500313

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500312

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500311

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500310

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500309

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 201:
            return 500308

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199:
            return 500307

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198:
            return 500306

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 500305

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13:
            return 500304

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 500303

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3:
            return 500302

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107:
            return 500301

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 6:
            return 500300

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 5:
            return 500299

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 25 and typeOfFirstFixedSurface == 107:
            return 500298

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 4:
            return 500297

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 3:
            return 500296

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 2:
            return 500295

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 1:
            return 500294

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 0:
            return 500293

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25:
            return 500292

        if discipline == 0 and parameterCategory == 193 and parameterNumber == 24 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 500291

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 2:
            return 500290

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 194:
            return 500289

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 197:
            return 500288

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8:
            return 500287

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 25:
            return 500286

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51 and typeOfStatisticalProcessing == 2:
            return 500285

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23:
            return 500284

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0 and typeOfGeneratingProcess == 1:
            return 500283

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194:
            return 500282

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 500281

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193:
            return 500280

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 500279

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30175:
            return 500278

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30175:
            return 500277

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30175:
            return 500276

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30139:
            return 500275

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30139:
            return 500274

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30139:
            return 500273

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30138:
            return 500272

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30138:
            return 500271

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30138:
            return 500270

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30161:
            return 500269

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30161:
            return 500268

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30161:
            return 500267

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30000:
            return 500266

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30000:
            return 500265

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30000:
            return 500264

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30059:
            return 500263

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30059:
            return 500262

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30059:
            return 500261

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30079:
            return 500260

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30079:
            return 500259

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30079:
            return 500258

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30129:
            return 500257

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30129:
            return 500256

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30129:
            return 500255

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30172:
            return 500254

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30172:
            return 500253

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30172:
            return 500252

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30141:
            return 500251

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30141:
            return 500250

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30141:
            return 500249

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30067:
            return 500248

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30067:
            return 500247

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30067:
            return 500246

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 11 and constituentType == 30102:
            return 500245

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 12 and constituentType == 30102:
            return 500244

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 10 and constituentType == 30102:
            return 500243

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1:
            return 500242

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194:
            return 500241

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193:
            return 500240

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192:
            return 500239

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 30:
            return 500238

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2:
            return 500237

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1:
            return 500236

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193:
            return 500235

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 500234

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207:
            return 500233

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62008:
            return 500232

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62008:
            return 500231

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62009:
            return 500230

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62009:
            return 500229

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62010:
            return 500228

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62010:
            return 500227

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62001:
            return 500226

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62001:
            return 500225

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and typeOfStatisticalProcessing == 0 and constituentType == 62006:
            return 500224

        if discipline == 0 and parameterCategory == 20 and parameterNumber == 102 and constituentType == 62006:
            return 500223

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192:
            return 500222

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 500221

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 500220

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 0:
            return 500219

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30:
            return 500218

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29:
            return 500217

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and typeOfGeneratingProcess == 6:
            return 500216

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 197 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0 and typeOfGeneratingProcess == 6:
            return 500215

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 500214

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3:
            return 500213

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 2:
            return 500212

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 3:
            return 500211

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2:
            return 500210

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193:
            return 500209

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192:
            return 500208

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32:
            return 500207

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28:
            return 500206

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196:
            return 500205

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 199:
            return 500204

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22:
            return 500203

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21:
            return 500202

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24:
            return 500201

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20:
            return 500200

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195:
            return 500199

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194:
            return 500198

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 3 and typeOfGeneratingProcess == 7:
            return 500197

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 2 and typeOfGeneratingProcess == 7:
            return 500196

        if discipline == 0 and parameterCategory == 194 and parameterNumber == 5 and typeOfGeneratingProcess == 7:
            return 500195

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 31:
            return 500194

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 28:
            return 500193

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 25:
            return 500192

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 15:
            return 500191

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 34:
            return 500190

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 35:
            return 500189

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 36:
            return 500187

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 14:
            return 500185

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206:
            return 500184

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6:
            return 500183

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 2:
            return 500182

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 500181

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 500180

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 500179

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 500178

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193:
            return 500177

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 192:
            return 500176

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 500175

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1:
            return 500174

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500173

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8:
            return 500172

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16:
            return 500171

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18:
            return 500170

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13:
            return 500169

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 500168

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and typeOfFirstFixedSurface == 106:
            return 500167

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106:
            return 500166

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 500164

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3:
            return 500163

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19:
            return 500162

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29:
            return 500161

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20:
            return 500160

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31:
            return 500159

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11:
            return 500158

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196:
            return 500157

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 500156

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 24:
            return 500155

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 192:
            return 500154

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 192:
            return 500153

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 7 and typeOfFirstFixedSurface == 193:
            return 500152

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 193:
            return 500151

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193:
            return 500150

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192:
            return 500149

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192:
            return 500148

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61:
            return 500147

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfStatisticalProcessing == 1:
            return 500146

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75:
            return 500145

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202:
            return 500144

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 500143

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201:
            return 500142

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200:
            return 500141

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193:
            return 500140

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfStatisticalProcessing == 1:
            return 500139

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfStatisticalProcessing == 1:
            return 500138

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1:
            return 500137

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55:
            return 500136

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76:
            return 500135

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfStatisticalProcessing == 1:
            return 500134

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56:
            return 500133

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77:
            return 500132

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196:
            return 500131

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199:
            return 500130

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198:
            return 500129

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 500128

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 4:
            return 500127

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 500126

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193:
            return 500125

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192:
            return 500124

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197:
            return 500123

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192:
            return 500122

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 500121

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 500120

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 500119

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 500118

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195:
            return 500117

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 3:
            return 500116

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 2:
            return 500115

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194:
            return 500111

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193:
            return 500110

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfStatisticalProcessing == 1:
            return 500109

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78:
            return 500108

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 500107

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32:
            return 500106

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 500105

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 500104

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25:
            return 500103

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24:
            return 500102

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82:
            return 500101

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22:
            return 500100

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14:
            return 500099

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22:
            return 500098

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195:
            return 500097

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 106:
            return 500095

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 500094

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192:
            return 500093

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192:
            return 500092

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 500091

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500090

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500089

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500088

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500087

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500086

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 8:
            return 500085

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 500084

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 8:
            return 500083

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 8:
            return 500082

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 500081

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500080

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 500079

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500078

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 9:
            return 500077

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 8:
            return 500076

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 7:
            return 500075

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 6:
            return 500074

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 5:
            return 500073

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 4:
            return 500072

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 3:
            return 500071

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1:
            return 500070

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 500069

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 500068

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 500066

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4:
            return 500065

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 100 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 10:
            return 500064

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 10 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 0:
            return 500063

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == 2 and scaledValueOfSecondFixedSurface == 190 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 100:
            return 500062

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 500061

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 9:
            return 500060

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 41:
            return 500059

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == 2 and scaledValueOfFirstFixedSurface == 36:
            return 500058

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfStatisticalProcessing == 0:
            return 500057

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1:
            return 500056

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1:
            return 500055

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0:
            return 500054

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1:
            return 500053

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfStatisticalProcessing == 1:
            return 500052

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69:
            return 500051

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 500050

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400:
            return 500049

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and typeOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800:
            return 500048

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2:
            return 500047

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1:
            return 500046

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11:
            return 500045

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60:
            return 500044

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 500043

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 500042

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1:
            return 500041

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70:
            return 500040

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 500039

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64:
            return 500038

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 500037

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500036

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0:
            return 500035

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500034

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 500032

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 500031

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 500030

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 500029

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 500028

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 500027

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1:
            return 500026

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 500025

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0:
            return 500024

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10:
            return 500023

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 500022

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 500021

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 500020

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfStatisticalProcessing == 2 and typeOfSecondFixedSurface == 8 and typeOfFirstFixedSurface == 1:
            return 500019

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500018

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500017

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500016

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500015

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 500014

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2 and typeOfGeneratingProcess == 9:
            return 500013

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500012

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
            return 500011

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500010

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2:
            return 500009

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101:
            return 500008

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfSecondFixedSurface == 101 and typeOfFirstFixedSurface == 1:
            return 500007

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 500006

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfSecondFixedSurface == 105 and typeOfFirstFixedSurface == 105:
            return 500005

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 500004

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 500003

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1:
            return 500002

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 500001

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500000

    return wrapped
