# "Cmp2Csv"について   


## Ａ.概要 
+ "Cmp2Csv.py"は、KiCADv4の基板設計ソフトPcbnewで動作するマクロプログラムであり、Pcbnewのコンポーネントファイル(.cmp)から、部品情報csvファイルへ変換するソフトです。


## Ｂ.ファイル内容 
+ "Cmp2Csv.py" ... Pcbnewのコンポーネントファイルを、部品情報csvファイルへの変換ソフト（マクロ）


## Ｃ.動作確認環境 
+ KiCAD Ver4.07 on Windows7-64bit　/ Ubuntu14.04LTS-64bit  


## Ｄ.使用方法 
1. Pcbnewを起動し、「ファイル」->「エキスポート」->「コンポーネントファイル(.cmp)」を選択し、今設計している基板のコンポーネントファイルを作成する。
2. Pythonコンソールを選択実行する。　
3. コンソール内で、「pwd」を実行し、出てきたフォルダ（普通は"C:\Program Files\KiCad")へ、本ソフト"Cmp2Csv.py"をコピーする。
4. コンソール内で、「execfile("Cmp2Csv.py")」と入力、実行する。
5. 部品情報csvファイル"@partlist.csv"が生成される。


## Ｅ.参考にさせて頂いたサイト 
+ 「KiCad用のPythonスクリプト ～ ほぼ回路図の配置通りにフットプリントを予備配置する」
        <https://qiita.com/silvermoon/items/da4fcdba319f46570a60>


## Ｇ.変更履歴 
---
2017/11/10   (1st commit)
      
---
  
