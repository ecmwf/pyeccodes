import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500388

        if table2Version == 207 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 500387

        if table2Version == 207 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 500386

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500385

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 500384

        if table2Version == 206 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 500383

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 500382

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 500381

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 500380

        if table2Version == 206 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return 500379

        if table2Version == 206 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 500378

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500377

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500376

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500375

        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 500374

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 500373

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500372

        localElementNumber = h.get_l('localElementNumber')

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 4:
            return 500371

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 500370

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 4:
            return 500369

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 4:
            return 500368

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 500367

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 4:
            return 500366

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 4:
            return 500365

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 4:
            return 500364

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 3:
            return 500363

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 500362

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 3:
            return 500361

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 3:
            return 500360

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 500359

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 3:
            return 500358

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 3:
            return 500357

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 3:
            return 500356

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 2:
            return 500355

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 500354

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 2:
            return 500353

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 500352

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 2:
            return 500351

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 2:
            return 500350

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 2:
            return 500349

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 2:
            return 500348

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 3 and localElementNumber == 1:
            return 500347

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 500346

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 5 and localElementNumber == 1:
            return 500345

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 4 and localElementNumber == 1:
            return 500344

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 500343

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 8 and localElementNumber == 1:
            return 500342

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 7 and localElementNumber == 1:
            return 500341

        if table2Version == 205 and indicatorOfParameter == 4 and indicatorOfTypeOfLevel == 222 and level == 6 and localElementNumber == 1:
            return 500340

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 4:
            return 500339

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 4:
            return 500338

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 3:
            return 500337

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 3:
            return 500336

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 2:
            return 500335

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 2:
            return 500334

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 1 and localElementNumber == 1:
            return 500333

        if table2Version == 205 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 222 and level == 2 and localElementNumber == 1:
            return 500332

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 500331

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 500330

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 500329

        if table2Version == 205 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 500328

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 4:
            return 500327

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 3:
            return 500326

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 2:
            return 500325

        if table2Version == 205 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 222 and localElementNumber == 1:
            return 500324

        if table2Version == 204 and indicatorOfParameter == 16:
            return 500323

        if table2Version == 204 and indicatorOfParameter == 15:
            return 500322

        if table2Version == 204 and indicatorOfParameter == 14:
            return 500321

        if table2Version == 204 and indicatorOfParameter == 13:
            return 500320

        if table2Version == 204 and indicatorOfParameter == 12:
            return 500319

        if table2Version == 204 and indicatorOfParameter == 11:
            return 500318

        if table2Version == 204 and indicatorOfParameter == 10:
            return 500317

        if table2Version == 204 and indicatorOfParameter == 9:
            return 500316

        if table2Version == 204 and indicatorOfParameter == 8:
            return 500315

        if table2Version == 204 and indicatorOfParameter == 7:
            return 500314

        if table2Version == 204 and indicatorOfParameter == 6:
            return 500313

        if table2Version == 204 and indicatorOfParameter == 5:
            return 500312

        if table2Version == 204 and indicatorOfParameter == 4:
            return 500311

        if table2Version == 204 and indicatorOfParameter == 3:
            return 500310

        if table2Version == 204 and indicatorOfParameter == 2:
            return 500309

        if table2Version == 204 and indicatorOfParameter == 1:
            return 500308

        if table2Version == 203 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 500307

        if table2Version == 203 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 500306

        if table2Version == 203 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 100:
            return 500305

        if table2Version == 203 and indicatorOfParameter == 157 and indicatorOfTypeOfLevel == 1:
            return 500304

        if table2Version == 203 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 100:
            return 500303

        if table2Version == 203 and indicatorOfParameter == 140 and indicatorOfTypeOfLevel == 1:
            return 500302

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 500301

        if table2Version == 203 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 100:
            return 500300

        if table2Version == 203 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 100:
            return 500299

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 500298

        if table2Version == 203 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 100:
            return 500297

        if table2Version == 203 and indicatorOfParameter == 109 and indicatorOfTypeOfLevel == 100:
            return 500296

        if table2Version == 203 and indicatorOfParameter == 107 and indicatorOfTypeOfLevel == 101:
            return 500295

        if table2Version == 203 and indicatorOfParameter == 103 and indicatorOfTypeOfLevel == 101:
            return 500294

        if table2Version == 203 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 100:
            return 500293

        if table2Version == 203 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 1:
            return 500292

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 500291

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 500290

        if table2Version == 203 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 1:
            return 500289

        if table2Version == 203 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 100:
            return 500288

        if table2Version == 203 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 500287

        if table2Version == 203 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 500286

        if table2Version == 202 and indicatorOfParameter == 248 and indicatorOfTypeOfLevel == 1:
            return 500285

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500284

        if table2Version == 202 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500283

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500282

        if table2Version == 202 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500281

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500280

        if table2Version == 202 and indicatorOfParameter == 231 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500279

        if table2Version == 202 and indicatorOfParameter == 229 and indicatorOfTypeOfLevel == 1:
            return 500278

        if table2Version == 202 and indicatorOfParameter == 228 and indicatorOfTypeOfLevel == 1:
            return 500277

        if table2Version == 202 and indicatorOfParameter == 227:
            return 500276

        if table2Version == 202 and indicatorOfParameter == 226 and indicatorOfTypeOfLevel == 1:
            return 500275

        if table2Version == 202 and indicatorOfParameter == 225 and indicatorOfTypeOfLevel == 1:
            return 500274

        if table2Version == 202 and indicatorOfParameter == 224:
            return 500273

        if table2Version == 202 and indicatorOfParameter == 223 and indicatorOfTypeOfLevel == 1:
            return 500272

        if table2Version == 202 and indicatorOfParameter == 222 and indicatorOfTypeOfLevel == 1:
            return 500271

        if table2Version == 202 and indicatorOfParameter == 221:
            return 500270

        if table2Version == 202 and indicatorOfParameter == 220 and indicatorOfTypeOfLevel == 1:
            return 500269

        if table2Version == 202 and indicatorOfParameter == 219 and indicatorOfTypeOfLevel == 1:
            return 500268

        if table2Version == 202 and indicatorOfParameter == 218:
            return 500267

        if table2Version == 202 and indicatorOfParameter == 217 and indicatorOfTypeOfLevel == 1:
            return 500266

        if table2Version == 202 and indicatorOfParameter == 216 and indicatorOfTypeOfLevel == 1:
            return 500265

        if table2Version == 202 and indicatorOfParameter == 215:
            return 500264

        if table2Version == 202 and indicatorOfParameter == 214 and indicatorOfTypeOfLevel == 1:
            return 500263

        if table2Version == 202 and indicatorOfParameter == 213 and indicatorOfTypeOfLevel == 1:
            return 500262

        if table2Version == 202 and indicatorOfParameter == 212:
            return 500261

        if table2Version == 202 and indicatorOfParameter == 211 and indicatorOfTypeOfLevel == 1:
            return 500260

        if table2Version == 202 and indicatorOfParameter == 210 and indicatorOfTypeOfLevel == 1:
            return 500259

        if table2Version == 202 and indicatorOfParameter == 209:
            return 500258

        if table2Version == 202 and indicatorOfParameter == 208 and indicatorOfTypeOfLevel == 1:
            return 500257

        if table2Version == 202 and indicatorOfParameter == 207 and indicatorOfTypeOfLevel == 1:
            return 500256

        if table2Version == 202 and indicatorOfParameter == 206:
            return 500255

        if table2Version == 202 and indicatorOfParameter == 205 and indicatorOfTypeOfLevel == 1:
            return 500254

        if table2Version == 202 and indicatorOfParameter == 204 and indicatorOfTypeOfLevel == 1:
            return 500253

        if table2Version == 202 and indicatorOfParameter == 203:
            return 500252

        if table2Version == 202 and indicatorOfParameter == 202 and indicatorOfTypeOfLevel == 1:
            return 500251

        if table2Version == 202 and indicatorOfParameter == 201 and indicatorOfTypeOfLevel == 1:
            return 500250

        if table2Version == 202 and indicatorOfParameter == 200:
            return 500249

        if table2Version == 202 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 1:
            return 500248

        if table2Version == 202 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 1:
            return 500247

        if table2Version == 202 and indicatorOfParameter == 197:
            return 500246

        if table2Version == 202 and indicatorOfParameter == 196 and indicatorOfTypeOfLevel == 1:
            return 500245

        if table2Version == 202 and indicatorOfParameter == 195 and indicatorOfTypeOfLevel == 1:
            return 500244

        if table2Version == 202 and indicatorOfParameter == 194:
            return 500243

        if table2Version == 202 and indicatorOfParameter == 180 and indicatorOfTypeOfLevel == 110:
            return 500242

        if table2Version == 202 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 500241

        if table2Version == 202 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 500240

        if table2Version == 202 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 500239

        if table2Version == 202 and indicatorOfParameter == 120 and indicatorOfTypeOfLevel == 110:
            return 500238

        if table2Version == 202 and indicatorOfParameter == 115 and indicatorOfTypeOfLevel == 1:
            return 500237

        if table2Version == 202 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 1:
            return 500236

        if table2Version == 202 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1:
            return 500235

        if table2Version == 202 and indicatorOfParameter == 105 and indicatorOfTypeOfLevel == 1:
            return 500234

        if table2Version == 202 and indicatorOfParameter == 104 and indicatorOfTypeOfLevel == 110:
            return 500233

        if table2Version == 202 and indicatorOfParameter == 93 and timeRangeIndicator == 3:
            return 500232

        if table2Version == 202 and indicatorOfParameter == 93:
            return 500231

        if table2Version == 202 and indicatorOfParameter == 92 and timeRangeIndicator == 3:
            return 500230

        if table2Version == 202 and indicatorOfParameter == 92:
            return 500229

        if table2Version == 202 and indicatorOfParameter == 91 and timeRangeIndicator == 3:
            return 500228

        if table2Version == 202 and indicatorOfParameter == 91:
            return 500227

        if table2Version == 202 and indicatorOfParameter == 86 and timeRangeIndicator == 3:
            return 500226

        if table2Version == 202 and indicatorOfParameter == 86:
            return 500225

        if table2Version == 202 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 500224

        if table2Version == 202 and indicatorOfParameter == 84:
            return 500223

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500222

        if table2Version == 202 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1:
            return 500221

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 3:
            return 500220

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 500219

        if table2Version == 202 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 500218

        if table2Version == 202 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 500217

        topLevel = h.get_l('topLevel')
        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 500216

        if table2Version == 202 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 500215

        if table2Version == 202 and indicatorOfParameter == 71:
            return 500214

        if table2Version == 202 and indicatorOfParameter == 70 and indicatorOfTypeOfLevel == 1:
            return 500213

        if table2Version == 202 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 1:
            return 500212

        if table2Version == 202 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 1:
            return 500211

        if table2Version == 202 and indicatorOfParameter == 67 and indicatorOfTypeOfLevel == 1:
            return 500210

        if table2Version == 202 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 500209

        if table2Version == 202 and indicatorOfParameter == 64 and indicatorOfTypeOfLevel == 1:
            return 500208

        if table2Version == 202 and indicatorOfParameter == 62 and indicatorOfTypeOfLevel == 1:
            return 500207

        if table2Version == 202 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1:
            return 500206

        if table2Version == 202 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 500205

        if table2Version == 202 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 1 and level == 0 and timeRangeIndicator == 0:
            return 500204

        if table2Version == 202 and indicatorOfParameter == 49 and indicatorOfTypeOfLevel == 1:
            return 500203

        if table2Version == 202 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 1:
            return 500202

        if table2Version == 202 and indicatorOfParameter == 47 and indicatorOfTypeOfLevel == 1:
            return 500201

        if table2Version == 202 and indicatorOfParameter == 46 and indicatorOfTypeOfLevel == 1:
            return 500200

        if table2Version == 202 and indicatorOfParameter == 45 and indicatorOfTypeOfLevel == 110:
            return 500199

        if table2Version == 202 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 500198

        if table2Version == 202 and indicatorOfParameter == 42 and level == 100:
            return 500197

        if table2Version == 202 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 100:
            return 500196

        if table2Version == 202 and indicatorOfParameter == 40 and indicatorOfTypeOfLevel == 100:
            return 500195

        if table2Version == 202 and indicatorOfParameter == 19:
            return 500194

        if table2Version == 202 and indicatorOfParameter == 18:
            return 500193

        if table2Version == 202 and indicatorOfParameter == 17:
            return 500192

        if table2Version == 202 and indicatorOfParameter == 10:
            return 500191

        if table2Version == 202 and indicatorOfParameter == 9:
            return 500190

        if table2Version == 202 and indicatorOfParameter == 8:
            return 500189

        if table2Version == 202 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 102:
            return 500188

        if table2Version == 202 and indicatorOfParameter == 7:
            return 500187

        if table2Version == 202 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 102:
            return 500186

        if table2Version == 202 and indicatorOfParameter == 4:
            return 500185

        if table2Version == 201 and indicatorOfParameter == 243 and indicatorOfTypeOfLevel == 1:
            return 500184

        if table2Version == 201 and indicatorOfParameter == 241 and indicatorOfTypeOfLevel == 1:
            return 500183

        if table2Version == 201 and indicatorOfParameter == 240 and indicatorOfTypeOfLevel == 1:
            return 500182

        if table2Version == 201 and indicatorOfParameter == 239:
            return 500181

        if table2Version == 201 and indicatorOfParameter == 238:
            return 500180

        if table2Version == 201 and indicatorOfParameter == 237:
            return 500179

        if table2Version == 201 and indicatorOfParameter == 236:
            return 500178

        if table2Version == 201 and indicatorOfParameter == 233 and indicatorOfTypeOfLevel == 110:
            return 500177

        if table2Version == 201 and indicatorOfParameter == 232 and indicatorOfTypeOfLevel == 110:
            return 500176

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 500175

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 500174

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 500173

        if table2Version == 201 and indicatorOfParameter == 215 and indicatorOfTypeOfLevel == 1:
            return 500172

        if table2Version == 201 and indicatorOfParameter == 212 and indicatorOfTypeOfLevel == 1:
            return 500171

        if table2Version == 201 and indicatorOfParameter == 203 and indicatorOfTypeOfLevel == 1:
            return 500170

        if table2Version == 201 and indicatorOfParameter == 200 and indicatorOfTypeOfLevel == 1:
            return 500169

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 500168

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 500167

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 500166

        if table2Version == 201 and indicatorOfParameter == 194 and indicatorOfTypeOfLevel == 100:
            return 500165

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10 and timeRangeIndicator == 2:
            return 500164

        if table2Version == 201 and indicatorOfParameter == 173 and indicatorOfTypeOfLevel == 1:
            return 500163

        if table2Version == 201 and indicatorOfParameter == 171 and indicatorOfTypeOfLevel == 1:
            return 500162

        if table2Version == 201 and indicatorOfParameter == 170 and indicatorOfTypeOfLevel == 1:
            return 500161

        if table2Version == 201 and indicatorOfParameter == 154 and indicatorOfTypeOfLevel == 109:
            return 500160

        if table2Version == 201 and indicatorOfParameter == 153 and indicatorOfTypeOfLevel == 109:
            return 500159

        if table2Version == 201 and indicatorOfParameter == 152 and indicatorOfTypeOfLevel == 109:
            return 500158

        if table2Version == 201 and indicatorOfParameter == 149 and indicatorOfTypeOfLevel == 110:
            return 500157

        if table2Version == 201 and indicatorOfParameter == 148 and indicatorOfTypeOfLevel == 109:
            return 500156

        if table2Version == 201 and indicatorOfParameter == 147:
            return 500155

        if table2Version == 201 and indicatorOfParameter == 146 and indicatorOfTypeOfLevel == 1:
            return 500154

        if table2Version == 201 and indicatorOfParameter == 145 and indicatorOfTypeOfLevel == 1:
            return 500153

        if table2Version == 201 and indicatorOfParameter == 144 and indicatorOfTypeOfLevel == 1:
            return 500152

        if table2Version == 201 and indicatorOfParameter == 143 and indicatorOfTypeOfLevel == 1:
            return 500151

        if table2Version == 201 and indicatorOfParameter == 142 and indicatorOfTypeOfLevel == 1:
            return 500150

        if table2Version == 201 and indicatorOfParameter == 141 and indicatorOfTypeOfLevel == 1:
            return 500149

        if table2Version == 201 and indicatorOfParameter == 139 and indicatorOfTypeOfLevel == 110:
            return 500148

        if table2Version == 201 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 1:
            return 500147

        if table2Version == 201 and indicatorOfParameter == 132 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500146

        if table2Version == 201 and indicatorOfParameter == 131 and indicatorOfTypeOfLevel == 1:
            return 500145

        if table2Version == 201 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 110:
            return 500144

        if table2Version == 201 and indicatorOfParameter == 129 and indicatorOfTypeOfLevel == 1:
            return 500143

        if table2Version == 201 and indicatorOfParameter == 127 and indicatorOfTypeOfLevel == 110:
            return 500142

        if table2Version == 201 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 110:
            return 500141

        if table2Version == 201 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 110:
            return 500140

        if table2Version == 201 and indicatorOfParameter == 123 and indicatorOfTypeOfLevel == 1:
            return 500139

        if table2Version == 201 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 500138

        if table2Version == 201 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500137

        if table2Version == 201 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 500136

        if table2Version == 201 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
            return 500135

        if table2Version == 201 and indicatorOfParameter == 102 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500134

        if table2Version == 201 and indicatorOfParameter == 101 and indicatorOfTypeOfLevel == 1:
            return 500133

        if table2Version == 201 and indicatorOfParameter == 100 and indicatorOfTypeOfLevel == 1:
            return 500132

        if table2Version == 201 and indicatorOfParameter == 99 and indicatorOfTypeOfLevel == 110:
            return 500131

        if table2Version == 201 and indicatorOfParameter == 89 and indicatorOfTypeOfLevel == 110:
            return 500130

        if table2Version == 201 and indicatorOfParameter == 88 and indicatorOfTypeOfLevel == 110:
            return 500129

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 500128

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 500127

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 500126

        if table2Version == 201 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 110:
            return 500125

        if table2Version == 201 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 110:
            return 500124

        if table2Version == 201 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 110:
            return 500123

        if table2Version == 201 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 110:
            return 500122

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 500121

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 500120

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 500119

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 500118

        if table2Version == 201 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 110:
            return 500117

        if table2Version == 201 and indicatorOfParameter == 59 and indicatorOfTypeOfLevel == 3:
            return 500116

        if table2Version == 201 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 2:
            return 500115

        if table2Version == 201 and indicatorOfParameter == 53:
            return 500114

        if table2Version == 201 and indicatorOfParameter == 52:
            return 500113

        if table2Version == 201 and indicatorOfParameter == 51:
            return 500112

        if table2Version == 201 and indicatorOfParameter == 44 and indicatorOfTypeOfLevel == 110:
            return 500111

        if table2Version == 201 and indicatorOfParameter == 43 and indicatorOfTypeOfLevel == 110:
            return 500110

        if table2Version == 201 and indicatorOfParameter == 42 and indicatorOfTypeOfLevel == 1:
            return 500109

        if table2Version == 201 and indicatorOfParameter == 41 and indicatorOfTypeOfLevel == 1:
            return 500108

        if table2Version == 201 and indicatorOfParameter == 40:
            return 500107

        if table2Version == 201 and indicatorOfParameter == 39 and indicatorOfTypeOfLevel == 110:
            return 500106

        if table2Version == 201 and indicatorOfParameter == 38 and indicatorOfTypeOfLevel == 1:
            return 500105

        if table2Version == 201 and indicatorOfParameter == 37 and indicatorOfTypeOfLevel == 1:
            return 500104

        if table2Version == 201 and indicatorOfParameter == 36 and indicatorOfTypeOfLevel == 110:
            return 500103

        if table2Version == 201 and indicatorOfParameter == 35 and indicatorOfTypeOfLevel == 110:
            return 500102

        if table2Version == 201 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 110:
            return 500101

        if table2Version == 201 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 500100

        if table2Version == 201 and indicatorOfParameter == 30 and indicatorOfTypeOfLevel == 110:
            return 500099

        if table2Version == 201 and indicatorOfParameter == 29 and indicatorOfTypeOfLevel == 110:
            return 500098

        if table2Version == 201 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500097

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 500096

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 500095

        if table2Version == 201 and indicatorOfParameter == 18 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500094

        if table2Version == 201 and indicatorOfParameter == 14 and indicatorOfTypeOfLevel == 110:
            return 500093

        if table2Version == 201 and indicatorOfParameter == 13 and indicatorOfTypeOfLevel == 110:
            return 500092

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500091

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500090

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500089

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500088

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500087

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500086

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 500085

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 500084

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 0:
            return 500083

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 500082

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500081

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500080

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500079

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500078

        if table2Version == 2 and indicatorOfParameter == 106:
            return 500077

        if table2Version == 2 and indicatorOfParameter == 105:
            return 500076

        if table2Version == 2 and indicatorOfParameter == 104:
            return 500075

        if table2Version == 2 and indicatorOfParameter == 103:
            return 500074

        if table2Version == 2 and indicatorOfParameter == 102:
            return 500073

        if table2Version == 2 and indicatorOfParameter == 101:
            return 500072

        if table2Version == 2 and indicatorOfParameter == 100:
            return 500071

        if table2Version == 2 and indicatorOfParameter == 92 and indicatorOfTypeOfLevel == 1:
            return 500070

        if table2Version == 2 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 500069

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and bottomLevel == 10 and topLevel == 0 and timeRangeIndicator == 4:
            return 500068

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and timeRangeIndicator == 4 and bottomLevel == 190:
            return 500067

        if table2Version == 2 and indicatorOfParameter == 90 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and timeRangeIndicator == 4 and bottomLevel == 100:
            return 500066

        if table2Version == 2 and indicatorOfParameter == 87 and indicatorOfTypeOfLevel == 1:
            return 500065

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 500064

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 10 and topLevel == 0:
            return 500063

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and bottomLevel == 190 and topLevel == 100:
            return 500062

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 500061

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 500060

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 500059

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 500058

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500057

        if table2Version == 2 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 1:
            return 500056

        if table2Version == 2 and indicatorOfParameter == 83 and indicatorOfTypeOfLevel == 1:
            return 500055

        if table2Version == 2 and indicatorOfParameter == 81 and indicatorOfTypeOfLevel == 1:
            return 500054

        if table2Version == 2 and indicatorOfParameter == 79 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500053

        if table2Version == 2 and indicatorOfParameter == 78 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500052

        if table2Version == 2 and indicatorOfParameter == 76 and indicatorOfTypeOfLevel == 1:
            return 500051

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 500050

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 500049

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 500048

        if table2Version == 2 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 110:
            return 500047

        if table2Version == 2 and indicatorOfParameter == 71 and indicatorOfTypeOfLevel == 1:
            return 500046

        if table2Version == 2 and indicatorOfParameter == 66 and indicatorOfTypeOfLevel == 1:
            return 500045

        if table2Version == 2 and indicatorOfParameter == 65 and indicatorOfTypeOfLevel == 1:
            return 500044

        if table2Version == 2 and indicatorOfParameter == 63 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500043

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 500042

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500041

        if table2Version == 2 and indicatorOfParameter == 58 and indicatorOfTypeOfLevel == 1:
            return 500040

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 4:
            return 500039

        if table2Version == 2 and indicatorOfParameter == 54 and indicatorOfTypeOfLevel == 1:
            return 500038

        if table2Version == 2 and indicatorOfParameter == 52:
            return 500037

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500036

        if table2Version == 2 and indicatorOfParameter == 51:
            return 500035

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500034

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 500033

        if table2Version == 2 and indicatorOfParameter == 40:
            return 500032

        if table2Version == 2 and indicatorOfParameter == 39:
            return 500031

        if table2Version == 2 and indicatorOfParameter == 34:
            return 500030

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500029

        if table2Version == 2 and indicatorOfParameter == 33:
            return 500028

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500027

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 110:
            return 500026

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500025

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 110:
            return 500024

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500023

        if table2Version == 2 and indicatorOfParameter == 30:
            return 500022

        if table2Version == 2 and indicatorOfParameter == 29:
            return 500021

        if table2Version == 2 and indicatorOfParameter == 28:
            return 500020

        if table2Version == 2 and indicatorOfParameter == 21 and indicatorOfTypeOfLevel == 1:
            return 500019

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 500018

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500017

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 500016

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 2:
            return 500015

        if table2Version == 2 and indicatorOfParameter == 11:
            return 500014

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 500013

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2 and timeRangeIndicator == 3:
            return 500012

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 500010

        if table2Version == 2 and indicatorOfParameter == 10 and indicatorOfTypeOfLevel == 1:
            return 500009

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 109:
            return 500008

        if table2Version == 2 and indicatorOfParameter == 8 and indicatorOfTypeOfLevel == 1:
            return 500007

        if table2Version == 2 and indicatorOfParameter == 6:
            return 500006

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 110:
            return 500005

        if table2Version == 2 and indicatorOfParameter == 6 and indicatorOfTypeOfLevel == 1:
            return 500004

        if table2Version == 2 and indicatorOfParameter == 3 and indicatorOfTypeOfLevel == 1:
            return 500003

        if table2Version == 2 and indicatorOfParameter == 2 and indicatorOfTypeOfLevel == 102:
            return 500002

        if table2Version == 2 and indicatorOfParameter == 1:
            return 500001

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 500000

    return wrapped
