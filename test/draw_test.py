from PIL import Image
from PIL import ImageDraw

img = Image.open("../test_image_dir/287372b32bafc0a65daabbbb31509e5349859.jpg")  # 画像ファイル読み込み

draw = ImageDraw.Draw(img)  # 矩形の描画の準備

rectcolor = (255, 0, 0)  # 矩形の色(RGB)。red
linewidth = 4  # 線の太さ
draw.rectangle([(161, 50), (260, 162)], \
               outline=rectcolor, width=linewidth)  # 矩形の描画

textcolor = (255, 255, 255)  # テキストの色(RGB)。今回は白色です。
textsize = 14  # 描画するテキストの大きさ。今回は14px。

# テキストの描画の準備。"arial.ttf"はフォント名。
# font = ImageFont.truetype("arial.ttf", size=textsize)

text = " woman " + str(0.51) + " "

left, top = (161, 50)  # 矩形の左上の座標(x, y)をleft, topという変数に格納

txpos = (left, top - textsize - linewidth // 2)  # テキストの描画を開始する座標
# x座標はleftと同じ。
# y座標はtopよりテキストの大きさと矩形の線の太さの半分だけ上にする。
# テキストの大きさ(=textsize)。矩形の線の太さの半分(=linewidth//2)。

txw, txh = draw.textsize(text)
# 文字列"text"が占める領域のサイズを取得

draw.rectangle([txpos, (left + txw, top)], \
               outline=rectcolor, fill=rectcolor, width=linewidth)
# テキストを描画する領域を"rectcolor"で塗りつぶし。
# 左上座標をtxpos、右下座標を (left+txw, top)とする矩形をrectcolor(=赤色)で塗りつぶし。

draw.text(txpos, text, fill=textcolor)
# テキストをtextcolor(=白色)で描画
img.show()
# ファイルの保存
