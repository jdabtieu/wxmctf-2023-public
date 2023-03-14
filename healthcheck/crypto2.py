import requests

r = requests.get("http://factordb.com/index.php?id=1100000004378956268")

if '<td><a href="index.php?id=1100000004378956268"><font color="#002099">1008091901...83</font></a><sub>&lt;617&gt;</sub> = <a href="index.php?id=1100000004378956268"><font color="#002099">1008091901...83</font></a><sub>&lt;617&gt;</sub></td>' in r.text:
  print("healthcheck")
