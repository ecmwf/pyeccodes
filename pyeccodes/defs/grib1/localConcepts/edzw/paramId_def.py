import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')

        if table2Version == 202 and indicatorOfParameter == 39:
            return 503425

        if table2Version == 202 and indicatorOfParameter == 37:
            return 503422

        if table2Version == 202 and indicatorOfParameter == 36:
            return 503421

        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        timeRangeIndicator = h.get_l('timeRangeIndicator')

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 503349

        if table2Version == 201 and indicatorOfParameter == 196 and timeRangeIndicator == 2:
            return 503348

        if table2Version == 201 and indicatorOfParameter == 234:
            return 503347

        if table2Version == 201 and indicatorOfParameter == 235:
            return 503346

        if table2Version == 201 and indicatorOfParameter == 48 and indicatorOfTypeOfLevel == 200 and timeRangeIndicator == 2:
            return 503345

        if table2Version == 201 and indicatorOfParameter == 49 and timeRangeIndicator == 2:
            return 503344

        if table2Version == 203 and indicatorOfParameter == 37 and timeRangeIndicator == 2:
            return 503343

        if table2Version == 203 and indicatorOfParameter == 36 and timeRangeIndicator == 2:
            return 503342

        if table2Version == 203 and indicatorOfParameter == 35 and timeRangeIndicator == 2:
            return 503341

        if table2Version == 201 and indicatorOfParameter == 196:
            return 503325

        if table2Version == 202 and indicatorOfParameter == 34:
            return 503287

        if table2Version == 202 and indicatorOfParameter == 33:
            return 503286

        if table2Version == 201 and indicatorOfParameter == 196:
            return 503142

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 4:
            return 503136

        if table2Version == 201 and indicatorOfParameter == 25 and timeRangeIndicator == 3:
            return 503135

        if table2Version == 201 and indicatorOfParameter == 25:
            return 503134

        if table2Version == 202 and indicatorOfParameter == 120:
            return 503082

        if table2Version == 250 and indicatorOfParameter == 20:
            return 503078

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 3:
            return 503076

        if table2Version == 204 and indicatorOfParameter == 46:
            return 503073

        if table2Version == 203 and indicatorOfParameter == 77:
            return 503072

        if table2Version == 203 and indicatorOfParameter == 76:
            return 503071

        if table2Version == 203 and indicatorOfParameter == 75:
            return 503070

        if table2Version == 203 and indicatorOfParameter == 73:
            return 503069

        if table2Version == 203 and indicatorOfParameter == 72:
            return 503068

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 1:
            return 503066

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 1:
            return 503065

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1:
            return 503062

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1:
            return 503061

        if table2Version == 201 and indicatorOfParameter == 151:
            return 503049

        if table2Version == 203 and indicatorOfParameter == 71:
            return 502796

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1:
            return 502339

        if table2Version == 202 and indicatorOfParameter == 38:
            return 502336

        if table2Version == 202 and indicatorOfParameter == 129:
            return 502308

        if table2Version == 202 and indicatorOfParameter == 129 and timeRangeIndicator == 3:
            return 502307

        if table2Version == 254 and indicatorOfParameter == 254:
            return 500904

        if table2Version == 254 and indicatorOfParameter == 253:
            return 500903

        if table2Version == 254 and indicatorOfParameter == 252:
            return 500902

        if table2Version == 254 and indicatorOfParameter == 251:
            return 500901

        if table2Version == 254 and indicatorOfParameter == 250:
            return 500900

        if table2Version == 254 and indicatorOfParameter == 249:
            return 500899

        if table2Version == 254 and indicatorOfParameter == 248:
            return 500898

        if table2Version == 254 and indicatorOfParameter == 247:
            return 500897

        if table2Version == 254 and indicatorOfParameter == 246:
            return 500896

        if table2Version == 254 and indicatorOfParameter == 245:
            return 500895

        if table2Version == 254 and indicatorOfParameter == 244:
            return 500894

        if table2Version == 254 and indicatorOfParameter == 243:
            return 500893

        if table2Version == 254 and indicatorOfParameter == 242:
            return 500892

        if table2Version == 254 and indicatorOfParameter == 241:
            return 500891

        if table2Version == 254 and indicatorOfParameter == 240:
            return 500890

        if table2Version == 254 and indicatorOfParameter == 239:
            return 500889

        if table2Version == 254 and indicatorOfParameter == 238:
            return 500888

        if table2Version == 254 and indicatorOfParameter == 237:
            return 500887

        if table2Version == 254 and indicatorOfParameter == 236:
            return 500886

        if table2Version == 254 and indicatorOfParameter == 235:
            return 500885

        if table2Version == 254 and indicatorOfParameter == 234:
            return 500884

        if table2Version == 254 and indicatorOfParameter == 233:
            return 500883

        if table2Version == 254 and indicatorOfParameter == 232:
            return 500882

        if table2Version == 254 and indicatorOfParameter == 231:
            return 500881

        if table2Version == 254 and indicatorOfParameter == 230:
            return 500880

        if table2Version == 254 and indicatorOfParameter == 229:
            return 500879

        if table2Version == 254 and indicatorOfParameter == 228:
            return 500878

        if table2Version == 254 and indicatorOfParameter == 227:
            return 500877

        if table2Version == 254 and indicatorOfParameter == 226:
            return 500876

        if table2Version == 254 and indicatorOfParameter == 225:
            return 500875

        if table2Version == 254 and indicatorOfParameter == 224:
            return 500874

        if table2Version == 254 and indicatorOfParameter == 223:
            return 500873

        if table2Version == 254 and indicatorOfParameter == 222:
            return 500872

        if table2Version == 254 and indicatorOfParameter == 221:
            return 500871

        if table2Version == 254 and indicatorOfParameter == 220:
            return 500870

        if table2Version == 254 and indicatorOfParameter == 219:
            return 500869

        if table2Version == 254 and indicatorOfParameter == 218:
            return 500868

        if table2Version == 254 and indicatorOfParameter == 217:
            return 500867

        if table2Version == 254 and indicatorOfParameter == 216:
            return 500866

        if table2Version == 254 and indicatorOfParameter == 215:
            return 500865

        if table2Version == 254 and indicatorOfParameter == 214:
            return 500864

        if table2Version == 254 and indicatorOfParameter == 213:
            return 500863

        if table2Version == 254 and indicatorOfParameter == 212:
            return 500862

        if table2Version == 254 and indicatorOfParameter == 211:
            return 500861

        if table2Version == 254 and indicatorOfParameter == 210:
            return 500860

        if table2Version == 254 and indicatorOfParameter == 209:
            return 500859

        if table2Version == 254 and indicatorOfParameter == 208:
            return 500858

        if table2Version == 254 and indicatorOfParameter == 207:
            return 500857

        if table2Version == 254 and indicatorOfParameter == 206:
            return 500856

        if table2Version == 254 and indicatorOfParameter == 205:
            return 500855

        if table2Version == 254 and indicatorOfParameter == 204:
            return 500854

        if table2Version == 254 and indicatorOfParameter == 203:
            return 500853

        if table2Version == 254 and indicatorOfParameter == 202:
            return 500852

        if table2Version == 254 and indicatorOfParameter == 201:
            return 500851

        if table2Version == 254 and indicatorOfParameter == 200:
            return 500850

        if table2Version == 254 and indicatorOfParameter == 199:
            return 500849

        if table2Version == 254 and indicatorOfParameter == 198:
            return 500848

        if table2Version == 254 and indicatorOfParameter == 197:
            return 500847

        if table2Version == 254 and indicatorOfParameter == 196:
            return 500846

        if table2Version == 254 and indicatorOfParameter == 195:
            return 500845

        if table2Version == 254 and indicatorOfParameter == 194:
            return 500844

        if table2Version == 254 and indicatorOfParameter == 193:
            return 500843

        if table2Version == 254 and indicatorOfParameter == 192:
            return 500842

        if table2Version == 254 and indicatorOfParameter == 191:
            return 500841

        if table2Version == 254 and indicatorOfParameter == 190:
            return 500840

        if table2Version == 254 and indicatorOfParameter == 189:
            return 500839

        if table2Version == 254 and indicatorOfParameter == 188:
            return 500838

        if table2Version == 254 and indicatorOfParameter == 187:
            return 500837

        if table2Version == 254 and indicatorOfParameter == 186:
            return 500836

        if table2Version == 254 and indicatorOfParameter == 185:
            return 500835

        if table2Version == 254 and indicatorOfParameter == 184:
            return 500834

        if table2Version == 254 and indicatorOfParameter == 183:
            return 500833

        if table2Version == 254 and indicatorOfParameter == 182:
            return 500832

        if table2Version == 254 and indicatorOfParameter == 181:
            return 500831

        if table2Version == 254 and indicatorOfParameter == 180:
            return 500830

        if table2Version == 254 and indicatorOfParameter == 179:
            return 500829

        if table2Version == 254 and indicatorOfParameter == 178:
            return 500828

        if table2Version == 254 and indicatorOfParameter == 177:
            return 500827

        if table2Version == 254 and indicatorOfParameter == 176:
            return 500826

        if table2Version == 254 and indicatorOfParameter == 175:
            return 500825

        if table2Version == 254 and indicatorOfParameter == 174:
            return 500824

        if table2Version == 254 and indicatorOfParameter == 173:
            return 500823

        if table2Version == 254 and indicatorOfParameter == 172:
            return 500822

        if table2Version == 254 and indicatorOfParameter == 171:
            return 500821

        if table2Version == 254 and indicatorOfParameter == 170:
            return 500820

        if table2Version == 254 and indicatorOfParameter == 169:
            return 500819

        if table2Version == 254 and indicatorOfParameter == 168:
            return 500818

        if table2Version == 254 and indicatorOfParameter == 167:
            return 500817

        if table2Version == 254 and indicatorOfParameter == 166:
            return 500816

        if table2Version == 254 and indicatorOfParameter == 165:
            return 500815

        if table2Version == 254 and indicatorOfParameter == 164:
            return 500814

        if table2Version == 254 and indicatorOfParameter == 163:
            return 500813

        if table2Version == 254 and indicatorOfParameter == 162:
            return 500812

        if table2Version == 254 and indicatorOfParameter == 161:
            return 500811

        if table2Version == 254 and indicatorOfParameter == 160:
            return 500810

        if table2Version == 254 and indicatorOfParameter == 159:
            return 500809

        if table2Version == 254 and indicatorOfParameter == 158:
            return 500808

        if table2Version == 254 and indicatorOfParameter == 157:
            return 500807

        if table2Version == 254 and indicatorOfParameter == 156:
            return 500806

        if table2Version == 254 and indicatorOfParameter == 155:
            return 500805

        if table2Version == 254 and indicatorOfParameter == 154:
            return 500804

        if table2Version == 254 and indicatorOfParameter == 153:
            return 500803

        if table2Version == 254 and indicatorOfParameter == 152:
            return 500802

        if table2Version == 254 and indicatorOfParameter == 151:
            return 500801

        if table2Version == 254 and indicatorOfParameter == 150:
            return 500800

        if table2Version == 254 and indicatorOfParameter == 149:
            return 500799

        if table2Version == 254 and indicatorOfParameter == 148:
            return 500798

        if table2Version == 254 and indicatorOfParameter == 147:
            return 500797

        if table2Version == 254 and indicatorOfParameter == 146:
            return 500796

        if table2Version == 254 and indicatorOfParameter == 145:
            return 500795

        if table2Version == 254 and indicatorOfParameter == 144:
            return 500794

        if table2Version == 254 and indicatorOfParameter == 143:
            return 500793

        if table2Version == 254 and indicatorOfParameter == 142:
            return 500792

        if table2Version == 254 and indicatorOfParameter == 141:
            return 500791

        if table2Version == 254 and indicatorOfParameter == 140:
            return 500790

        if table2Version == 254 and indicatorOfParameter == 139:
            return 500789

        if table2Version == 254 and indicatorOfParameter == 138:
            return 500788

        if table2Version == 254 and indicatorOfParameter == 137:
            return 500787

        if table2Version == 254 and indicatorOfParameter == 136:
            return 500786

        if table2Version == 254 and indicatorOfParameter == 135:
            return 500785

        if table2Version == 254 and indicatorOfParameter == 134:
            return 500784

        if table2Version == 254 and indicatorOfParameter == 133:
            return 500783

        if table2Version == 254 and indicatorOfParameter == 132:
            return 500782

        if table2Version == 254 and indicatorOfParameter == 131:
            return 500781

        if table2Version == 254 and indicatorOfParameter == 130:
            return 500780

        if table2Version == 254 and indicatorOfParameter == 129:
            return 500779

        if table2Version == 254 and indicatorOfParameter == 128:
            return 500778

        if table2Version == 254 and indicatorOfParameter == 127:
            return 500777

        if table2Version == 254 and indicatorOfParameter == 126:
            return 500776

        if table2Version == 254 and indicatorOfParameter == 125:
            return 500775

        if table2Version == 254 and indicatorOfParameter == 124:
            return 500774

        if table2Version == 254 and indicatorOfParameter == 123:
            return 500773

        if table2Version == 254 and indicatorOfParameter == 122:
            return 500772

        if table2Version == 254 and indicatorOfParameter == 121:
            return 500771

        if table2Version == 254 and indicatorOfParameter == 120:
            return 500770

        if table2Version == 254 and indicatorOfParameter == 119:
            return 500769

        if table2Version == 254 and indicatorOfParameter == 118:
            return 500768

        if table2Version == 254 and indicatorOfParameter == 117:
            return 500767

        if table2Version == 254 and indicatorOfParameter == 116:
            return 500766

        if table2Version == 254 and indicatorOfParameter == 115:
            return 500765

        if table2Version == 254 and indicatorOfParameter == 114:
            return 500764

        if table2Version == 254 and indicatorOfParameter == 113:
            return 500763

        if table2Version == 254 and indicatorOfParameter == 112:
            return 500762

        if table2Version == 254 and indicatorOfParameter == 111:
            return 500761

        if table2Version == 254 and indicatorOfParameter == 110:
            return 500760

        if table2Version == 254 and indicatorOfParameter == 109:
            return 500759

        if table2Version == 254 and indicatorOfParameter == 108:
            return 500758

        if table2Version == 254 and indicatorOfParameter == 107:
            return 500757

        if table2Version == 254 and indicatorOfParameter == 106:
            return 500756

        if table2Version == 254 and indicatorOfParameter == 105:
            return 500755

        if table2Version == 254 and indicatorOfParameter == 104:
            return 500754

        if table2Version == 254 and indicatorOfParameter == 103:
            return 500753

        if table2Version == 254 and indicatorOfParameter == 102:
            return 500752

        if table2Version == 254 and indicatorOfParameter == 101:
            return 500751

        if table2Version == 254 and indicatorOfParameter == 100:
            return 500750

        if table2Version == 254 and indicatorOfParameter == 99:
            return 500749

        if table2Version == 254 and indicatorOfParameter == 98:
            return 500748

        if table2Version == 254 and indicatorOfParameter == 97:
            return 500747

        if table2Version == 254 and indicatorOfParameter == 96:
            return 500746

        if table2Version == 254 and indicatorOfParameter == 95:
            return 500745

        if table2Version == 254 and indicatorOfParameter == 94:
            return 500744

        if table2Version == 254 and indicatorOfParameter == 93:
            return 500743

        if table2Version == 254 and indicatorOfParameter == 92:
            return 500742

        if table2Version == 254 and indicatorOfParameter == 91:
            return 500741

        if table2Version == 254 and indicatorOfParameter == 90:
            return 500740

        if table2Version == 254 and indicatorOfParameter == 89:
            return 500739

        if table2Version == 254 and indicatorOfParameter == 88:
            return 500738

        if table2Version == 254 and indicatorOfParameter == 87:
            return 500737

        if table2Version == 254 and indicatorOfParameter == 86:
            return 500736

        if table2Version == 254 and indicatorOfParameter == 85:
            return 500735

        if table2Version == 254 and indicatorOfParameter == 84:
            return 500734

        if table2Version == 254 and indicatorOfParameter == 83:
            return 500733

        if table2Version == 254 and indicatorOfParameter == 82:
            return 500732

        if table2Version == 254 and indicatorOfParameter == 81:
            return 500731

        if table2Version == 254 and indicatorOfParameter == 80:
            return 500730

        if table2Version == 254 and indicatorOfParameter == 79:
            return 500729

        if table2Version == 254 and indicatorOfParameter == 78:
            return 500728

        if table2Version == 254 and indicatorOfParameter == 77:
            return 500727

        if table2Version == 254 and indicatorOfParameter == 76:
            return 500726

        if table2Version == 254 and indicatorOfParameter == 75:
            return 500725

        if table2Version == 254 and indicatorOfParameter == 74:
            return 500724

        if table2Version == 254 and indicatorOfParameter == 73:
            return 500723

        if table2Version == 254 and indicatorOfParameter == 72:
            return 500722

        if table2Version == 254 and indicatorOfParameter == 71:
            return 500721

        if table2Version == 254 and indicatorOfParameter == 70:
            return 500720

        if table2Version == 254 and indicatorOfParameter == 69:
            return 500719

        if table2Version == 254 and indicatorOfParameter == 68:
            return 500718

        if table2Version == 254 and indicatorOfParameter == 67:
            return 500717

        if table2Version == 254 and indicatorOfParameter == 66:
            return 500716

        if table2Version == 254 and indicatorOfParameter == 65:
            return 500715

        if table2Version == 254 and indicatorOfParameter == 64:
            return 500714

        if table2Version == 254 and indicatorOfParameter == 63:
            return 500713

        if table2Version == 254 and indicatorOfParameter == 62:
            return 500712

        if table2Version == 254 and indicatorOfParameter == 61:
            return 500711

        if table2Version == 254 and indicatorOfParameter == 60:
            return 500710

        if table2Version == 254 and indicatorOfParameter == 59:
            return 500709

        if table2Version == 254 and indicatorOfParameter == 58:
            return 500708

        if table2Version == 254 and indicatorOfParameter == 57:
            return 500707

        if table2Version == 254 and indicatorOfParameter == 56:
            return 500706

        if table2Version == 254 and indicatorOfParameter == 55:
            return 500705

        if table2Version == 254 and indicatorOfParameter == 54:
            return 500704

        if table2Version == 254 and indicatorOfParameter == 53:
            return 500703

        if table2Version == 254 and indicatorOfParameter == 52:
            return 500702

        if table2Version == 254 and indicatorOfParameter == 51:
            return 500701

        if table2Version == 254 and indicatorOfParameter == 50:
            return 500700

        if table2Version == 254 and indicatorOfParameter == 49:
            return 500699

        if table2Version == 254 and indicatorOfParameter == 48:
            return 500698

        if table2Version == 254 and indicatorOfParameter == 47:
            return 500697

        if table2Version == 254 and indicatorOfParameter == 46:
            return 500696

        if table2Version == 254 and indicatorOfParameter == 45:
            return 500695

        if table2Version == 254 and indicatorOfParameter == 44:
            return 500694

        if table2Version == 254 and indicatorOfParameter == 43:
            return 500693

        if table2Version == 254 and indicatorOfParameter == 42:
            return 500692

        if table2Version == 254 and indicatorOfParameter == 41:
            return 500691

        if table2Version == 254 and indicatorOfParameter == 40:
            return 500690

        if table2Version == 254 and indicatorOfParameter == 39:
            return 500689

        if table2Version == 254 and indicatorOfParameter == 38:
            return 500688

        if table2Version == 254 and indicatorOfParameter == 37:
            return 500687

        if table2Version == 254 and indicatorOfParameter == 36:
            return 500686

        if table2Version == 254 and indicatorOfParameter == 35:
            return 500685

        if table2Version == 254 and indicatorOfParameter == 34:
            return 500684

        if table2Version == 254 and indicatorOfParameter == 33:
            return 500683

        if table2Version == 254 and indicatorOfParameter == 32:
            return 500682

        if table2Version == 254 and indicatorOfParameter == 31:
            return 500681

        if table2Version == 254 and indicatorOfParameter == 30:
            return 500680

        if table2Version == 254 and indicatorOfParameter == 29:
            return 500679

        if table2Version == 254 and indicatorOfParameter == 28:
            return 500678

        if table2Version == 254 and indicatorOfParameter == 27:
            return 500677

        if table2Version == 254 and indicatorOfParameter == 26:
            return 500676

        if table2Version == 254 and indicatorOfParameter == 25:
            return 500675

        if table2Version == 254 and indicatorOfParameter == 24:
            return 500674

        if table2Version == 254 and indicatorOfParameter == 23:
            return 500673

        if table2Version == 254 and indicatorOfParameter == 22:
            return 500672

        if table2Version == 254 and indicatorOfParameter == 21:
            return 500671

        if table2Version == 254 and indicatorOfParameter == 20:
            return 500670

        if table2Version == 254 and indicatorOfParameter == 19:
            return 500669

        if table2Version == 254 and indicatorOfParameter == 18:
            return 500668

        if table2Version == 254 and indicatorOfParameter == 17:
            return 500667

        if table2Version == 254 and indicatorOfParameter == 16:
            return 500666

        if table2Version == 254 and indicatorOfParameter == 15:
            return 500665

        if table2Version == 254 and indicatorOfParameter == 14:
            return 500664

        if table2Version == 254 and indicatorOfParameter == 13:
            return 500663

        if table2Version == 254 and indicatorOfParameter == 12:
            return 500662

        if table2Version == 254 and indicatorOfParameter == 11:
            return 500661

        if table2Version == 254 and indicatorOfParameter == 10:
            return 500660

        if table2Version == 254 and indicatorOfParameter == 9:
            return 500659

        if table2Version == 254 and indicatorOfParameter == 8:
            return 500658

        if table2Version == 254 and indicatorOfParameter == 7:
            return 500657

        if table2Version == 254 and indicatorOfParameter == 6:
            return 500656

        if table2Version == 254 and indicatorOfParameter == 5:
            return 500655

        if table2Version == 254 and indicatorOfParameter == 4:
            return 500654

        if table2Version == 254 and indicatorOfParameter == 3:
            return 500652

        if table2Version == 254 and indicatorOfParameter == 2:
            return 500651

        if table2Version == 254 and indicatorOfParameter == 1:
            return 500650

        if table2Version == 242 and indicatorOfParameter == 252:
            return 500649

        if table2Version == 242 and indicatorOfParameter == 251:
            return 500648

        if table2Version == 242 and indicatorOfParameter == 74:
            return 500647

        if table2Version == 242 and indicatorOfParameter == 73:
            return 500646

        if table2Version == 242 and indicatorOfParameter == 72:
            return 500645

        if table2Version == 242 and indicatorOfParameter == 35:
            return 500644

        if table2Version == 242 and indicatorOfParameter == 34:
            return 500643

        if table2Version == 242 and indicatorOfParameter == 33:
            return 500640

        if table2Version == 201 and indicatorOfParameter == 90:
            return 500639

        if table2Version == 201 and indicatorOfParameter == 211:
            return 500638

        if table2Version == 201 and indicatorOfParameter == 157:
            return 500636

        if table2Version == 201 and indicatorOfParameter == 156:
            return 500635

        if table2Version == 201 and indicatorOfParameter == 155:
            return 500634

        if table2Version == 210 and indicatorOfParameter == 34:
            return 500633

        if table2Version == 210 and indicatorOfParameter == 33:
            return 500632

        if table2Version == 210 and indicatorOfParameter == 32:
            return 500631

        if table2Version == 210 and indicatorOfParameter == 31:
            return 500630

        if table2Version == 210 and indicatorOfParameter == 30:
            return 500629

        if table2Version == 210 and indicatorOfParameter == 29:
            return 500628

        if table2Version == 210 and indicatorOfParameter == 28:
            return 500627

        if table2Version == 210 and indicatorOfParameter == 27:
            return 500626

        if table2Version == 210 and indicatorOfParameter == 26:
            return 500625

        if table2Version == 210 and indicatorOfParameter == 25:
            return 500624

        if table2Version == 210 and indicatorOfParameter == 24:
            return 500623

        if table2Version == 210 and indicatorOfParameter == 23:
            return 500622

        if table2Version == 210 and indicatorOfParameter == 22:
            return 500621

        if table2Version == 210 and indicatorOfParameter == 21:
            return 500620

        if table2Version == 210 and indicatorOfParameter == 20:
            return 500619

        if table2Version == 210 and indicatorOfParameter == 19:
            return 500618

        if table2Version == 210 and indicatorOfParameter == 18:
            return 500617

        if table2Version == 210 and indicatorOfParameter == 17:
            return 500616

        if table2Version == 210 and indicatorOfParameter == 16:
            return 500615

        if table2Version == 210 and indicatorOfParameter == 15:
            return 500614

        if table2Version == 210 and indicatorOfParameter == 14:
            return 500613

        if table2Version == 210 and indicatorOfParameter == 13:
            return 500612

        if table2Version == 210 and indicatorOfParameter == 12:
            return 500611

        if table2Version == 210 and indicatorOfParameter == 11:
            return 500610

        if table2Version == 210 and indicatorOfParameter == 10:
            return 500609

        if table2Version == 210 and indicatorOfParameter == 9:
            return 500608

        if table2Version == 210 and indicatorOfParameter == 8:
            return 500607

        if table2Version == 210 and indicatorOfParameter == 7:
            return 500606

        if table2Version == 210 and indicatorOfParameter == 6:
            return 500605

        if table2Version == 210 and indicatorOfParameter == 5:
            return 500604

        if table2Version == 210 and indicatorOfParameter == 4:
            return 500603

        if table2Version == 210 and indicatorOfParameter == 3:
            return 500602

        if table2Version == 210 and indicatorOfParameter == 2:
            return 500601

        if table2Version == 210 and indicatorOfParameter == 1:
            return 500600

        if table2Version == 203 and indicatorOfParameter == 2:
            return 500592

        if table2Version == 204 and indicatorOfParameter == 71:
            return 500586

        if table2Version == 204 and indicatorOfParameter == 70:
            return 500585

        localElementNumber = h.get_l('localElementNumber')
        topLevel = h.get_l('topLevel')

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 500576

        if table2Version == 203 and indicatorOfParameter == 10:
            return 500575

        if table2Version == 202 and indicatorOfParameter == 119:
            return 500574

        if table2Version == 202 and indicatorOfParameter == 117:
            return 500573

        if table2Version == 202 and indicatorOfParameter == 101:
            return 500572

        if table2Version == 201 and indicatorOfParameter == 231:
            return 500571

        if table2Version == 201 and indicatorOfParameter == 83:
            return 500570

        if table2Version == 203 and indicatorOfParameter == 146:
            return 500567

        if table2Version == 203 and indicatorOfParameter == 128:
            return 500566

        if table2Version == 203 and indicatorOfParameter == 127:
            return 500565

        if table2Version == 203 and indicatorOfParameter == 126:
            return 500564

        if table2Version == 203 and indicatorOfParameter == 125:
            return 500563

        if table2Version == 203 and indicatorOfParameter == 123:
            return 500562

        if table2Version == 203 and indicatorOfParameter == 118:
            return 500560

        if table2Version == 203 and indicatorOfParameter == 117:
            return 500559

        if table2Version == 203 and indicatorOfParameter == 116:
            return 500558

        if table2Version == 203 and indicatorOfParameter == 115:
            return 500557

        if table2Version == 203 and indicatorOfParameter == 114:
            return 500556

        if table2Version == 203 and indicatorOfParameter == 113:
            return 500555

        if table2Version == 203 and indicatorOfParameter == 112:
            return 500554

        if table2Version == 203 and indicatorOfParameter == 111:
            return 500553

        if table2Version == 203 and indicatorOfParameter == 105:
            return 500552

        if table2Version == 203 and indicatorOfParameter == 100:
            return 500551

        if table2Version == 203 and indicatorOfParameter == 119:
            return 500550

        if table2Version == 202 and indicatorOfParameter == 134:
            return 500542

        if table2Version == 202 and indicatorOfParameter == 133:
            return 500541

        if table2Version == 203 and indicatorOfParameter == 205:
            return 500531

        if table2Version == 203 and indicatorOfParameter == 194:
            return 500530

        if table2Version == 203 and indicatorOfParameter == 193:
            return 500529

        if table2Version == 203 and indicatorOfParameter == 192:
            return 500528

        if table2Version == 203 and indicatorOfParameter == 191:
            return 500527

        level = h.get_l('level')

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 500526

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 500525

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 500524

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 500523

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 500522

        if table2Version == 203 and indicatorOfParameter == 184 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 500521

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 500520

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 500519

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 500518

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 500517

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 500516

        if table2Version == 203 and indicatorOfParameter == 183 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 500515

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 500514

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 500513

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 500512

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 500511

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 500510

        if table2Version == 203 and indicatorOfParameter == 182 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 500509

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 6:
            return 500508

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 5:
            return 500507

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 4:
            return 500506

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 3:
            return 500505

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 2:
            return 500504

        if table2Version == 203 and indicatorOfParameter == 181 and indicatorOfTypeOfLevel == 202 and level == 1:
            return 500503

        if table2Version == 201 and indicatorOfParameter == 94:
            return 500502

        if table2Version == 201 and indicatorOfParameter == 192:
            return 500501

        if table2Version == 201 and indicatorOfParameter == 91:
            return 500500

        if table2Version == 201 and indicatorOfParameter == 95:
            return 500499

        if table2Version == 201 and indicatorOfParameter == 191:
            return 500498

        if table2Version == 201 and indicatorOfParameter == 193:
            return 500497

        if table2Version == 201 and indicatorOfParameter == 194:
            return 500496

        if table2Version == 201 and indicatorOfParameter == 190:
            return 500495

        if table2Version == 201 and indicatorOfParameter == 93:
            return 500494

        if table2Version == 201 and indicatorOfParameter == 92:
            return 500493

        if table2Version == 201 and indicatorOfParameter == 97:
            return 500492

        if table2Version == 201 and indicatorOfParameter == 96:
            return 500491

        if table2Version == 202 and indicatorOfParameter == 55:
            return 500490

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500489

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500488

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500487

        if table2Version == 201 and indicatorOfParameter == 42 and timeRangeIndicator == 0:
            return 500486

        if table2Version == 201 and indicatorOfParameter == 24 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500482

        if table2Version == 201 and indicatorOfParameter == 23 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500481

        if table2Version == 201 and indicatorOfParameter == 22 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500480

        if table2Version == 203 and indicatorOfParameter == 58:
            return 500479

        if table2Version == 203 and indicatorOfParameter == 57:
            return 500478

        if table2Version == 203 and indicatorOfParameter == 61:
            return 500476

        if table2Version == 203 and indicatorOfParameter == 60:
            return 500473

        if table2Version == 203 and indicatorOfParameter == 93:
            return 500472

        if table2Version == 202 and indicatorOfParameter == 249:
            return 500471

        if table2Version == 202 and indicatorOfParameter == 247:
            return 500469

        if table2Version == 202 and indicatorOfParameter == 243:
            return 500468

        if table2Version == 202 and indicatorOfParameter == 242:
            return 500467

        if table2Version == 202 and indicatorOfParameter == 241:
            return 500466

        if table2Version == 202 and indicatorOfParameter == 240:
            return 500465

        if table2Version == 208 and indicatorOfParameter == 236:
            return 500464

        if table2Version == 208 and indicatorOfParameter == 232:
            return 500463

        if table2Version == 208 and indicatorOfParameter == 213:
            return 500462

        if table2Version == 208 and indicatorOfParameter == 212:
            return 500461

        if table2Version == 208 and indicatorOfParameter == 199:
            return 500460

        if table2Version == 208 and indicatorOfParameter == 198:
            return 500459

        if table2Version == 208 and indicatorOfParameter == 197:
            return 500458

        if table2Version == 208 and indicatorOfParameter == 191:
            return 500457

        if table2Version == 208 and indicatorOfParameter == 139:
            return 500456

        if table2Version == 208 and indicatorOfParameter == 138:
            return 500455

        if table2Version == 208 and indicatorOfParameter == 137:
            return 500454

        if table2Version == 208 and indicatorOfParameter == 136:
            return 500453

        if table2Version == 208 and indicatorOfParameter == 134:
            return 500452

        if table2Version == 208 and indicatorOfParameter == 132:
            return 500451

        if table2Version == 208 and indicatorOfParameter == 77:
            return 500450

        if table2Version == 208 and indicatorOfParameter == 75:
            return 500449

        if table2Version == 208 and indicatorOfParameter == 74:
            return 500448

        if table2Version == 208 and indicatorOfParameter == 72:
            return 500447

        if table2Version == 208 and indicatorOfParameter == 71:
            return 500446

        if table2Version == 208 and indicatorOfParameter == 70:
            return 500445

        if table2Version == 208 and indicatorOfParameter == 69:
            return 500444

        if table2Version == 208 and indicatorOfParameter == 32:
            return 500443

        if table2Version == 208 and indicatorOfParameter == 29:
            return 500442

        if table2Version == 208 and indicatorOfParameter == 26:
            return 500441

        if table2Version == 208 and indicatorOfParameter == 17:
            return 500440

        if table2Version == 208 and indicatorOfParameter == 14:
            return 500439

        if table2Version == 208 and indicatorOfParameter == 3:
            return 500438

        if table2Version == 208 and indicatorOfParameter == 1:
            return 500437

        if table2Version == 201 and indicatorOfParameter == 132 and timeRangeIndicator == 0:
            return 500436

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 1:
            return 500434

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 1:
            return 500433

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500432

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 10:
            return 500412

        if table2Version == 201 and indicatorOfParameter == 113 and timeRangeIndicator == 0:
            return 500410

        if table2Version == 201 and indicatorOfParameter == 102 and timeRangeIndicator == 0:
            return 500408

        if table2Version == 203 and indicatorOfParameter == 56 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 500403

        if table2Version == 203 and indicatorOfParameter == 55 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 500402

        if table2Version == 207 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500388

        if table2Version == 207 and indicatorOfParameter == 79:
            return 500387

        if table2Version == 207 and indicatorOfParameter == 61:
            return 500386

        if table2Version == 206 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500385

        if table2Version == 206 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 0:
            return 500384

        if table2Version == 206 and indicatorOfParameter == 79:
            return 500383

        if table2Version == 206 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 500382

        if table2Version == 206 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 500381

        if table2Version == 206 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 500380

        if table2Version == 206 and indicatorOfParameter == 71:
            return 500379

        if table2Version == 206 and indicatorOfParameter == 61:
            return 500378

        if table2Version == 206 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500377

        if table2Version == 206 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500376

        if table2Version == 206 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500375

        if table2Version == 206 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 500374

        if table2Version == 206 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 2 and level == 2:
            return 500373

        if table2Version == 206 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500372

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 500371

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500370

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 500369

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 500368

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500367

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 500366

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 500365

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 500364

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 500363

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500362

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 500361

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 500360

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500359

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 500358

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 500357

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 500356

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 500355

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500354

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 500353

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500352

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 500351

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 500350

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 500349

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 500348

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 3:
            return 500347

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500346

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 5:
            return 500345

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 4:
            return 500344

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500343

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 8:
            return 500342

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 7:
            return 500341

        if table2Version == 205 and indicatorOfParameter == 4 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 6:
            return 500340

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500339

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500338

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500337

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500336

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500335

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500334

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 1:
            return 500333

        if table2Version == 205 and indicatorOfParameter == 3 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222 and level == 2:
            return 500332

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 500331

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 500330

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 500329

        if table2Version == 205 and indicatorOfParameter == 2 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
            return 500328

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 4 and indicatorOfTypeOfLevel == 222:
            return 500327

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 3 and indicatorOfTypeOfLevel == 222:
            return 500326

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 2 and indicatorOfTypeOfLevel == 222:
            return 500325

        if table2Version == 205 and indicatorOfParameter == 1 and localElementNumber == 1 and indicatorOfTypeOfLevel == 222:
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

        if table2Version == 203 and indicatorOfParameter == 204:
            return 500307

        if table2Version == 203 and indicatorOfParameter == 203:
            return 500306

        if table2Version == 203 and indicatorOfParameter == 196:
            return 500305

        if table2Version == 203 and indicatorOfParameter == 157:
            return 500304

        if table2Version == 203 and indicatorOfParameter == 154:
            return 500303

        if table2Version == 203 and indicatorOfParameter == 140:
            return 500302

        if table2Version == 203 and indicatorOfParameter == 133 and indicatorOfTypeOfLevel == 100:
            return 500301

        if table2Version == 203 and indicatorOfParameter == 132:
            return 500300

        if table2Version == 203 and indicatorOfParameter == 131:
            return 500299

        if table2Version == 203 and indicatorOfParameter == 130 and indicatorOfTypeOfLevel == 100:
            return 500298

        if table2Version == 203 and indicatorOfParameter == 124:
            return 500297

        if table2Version == 203 and indicatorOfParameter == 109:
            return 500296

        if table2Version == 203 and indicatorOfParameter == 107:
            return 500295

        if table2Version == 203 and indicatorOfParameter == 103:
            return 500294

        if table2Version == 203 and indicatorOfParameter == 101:
            return 500293

        if table2Version == 203 and indicatorOfParameter == 99:
            return 500292

        if table2Version == 203 and indicatorOfParameter == 94 and indicatorOfTypeOfLevel == 1:
            return 500291

        if table2Version == 203 and indicatorOfParameter == 91 and indicatorOfTypeOfLevel == 1:
            return 500290

        if table2Version == 203 and indicatorOfParameter == 90:
            return 500289

        if table2Version == 203 and indicatorOfParameter == 33:
            return 500288

        if table2Version == 203 and indicatorOfParameter == 30:
            return 500287

        if table2Version == 203 and indicatorOfParameter == 29:
            return 500286

        if table2Version == 202 and indicatorOfParameter == 248:
            return 500285

        if table2Version == 202 and indicatorOfParameter == 233:
            return 500284

        if table2Version == 202 and indicatorOfParameter == 233 and timeRangeIndicator == 1:
            return 500283

        if table2Version == 202 and indicatorOfParameter == 232:
            return 500282

        if table2Version == 202 and indicatorOfParameter == 232 and timeRangeIndicator == 3:
            return 500281

        if table2Version == 202 and indicatorOfParameter == 231:
            return 500280

        if table2Version == 202 and indicatorOfParameter == 231 and timeRangeIndicator == 3:
            return 500279

        if table2Version == 202 and indicatorOfParameter == 229:
            return 500278

        if table2Version == 202 and indicatorOfParameter == 228:
            return 500277

        if table2Version == 202 and indicatorOfParameter == 227:
            return 500276

        if table2Version == 202 and indicatorOfParameter == 226:
            return 500275

        if table2Version == 202 and indicatorOfParameter == 225:
            return 500274

        if table2Version == 202 and indicatorOfParameter == 224:
            return 500273

        if table2Version == 202 and indicatorOfParameter == 223:
            return 500272

        if table2Version == 202 and indicatorOfParameter == 222:
            return 500271

        if table2Version == 202 and indicatorOfParameter == 221:
            return 500270

        if table2Version == 202 and indicatorOfParameter == 220:
            return 500269

        if table2Version == 202 and indicatorOfParameter == 219:
            return 500268

        if table2Version == 202 and indicatorOfParameter == 218:
            return 500267

        if table2Version == 202 and indicatorOfParameter == 217:
            return 500266

        if table2Version == 202 and indicatorOfParameter == 216:
            return 500265

        if table2Version == 202 and indicatorOfParameter == 215:
            return 500264

        if table2Version == 202 and indicatorOfParameter == 214:
            return 500263

        if table2Version == 202 and indicatorOfParameter == 213:
            return 500262

        if table2Version == 202 and indicatorOfParameter == 212:
            return 500261

        if table2Version == 202 and indicatorOfParameter == 211:
            return 500260

        if table2Version == 202 and indicatorOfParameter == 210:
            return 500259

        if table2Version == 202 and indicatorOfParameter == 209:
            return 500258

        if table2Version == 202 and indicatorOfParameter == 208:
            return 500257

        if table2Version == 202 and indicatorOfParameter == 207:
            return 500256

        if table2Version == 202 and indicatorOfParameter == 206:
            return 500255

        if table2Version == 202 and indicatorOfParameter == 205:
            return 500254

        if table2Version == 202 and indicatorOfParameter == 204:
            return 500253

        if table2Version == 202 and indicatorOfParameter == 203:
            return 500252

        if table2Version == 202 and indicatorOfParameter == 202:
            return 500251

        if table2Version == 202 and indicatorOfParameter == 201:
            return 500250

        if table2Version == 202 and indicatorOfParameter == 200:
            return 500249

        if table2Version == 202 and indicatorOfParameter == 199:
            return 500248

        if table2Version == 202 and indicatorOfParameter == 198:
            return 500247

        if table2Version == 202 and indicatorOfParameter == 197:
            return 500246

        if table2Version == 202 and indicatorOfParameter == 196:
            return 500245

        if table2Version == 202 and indicatorOfParameter == 195:
            return 500244

        if table2Version == 202 and indicatorOfParameter == 194:
            return 500243

        if table2Version == 202 and indicatorOfParameter == 180:
            return 500242

        if table2Version == 202 and indicatorOfParameter == 123:
            return 500241

        if table2Version == 202 and indicatorOfParameter == 122:
            return 500240

        if table2Version == 202 and indicatorOfParameter == 121:
            return 500239

        if table2Version == 202 and indicatorOfParameter == 115:
            return 500237

        if table2Version == 202 and indicatorOfParameter == 114:
            return 500236

        if table2Version == 202 and indicatorOfParameter == 113:
            return 500235

        if table2Version == 202 and indicatorOfParameter == 105:
            return 500234

        if table2Version == 202 and indicatorOfParameter == 104:
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

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 500222

        if table2Version == 202 and indicatorOfParameter == 79 and timeRangeIndicator == 3:
            return 500221

        if table2Version == 202 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 500220

        if table2Version == 202 and indicatorOfParameter == 77 and timeRangeIndicator == 3:
            return 500219

        if table2Version == 202 and indicatorOfParameter == 76:
            return 500218

        if table2Version == 202 and indicatorOfParameter == 75:
            return 500217

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 2 and indicatorOfTypeOfLevel == 112:
            return 500216

        if table2Version == 202 and indicatorOfParameter == 74 and localElementNumber == 1 and indicatorOfTypeOfLevel == 112 and topLevel == 0:
            return 500215

        if table2Version == 202 and indicatorOfParameter == 71:
            return 500214

        if table2Version == 202 and indicatorOfParameter == 70:
            return 500213

        if table2Version == 202 and indicatorOfParameter == 69:
            return 500212

        if table2Version == 202 and indicatorOfParameter == 68:
            return 500211

        if table2Version == 202 and indicatorOfParameter == 67:
            return 500210

        if table2Version == 202 and indicatorOfParameter == 65:
            return 500209

        if table2Version == 202 and indicatorOfParameter == 64:
            return 500208

        if table2Version == 202 and indicatorOfParameter == 62:
            return 500207

        if table2Version == 202 and indicatorOfParameter == 61:
            return 500206

        if table2Version == 202 and indicatorOfParameter == 57:
            return 500205

        if table2Version == 202 and indicatorOfParameter == 56:
            return 500204

        if table2Version == 202 and indicatorOfParameter == 49:
            return 500203

        if table2Version == 202 and indicatorOfParameter == 48:
            return 500202

        if table2Version == 202 and indicatorOfParameter == 47:
            return 500201

        if table2Version == 202 and indicatorOfParameter == 46:
            return 500200

        if table2Version == 202 and indicatorOfParameter == 45:
            return 500199

        if table2Version == 202 and indicatorOfParameter == 44:
            return 500198

        if table2Version == 202 and indicatorOfParameter == 42:
            return 500197

        if table2Version == 202 and indicatorOfParameter == 41:
            return 500196

        if table2Version == 202 and indicatorOfParameter == 40:
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

        if table2Version == 202 and indicatorOfParameter == 7:
            return 500187

        if table2Version == 202 and indicatorOfParameter == 4:
            return 500185

        if table2Version == 201 and indicatorOfParameter == 243:
            return 500184

        if table2Version == 201 and indicatorOfParameter == 241:
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

        if table2Version == 201 and indicatorOfParameter == 233:
            return 500177

        if table2Version == 201 and indicatorOfParameter == 232:
            return 500176

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 200:
            return 500175

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 110:
            return 500174

        if table2Version == 201 and indicatorOfParameter == 230 and indicatorOfTypeOfLevel == 1:
            return 500173

        if table2Version == 201 and indicatorOfParameter == 215:
            return 500172

        if table2Version == 201 and indicatorOfParameter == 212:
            return 500171

        if table2Version == 201 and indicatorOfParameter == 203:
            return 500170

        if table2Version == 201 and indicatorOfParameter == 200:
            return 500169

        if table2Version == 201 and indicatorOfParameter == 199 and indicatorOfTypeOfLevel == 111:
            return 500168

        if table2Version == 201 and indicatorOfParameter == 198 and indicatorOfTypeOfLevel == 111:
            return 500167

        if table2Version == 201 and indicatorOfParameter == 197 and indicatorOfTypeOfLevel == 111:
            return 500166

        if table2Version == 201 and indicatorOfParameter == 187 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500164

        if table2Version == 201 and indicatorOfParameter == 173:
            return 500163

        if table2Version == 201 and indicatorOfParameter == 171:
            return 500162

        if table2Version == 201 and indicatorOfParameter == 170:
            return 500161

        if table2Version == 201 and indicatorOfParameter == 154:
            return 500160

        if table2Version == 201 and indicatorOfParameter == 153:
            return 500159

        if table2Version == 201 and indicatorOfParameter == 152:
            return 500158

        if table2Version == 201 and indicatorOfParameter == 149:
            return 500157

        if table2Version == 201 and indicatorOfParameter == 148:
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

        if table2Version == 201 and indicatorOfParameter == 142:
            return 500150

        if table2Version == 201 and indicatorOfParameter == 141:
            return 500149

        if table2Version == 201 and indicatorOfParameter == 139:
            return 500148

        if table2Version == 201 and indicatorOfParameter == 133:
            return 500147

        if table2Version == 201 and indicatorOfParameter == 132:
            return 500146

        if table2Version == 201 and indicatorOfParameter == 131:
            return 500145

        if table2Version == 201 and indicatorOfParameter == 130:
            return 500144

        if table2Version == 201 and indicatorOfParameter == 129:
            return 500143

        if table2Version == 201 and indicatorOfParameter == 127:
            return 500142

        if table2Version == 201 and indicatorOfParameter == 125:
            return 500141

        if table2Version == 201 and indicatorOfParameter == 124:
            return 500140

        if table2Version == 201 and indicatorOfParameter == 123:
            return 500139

        if table2Version == 201 and indicatorOfParameter == 122:
            return 500138

        if table2Version == 201 and indicatorOfParameter == 113:
            return 500137

        if table2Version == 201 and indicatorOfParameter == 112:
            return 500136

        if table2Version == 201 and indicatorOfParameter == 111:
            return 500135

        if table2Version == 201 and indicatorOfParameter == 102:
            return 500134

        if table2Version == 201 and indicatorOfParameter == 101:
            return 500133

        if table2Version == 201 and indicatorOfParameter == 100:
            return 500132

        if table2Version == 201 and indicatorOfParameter == 99:
            return 500131

        if table2Version == 201 and indicatorOfParameter == 89:
            return 500130

        if table2Version == 201 and indicatorOfParameter == 88:
            return 500129

        if table2Version == 201 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 4:
            return 500128

        if table2Version == 201 and indicatorOfParameter == 84 and indicatorOfTypeOfLevel == 4:
            return 500127

        if table2Version == 201 and indicatorOfParameter == 82 and indicatorOfTypeOfLevel == 1:
            return 500126

        if table2Version == 201 and indicatorOfParameter == 79:
            return 500125

        if table2Version == 201 and indicatorOfParameter == 78:
            return 500124

        if table2Version == 201 and indicatorOfParameter == 75:
            return 500123

        if table2Version == 201 and indicatorOfParameter == 74:
            return 500122

        if table2Version == 201 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 500121

        if table2Version == 201 and indicatorOfParameter == 72 and indicatorOfTypeOfLevel == 1:
            return 500120

        if table2Version == 201 and indicatorOfParameter == 69 and indicatorOfTypeOfLevel == 3:
            return 500119

        if table2Version == 201 and indicatorOfParameter == 68 and indicatorOfTypeOfLevel == 2:
            return 500118

        if table2Version == 201 and indicatorOfParameter == 61:
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

        if table2Version == 201 and indicatorOfParameter == 44:
            return 500111

        if table2Version == 201 and indicatorOfParameter == 43:
            return 500110

        if table2Version == 201 and indicatorOfParameter == 42:
            return 500109

        if table2Version == 201 and indicatorOfParameter == 41:
            return 500108

        if table2Version == 201 and indicatorOfParameter == 40:
            return 500107

        if table2Version == 201 and indicatorOfParameter == 39:
            return 500106

        if table2Version == 201 and indicatorOfParameter == 38:
            return 500105

        if table2Version == 201 and indicatorOfParameter == 37:
            return 500104

        if table2Version == 201 and indicatorOfParameter == 36:
            return 500103

        if table2Version == 201 and indicatorOfParameter == 35:
            return 500102

        if table2Version == 201 and indicatorOfParameter == 33:
            return 500101

        if table2Version == 201 and indicatorOfParameter == 31:
            return 500100

        if table2Version == 201 and indicatorOfParameter == 30:
            return 500099

        if table2Version == 201 and indicatorOfParameter == 29:
            return 500098

        if table2Version == 201 and indicatorOfParameter == 21 and timeRangeIndicator == 0:
            return 500097

        if table2Version == 201 and indicatorOfParameter == 20 and timeRangeIndicator == 4:
            return 500096

        if table2Version == 201 and indicatorOfParameter == 19 and indicatorOfTypeOfLevel == 111 and timeRangeIndicator == 3:
            return 500095

        if table2Version == 201 and indicatorOfParameter == 18 and timeRangeIndicator == 3:
            return 500094

        if table2Version == 201 and indicatorOfParameter == 14:
            return 500093

        if table2Version == 201 and indicatorOfParameter == 13:
            return 500092

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1:
            return 500091

        if table2Version == 201 and indicatorOfParameter == 5 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500090

        if table2Version == 2 and indicatorOfParameter == 43:
            return 503350

        if table2Version == 3 and indicatorOfParameter == 149:
            return 503141

        if table2Version == 3 and indicatorOfParameter == 148:
            return 503140

        if table2Version == 3 and indicatorOfParameter == 162:
            return 503105

        if table2Version == 3 and indicatorOfParameter == 152:
            return 503104

        if table2Version == 3 and indicatorOfParameter == 151:
            return 503103

        if table2Version == 3 and indicatorOfParameter == 207:
            return 503101

        if table2Version == 3 and indicatorOfParameter == 140:
            return 503100

        if table2Version == 3 and indicatorOfParameter == 138:
            return 503099

        if table2Version == 3 and indicatorOfParameter == 40:
            return 503098

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1:
            return 503064

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1:
            return 503063

        if table2Version == 1 and indicatorOfParameter == 35:
            return 502750

        if table2Version == 1 and indicatorOfParameter == 36:
            return 502697

        if table2Version == 3 and indicatorOfParameter == 98:
            return 502696

        if table2Version == 1 and indicatorOfParameter == 98:
            return 502695

        if table2Version == 2 and indicatorOfParameter == 98:
            return 502694

        if table2Version == 2 and indicatorOfParameter == 13:
            return 502693

        if table2Version == 1 and indicatorOfParameter == 61:
            return 502692

        if table2Version == 1 and indicatorOfParameter == 71:
            return 502691

        if table2Version == 1 and indicatorOfParameter == 65:
            return 502690

        if table2Version == 1 and indicatorOfParameter == 66:
            return 502689

        if table2Version == 1 and indicatorOfParameter == 85:
            return 502688

        if table2Version == 1 and indicatorOfParameter == 86:
            return 502687

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 502686

        if table2Version == 1 and indicatorOfParameter == 127:
            return 502685

        if table2Version == 1 and indicatorOfParameter == 126:
            return 502684

        if table2Version == 1 and indicatorOfParameter == 125:
            return 502683

        if table2Version == 1 and indicatorOfParameter == 124:
            return 502682

        if table2Version == 1 and indicatorOfParameter == 120:
            return 502681

        if table2Version == 1 and indicatorOfParameter == 119:
            return 502680

        if table2Version == 1 and indicatorOfParameter == 117:
            return 502679

        if table2Version == 1 and indicatorOfParameter == 116:
            return 502678

        if table2Version == 1 and indicatorOfParameter == 115:
            return 502677

        if table2Version == 1 and indicatorOfParameter == 114:
            return 502676

        if table2Version == 1 and indicatorOfParameter == 113:
            return 502675

        if table2Version == 1 and indicatorOfParameter == 112:
            return 502674

        if table2Version == 1 and indicatorOfParameter == 111:
            return 502673

        if table2Version == 1 and indicatorOfParameter == 110:
            return 502672

        if table2Version == 1 and indicatorOfParameter == 109:
            return 502671

        if table2Version == 1 and indicatorOfParameter == 106:
            return 502668

        if table2Version == 1 and indicatorOfParameter == 105:
            return 502667

        if table2Version == 1 and indicatorOfParameter == 104:
            return 502666

        if table2Version == 1 and indicatorOfParameter == 103:
            return 502665

        if table2Version == 1 and indicatorOfParameter == 102:
            return 502664

        if table2Version == 1 and indicatorOfParameter == 101:
            return 502663

        if table2Version == 1 and indicatorOfParameter == 100:
            return 502662

        if table2Version == 1 and indicatorOfParameter == 97:
            return 502660

        if table2Version == 1 and indicatorOfParameter == 96:
            return 502659

        if table2Version == 1 and indicatorOfParameter == 95:
            return 502658

        if table2Version == 1 and indicatorOfParameter == 94:
            return 502657

        if table2Version == 1 and indicatorOfParameter == 93:
            return 502656

        if table2Version == 1 and indicatorOfParameter == 92:
            return 502655

        if table2Version == 1 and indicatorOfParameter == 91:
            return 502654

        if table2Version == 1 and indicatorOfParameter == 89:
            return 502653

        if table2Version == 1 and indicatorOfParameter == 88:
            return 502652

        if table2Version == 1 and indicatorOfParameter == 86:
            return 502651

        if table2Version == 1 and indicatorOfParameter == 82:
            return 502650

        if table2Version == 1 and indicatorOfParameter == 80:
            return 502649

        if table2Version == 1 and indicatorOfParameter == 77:
            return 502648

        if table2Version == 1 and indicatorOfParameter == 70:
            return 502647

        if table2Version == 1 and indicatorOfParameter == 69:
            return 502646

        if table2Version == 1 and indicatorOfParameter == 68:
            return 502645

        if table2Version == 1 and indicatorOfParameter == 67:
            return 502644

        if table2Version == 1 and indicatorOfParameter == 64:
            return 502643

        if table2Version == 1 and indicatorOfParameter == 63:
            return 502642

        if table2Version == 1 and indicatorOfParameter == 60:
            return 502641

        if table2Version == 1 and indicatorOfParameter == 59:
            return 502640

        if table2Version == 1 and indicatorOfParameter == 56:
            return 502639

        if table2Version == 1 and indicatorOfParameter == 55:
            return 502638

        if table2Version == 1 and indicatorOfParameter == 54:
            return 502637

        if table2Version == 1 and indicatorOfParameter == 53:
            return 502636

        if table2Version == 1 and indicatorOfParameter == 50:
            return 502635

        if table2Version == 1 and indicatorOfParameter == 49:
            return 502634

        if table2Version == 1 and indicatorOfParameter == 48:
            return 502633

        if table2Version == 1 and indicatorOfParameter == 47:
            return 502632

        if table2Version == 1 and indicatorOfParameter == 46:
            return 502631

        if table2Version == 1 and indicatorOfParameter == 45:
            return 502630

        if table2Version == 1 and indicatorOfParameter == 42:
            return 502629

        if table2Version == 1 and indicatorOfParameter == 41:
            return 502628

        if table2Version == 1 and indicatorOfParameter == 38:
            return 502627

        if table2Version == 1 and indicatorOfParameter == 37:
            return 502626

        if table2Version == 1 and indicatorOfParameter == 31:
            return 502625

        if table2Version == 1 and indicatorOfParameter == 30:
            return 502624

        if table2Version == 1 and indicatorOfParameter == 29:
            return 502623

        if table2Version == 1 and indicatorOfParameter == 28:
            return 502622

        if table2Version == 1 and indicatorOfParameter == 27:
            return 502621

        if table2Version == 1 and indicatorOfParameter == 26:
            return 502620

        if table2Version == 1 and indicatorOfParameter == 25:
            return 502619

        if table2Version == 1 and indicatorOfParameter == 24:
            return 502618

        if table2Version == 1 and indicatorOfParameter == 23:
            return 502617

        if table2Version == 1 and indicatorOfParameter == 22:
            return 502616

        if table2Version == 1 and indicatorOfParameter == 21:
            return 502615

        if table2Version == 1 and indicatorOfParameter == 20:
            return 502614

        if table2Version == 1 and indicatorOfParameter == 19:
            return 502613

        if table2Version == 1 and indicatorOfParameter == 18:
            return 502612

        if table2Version == 1 and indicatorOfParameter == 17:
            return 502611

        if table2Version == 1 and indicatorOfParameter == 16:
            return 502610

        if table2Version == 1 and indicatorOfParameter == 15:
            return 502609

        if table2Version == 1 and indicatorOfParameter == 14:
            return 502608

        if table2Version == 1 and indicatorOfParameter == 9:
            return 502607

        if table2Version == 1 and indicatorOfParameter == 8:
            return 502606

        if table2Version == 1 and indicatorOfParameter == 5:
            return 502605

        if table2Version == 1 and indicatorOfParameter == 3:
            return 502604

        if table2Version == 1 and indicatorOfParameter == 76:
            return 502603

        if table2Version == 1 and indicatorOfParameter == 62:
            return 502602

        if table2Version == 1 and indicatorOfParameter == 79:
            return 502601

        if table2Version == 1 and indicatorOfParameter == 78:
            return 502600

        if table2Version == 1 and indicatorOfParameter == 10:
            return 502599

        if table2Version == 1 and indicatorOfParameter == 90:
            return 502598

        if table2Version == 1 and indicatorOfParameter == 87:
            return 502597

        if table2Version == 1 and indicatorOfParameter == 118:
            return 502596

        if table2Version == 1 and indicatorOfParameter == 75:
            return 502595

        if table2Version == 1 and indicatorOfParameter == 74:
            return 502594

        if table2Version == 1 and indicatorOfParameter == 73:
            return 502593

        if table2Version == 1 and indicatorOfParameter == 72:
            return 502592

        if table2Version == 1 and indicatorOfParameter == 57:
            return 502591

        if table2Version == 1 and indicatorOfParameter == 84:
            return 502590

        if table2Version == 1 and indicatorOfParameter == 83:
            return 502589

        if table2Version == 1 and indicatorOfParameter == 81:
            return 502588

        if table2Version == 1 and indicatorOfParameter == 44:
            return 502587

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 502585

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 502584

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 502583

        if table2Version == 1 and indicatorOfParameter == 52:
            return 502582

        if table2Version == 1 and indicatorOfParameter == 7:
            return 502581

        if table2Version == 1 and indicatorOfParameter == 2:
            return 502579

        if table2Version == 1 and indicatorOfParameter == 121:
            return 502578

        if table2Version == 1 and indicatorOfParameter == 122:
            return 502577

        if table2Version == 1 and indicatorOfParameter == 123:
            return 502576

        if table2Version == 1 and indicatorOfParameter == 43:
            return 502575

        if table2Version == 1 and indicatorOfParameter == 39:
            return 502574

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 502573

        if table2Version == 1 and indicatorOfParameter == 51:
            return 502572

        if table2Version == 1 and indicatorOfParameter == 34:
            return 502571

        if table2Version == 1 and indicatorOfParameter == 33:
            return 502570

        if table2Version == 1 and indicatorOfParameter == 11:
            return 502569

        if table2Version == 1 and indicatorOfParameter == 6:
            return 502568

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 502567

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 502566

        if table2Version == 1 and indicatorOfParameter == 1:
            return 502565

        if table2Version == 1 and indicatorOfParameter == 32:
            return 502564

        if table2Version == 3 and indicatorOfParameter == 13:
            return 502563

        if table2Version == 1 and indicatorOfParameter == 13:
            return 502562

        if table2Version == 2 and indicatorOfParameter == 85:
            return 502560

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 502559

        if table2Version == 2 and indicatorOfParameter == 127:
            return 502558

        if table2Version == 2 and indicatorOfParameter == 126:
            return 502557

        if table2Version == 2 and indicatorOfParameter == 125:
            return 502556

        if table2Version == 2 and indicatorOfParameter == 124:
            return 502555

        if table2Version == 2 and indicatorOfParameter == 120:
            return 502554

        if table2Version == 2 and indicatorOfParameter == 119:
            return 502553

        if table2Version == 2 and indicatorOfParameter == 116:
            return 502552

        if table2Version == 2 and indicatorOfParameter == 115:
            return 502551

        if table2Version == 2 and indicatorOfParameter == 114:
            return 502550

        if table2Version == 2 and indicatorOfParameter == 113:
            return 502549

        if table2Version == 2 and indicatorOfParameter == 112:
            return 502548

        if table2Version == 2 and indicatorOfParameter == 111:
            return 502547

        if table2Version == 2 and indicatorOfParameter == 110:
            return 502546

        if table2Version == 2 and indicatorOfParameter == 109:
            return 502545

        if table2Version == 2 and indicatorOfParameter == 99:
            return 502542

        if table2Version == 2 and indicatorOfParameter == 97:
            return 502540

        if table2Version == 2 and indicatorOfParameter == 96:
            return 502539

        if table2Version == 2 and indicatorOfParameter == 95:
            return 502538

        if table2Version == 2 and indicatorOfParameter == 94:
            return 502537

        if table2Version == 2 and indicatorOfParameter == 93:
            return 502536

        if table2Version == 2 and indicatorOfParameter == 86:
            return 502535

        if table2Version == 2 and indicatorOfParameter == 82:
            return 502534

        if table2Version == 2 and indicatorOfParameter == 77:
            return 502533

        if table2Version == 2 and indicatorOfParameter == 70:
            return 502532

        if table2Version == 2 and indicatorOfParameter == 69:
            return 502531

        if table2Version == 2 and indicatorOfParameter == 68:
            return 502530

        if table2Version == 2 and indicatorOfParameter == 67:
            return 502529

        if table2Version == 2 and indicatorOfParameter == 64:
            return 502528

        if table2Version == 2 and indicatorOfParameter == 63:
            return 502527

        if table2Version == 2 and indicatorOfParameter == 60:
            return 502526

        if table2Version == 2 and indicatorOfParameter == 59:
            return 502525

        if table2Version == 2 and indicatorOfParameter == 56:
            return 502524

        if table2Version == 2 and indicatorOfParameter == 55:
            return 502523

        if table2Version == 2 and indicatorOfParameter == 53:
            return 502522

        if table2Version == 2 and indicatorOfParameter == 50:
            return 502521

        if table2Version == 2 and indicatorOfParameter == 49:
            return 502520

        if table2Version == 2 and indicatorOfParameter == 48:
            return 502519

        if table2Version == 2 and indicatorOfParameter == 47:
            return 502518

        if table2Version == 2 and indicatorOfParameter == 46:
            return 502517

        if table2Version == 2 and indicatorOfParameter == 45:
            return 502516

        if table2Version == 2 and indicatorOfParameter == 42:
            return 502515

        if table2Version == 2 and indicatorOfParameter == 38:
            return 502514

        if table2Version == 3 and indicatorOfParameter == 37:
            return 502513

        if table2Version == 2 and indicatorOfParameter == 37:
            return 502512

        if table2Version == 2 and indicatorOfParameter == 27:
            return 502511

        if table2Version == 2 and indicatorOfParameter == 26:
            return 502510

        if table2Version == 2 and indicatorOfParameter == 25:
            return 502509

        if table2Version == 2 and indicatorOfParameter == 24:
            return 502508

        if table2Version == 2 and indicatorOfParameter == 23:
            return 502507

        if table2Version == 2 and indicatorOfParameter == 22:
            return 502506

        if table2Version == 2 and indicatorOfParameter == 20:
            return 502505

        if table2Version == 2 and indicatorOfParameter == 18:
            return 502504

        if table2Version == 2 and indicatorOfParameter == 17:
            return 502503

        if table2Version == 2 and indicatorOfParameter == 16:
            return 502502

        if table2Version == 2 and indicatorOfParameter == 15:
            return 502501

        if table2Version == 3 and indicatorOfParameter == 14:
            return 502500

        if table2Version == 2 and indicatorOfParameter == 14:
            return 502499

        if table2Version == 3 and indicatorOfParameter == 9:
            return 502498

        if table2Version == 2 and indicatorOfParameter == 9:
            return 502497

        if table2Version == 2 and indicatorOfParameter == 8:
            return 502496

        if table2Version == 2 and indicatorOfParameter == 90:
            return 502495

        if table2Version == 2 and indicatorOfParameter == 118:
            return 502494

        if table2Version == 2 and indicatorOfParameter == 75:
            return 502493

        if table2Version == 2 and indicatorOfParameter == 74:
            return 502492

        if table2Version == 2 and indicatorOfParameter == 73:
            return 502491

        if table2Version == 2 and indicatorOfParameter == 57:
            return 502490

        if table2Version == 2 and indicatorOfParameter == 121:
            return 502488

        if table2Version == 2 and indicatorOfParameter == 122:
            return 502487

        if table2Version == 2 and indicatorOfParameter == 123:
            return 502486

        if table2Version == 3 and indicatorOfParameter == 61:
            return 502485

        if table2Version == 3 and indicatorOfParameter == 71:
            return 502484

        if table2Version == 3 and indicatorOfParameter == 65:
            return 502483

        if table2Version == 3 and indicatorOfParameter == 66:
            return 502482

        if table2Version == 3 and indicatorOfParameter == 85:
            return 502481

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 502480

        if table2Version == 3 and indicatorOfParameter == 127:
            return 502479

        if table2Version == 3 and indicatorOfParameter == 126:
            return 502478

        if table2Version == 3 and indicatorOfParameter == 125:
            return 502477

        if table2Version == 3 and indicatorOfParameter == 124:
            return 502476

        if table2Version == 3 and indicatorOfParameter == 120:
            return 502475

        if table2Version == 3 and indicatorOfParameter == 119:
            return 502474

        if table2Version == 3 and indicatorOfParameter == 117:
            return 502473

        if table2Version == 3 and indicatorOfParameter == 116:
            return 502472

        if table2Version == 3 and indicatorOfParameter == 115:
            return 502471

        if table2Version == 3 and indicatorOfParameter == 114:
            return 502470

        if table2Version == 3 and indicatorOfParameter == 113:
            return 502469

        if table2Version == 3 and indicatorOfParameter == 112:
            return 502468

        if table2Version == 3 and indicatorOfParameter == 111:
            return 502467

        if table2Version == 3 and indicatorOfParameter == 110:
            return 502466

        if table2Version == 3 and indicatorOfParameter == 109:
            return 502465

        if table2Version == 3 and indicatorOfParameter == 106:
            return 502462

        if table2Version == 3 and indicatorOfParameter == 105:
            return 502461

        if table2Version == 3 and indicatorOfParameter == 104:
            return 502460

        if table2Version == 3 and indicatorOfParameter == 103:
            return 502459

        if table2Version == 3 and indicatorOfParameter == 102:
            return 502458

        if table2Version == 3 and indicatorOfParameter == 101:
            return 502457

        if table2Version == 3 and indicatorOfParameter == 100:
            return 502456

        if table2Version == 3 and indicatorOfParameter == 99:
            return 502455

        if table2Version == 3 and indicatorOfParameter == 97:
            return 502454

        if table2Version == 3 and indicatorOfParameter == 96:
            return 502453

        if table2Version == 3 and indicatorOfParameter == 95:
            return 502452

        if table2Version == 3 and indicatorOfParameter == 94:
            return 502451

        if table2Version == 3 and indicatorOfParameter == 93:
            return 502450

        if table2Version == 3 and indicatorOfParameter == 92:
            return 502449

        if table2Version == 3 and indicatorOfParameter == 91:
            return 502448

        if table2Version == 3 and indicatorOfParameter == 89:
            return 502447

        if table2Version == 3 and indicatorOfParameter == 88:
            return 502446

        if table2Version == 3 and indicatorOfParameter == 86:
            return 502445

        if table2Version == 3 and indicatorOfParameter == 82:
            return 502444

        if table2Version == 3 and indicatorOfParameter == 80:
            return 502443

        if table2Version == 3 and indicatorOfParameter == 77:
            return 502442

        if table2Version == 3 and indicatorOfParameter == 70:
            return 502441

        if table2Version == 3 and indicatorOfParameter == 69:
            return 502440

        if table2Version == 3 and indicatorOfParameter == 68:
            return 502439

        if table2Version == 3 and indicatorOfParameter == 67:
            return 502438

        if table2Version == 3 and indicatorOfParameter == 64:
            return 502437

        if table2Version == 3 and indicatorOfParameter == 63:
            return 502436

        if table2Version == 3 and indicatorOfParameter == 60:
            return 502435

        if table2Version == 3 and indicatorOfParameter == 59:
            return 502434

        if table2Version == 3 and indicatorOfParameter == 56:
            return 502433

        if table2Version == 3 and indicatorOfParameter == 55:
            return 502432

        if table2Version == 3 and indicatorOfParameter == 54:
            return 502431

        if table2Version == 3 and indicatorOfParameter == 53:
            return 502430

        if table2Version == 3 and indicatorOfParameter == 50:
            return 502429

        if table2Version == 3 and indicatorOfParameter == 49:
            return 502428

        if table2Version == 3 and indicatorOfParameter == 48:
            return 502427

        if table2Version == 3 and indicatorOfParameter == 47:
            return 502426

        if table2Version == 2 and indicatorOfParameter == 46:
            return 502425

        if table2Version == 2 and indicatorOfParameter == 45:
            return 502424

        if table2Version == 3 and indicatorOfParameter == 42:
            return 502423

        if table2Version == 3 and indicatorOfParameter == 41:
            return 502422

        if table2Version == 3 and indicatorOfParameter == 38:
            return 502421

        if table2Version == 3 and indicatorOfParameter == 31:
            return 502420

        if table2Version == 3 and indicatorOfParameter == 30:
            return 502419

        if table2Version == 3 and indicatorOfParameter == 29:
            return 502418

        if table2Version == 3 and indicatorOfParameter == 28:
            return 502417

        if table2Version == 3 and indicatorOfParameter == 27:
            return 502416

        if table2Version == 3 and indicatorOfParameter == 26:
            return 502415

        if table2Version == 3 and indicatorOfParameter == 25:
            return 502414

        if table2Version == 3 and indicatorOfParameter == 24:
            return 502413

        if table2Version == 3 and indicatorOfParameter == 23:
            return 502412

        if table2Version == 3 and indicatorOfParameter == 22:
            return 502411

        if table2Version == 3 and indicatorOfParameter == 21:
            return 502410

        if table2Version == 3 and indicatorOfParameter == 20:
            return 502409

        if table2Version == 3 and indicatorOfParameter == 19:
            return 502408

        if table2Version == 3 and indicatorOfParameter == 18:
            return 502407

        if table2Version == 3 and indicatorOfParameter == 17:
            return 502406

        if table2Version == 3 and indicatorOfParameter == 16:
            return 502405

        if table2Version == 3 and indicatorOfParameter == 15:
            return 502404

        if table2Version == 3 and indicatorOfParameter == 8:
            return 502403

        if table2Version == 3 and indicatorOfParameter == 5:
            return 502402

        if table2Version == 3 and indicatorOfParameter == 3:
            return 502401

        if table2Version == 3 and indicatorOfParameter == 123:
            return 502400

        if table2Version == 3 and indicatorOfParameter == 118:
            return 502399

        if table2Version == 3 and indicatorOfParameter == 12:
            return 502398

        if table2Version == 2 and indicatorOfParameter == 12:
            return 502397

        if table2Version == 1 and indicatorOfParameter == 12:
            return 502396

        if table2Version == 3 and indicatorOfParameter == 76:
            return 502395

        if table2Version == 3 and indicatorOfParameter == 62:
            return 502394

        if table2Version == 3 and indicatorOfParameter == 79:
            return 502393

        if table2Version == 3 and indicatorOfParameter == 78:
            return 502392

        if table2Version == 3 and indicatorOfParameter == 10:
            return 502391

        if table2Version == 3 and indicatorOfParameter == 90:
            return 502390

        if table2Version == 3 and indicatorOfParameter == 87:
            return 502389

        if table2Version == 3 and indicatorOfParameter == 75:
            return 502388

        if table2Version == 3 and indicatorOfParameter == 74:
            return 502387

        if table2Version == 3 and indicatorOfParameter == 73:
            return 502386

        if table2Version == 3 and indicatorOfParameter == 72:
            return 502385

        if table2Version == 3 and indicatorOfParameter == 57:
            return 502384

        if table2Version == 3 and indicatorOfParameter == 84:
            return 502383

        if table2Version == 3 and indicatorOfParameter == 83:
            return 502382

        if table2Version == 3 and indicatorOfParameter == 81:
            return 502381

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 502379

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 502378

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 502377

        if table2Version == 3 and indicatorOfParameter == 52:
            return 502376

        if table2Version == 3 and indicatorOfParameter == 7:
            return 502375

        if table2Version == 3 and indicatorOfParameter == 44:
            return 502374

        if table2Version == 3 and indicatorOfParameter == 2:
            return 502373

        if table2Version == 3 and indicatorOfParameter == 121:
            return 502372

        if table2Version == 3 and indicatorOfParameter == 122:
            return 502371

        if table2Version == 3 and indicatorOfParameter == 43:
            return 502370

        if table2Version == 3 and indicatorOfParameter == 39:
            return 502369

        if table2Version == 3 and indicatorOfParameter == 51:
            return 502368

        if table2Version == 3 and indicatorOfParameter == 34:
            return 502367

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 502366

        if table2Version == 3 and indicatorOfParameter == 33:
            return 502365

        if table2Version == 3 and indicatorOfParameter == 11:
            return 502364

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 502363

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 502362

        if table2Version == 3 and indicatorOfParameter == 6:
            return 502361

        if table2Version == 3 and indicatorOfParameter == 4:
            return 502360

        if table2Version == 1 and indicatorOfParameter == 4:
            return 502359

        if table2Version == 3 and indicatorOfParameter == 1:
            return 502358

        if table2Version == 3 and indicatorOfParameter == 32:
            return 502357

        if table2Version == 3 and indicatorOfParameter == 36:
            return 502356

        if table2Version == 3 and indicatorOfParameter == 35:
            return 502355

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 502350

        if table2Version == 2 and indicatorOfParameter == 36:
            return 502335

        if table2Version == 2 and indicatorOfParameter == 35:
            return 502334

        if table2Version == 2 and indicatorOfParameter == 88:
            return 502333

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1:
            return 502318

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1:
            return 502317

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 1:
            return 500905

        if table2Version == 2 and indicatorOfParameter == 19:
            return 500642

        if table2Version == 2 and indicatorOfParameter == 117:
            return 500593

        if table2Version == 2 and indicatorOfParameter == 5:
            return 500590

        if table2Version == 1 and indicatorOfParameter == 99:
            return 500588

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 500583

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 1 and level == 2:
            return 500582

        bottomLevel = h.get_l('bottomLevel')

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 7 and bottomLevel == 50:
            return 500581

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 7:
            return 500580

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 112:
            return 500579

        if table2Version == 2 and indicatorOfParameter == 44:
            return 500569

        if table2Version == 2 and indicatorOfParameter == 7:
            return 500568

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 5:
            return 500547

        if table2Version == 2 and indicatorOfParameter == 89:
            return 500545

        if table2Version == 2 and indicatorOfParameter == 4:
            return 500544

        if table2Version == 2 and indicatorOfParameter == 43:
            return 500543

        if table2Version == 2 and indicatorOfParameter == 41:
            return 500477

        if table2Version == 2 and indicatorOfParameter == 80:
            return 500475

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500431

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500430

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500429

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500428

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 1:
            return 500425

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 1:
            return 500424

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 1:
            return 500423

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500422

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 1:
            return 500421

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 500420

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 1:
            return 500419

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 500418

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 0 and level == 2:
            return 500417

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 0:
            return 500416

        if table2Version == 2 and indicatorOfParameter == 78 and timeRangeIndicator == 0:
            return 500411

        if table2Version == 2 and indicatorOfParameter == 79 and timeRangeIndicator == 0:
            return 500409

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 0:
            return 500404

        if table2Version == 2 and indicatorOfParameter == 61 and timeRangeIndicator == 5:
            return 500401

        if table2Version == 2 and indicatorOfParameter == 125 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500089

        if table2Version == 2 and indicatorOfParameter == 124 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500088

        if table2Version == 2 and indicatorOfParameter == 122 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500087

        if table2Version == 2 and indicatorOfParameter == 121 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500086

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8:
            return 500085

        if table2Version == 2 and indicatorOfParameter == 114 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 500084

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8:
            return 500083

        if table2Version == 2 and indicatorOfParameter == 113 and indicatorOfTypeOfLevel == 8 and timeRangeIndicator == 3:
            return 500082

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1:
            return 500081

        if table2Version == 2 and indicatorOfParameter == 112 and indicatorOfTypeOfLevel == 1 and timeRangeIndicator == 3:
            return 500080

        if table2Version == 2 and indicatorOfParameter == 111 and indicatorOfTypeOfLevel == 1:
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

        if table2Version == 2 and indicatorOfParameter == 92:
            return 500070

        if table2Version == 2 and indicatorOfParameter == 91:
            return 500069

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 0:
            return 500068

        if table2Version == 2 and indicatorOfParameter == 90 and topLevel == 10:
            return 500066

        if table2Version == 2 and indicatorOfParameter == 87:
            return 500065

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 10 and bottomLevel == 100:
            return 500064

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 0 and bottomLevel == 10:
            return 500063

        if table2Version == 2 and indicatorOfParameter == 86 and indicatorOfTypeOfLevel == 112 and topLevel == 100 and bottomLevel == 190:
            return 500062

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111:
            return 500061

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 9:
            return 500060

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 41:
            return 500059

        if table2Version == 2 and indicatorOfParameter == 85 and indicatorOfTypeOfLevel == 111 and level == 36:
            return 500058

        if table2Version == 2 and indicatorOfParameter == 84 and timeRangeIndicator == 3:
            return 500057

        if table2Version == 2 and indicatorOfParameter == 84:
            return 500056

        if table2Version == 2 and indicatorOfParameter == 83:
            return 500055

        if table2Version == 2 and indicatorOfParameter == 81:
            return 500054

        if table2Version == 2 and indicatorOfParameter == 79:
            return 500053

        if table2Version == 2 and indicatorOfParameter == 78:
            return 500052

        if table2Version == 2 and indicatorOfParameter == 76:
            return 500051

        if table2Version == 2 and indicatorOfParameter == 75 and indicatorOfTypeOfLevel == 1:
            return 500050

        if table2Version == 2 and indicatorOfParameter == 74 and indicatorOfTypeOfLevel == 1:
            return 500049

        if table2Version == 2 and indicatorOfParameter == 73 and indicatorOfTypeOfLevel == 1:
            return 500048

        if table2Version == 2 and indicatorOfParameter == 72:
            return 500047

        if table2Version == 2 and indicatorOfParameter == 71:
            return 500046

        if table2Version == 2 and indicatorOfParameter == 66:
            return 500045

        if table2Version == 2 and indicatorOfParameter == 65:
            return 500044

        if table2Version == 2 and indicatorOfParameter == 63 and timeRangeIndicator == 4:
            return 500043

        if table2Version == 2 and indicatorOfParameter == 62 and timeRangeIndicator == 4:
            return 500042

        if table2Version == 2 and indicatorOfParameter == 61:
            return 500041

        if table2Version == 2 and indicatorOfParameter == 58:
            return 500040

        if table2Version == 2 and indicatorOfParameter == 57 and indicatorOfTypeOfLevel == 1:
            return 500039

        if table2Version == 2 and indicatorOfParameter == 54:
            return 500038

        if table2Version == 2 and indicatorOfParameter == 52:
            return 500037

        if table2Version == 2 and indicatorOfParameter == 52 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500036

        if table2Version == 2 and indicatorOfParameter == 51:
            return 500035

        if table2Version == 2 and indicatorOfParameter == 51 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500034

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

        if table2Version == 2 and indicatorOfParameter == 32:
            return 500026

        if table2Version == 2 and indicatorOfParameter == 32 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500025

        if table2Version == 2 and indicatorOfParameter == 31:
            return 500024

        if table2Version == 2 and indicatorOfParameter == 31 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 500023

        if table2Version == 2 and indicatorOfParameter == 30:
            return 500022

        if table2Version == 2 and indicatorOfParameter == 29:
            return 500021

        if table2Version == 2 and indicatorOfParameter == 28:
            return 500020

        if table2Version == 2 and indicatorOfParameter == 21:
            return 500019

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 500018

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500017

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500016

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500015

        if table2Version == 2 and indicatorOfParameter == 11:
            return 500014

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 500013

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and timeRangeIndicator == 3 and level == 2:
            return 500012

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 500011

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 1:
            return 500010

        if table2Version == 2 and indicatorOfParameter == 10:
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

        if table2Version == 2 and indicatorOfParameter == 2:
            return 500002

        if table2Version == 2 and indicatorOfParameter == 1:
            return 500001

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 500000

    return wrapped
