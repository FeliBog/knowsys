# KnowSys

<div align="center">
  <img src="https://img.shields.io/github/repo-size/FeliBog/knowsys?style=plastic"/>
  <img src="https://img.shields.io/github/license/FeliBog/knowsys?style=plastic"/>
  <img src="https://tokei.rs/b1/github/FeliBog/knowsys"/>
</div>

## Navigation
[Why is it developed](#why-is-it-developed)

[License](#license)

[Examples](#examples)

[All libraries](#project-using)

## Why is it developed
This project was designed to simplify the creation of applications that collect information about the system.

## License
> MIT License
Copyright (c) 2025 FeliBog

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. 

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Examples

### Get RAM Usage in %
```
import knowsys, time
ram = knowsys.RAM()
while 1:
  ram.update()
  print(ram.percent)
  time.sleep(1)
```

### Get Processor Usage in %
```
import knowsys, time
proc = knowsys.Processor()
while 1:
  proc.update()
  print(proc.percent)
  time.sleep(1)
```

### Get Battery Time to Discharge
```
import knowsys, time
battery = knowsys.Battery()
while 1:
  battery.update()
  print(f"{battery.discharge} seconds")
  time.sleep(1)
```

## Project using

platform: processor architecture and name

psutil: battery, RAM

requests: public ip