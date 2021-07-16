# Webカメラでeye tracking（アイトラッキング・視線計測）をする【Windows10】
https://github.com/sassa4771/eyetrack/tree/main/Eye_Tracking_Program_by_dlib<br>
ここのファイルの中身説明↑

## Qiita
https://qiita.com/sassa4771/items/fbfb0012744350cf4d93

## このGitHubでできること
・webカメラを利用した視線計測(以下の動画のイメージ)
<br><br>
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye04.gif" alt="アイトラッキング完成イメージ" title="eye03">

## 目次
①eyetracking(アイトラッキング・視線計測)とは？<br>
②必要なライブラリ・動作環境(※とりあえず動かしたい人はここから)<br>
③dlibを使った顔ランドマーク検出<br>
④瞳の区画切り出し<br>
⑤機械学習で検出（失敗）<br>
⑥画像処理で検出（成功）<br>
⑦その他試したこと(Docker接続など)<br>
⑧完成<br>

## ①eyetracking(アイトラッキング・視線計測)とは？
【eye trackingとは】
eye trackingとは、ユーザーの視線の動きを計測し分析するアイトラッキング（視線計測）技術のこと。<br><br>

ヒトの眼球運動を分析し、視覚的注意などを明らかにする生体計測手法です。<br>
ヒトの視線の場所（注視点）や動きを、アイトラッカーと呼ばれる専門の機械で計測。<br>
取得したデータを分析し、よく見られていた場所や、見る順序、反対に全く見られてい<br>
なかった場所などを明らかにします。<br><br>

