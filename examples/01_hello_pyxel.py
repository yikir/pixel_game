import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        # 颜色变化的字体, 这个里面最多16色
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        # 将xy处将iamge0的左上角+wh 描绘上去
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()
