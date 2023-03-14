Credit: glrz01

This challenge was under the forensics category, also a relatively simple challenge. I first-blooded this challenge within seconds.
First, we could check the file type by running the `file` command.

![image](https://user-images.githubusercontent.com/62577178/227689264-b9a0e34b-302d-4456-919e-b5523fe8e2e4.png)

 
This confirmed that it was a [PCX](https://en.wikipedia.org/wiki/PCX) file. We could then open this file in `GIMP`.
```
┌──(kali㉿kali)-[~/Downloads]
└─$ gimp public.pcx
```
Opening it in GIMP, we would be able to see the flag.

![image](https://user-images.githubusercontent.com/62577178/227689303-591f08cd-08a9-4367-9b4a-09469329731f.png)

Alternatively, we could also open the file using `ImageMagick` as such:
```
┌──(kali㉿kali)-[~/Downloads]
└─$ display public.pcx
```

![image](https://user-images.githubusercontent.com/62577178/227689315-d6edf881-b749-403c-8bdc-49a332294a85.png)

Photoshop also works too

![image](https://user-images.githubusercontent.com/62577178/227689350-905f5420-5758-4951-9b4c-843b62cc219b.png)

Flag: `CTF{digital_archaeology_42}`