心理学や認知科学などの学術領域のほか、マーケティング領域、観光分野、医療・教育・<br>
スポーツの研究など、さまざまな分野で利活用されているほか、近年ではVR空間内での計測や<br>
AIによる視線推定などの研究も盛んに行われており、今後も成長が期待されている技術です。<br>
(参考：https://neu-brains.co.jp/information/case-study/2020/09/25/1489.html)

要するに<h3>視線がどこにあるかわかる！</h3><br>

【製品】<br>
製品は、Tobiが有名<br>
・https://www.tobiipro.com/ja/<br>
・https://www.tobiipro.com/ja/service-support/learning-center/eye-tracking-essentials/what-is-dark-and-bright-pupil-tracking/<br><br>

【瞳孔検出方法】<br>
赤外線を利用した検出方法が主流<br>
・file:///C:/Users/sasat/Downloads/IPSJ-Z69-5P-08.pdf<br>
・https://www.tobiipro.com/ja/service-support/learning-center/eye-tracking-essentials/what-is-dark-and-bright-pupil-tracking/<br><br>

## ②必要なライブラリ・動作環境
【動作環境：(Let's Note)】<br>
OS:windows10 Pro<br>
CPU:Corei7<br>
メモリ:12GB<br>

【必要なライブラリ】<br>
・dlib
・opencv
・numpy
<br><br>

【Anaconda環境インストールコマンド】<br>
使用した環境は<a href='https://github.com/sassa4771/eyetrack/tree/main/Anaconda%20Environment'>eyetrack.yaml</a>にあります。<br>

```
cd 【eyetrack.yamlがあるとディレクトリ】
conda env create -n eyetrack -f eyetrack.yaml
```
環境をインストールしたらmainファイルの<a href='https://github.com/sassa4771/eyetrack/tree/main/Eye_Tracking_Program_by_dlib'>run.bat</a>を起動するとソフトが起動できる。<br>

## ③dlibを使った顔ランドマーク検出
【dlibのインストール】<br>
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye00.gif" alt="dlibの顔ランドマーク検出" title="eye00">
<br>
※インストールが若干めんどくさい（windowsの場合）<br>
windowsでdlibを利用するにはPowerShellからCMakeをインストールしないといけない。<br><br>

参考にしたサイト：https://rikoubou.hatenablog.com/entry/2019/06/17/160248<br>
【CMakeダウンロードサイト】：https://cmake.org/download/<br><br>

【opencvのダウンロード】<br>
参考サイト：https://qiita.com/fiftystorm36/items/1a285b5fbf99f8ac82eb<br>
よくコマンドを忘れるので、注意。<br>

## ④瞳の区画切り出し
【瞳の区画切り出し】<br>
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye01.gif" alt="瞳の区画切り出し" title="eye01">
<br><br>

【opencvで画像の切り出し方法】<br>
参考サイト：https://qiita.com/mo256man/items/e36797f9f44a64caf81c<br><br>
【opencvで画像サイズの拡大方法】<br>
参考サイト：https://qiita.com/kenfukaya/items/dfa548309c301c7087c4<br><br>
【opencvウィンドウの変更】<br>
参考サイト：https://qiita.com/Kazuhito/items/b2ebd9f9010f1ffcac5b<br>
ウィンドウが表示される場所を固定するため。<br><br>
【int型をstring型に変更する方法】<br>
参考サイト：https://www.javadrive.jp/python/string/index9.html<br><br>
【opencv画像を指定して保存】<br>
参考サイト：https://www.it-swarm-ja.tech/ja/python/opencv%E9%81%B8%E6%8A%9E%E3%81%97%E3%81%9F%E7%89%B9%E5%AE%9A%E3%81%AE%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%83%BC%E3%81%AB%E7%94%BB%E5%83%8F%E3%82%92%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B/830422001/<br><br>
【画像の二値化】<br>
参考サイト：https://qiita.com/tokkuri/items/ad5e858cbff8159829e9<br>
<br>

## ⑤機械学習で検出（失敗）
https://github.com/sassa4771/eyetrack/tree/main/tensorflow_pictures<br>
↑ここのファイルの中身においてある。<br><br>

GoogleのTeachable Machineを利用としたが、dlibに使うnumpyと機械学習で使うTensorflowのnumpyが合わなかったため断念。<br>
Teachable Machine:https://teachablemachine.withgoogle.com/<br><br>

keras==2.2.4,tensorflow==1.15.0,pillow==7.0.0
をダウンロードしないと動かないらしい。<br>

## ⑥画像処理で検出（成功）
【画像処理で検出】<br>
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye02.gif" alt="画像処理で検出" title="eye02"><br><br>

【平滑化、二値化、輪郭の抽出】<br>
参考サイト：https://qiita.com/ankomotch/items/74884b0ca24b739159c0<br><br>

【抽出した座標に長方形・円を表示】<br>
参考サイト：https://note.nkmk.me/python-opencv-draw-function/<br><br>

<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye03.gif" alt="画像処理で検出" title="eye03"><br><br>

## ⑦その他試したこと(Docker接続など)
【Docker】<br>
opencvとnumpyのインストールで苦戦したので、環境のリセットが容易なDockerをしようと試みた。<br>
Windows版のDockerでは、カメラデバイスを検出できないため断念。<br>
(一応VirtualBoxを使えばできるらしいが、せっかくのコンテナなのにホスト型の仮想環境を使うのはナンセンスと思った。)<br><br>

【opencvのインポートでエラー】<br>
<h3>ImportError: numpy.core.multiarray failed to import</h3>
がでる。<br><br>

opencvとnumpyのバージョンを合わせると解決する。<br><br>

<br>
・pip uninstall opencv-python<br>
・pip uninstall numpy<br><br>

・conda uninstall opencv-python<br>
・conda uninstall numpy<br><br>
でアンインストールしてから、<br><br>

・pip install opencv-python==3.4.2.17 numpy==1.14.5<br>
をする。<br>
※↑python=3.6じゃないとインストールできない<br><br>

## ⑧完成
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye04.gif" alt="画像処理で検出" title="eye04"><br><br>

次は、web版でopencvとか使いたい。

## 追記
【瞬きの判定を入れた】
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye05.gif" alt="瞬き判定" title="eye05"><br><br>
