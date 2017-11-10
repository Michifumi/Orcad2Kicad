# -*- coding: utf-8 -*-
import re
import os
import pcbnew



def File_NetOut(f, netno, name, net, total) :
    for i, w in enumerate(net) :
        if i > 0 :
            f.write(', ')
        if (i // 8) > 0 and (i % 8) == 0 :
            f.write('\n')
        f.write(w)
    f.write('\n')
    str = "#####  NET No.{0:6d},   Name:{1:10s},   Parts:{2:6d},   Total:{3:8d}    #####\n".format(netno, name, len(net), total)
    f.write(str)


#************************************************************************************************************************************************
#/TEC      R015(2) C411(2) C308(1) T14(1);
#/S5V      R328(2) C325(2) J3(22) C326(2) R325(2) R323(2) R011(1) C006(2),
#          Q001(2);
#/A5VL     C328(1) C306(2) U301(106) U301(41) U301(70) U301(55) U301(128) C302(2),
#          U301(18) C310(1) C021(1) U301(29) C309(1) U301(107) U301(99) U301(144),
#          U301(113) U301(145) C305(1) U301(81) U301(114) U301(92) C301(1) U301(3),
#          SHORT7(2);
#/RFI      C332(2) U309(2) U301(91);
#
# FORMAT : Calay
def Calay_Read(rfname, wfname = 'NET.TXT') :

    f = open(wfname, 'w')

    netname = []; netlist = []; net = []
    name = ''; n = 0; t = 0
    for line in open(rfname, 'r'):
        f.write(line)
        line = line.replace('\n', '')        #改行削除
        line = line.replace('\r', '')        #改行削除
        #print(line)
        words = re.split(" +", line)         #１行をスペースで分離
        #print(words)
        if n == 0 :                          #ネット名前を記憶
            name = words[0].strip()

        if len(words) > 0 :                  #ネットが存在する時        
            w = words[-1]
            if w == '' :
                EOF = 1
            elif w[-1] == ';' :              #最後の文字が';'の時
                words[-1] = w[:-1]           #';'削除の上、再登録
                for w in words[1:] :         #ネットを記憶
                    w = w.strip()
                    if len(w) > 0 :
                        net.append(w)
                EOF = 1
                #print(name)
                #print(net)
                #print()
            elif w[-1] == ',' :             #最後の文字が','の時
                words[-1] = w[:-1]          #','削除の上、再登録
                for w in words[1:] :        #ネットを記憶
                    w = w.strip()
                    if len(w) > 0 :
                        net.append(w)
                EOF = 0
            else :
                EOF = 1
        else :
            EOF = 1

        
        if EOF == 1 :
            if name != '' and len(net) > 0 : 
                net.sort()                  #ネットリストの並べ替え
                netname.append(name)
                netlist.append(net)

                t += len(net)
                File_NetOut(f, len(netname), name, net, t)

            net = []; name = ''
            n = 0
        else :
            n += 1

    f.close()
    return (netname, netlist, rfname)


#Cmp-Mod V01 Created by PcbNew   date = 2017年10月30日 21時24分46秒
#
#BeginCmp
#TimeStamp = 59F71BA6
#Path = /A400
#Reference = BT1;
#ValeurCmp = BT:2;
#IdModule  = Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm;
#EndCmp
def Cmp_Read(rfname) :

    data = []
    n = 0; lock = 0
    for line in open(rfname, 'r'):
        #print(line)
        line = line.replace('\n', '')        #改行削除
        line = line.replace('\r', '')        #改行削除
        n += 1
        if n == 1 :                        #ヘッダーチェック
            if line[0:7] != 'Cmp-Mod' :
                break
            else :
                continue
    
        if lock == 0 :                       #「BeginCmp」まで読み飛ばし処理
            if line[0:8] == 'BeginCmp' :
                Ref = ''; Val = ''; Fot = ''; Tim = ''; Pth = ''
                lock = 1
            continue
        else :                               #「EndCmp」までの部品情報を記録
            if line[0:12] == 'Reference = ' and line[-1] == ';' :
                Ref = line[12:-1]
                continue
            elif line[0:12] == 'ValeurCmp = ' and line[-1] == ';' :
                Val = line[12:-1]
                continue
            elif line[0:12] == 'IdModule  = ' and line[-1] == ';' :
                Fot = line[12:-1]
                continue
            elif line[0:6] == 'EndCmp' :
                data.append([Ref, Val, Fot, Tim, Pth])
                lock = 0
                continue
            elif line[0:12] == 'TimeStamp = ' :
                Tim = line[12:]
                continue
            elif line[0:7] == 'Path = ' :
                Pth = line[7:]
		if Pth[0] == '/' :
		    Pth = Pth[1:]
                continue
                  
    return data



#************************************************************************************************************************************************
#(export (version D)
#  (components
#    (comp (ref C1)
#      (value C_Small)
#      (footprint Capacitors_SMD:C_0603_HandSoldering)
#      (libsource (lib device) (part C_Small))
#      (sheetpath (names /) (tstamps /))
#      (tstamp A407))
#    (comp (ref R1)
#      (value R_Small)
#      (footprint Resistors_SMD:R_0603_HandSoldering)
#      (libsource (lib device) (part R_Small))
#      (sheetpath (names /) (tstamps /))
#      (tstamp A4B3))
#    (comp (ref L1)
#      (value L_Small)
#      (footprint Inductors_SMD:L_0603_HandSoldering)
#      (libsource (lib device) (part L_Small))
#      (sheetpath (names /) (tstamps /))
#      (tstamp A53E)))
#  (nets
#    (net (code 1) (name "Net-(L1-Pad1)")
#      (node (ref R1) (pin 1))
#      (node (ref L1) (pin 1)))
#    (net (code 2) (name "Net-(C1-Pad1)")
#      (node (ref C1) (pin 1))
#      (node (ref R1) (pin 2)))
#    (net (code 3) (name "Net-(C1-Pad2)")
#      (node (ref C1) (pin 2))
#      (node (ref L1) (pin 2)))))
#
# FORMAT : KiCAD
def Kicad_Write(netlist, wfname = 'kicad.net', rfname = '') :
    TSTAMP_OFFSET = 0xA400		#タイムスタンプオフセット値

    
    f = open(wfname, 'w')
    f.write("(export (version D)\n")


    if rfname != '' and os.path.isfile(rfname) :
        import csv
        #Reference, Value, Footprint, Datasheet
        #"C1","C_Small","Capacitors_SMD:C_0603_HandSoldering",""
        #"R1","R_Small","Resistors_SMD:R_0603_HandSoldering",""
        #"L1","L_Small","Inductors_SMD:L_0603_HandSoldering",""
      
	#csvファイルから部品情報を読み取る
        data = []
        with open(rfname, 'r') as fcsv:
            reader = csv.reader(fcsv)       # readerオブジェクトを作成
            header = next(reader)           # 最初の一行をヘッダーとして取得
            #print(header)                  # ヘッダーを表示
            if (header[0].strip() == 'Reference') and (header[1].strip() == 'Value') and (header[2].strip() == 'Footprint') :
                # 行ごとのリストを処理する
                for row in reader:
                    data.append(row)        # １行ずつデータ追加

        #print(data)

	#部品情報データを書き込む
        data_n = len(data); data_n -= 1
        for i, w in enumerate(data) :
            value =  w[1].decode('utf8')
            j = value.find('(')		    #　value値にある"("以降の文字列削除
            if j >= 0 :
	        value = value[0:j]
            f.write("  (components\n")
            f.write('    (comp (ref {0:s})\n'.format( w[0].decode('utf8') ))
            f.write('      (value {0:s})\n'.format( value ))
            f.write('      (footprint {0:s})\n'.format( w[2].decode('utf8') ))
            f.write('      (libsource (lib device) (part ""))\n')           
            f.write('      (sheetpath (names /) (tstamps /))\n')            
            f.write('      (tstamp {0:X}))'.format(i + TSTAMP_OFFSET))     
            if i >= data_n :
                f.write(")")              
            f.write("\n")
    
    else :
	#コンポーネンツファイルが存在するならば、データを読み取る
	cmp = []
	cfname = wfname.replace('.net','.cmp')
	if os.path.isfile(cfname) :
	    cmp = Cmp_Read(cfname)

	#コンポーネンツファイルの「Path」の最大値を求める
	ptn_max = 0
	for w in cmp :
	    i = int(w[4], 16)
	    if i >= TSTAMP_OFFSET :
		i -= TSTAMP_OFFSET		#オフセット値を引く
	    if i > ptn_max :
		ptn_max = i

	#ネットリストから使われている部番を調べる
        data = []
        for net in netlist[1] :
            for w in net :
                words = w.split("(")
                if (words[0] in data) == False :
                    data.append(words[0])

	#各部番の部品情報データを書き込む
	dfp_n = 0
        data.sort()
        data_n = len(data); data_n -= 1
        for i, w in enumerate(data) :

	    #部番wがコンポーネンツデータがあるならば、そのデータを使って処理
	    cmpf = False
	    for w1 in cmp :
		if w1[0] == w :
		    cmpf = True    
		    #コンポーネンツデータで部品情報データを書き込む            
        	    f.write("  (components\n")
            	    f.write('    (comp (ref {0:s})\n'.format(w1[0]))
            	    f.write('      (value "{0:s}")\n'.format(w1[1]))
                    f.write('      (footprint "{0:s}")\n'.format(w1[2]))
            	    f.write('      (libsource (lib device) (part ""))\n')           
                    #f.write('      (sheetpath (names /) (tstamps /{0:s}))\n'.format(w1[3]))            
                    f.write('      (sheetpath (names /) (tstamps /))\n')            
                    f.write('      (tstamp {0:s}))'.format(w1[4]))     
            	    if i >= data_n :
                	f.write(")")
            	    f.write("\n")
		    break
	    if cmpf :
		continue 

	    #以降、コンポーネンツデータが無かった場合
	    #ネットリストから部品情報を作る処理
	    dfp_n += 1

	    #部番wの最大ピン数を調べる
            pin_max = 1; pin_cnt = 0
            for net in netlist[1] :
                for w1 in net :
                    words = w1.split("(")
                    if words[0] == w :		#部品番号が一致した場合ピン数をアップカウント
			pin_cnt += 1
			w2 = words[1].rstrip(")")
			if w2.isdigit() :	#ピン番号が数字の場合
                            pin = int(w2)
			else :			#ピン番号をカウントしたピン数にする
			    pin = pin_cnt

                        if pin > pin_max :
                            pin_max = pin

	    #最大ピン数から、ピンヘッダやQFPとして部品情報データを書き込む            
            f.write("  (components\n")
            f.write('    (comp (ref {0:s})\n'.format(w))
            f.write('      (value "{0:s}:{1:d}")\n'.format(w.rstrip("0123456789"), pin_max))
            if pin_max <= 40 :
                f.write('      (footprint "Pin_Headers:Pin_Header_Straight_1x{0:0>2d}_Pitch2.54mm")\n'.format(pin_max))
            elif pin_max <= 80 :
                f.write('      (footprint "Pin_Headers:Pin_Header_Straight_2x{0:0>2d}_Pitch2.54mm")\n'.format(pin_max//2 + pin_max%2))
            elif pin_max <= 100 :
                f.write('      (footprint "Housings_QFP:LQFP-100_14x14mm_Pitch0.5mm")\n')
            elif pin_max <= 208 :
                f.write('      (footprint "Housings_QFP:LQFP-208_28x28mm_Pitch0.5mm")\n')
            else :
                f.write('      (footprint "Housings_QFP:PQFP-256_28x28mm_Pitch0.4mm")\n')                
            f.write('      (libsource (lib device) (part ""))\n')           
            f.write('      (sheetpath (names /) (tstamps /))\n')            
            f.write('      (tstamp {0:X}))'.format(TSTAMP_OFFSET + ptn_max + dfp_n))     
            if i >= data_n :
                f.write(")")
            f.write("\n")
            
    #ネット接続データを書き込む
    name_n = len(netlist[0]); name_n -= 1   
    f.write("  (nets\n")
    for i, (name, net) in enumerate(zip(netlist[0], netlist[1])) :

        net_n = len(net); net_n -= 1
        
        str = '    (net (code {0:d}) (name "{1:s}")\n'.format((i + 1), name)
        f.write(str)

        for j, w in enumerate(net) :
            words = w.split('(')
            str = '      (node (ref {0:s}) (pin {1:s}))'.format(words[0], words[1].rstrip(")"))
            f.write(str)
            if j >= net_n :
                f.write(")")
                if i >= name_n :
                    f.write("))")

            f.write("\n")
            
           
    f.close()



#今実行しているディレクトリ名を取得
pcb = pcbnew.GetBoard()
pcb_file = pcb.GetFileName()
pcb_dir = os.path.dirname(pcb_file)
#pcb_name =  os.path.basename(pcb_file)
#print("Dir:{0:s}   Name:{1:s}\n").format(pcb_dir, pcb_name)

#作業ディレクトリを記憶
now_dir = os.getcwd() 
#作業ディレクトリを今実行しているディレクトリへ移動
os.chdir(pcb_dir)


#Calayネットリストを読み込む
net = Calay_Read('calay.net')

#KiCADネットリストを部品情報付で出力する
#部品情報自動作成（部品パッドを自動的にピンヘッダー）する場合
#Kicad_Write(net, pcb_file.replace('.kicad_pcb','.net'))
#部品情報（パーツリスト）をcsvファイルで指定する場合
Kicad_Write(net, pcb_file.replace('.kicad_pcb','.net'), 'partlist.csv')

#作業ディレクトリを元に戻す
os.chdir(now_dir)

