# WxMCTF - Bonus: Hidden Challenge

Snoop around WxMCTF related pages, find our [contest page](https://ctf.mcpt.ca/contest/wxmctf), see graphic has sus repeating binary numbers, not very 'design-aesthetic', conclude it must be purposely there.

![img](https://media.discordapp.net/attachments/1029527667088834621/1079964076379222077/image_5.png?)

Alright, so the flag is split up into 3 parts. Two are in plain sight. 

### 1. binary in the background

`0111011101111000011011010110001101110100011001100111101101110111011010000101100101011111` -> `wxmctf{whY_`

### 2. bottom corner text

zoom in, see text, increase contrast

![image](https://user-images.githubusercontent.com/80985676/227792706-d36511a7-61f7-4490-9700-d635ea5e265c.png)

`ar3_u_hEr3_g0_`

### 3. bit planes

view the red bit plane (u can also see 2. if u didnt get it before)

![image](https://user-images.githubusercontent.com/80985676/227792795-75ae009f-f5ba-424e-b4fc-efb77af03c4b.png)

loud and clear for you, `toUch_s0me_gr4s5}`

---

### the flag

`wxmctf{whY_ar3_u_hEr3_g0_toUch_s0me_gr4s5}`
