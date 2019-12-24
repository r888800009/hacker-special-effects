# hacker-special-effects

Let you like a Hollywood hacker

install dependencies
``` bash
sudo pacman -S python highlight
```

## Typer
auto typing code

``` bash
highlight source.c -O xterm256 | ./typer.py  
```

loop
``` bash
while true
do
  highlight source.c -O xterm256 | ./typer.py
  sleep 0.01
done
```

![](./typer.gif)

