## C To LLVM

### Setup
```bash
bash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"
virtualenv venv
pip install -r requirements.txt
```

### Compile And Run
```bash
# python parse.py source.c out.ll
python parse.py test.c out.ll

lli out.ll
```

### Tests

#### Palindrome
```bash
python parse.py tests/palindrome.c out.ll

lli out.ll
```

#### Sort
```bash
python parse.py tests/sort.c out.ll

lli out.ll
```

#### Kmp
```bash
python parse.py tests/kmp.c out.ll

lli out.ll
```

#### Calc
```bash
python parse.py tests/calc.c out.ll

lli out.ll
```

#### Dfs
```bash
python parse.py tests/dfs.c out.ll

lli out.ll
```

