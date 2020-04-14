import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get_l('discipline')
        parameterCategory = h.get_l('parameterCategory')
        parameterNumber = h.get_l('parameterNumber')
        typeOfGeneratingProcess = h.get_l('typeOfGeneratingProcess')
        satelliteSeries = h.get_l('satelliteSeries')
        satelliteNumber = h.get_l('satelliteNumber')
        instrumentType = h.get_l('instrumentType')
        scaledValueOfCentralWaveNumber = h.get_l('scaledValueOfCentralWaveNumber')

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500400

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500399

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500398

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500397

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500396

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500395

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 83333:
            return 500394

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 2 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500393

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1250000:
            return 500392

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 1666666 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500391

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 625000:
            return 500390

        if discipline == 3 and parameterCategory == 0 and parameterNumber == 1 and typeOfGeneratingProcess == 8 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 2000000:
            return 500389

        typeOfStatisticalProcessing = h.get_l('typeOfStatisticalProcessing')
        typeOfFirstFixedSurface = h.get_l('typeOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get_l('scaleFactorOfFirstFixedSurface')
        scaledValueOfFirstFixedSurface = h.get_l('scaledValueOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 198:
            return 500388

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198:
            return 500387

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 198:
            return 500386

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 500385

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2 and typeOfGeneratingProcess == 197:
            return 500384

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfGeneratingProcess == 197 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 500383

        typeOfSecondFixedSurface = h.get_l('typeOfSecondFixedSurface')
        scaleFactorOfSecondFixedSurface = h.get_l('scaleFactorOfSecondFixedSurface')
        scaledValueOfSecondFixedSurface = h.get_l('scaledValueOfSecondFixedSurface')

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400 and typeOfGeneratingProcess == 197 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0:
            return 500382

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 800 and typeOfGeneratingProcess == 197:
            return 500381

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 1 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 800 and typeOfGeneratingProcess == 197:
            return 500380

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return 500379

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1 and typeOfGeneratingProcess == 197:
            return 500378

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 500377

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 10 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0:
            return 500376

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfGeneratingProcess == 197 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 2:
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

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410 and satelliteSeries == 333:
            return 500367

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626 and satelliteSeries == 333 and satelliteNumber == 72:
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

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942 and satelliteSeries == 333:
            return 500360

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500359

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626:
            return 500358

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and scaledValueOfCentralWaveNumber == 82644 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 500357

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500356

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500355

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 161290 and satelliteSeries == 333:
            return 500354

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500353

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410:
            return 500352

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 74626 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500351

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500350

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500349

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942:
            return 500348

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 136986:
            return 500347

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 161290 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 500346

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 103092:
            return 500345

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 114942 and satelliteSeries == 333:
            return 500344

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 256410 and satelliteSeries == 333 and satelliteNumber == 72:
            return 500343

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and scaledValueOfCentralWaveNumber == 74626 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207:
            return 500342

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 82644:
            return 500341

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 333 and satelliteNumber == 72 and instrumentType == 207 and scaledValueOfCentralWaveNumber == 92592:
            return 500340

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500339

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500338

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 54:
            return 500337

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500336

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500335

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500334

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500333

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 54 and instrumentType == 205:
            return 500332

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500331

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500330

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500329

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteSeries == 331 and satelliteNumber == 53 and instrumentType == 205:
            return 500328

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 17 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 500327

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 16 and satelliteSeries == 331 and satelliteNumber == 52 and instrumentType == 205:
            return 500326

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 15 and instrumentType == 205 and satelliteSeries == 331 and satelliteNumber == 52:
            return 500325

        if discipline == 3 and parameterCategory == 1 and parameterNumber == 14 and satelliteNumber == 52 and instrumentType == 205 and satelliteSeries == 331:
            return 500324

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500323

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500322

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500321

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500320

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500319

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500318

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500317

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500316

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500315

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500314

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500313

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500312

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 200:
            return 500311

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500310

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfGeneratingProcess == 200 and typeOfStatisticalProcessing == 5:
            return 500309

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfStatisticalProcessing == 5 and typeOfGeneratingProcess == 199:
            return 500308

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 199 and typeOfFirstFixedSurface == 1:
            return 500307

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 198 and typeOfFirstFixedSurface == 1:
            return 500306

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 7:
            return 500305

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 500304

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 3:
            return 500303

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 500302

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 107 and scaleFactorOfFirstFixedSurface == -2:
            return 500301

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 14 and typeOfFirstFixedSurface == 107:
            return 500298

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 25 and typeOfFirstFixedSurface == 1:
            return 500292

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 1:
            return 500291

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 10:
            return 500288

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 8 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500287

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 105:
            return 500286

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 51:
            return 500285

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfFirstFixedSurface == 1:
            return 500284

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 23 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500283

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 500282

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 194 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500281

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 500280

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 193 and typeOfStatisticalProcessing == 0 and typeOfFirstFixedSurface == 1:
            return 500279

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 227:
            return 500278

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 226:
            return 500277

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 225:
            return 500276

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 224:
            return 500275

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 223:
            return 500274

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 222:
            return 500273

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 221:
            return 500272

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 220:
            return 500271

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 219:
            return 500270

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 218:
            return 500269

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 217:
            return 500268

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 216:
            return 500267

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 215:
            return 500266

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 214:
            return 500265

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 213:
            return 500264

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 212:
            return 500263

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 211:
            return 500262

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 210:
            return 500261

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 209:
            return 500260

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 208:
            return 500259

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 207:
            return 500258

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 206:
            return 500257

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 205:
            return 500256

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 204:
            return 500255

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 203:
            return 500254

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 202:
            return 500253

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 201:
            return 500252

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 200:
            return 500251

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 199:
            return 500250

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 198:
            return 500249

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 197:
            return 500248

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 196:
            return 500247

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 195:
            return 500246

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 194:
            return 500245

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 193:
            return 500244

        if discipline == 0 and parameterCategory == 18 and parameterNumber == 192:
            return 500243

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 1 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500242

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 500241

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 500240

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 500239

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 200 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500238

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 500237

        if discipline == 0 and parameterCategory == 191 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500236

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 500235

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 208:
            return 500234

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 207 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500233

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196 and typeOfStatisticalProcessing == 0:
            return 500232

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 196:
            return 500231

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195 and typeOfStatisticalProcessing == 0:
            return 500230

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 195:
            return 500229

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194 and typeOfStatisticalProcessing == 0:
            return 500228

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 194:
            return 500227

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193 and typeOfStatisticalProcessing == 0:
            return 500226

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 193:
            return 500225

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192 and typeOfStatisticalProcessing == 0:
            return 500224

        if discipline == 0 and parameterCategory == 13 and parameterNumber == 192:
            return 500223

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 500222

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500221

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31 and typeOfStatisticalProcessing == 2:
            return 500220

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 31:
            return 500219

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 30 and typeOfFirstFixedSurface == 1:
            return 500218

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return 500217

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and typeOfStatisticalProcessing == 7 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 100:
            return 500216

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfSecondFixedSurface == 10 and typeOfStatisticalProcessing == 7:
            return 500215

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 7:
            return 500214

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 1:
            return 500213

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1:
            return 500212

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 3:
            return 500211

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 1:
            return 500210

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 500209

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 500208

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 32 and typeOfFirstFixedSurface == 1:
            return 500207

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 28 and typeOfFirstFixedSurface == 1:
            return 500206

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500205

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 500204

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 1:
            return 500203

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 21 and typeOfFirstFixedSurface == 1:
            return 500202

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 24 and typeOfFirstFixedSurface == 1:
            return 500201

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 1:
            return 500200

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 195 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500199

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500198

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 500197

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 500196

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 5 and typeOfStatisticalProcessing == 6 and typeOfGeneratingProcess == 7:
            return 500195

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 199:
            return 500194

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 198:
            return 500193

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 197:
            return 500192

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 196:
            return 500191

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 195:
            return 500190

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194:
            return 500189

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 194 and typeOfFirstFixedSurface == 101:
            return 500188

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193:
            return 500187

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 193 and typeOfFirstFixedSurface == 101:
            return 500186

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 192:
            return 500185

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 206 and typeOfFirstFixedSurface == 1:
            return 500184

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 500183

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 205 and typeOfFirstFixedSurface == 1:
            return 500182

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 195:
            return 500181

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 194:
            return 500180

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 193:
            return 500179

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 192:
            return 500178

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500177

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500176

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 10:
            return 500175

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500174

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500173

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 8 and typeOfFirstFixedSurface == 1:
            return 500172

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 16 and typeOfFirstFixedSurface == 1:
            return 500171

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 18 and typeOfFirstFixedSurface == 1:
            return 500170

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 13 and typeOfFirstFixedSurface == 1:
            return 500169

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 22 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 500168

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 500167

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaleFactorOfFirstFixedSurface == -2:
            return 500166

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192:
            return 500165

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and scaledValueOfFirstFixedSurface == 10 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103:
            return 500164

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 3 and typeOfFirstFixedSurface == 1:
            return 500163

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 19 and typeOfFirstFixedSurface == 1:
            return 500162

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 29 and typeOfFirstFixedSurface == 1:
            return 500161

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 20 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500160

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 31 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500159

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 11 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500158

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 196 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500157

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
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

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 193 and typeOfFirstFixedSurface == 1:
            return 500150

        if discipline == 0 and parameterCategory == 7 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 500149

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 192 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500148

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 61 and typeOfFirstFixedSurface == 1:
            return 500147

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500146

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 75 and typeOfFirstFixedSurface == 1:
            return 500145

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 202 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500144

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 203:
            return 500143

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 201 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500142

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 200 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500141

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500140

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 66 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500139

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 65 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500138

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfStatisticalProcessing == 1 and typeOfFirstFixedSurface == 1:
            return 500137

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfFirstFixedSurface == 1:
            return 500136

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 76 and typeOfFirstFixedSurface == 1:
            return 500135

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500134

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1:
            return 500133

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 77 and typeOfFirstFixedSurface == 1:
            return 500132

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 196 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500131

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 199 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500130

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 198 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500129

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 204:
            return 500128

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 200 and typeOfFirstFixedSurface == 4:
            return 500127

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 196 and typeOfFirstFixedSurface == 1:
            return 500126

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500125

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500124

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 197 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500123

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500122

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 500121

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 194 and typeOfFirstFixedSurface == 1:
            return 500120

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 27 and typeOfFirstFixedSurface == 3:
            return 500119

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 26 and typeOfFirstFixedSurface == 2:
            return 500118

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 195 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500117

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 193 and typeOfFirstFixedSurface == 3:
            return 500116

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 192 and typeOfFirstFixedSurface == 2:
            return 500115

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500111

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 193 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500110

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 192 and typeOfFirstFixedSurface == 1:
            return 500109

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 78 and typeOfFirstFixedSurface == 1:
            return 500108

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 74:
            return 500107

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 32 and typeOfFirstFixedSurface == 105 and scaleFactorOfFirstFixedSurface == 0:
            return 500106

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 46:
            return 500105

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 45:
            return 500104

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 25 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500103

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 24 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500102

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 82 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500101

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500100

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 14 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500099

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500098

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 195 and typeOfFirstFixedSurface == 1:
            return 500097

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 24 and typeOfStatisticalProcessing == 1:
            return 500096

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 194 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and typeOfStatisticalProcessing == 0:
            return 500095

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 193 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500094

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500093

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 192 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500092

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1:
            return 500091

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500090

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 18 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500089

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 17 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500088

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 11 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500087

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 10 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500086

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0:
            return 500085

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 500084

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0:
            return 500083

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 0 and typeOfStatisticalProcessing == 0:
            return 500082

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1:
            return 500081

        if discipline == 0 and parameterCategory == 5 and parameterNumber == 5 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500080

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1:
            return 500079

        if discipline == 0 and parameterCategory == 4 and parameterNumber == 9 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
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

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500070

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500069

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and typeOfStatisticalProcessing == 1 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2:
            return 500068

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 1 and scaledValueOfSecondFixedSurface == 190:
            return 500067

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 5 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2 and typeOfStatisticalProcessing == 1 and scaledValueOfSecondFixedSurface == 100:
            return 500066

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 500065

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == -2:
            return 500064

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfSecondFixedSurface == 10 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2:
            return 500063

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 20 and typeOfFirstFixedSurface == 106 and typeOfSecondFixedSurface == 106 and scaledValueOfFirstFixedSurface == 100 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 190 and scaleFactorOfSecondFixedSurface == -2:
            return 500062

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 500061

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 9:
            return 500060

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and scaledValueOfFirstFixedSurface == 41 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 106:
            return 500059

        if discipline == 2 and parameterCategory == 3 and parameterNumber == 18 and typeOfFirstFixedSurface == 106 and scaledValueOfFirstFixedSurface == 36 and scaleFactorOfFirstFixedSurface == -2:
            return 500058

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 0:
            return 500057

        if discipline == 0 and parameterCategory == 19 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500056

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500055

        if discipline == 2 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500054

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 56 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500053

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 55 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500052

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 69 and typeOfFirstFixedSurface == 1:
            return 500051

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 0 and scaleFactorOfFirstFixedSurface == -2 and scaledValueOfSecondFixedSurface == 400:
            return 500050

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfFirstFixedSurface == 100 and typeOfSecondFixedSurface == 100 and scaledValueOfSecondFixedSurface == 800 and scaleFactorOfSecondFixedSurface == -2 and scaledValueOfFirstFixedSurface == 400 and scaleFactorOfFirstFixedSurface == -2:
            return 500049

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 22 and typeOfSecondFixedSurface == 1 and scaledValueOfFirstFixedSurface == 800 and scaleFactorOfFirstFixedSurface == -2 and typeOfFirstFixedSurface == 100:
            return 500048

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500047

        if discipline == 0 and parameterCategory == 6 and parameterNumber == 1 and typeOfFirstFixedSurface == 1:
            return 500046

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 11 and typeOfFirstFixedSurface == 1:
            return 500045

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 60 and typeOfFirstFixedSurface == 1:
            return 500044

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 37 and typeOfStatisticalProcessing == 1:
            return 500043

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 54 and typeOfStatisticalProcessing == 1:
            return 500042

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 52 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500041

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 70 and typeOfFirstFixedSurface == 1:
            return 500040

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 79 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 1:
            return 500039

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 64 and typeOfFirstFixedSurface == 1:
            return 500038

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1:
            return 500037

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 500036

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0:
            return 500035

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 500034

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500033

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 9:
            return 500032

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 8:
            return 500031

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3:
            return 500030

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 3 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 500029

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2:
            return 500028

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 2 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 500027

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500026

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 500025

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500024

        if discipline == 0 and parameterCategory == 2 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 10 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 500023

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 2:
            return 500022

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 1:
            return 500021

        if discipline == 10 and parameterCategory == 0 and parameterNumber == 0:
            return 500020

        if discipline == 0 and parameterCategory == 15 and parameterNumber == 6 and typeOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2:
            return 500019

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 0:
            return 500018

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 3:
            return 500016

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2:
            return 500015

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0:
            return 500014

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 0 and typeOfGeneratingProcess == 9:
            return 500013

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500010

        if discipline == 0 and parameterCategory == 14 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 500009

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500008

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 6 and typeOfFirstFixedSurface == 1:
            return 500007

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4:
            return 500006

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 105:
            return 500005

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 4 and typeOfFirstFixedSurface == 1:
            return 500004

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 2 and typeOfFirstFixedSurface == 1:
            return 500003

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 1 and typeOfFirstFixedSurface == 101:
            return 500002

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0:
            return 500001

        if discipline == 0 and parameterCategory == 3 and parameterNumber == 0 and typeOfFirstFixedSurface == 1:
            return 500000

        is_s2s = h.get_l('is_s2s')
        subCentre = h.get_l('subCentre')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and is_s2s == 1 and scaledValueOfFirstFixedSurface == 2 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 0 and subCentre == 102:
            return 168

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and scaledValueOfFirstFixedSurface == 2 and scaleFactorOfFirstFixedSurface == 0 and typeOfFirstFixedSurface == 103:
            return 168

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0 and subCentre == 102 and is_s2s == 1:
            return 31

        if discipline == 10 and parameterCategory == 2 and parameterNumber == 0:
            return 31

    return wrapped
