Recently i downloded Python3.10 Version 
and i like to introdue new feature o python3.10
which is Switch case in onther languge in pyton which is match case which is 
absent in previous version's

lets take examle 

```python3
def find(number:int)->str:
  match number:
    case 1:
      print("One")
    case 2:
      print("Two")
    case _ :
      print("something else")
      
find(1)
find(19)
```
