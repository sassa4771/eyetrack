rem 実行したい.pyファイルがあるフォルダに移動
cd ./
rem 仮想環境の立ち上げ

call C:\Users\ユーザー\Anaconda3\Scripts\activate.bat
call activate eyetrack
rem .pyファイルの実行
python eye_tracking.py