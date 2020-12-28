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

## ③dlibを使った顔ランドマーク検出
【dlibのインストール】
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye00.gif" alt="dlibの顔ランドマーク検出" title="eye00">
<br>
※インストールが若干めんどくさい（windowsの場合）<br>
windowsでdlibを利用するにはPowerShellからCMakeをインストールしないといけない。<br><br>

参考にしたサイト：https://rikoubou.hatenablog.com/entry/2019/06/17/160248<br>
【CMakeダウンロードサイト】：https://cmake.org/download/<br><br>

【opencvのダウンロード】<br>
参考サイト：https://qiita.com/fiftystorm36/items/1a285b5fbf99f8ac82eb<br>
よくコマンドを忘れるので、注意。

## ④瞳の区画切り出し
【瞳の区画切り出し】
<img src="https://github.com/sassa4771/eyetrack/blob/main/Gif/eye01.gif" alt="瞳の区画切り出し" title="eye01">
<br>

【opencvで画像の切り出し方法】
参考サイト：https://qiita.com/mo256man/items/e36797f9f44a64caf81c<br>
【opencvで画像サイズの拡大方法】
参考サイト：https://qiita.com/kenfukaya/items/dfa548309c301c7087c4<br>
【opencvウィンドウの変更】<br>
参考サイト：https://qiita.com/Kazuhito/items/b2ebd9f9010f1ffcac5b<br>
ウィンドウが表示される場所を固定するため。
【int型をstring型に変更する方法】
参考サイト：https://www.javadrive.jp/python/string/index9.html<br>
【opencv画像を指定して保存】<br>
参考サイト：https://www.it-swarm-ja.tech/ja/python/opencv%E9%81%B8%E6%8A%9E%E3%81%97%E3%81%9F%E7%89%B9%E5%AE%9A%E3%81%AE%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%83%BC%E3%81%AB%E7%94%BB%E5%83%8F%E3%82%92%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B/830422001/<br>

## ⑤機械学習で検出（失敗）
## ⑥画像処理で検出（成功）
## ⑥その他試したこと(Docker接続など)
