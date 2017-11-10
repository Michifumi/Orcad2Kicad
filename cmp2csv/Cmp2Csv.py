# -*- coding: utf-8 -*-
import os
import pcbnew


#************************************************************************************************************************************************
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
                continue
                  
    return data



#************************************************************************************************************************************************
#Reference, Value, Footprint, Datasheet
#"C1","C_Small","Capacitors_SMD:C_0603_HandSoldering",""
#"R1","R_Small","Resistors_SMD:R_0603_HandSoldering",""
#"L1","L_Small","Inductors_SMD:L_0603_HandSoldering",""
def Csv_Write(data, wfname) :

    bfname = wfname + '_bak'
    if os.path.isfile(wfname) :
	if os.path.isfile(bfname) :
		os.remove(bfname)
    	os.rename(wfname, bfname) 

    f = open(wfname, 'w')
    f.write("Reference, Value, Footprint, Datasheet\n")

    for i, w in enumerate(data) :
        f.write('"{0:s}","{1:s}","{2:s}",""\n'.format( w[0], w[1], w[2] ))

    f.close()



#今実行している基板ファイル名を取得
pcb = pcbnew.GetBoard()
pcb_file = pcb.GetFileName()
pcb_dir = os.path.dirname(pcb_file)
#pcb_name =  os.path.basename(pcb_file)
#print("Dir:{0:s}   Name:{1:s}\n").format(pcb_dir, pcb_name)

#作業ディレクトリを記憶
now_dir = os.getcwd() 
#作業ディレクトリを今実行しているディレクトリへ移動
os.chdir(pcb_dir)



#指定コンポーネントファイルから部品情報を読み取る
data = Cmp_Read(pcb_file.replace('.kicad_pcb','.cmp'))

#指定ファイルへ部品情報を書き込む
Csv_Write(data, '@partlist.csv')

#作業ディレクトリを元に戻す
os.chdir(now_dir)

