# Webカメラでeye tracking（アイトラッキング・視線計測）をする【Windows10】

## このGitHubでできること
・webカメラを利用した視線計測(以下の動画のイメージ)
<br><br>
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye04.gif" alt="アイトラッキング完成イメージ" title="eye03">

## 目次
①eyetracking(アイトラッキング・視線計測)とは？<br>
②必要なライブラリ・動作環境<br>
③dlibを使った顔ランドマーク検出<br>
④瞳の区画切り出し<br>
⑤機械学習で検出（失敗）<br>
⑥画像処理で検出（成功）<br>
⑥その他試したこと(Docker接続など)<br>
⑦参考サイト<br>

## ①eyetracking(アイトラッキング・視線計測)とは？
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
https://www.tobiipro.com/ja/<br>
https://www.tobiipro.com/ja/service-support/learning-center/eye-tracking-essentials/what-is-dark-and-bright-pupil-tracking/<br><br>

【瞳孔検出方法】<br>
赤外線を利用した検出方法が主流<br>
file:///C:/Users/sasat/Downloads/IPSJ-Z69-5P-08.pdf<br>
https://www.tobiipro.com/ja/service-support/learning-center/eye-tracking-essentials/what-is-dark-and-bright-pupil-tracking/<br><br>

## ②必要なライブラリ・動作環境
【動作環境：(Let's Note)】<br>
OS:windows10 Pro<br>
CPU:Corei7<br>
メモリ:12GB<br>

【必要なライブラリ】<br>
・dlib
・opencv
・numpy

## ③dlibを使った顔ランドマーク検出
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye00.gif" alt="dlibの顔ランドマーク検出" title="eye01">
<br>
※インストールが若干めんどくさい（windowsの場合）<br>
windowsでdlibを利用するにはPowerShellからCMakeをインストールしないといけない。<br><br>

参考にしたサイト：https://rikoubou.hatenablog.com/entry/2019/06/17/160248<br>
【CMakeダウンロードサイト：https://cmake.org/download/】<br><br>



## ④瞳の区画切り出し
## ⑤機械学習で検出（失敗）
## ⑥画像処理で検出（成功）
## ⑥その他試したこと(Docker接続など)
