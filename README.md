Password123 v0.1.0
--------------------------------------------

password123 is a command-line tool for checking if a password is one of the
10,000 most commonly used. Such passwords should not be used as they are highly
vulnerable to brute force attacks.

This tool complements my other password tools, [polonium](https://github.com/rgrannell1/polonium) and
[polonium-gui](https://github.com/rgrannell1/polonium-gui). These tools generate secure site-specific passwords given a secure master password, but they give little security if your master password is common.

The list of frequent passwords was compiled by Mark Burnett of [xato.net](https://xato.net/about/).

## Requirements

* A UNIX operating system.
* Python3.

## Installation

#### - Password123

To install password123, run

```bash
wget -q -O - https://raw.githubusercontent.com/rgrannell1/password123/master/install.sh | bash
```

### Licence

The MIT License

Copyright (c) 2014 Ryan Grannell

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Versioning

Versioning complies with the Semantic Versioning 2.0.0 standard.

http://semver.org/
