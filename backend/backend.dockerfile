[[package]]
name = "aiosmtplib"
version = "1.1.7"
description = "asyncio SMTP client"
category = "dev"
optional = false
python-versions = ">=3.5.2,<4.0.0"

[package.extras]
docs = ["jinja2 (>=2.0,<3.1)", "sphinx (>=2,<4)", "sphinx_autodoc_typehints (>=1.7.0,<2.0.0)"]
uvloop = ["uvloop (>=0.13,<0.15)"]

[[package]]
name = "alembic"
version = "1.8.1"
description = "A database migration tool for SQLAlchemy."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
Mako = "*"
SQLAlchemy = ">=1.3.0"

[package.extras]
tz = ["python-dateutil"]

[[package]]
name = "anyio"
version = "3.6.1"
description = "High level compatibility layer for multiple asynchronous event loop implementations"
category = "dev"
optional = false
python-versions = ">=3.6.2"

[package.dependencies]
idna = ">=2.8"
sniffio = ">=1.1"

[package.extras]
doc = ["packaging", "sphinx-autodoc-typehints (>=1.2.0)", "sphinx-rtd-theme"]
test = ["contextlib2", "coverage[toml] (>=4.5)", "hypothesis (>=4.0)", "mock (>=4)", "pytest (>=7.0)", "pytest-mock (>=3.6.1)", "trustme", "uvloop (<0.15)", "uvloop (>=0.15)"]
trio = ["trio (>=0.16)"]

[[package]]
name = "bcrypt"
version = "4.0.0"
description = "Modern password hashing for your software and your servers"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.extras]
tests = ["pytest (>=3.2.1,!=3.3.0)"]
typecheck = ["mypy"]

[[package]]
name = "black"
version = "22.8.0"
description = "The uncompromising code formatter."
category = "dev"
optional = false
python-versions = ">=3.6.2"

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
pathspec = ">=0.9.0"
platformdirs = ">=2"
tomli = {version = ">=1.1.0", markers = "python_full_version < \"3.11.0a7\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.7.4)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "blinker"
version = "1.5"
description = "Fast, simple object-to-object and broadcast signaling"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "certifi"
version = "2022.6.15.1"
description = "Python package for providing Mozilla's CA Bundle."
category = "dev"
optional = false
python-versions = ">=3.6"

[[package]]
name = "cffi"
version = "1.15.1"
description = "Foreign Function Interface for Python calling C code."
category = "dev"
optional = false
python-versions = "*"

[package.dependencies]
pycparser = "*"

[[package]]
name = "click"
version = "8.1.3"
description = "Composable command line interface toolkit"
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.5"
description = "Cross-platform colored terminal text."
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "cryptography"
version = "38.0.1"
description = "cryptography is a package which provides cryptographic recipes and primitives to Python developers."
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
cffi = ">=1.12"

[package.extras]
docs = ["sphinx (>=1.6.5,!=1.8.0,!=3.1.0,!=3.1.1)", "sphinx-rtd-theme"]
docstest = ["pyenchant (>=1.6.11)", "sphinxcontrib-spelling (>=4.0.1)", "twine (>=1.12.0)"]
pep8test = ["black", "flake8", "flake8-import-order", "pep8-naming"]
sdist = ["setuptools-rust (>=0.11.4)"]
ssh = ["bcrypt (>=3.1.5)"]
test = ["hypothesis (>=1.11.4,!=3.79.2)", "iso8601", "pretend", "pytest (>=6.2.0)", "pytest-benchmark", "pytest-cov", "pytest-subtests", "pytest-xdist", "pytz"]

[[package]]
name = "dnspython"
version = "2.2.1"
description = "DNS toolkit"
category = "dev"
optional = false
python-versions = ">=3.6,<4.0"

[package.extras]
curio = ["curio (>=1.2,<2.0)", "sniffio (>=1.1,<2.0)"]
dnssec = ["cryptography (>=2.6,<37.0)"]
doh = ["h2 (>=4.1.0)", "httpx (>=0.21.1)", "requests (>=2.23.0,<3.0.0)", "requests-toolbelt (>=0.9.1,<0.10.0)"]
idna = ["idna (>=2.1,<4.0)"]
trio = ["trio (>=0.14,<0.20)"]
wmi = ["wmi (>=1.5.1,<2.0.0)"]

[[package]]
name = "ecdsa"
version = "0.18.0"
description = "ECDSA cryptographic signature library (pure python)"
category = "dev"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"

[package.dependencies]
six = ">=1.9.0"

[package.extras]
gmpy = ["gmpy"]
gmpy2 = ["gmpy2"]

[[package]]
name = "email-validator"
version = "1.2.1"
description = "A robust email syntax and deliverability validation library."
category = "dev"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,>=2.7"

[package.dependencies]
dnspython = ">=1.15.0"
idna = ">=2.0.0"

[[package]]
name = "fastapi"
version = "0.83.0"
description = "FastAPI framework, high performance, easy to learn, fast to code, ready for production"
category = "dev"
optional = false
python-versions = ">=3.6.1"

[package.dependencies]
pydantic = ">=1.6.2,<1.7 || >1.7,<1.7.1 || >1.7.1,<1.7.2 || >1.7.2,<1.7.3 || >1.7.3,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0"
starlette = "0.19.1"

[package.extras]
all = ["email_validator (>=1.1.1,<2.0.0)", "itsdangerous (>=1.1.0,<3.0.0)", "jinja2 (>=2.11.2,<4.0.0)", "orjson (>=3.2.1,<4.0.0)", "python-multipart (>=0.0.5,<0.0.6)", "pyyaml (>=5.3.1,<7.0.0)", "requests (>=2.24.0,<3.0.0)", "ujson (>=4.0.1,!=4.0.2,!=4.1.0,!=4.2.0,!=4.3.0,!=5.0.0,!=5.1.0,<6.0.0)", "uvicorn[standard] (>=0.12.0,<0.18.0)"]
dev = ["autoflake (>=1.4.0,<2.0.0)", "flake8 (>=3.8.3,<6.0.0)", "passlib[bcrypt] (>=1.7.2,<2.0.0)", "pre-commit (>=2.17.0,<3.0.0)", "python-jose[cryptography] (>=3.3.0,<4.0.0)", "uvicorn[standard] (>=0.12.0,<0.18.0)"]
doc = ["mdx-include (>=1.4.1,<2.0.0)", "mkdocs (>=1.1.2,<2.0.0)", "mkdocs-markdownextradata-plugin (>=0.1.7,<0.3.0)", "mkdocs-material (>=8.1.4,<9.0.0)", "pyyaml (>=5.3.1,<7.0.0)", "typer (>=0.4.1,<0.5.0)"]
test = ["anyio[trio] (>=3.2.1,<4.0.0)", "black (==22.3.0)", "databases[sqlite] (>=0.3.2,<0.6.0)", "email_validator (>=1.1.1,<2.0.0)", "flake8 (>=3.8.3,<6.0.0)", "flask (>=1.1.2,<3.0.0)", "httpx (>=0.14.0,<0.19.0)", "isort (>=5.0.6,<6.0.0)", "mypy (==0.910)", "orjson (>=3.2.1,<4.0.0)", "peewee (>=3.13.3,<4.0.0)", "pytest (>=6.2.4,<7.0.0)", "pytest-cov (>=2.12.0,<4.0.0)", "python-multipart (>=0.0.5,<0.0.6)", "requests (>=2.24.0,<3.0.0)", "sqlalchemy (>=1.3.18,<1.5.0)", "types-dataclasses (==0.6.5)", "types-orjson (==3.6.2)", "types-ujson (==4.2.1)", "ujson (>=4.0.1,!=4.0.2,!=4.1.0,!=4.2.0,!=4.3.0,!=5.0.0,!=5.1.0,<6.0.0)"]

[[package]]
name = "fastapi-mail"
version = "1.1.4"
description = "Simple lightweight mail library for FastApi"
category = "dev"
optional = false
python-versions = ">=3.7,<4.0"

[package.dependencies]
aiosmtplib = ">=1.1.6,<2.0.0"
blinker = ">=1.5,<2.0"
email-validator = ">=1.1.3,<2.0.0"
Jinja2 = ">=3.0.1,<4.0.0"
pydantic = ">=1.8.2,<2.0.0"

[package.extras]
fakeredis = ["fakeredis[fakeredis] (>=1.8.2,<2.0.0)"]
httpx = ["httpx[httpx] (>=0.23.0,<0.24.0)"]

[[package]]
name = "greenlet"
version = "1.1.3"
description = "Lightweight in-process concurrent programming"
category = "dev"
optional = false
python-versions = ">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*"

[package.extras]
docs = ["Sphinx"]

[[package]]
name = "h11"
version = "0.13.0"
description = "A pure-Python, bring-your-own-I/O implementation of HTTP/1.1"
category = "dev"
optional = false
python-versions = ">=3.6"

[[package]]
name = "idna"
version = "3.3"
description = "Internationalized Domain Names in Applications (IDNA)"
category = "dev"
optional = false
python-versions = ">=3.5"

[[package]]
name = "Jinja2"
version = "3.1.2"
description = "A very fast and expressive template engine."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "Mako"
version = "1.2.3"
description = "A super-fast templating language that borrows the best ideas from the existing templating languages."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
MarkupSafe = ">=0.9.2"

[package.extras]
babel = ["Babel"]
lingua = ["lingua"]
testing = ["pytest"]

[[package]]
name = "MarkupSafe"
version = "2.1.1"
description = "Safely add untrusted strings to HTML/XML markup."
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "mypy-extensions"
version = "0.4.3"
description = "Experimental type system extensions for programs checked with the mypy typechecker."
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "passlib"
version = "1.7.4"
description = "comprehensive password hashing framework supporting over 30 schemes"
category = "dev"
optional = false
python-versions = "*"

[package.dependencies]
bcrypt = {version = ">=3.1.0", optional = true, markers = "extra == \"bcrypt\""}

[package.extras]
argon2 = ["argon2-cffi (>=18.2.0)"]
bcrypt = ["bcrypt (>=3.1.0)"]
build-docs = ["cloud-sptheme (>=1.10.1)", "sphinx (>=1.6)", "sphinxcontrib-fulltoc (>=1.2.0)"]
totp = ["cryptography"]

[[package]]
name = "pathspec"
version = "0.10.1"
description = "Utility library for gitignore style pattern matching of file paths."
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "platformdirs"
version = "2.5.2"
description = "A small Python module for determining appropriate platform-specific dirs, e.g. a \"user data dir\"."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.extras]
docs = ["furo (>=2021.7.5b38)", "proselint (>=0.10.2)", "sphinx (>=4)", "sphinx-autodoc-typehints (>=1.12)"]
test = ["appdirs (==1.4.4)", "pytest (>=6)", "pytest-cov (>=2.7)", "pytest-mock (>=3.6)"]

[[package]]
name = "psycopg2-binary"
version = "2.9.4"
description = "psycopg2 - Python-PostgreSQL Database Adapter"
category = "dev"
optional = false
python-versions = ">=3.6"

[[package]]
name = "pyasn1"
version = "0.4.8"
description = "ASN.1 types and codecs"
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "pycparser"
version = "2.21"
description = "C parser in Python"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"

[[package]]
name = "pydantic"
version = "1.10.2"
description = "Data validation and settings management using python type hints"
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
email-validator = {version = ">=1.0.3", optional = true, markers = "extra == \"email\""}
typing-extensions = ">=4.1.0"

[package.extras]
dotenv = ["python-dotenv (>=0.10.4)"]
email = ["email-validator (>=1.0.3)"]

[[package]]
name = "python-dateutil"
version = "2.8.2"
description = "Extensions to the standard Python datetime module"
category = "dev"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"

[package.dependencies]
six = ">=1.5"

[[package]]
name = "python-dotenv"
version = "0.21.0"
description = "Read key-value pairs from a .env file and set them as environment variables"
category = "dev"
optional = false
python-versions = ">=3.7"

[package.extras]
cli = ["click (>=5.0)"]

[[package]]
name = "python-jose"
version = "3.3.0"
description = "JOSE implementation in Python"
category = "dev"
optional = false
python-versions = "*"

[package.dependencies]
cryptography = {version = ">=3.4.0", optional = true, markers = "extra == \"cryptography\""}
ecdsa = "!=0.15"
pyasn1 = "*"
rsa = "*"

[package.extras]
cryptography = ["cryptography (>=3.4.0)"]
pycrypto = ["pyasn1", "pycrypto (>=2.6.0,<2.7.0)"]
pycryptodome = ["pyasn1", "pycryptodome (>=3.3.1,<4.0.0)"]

[[package]]
name = "python-multipart"
version = "0.0.5"
description = "A streaming multipart parser for Python"
category = "dev"
optional = false
python-versions = "*"

[package.dependencies]
six = ">=1.4.0"

[[package]]
name = "rsa"
version = "4.9"
description = "Pure-Python RSA implementation"
category = "dev"
optional = false
python-versions = ">=3.6,<4"

[package.dependencies]
pyasn1 = ">=0.1.3"

[[package]]
name = "sib-api-v3-sdk"
version = "7.5.0"
description = "SendinBlue API"
category = "dev"
optional = false
python-versions = "*"

[package.dependencies]
certifi = ">=2017.4.17"
python-dateutil = ">=2.1"
six = ">=1.10"
urllib3 = ">=1.23"

[[package]]
name = "six"
version = "1.16.0"
description = "Python 2 and 3 compatibility utilities"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*"

[[package]]
name = "sniffio"
version = "1.3.0"
description = "Sniff out which async library your code is running under"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "SQLAlchemy"
version = "1.4.41"
description = "Database Abstraction Library"
category = "dev"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,>=2.7"

[package.dependencies]
greenlet = {version = "!=0.4.17", markers = "python_version >= \"3\" and (platform_machine == \"aarch64\" or platform_machine == \"ppc64le\" or platform_machine == \"x86_64\" or platform_machine == \"amd64\" or platform_machine == \"AMD64\" or platform_machine == \"win32\" or platform_machine == \"WIN32\")"}

[package.extras]
aiomysql = ["aiomysql", "greenlet (!=0.4.17)"]
aiosqlite = ["aiosqlite", "greenlet (!=0.4.17)", "typing_extensions (!=3.10.0.1)"]
asyncio = ["greenlet (!=0.4.17)"]
asyncmy = ["asyncmy (>=0.2.3,!=0.2.4)", "greenlet (!=0.4.17)"]
mariadb-connector = ["mariadb (>=1.0.1,!=1.1.2)"]
mssql = ["pyodbc"]
mssql-pymssql = ["pymssql"]
mssql-pyodbc = ["pyodbc"]
mypy = ["mypy (>=0.910)", "sqlalchemy2-stubs"]
mysql = ["mysqlclient (>=1.4.0)", "mysqlclient (>=1.4.0,<2)"]
mysql-connector = ["mysql-connector-python"]
oracle = ["cx_oracle (>=7)", "cx_oracle (>=7,<8)"]
postgresql = ["psycopg2 (>=2.7)"]
postgresql-asyncpg = ["asyncpg", "greenlet (!=0.4.17)"]
postgresql-pg8000 = ["pg8000 (>=1.16.6,!=1.29.0)"]
postgresql-psycopg2binary = ["psycopg2-binary"]
postgresql-psycopg2cffi = ["psycopg2cffi"]
pymysql = ["pymysql", "pymysql (<1)"]
sqlcipher = ["sqlcipher3_binary"]

[[package]]
name = "sqlalchemy2-stubs"
version = "0.0.2a29"
description = "Typing Stubs for SQLAlchemy 1.4"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
typing-extensions = ">=3.7.4"

[[package]]
name = "sqlmodel"
version = "0.0.8"
description = "SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness."
category = "dev"
optional = false
python-versions = ">=3.6.1,<4.0.0"

[package.dependencies]
pydantic = ">=1.8.2,<2.0.0"
SQLAlchemy = ">=1.4.17,<=1.4.41"
sqlalchemy2-stubs = "*"

[[package]]
name = "starlette"
version = "0.19.1"
description = "The little ASGI library that shines."
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
anyio = ">=3.4.0,<5"

[package.extras]
full = ["itsdangerous", "jinja2", "python-multipart", "pyyaml", "requests"]

[[package]]
name = "tomli"
version = "2.0.1"
description = "A lil' TOML parser"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "typing-extensions"
version = "4.3.0"
description = "Backported and Experimental Type Hints for Python 3.7+"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "urllib3"
version = "1.26.12"
description = "HTTP library with thread-safe connection pooling, file post, and more."
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4"

[package.extras]
brotli = ["brotli (>=1.0.9)", "brotlicffi (>=0.8.0)", "brotlipy (>=0.6.0)"]
secure = ["certifi", "cryptography (>=1.3.4)", "idna (>=2.0.0)", "ipaddress", "pyOpenSSL (>=0.14)", "urllib3-secure-extra"]
socks = ["PySocks (>=1.5.6,!=1.5.7,<2.0)"]

[[package]]
name = "uvicorn"
version = "0.18.3"
description = "The lightning-fast ASGI server."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
click = ">=7.0"
h11 = ">=0.8"

[package.extras]
standard = ["colorama (>=0.4)", "httptools (>=0.4.0)", "python-dotenv (>=0.13)", "pyyaml (>=5.1)", "uvloop (>=0.14.0,!=0.15.0,!=0.15.1)", "watchfiles (>=0.13)", "websockets (>=10.0)"]

[metadata]
lock-version = "1.1"
python-versions = "^3.10"
content-hash = "499af44e8c5e8d45f953d09852c9592b4ebb021f539d89736f123244973546b6"

[metadata.files]
aiosmtplib = [
{file = "aiosmtplib-1.1.7-py3-none-any.whl", hash = "sha256:c1403e70fce769643820cb2c5bf0bd4f7ea83a01c60e854c81a6f5d7ccff2656"},
{file = "aiosmtplib-1.1.7.tar.gz", hash = "sha256:5810657a86b19476c93fa280c499ca3ef88ce26f2b74dae202989ae06377d107"},
]
alembic = [
{file = "alembic-1.8.1-py3-none-any.whl", hash = "sha256:0a024d7f2de88d738d7395ff866997314c837be6104e90c5724350313dee4da4"},
{file = "alembic-1.8.1.tar.gz", hash = "sha256:cd0b5e45b14b706426b833f06369b9a6d5ee03f826ec3238723ce8caaf6e5ffa"},
]
anyio = [
{file = "anyio-3.6.1-py3-none-any.whl", hash = "sha256:cb29b9c70620506a9a8f87a309591713446953302d7d995344d0d7c6c0c9a7be"},
{file = "anyio-3.6.1.tar.gz", hash = "sha256:413adf95f93886e442aea925f3ee43baa5a765a64a0f52c6081894f9992fdd0b"},
]
bcrypt = [
{file = "bcrypt-4.0.0-cp36-abi3-macosx_10_10_universal2.whl", hash = "sha256:845b1daf4df2dd94d2fdbc9454953ca9dd0e12970a0bfc9f3dcc6faea3fa96e4"},
{file = "bcrypt-4.0.0-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_24_aarch64.whl", hash = "sha256:8780e69f9deec9d60f947b169507d2c9816e4f11548f1f7ebee2af38b9b22ae4"},
{file = "bcrypt-4.0.0-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1c3334446fac200499e8bc04a530ce3cf0b3d7151e0e4ac5c0dddd3d95e97843"},
{file = "bcrypt-4.0.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bfb67f6a6c72dfb0a02f3df51550aa1862708e55128b22543e2b42c74f3620d7"},
{file = "bcrypt-4.0.0-cp36-abi3-manylinux_2_24_x86_64.whl", hash = "sha256:7c7dd6c1f05bf89e65261d97ac3a6520f34c2acb369afb57e3ea4449be6ff8fd"},
{file = "bcrypt-4.0.0-cp36-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:594780b364fb45f2634c46ec8d3e61c1c0f1811c4f2da60e8eb15594ecbf93ed"},
{file = "bcrypt-4.0.0-cp36-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:2d0dd19aad87e4ab882ef1d12df505f4c52b28b69666ce83c528f42c07379227"},
{file = "bcrypt-4.0.0-cp36-abi3-musllinux_1_1_aarch64.whl", hash = "sha256:bf413f2a9b0a2950fc750998899013f2e718d20fa4a58b85ca50b6df5ed1bbf9"},
{file = "bcrypt-4.0.0-cp36-abi3-musllinux_1_1_x86_64.whl", hash = "sha256:ede0f506554571c8eda80db22b83c139303ec6b595b8f60c4c8157bdd0bdee36"},
{file = "bcrypt-4.0.0-cp36-abi3-win32.whl", hash = "sha256:dc6ec3dc19b1c193b2f7cf279d3e32e7caf447532fbcb7af0906fe4398900c33"},
{file = "bcrypt-4.0.0-cp36-abi3-win_amd64.whl", hash = "sha256:0b0f0c7141622a31e9734b7f649451147c04ebb5122327ac0bd23744df84be90"},
{file = "bcrypt-4.0.0.tar.gz", hash = "sha256:c59c170fc9225faad04dde1ba61d85b413946e8ce2e5f5f5ff30dfd67283f319"},
]
black = [
{file = "black-22.8.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:ce957f1d6b78a8a231b18e0dd2d94a33d2ba738cd88a7fe64f53f659eea49fdd"},
{file = "black-22.8.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:5107ea36b2b61917956d018bd25129baf9ad1125e39324a9b18248d362156a27"},
{file = "black-22.8.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e8166b7bfe5dcb56d325385bd1d1e0f635f24aae14b3ae437102dedc0c186747"},
{file = "black-22.8.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dd82842bb272297503cbec1a2600b6bfb338dae017186f8f215c8958f8acf869"},
{file = "black-22.8.0-cp310-cp310-win_amd64.whl", hash = "sha256:d839150f61d09e7217f52917259831fe2b689f5c8e5e32611736351b89bb2a90"},
{file = "black-22.8.0-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:a05da0430bd5ced89176db098567973be52ce175a55677436a271102d7eaa3fe"},
{file = "black-22.8.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4a098a69a02596e1f2a58a2a1c8d5a05d5a74461af552b371e82f9fa4ada8342"},
{file = "black-22.8.0-cp36-cp36m-win_amd64.whl", hash = "sha256:5594efbdc35426e35a7defa1ea1a1cb97c7dbd34c0e49af7fb593a36bd45edab"},
{file = "black-22.8.0-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:a983526af1bea1e4cf6768e649990f28ee4f4137266921c2c3cee8116ae42ec3"},
{file = "black-22.8.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3b2c25f8dea5e8444bdc6788a2f543e1fb01494e144480bc17f806178378005e"},
{file = "black-22.8.0-cp37-cp37m-win_amd64.whl", hash = "sha256:78dd85caaab7c3153054756b9fe8c611efa63d9e7aecfa33e533060cb14b6d16"},
{file = "black-22.8.0-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:cea1b2542d4e2c02c332e83150e41e3ca80dc0fb8de20df3c5e98e242156222c"},
{file = "black-22.8.0-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:5b879eb439094751185d1cfdca43023bc6786bd3c60372462b6f051efa6281a5"},
{file = "black-22.8.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:0a12e4e1353819af41df998b02c6742643cfef58282915f781d0e4dd7a200411"},
{file = "black-22.8.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c3a73f66b6d5ba7288cd5d6dad9b4c9b43f4e8a4b789a94bf5abfb878c663eb3"},
{file = "black-22.8.0-cp38-cp38-win_amd64.whl", hash = "sha256:e981e20ec152dfb3e77418fb616077937378b322d7b26aa1ff87717fb18b4875"},
{file = "black-22.8.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:8ce13ffed7e66dda0da3e0b2eb1bdfc83f5812f66e09aca2b0978593ed636b6c"},
{file = "black-22.8.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:32a4b17f644fc288c6ee2bafdf5e3b045f4eff84693ac069d87b1a347d861497"},
{file = "black-22.8.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0ad827325a3a634bae88ae7747db1a395d5ee02cf05d9aa7a9bd77dfb10e940c"},
{file = "black-22.8.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:53198e28a1fb865e9fe97f88220da2e44df6da82b18833b588b1883b16bb5d41"},
{file = "black-22.8.0-cp39-cp39-win_amd64.whl", hash = "sha256:bc4d4123830a2d190e9cc42a2e43570f82ace35c3aeb26a512a2102bce5af7ec"},
{file = "black-22.8.0-py3-none-any.whl", hash = "sha256:d2c21d439b2baf7aa80d6dd4e3659259be64c6f49dfd0f32091063db0e006db4"},
{file = "black-22.8.0.tar.gz", hash = "sha256:792f7eb540ba9a17e8656538701d3eb1afcb134e3b45b71f20b25c77a8db7e6e"},
]
blinker = [
{file = "blinker-1.5-py2.py3-none-any.whl", hash = "sha256:1eb563df6fdbc39eeddc177d953203f99f097e9bf0e2b8f9f3cf18b6ca425e36"},
{file = "blinker-1.5.tar.gz", hash = "sha256:923e5e2f69c155f2cc42dafbbd70e16e3fde24d2d4aa2ab72fbe386238892462"},
]
certifi = [
{file = "certifi-2022.6.15.1-py3-none-any.whl", hash = "sha256:43dadad18a7f168740e66944e4fa82c6611848ff9056ad910f8f7a3e46ab89e0"},
{file = "certifi-2022.6.15.1.tar.gz", hash = "sha256:cffdcd380919da6137f76633531a5817e3a9f268575c128249fb637e4f9e73fb"},
]
cffi = [
{file = "cffi-1.15.1-cp27-cp27m-macosx_10_9_x86_64.whl", hash = "sha256:a66d3508133af6e8548451b25058d5812812ec3798c886bf38ed24a98216fab2"},
{file = "cffi-1.15.1-cp27-cp27m-manylinux1_i686.whl", hash = "sha256:470c103ae716238bbe698d67ad020e1db9d9dba34fa5a899b5e21577e6d52ed2"},
{file = "cffi-1.15.1-cp27-cp27m-manylinux1_x86_64.whl", hash = "sha256:9ad5db27f9cabae298d151c85cf2bad1d359a1b9c686a275df03385758e2f914"},
{file = "cffi-1.15.1-cp27-cp27m-win32.whl", hash = "sha256:b3bbeb01c2b273cca1e1e0c5df57f12dce9a4dd331b4fa1635b8bec26350bde3"},
{file = "cffi-1.15.1-cp27-cp27m-win_amd64.whl", hash = "sha256:e00b098126fd45523dd056d2efba6c5a63b71ffe9f2bbe1a4fe1716e1d0c331e"},
{file = "cffi-1.15.1-cp27-cp27mu-manylinux1_i686.whl", hash = "sha256:d61f4695e6c866a23a21acab0509af1cdfd2c013cf256bbf5b6b5e2695827162"},
{file = "cffi-1.15.1-cp27-cp27mu-manylinux1_x86_64.whl", hash = "sha256:ed9cb427ba5504c1dc15ede7d516b84757c3e3d7868ccc85121d9310d27eed0b"},
{file = "cffi-1.15.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:39d39875251ca8f612b6f33e6b1195af86d1b3e60086068be9cc053aa4376e21"},
{file = "cffi-1.15.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:285d29981935eb726a4399badae8f0ffdff4f5050eaa6d0cfc3f64b857b77185"},
{file = "cffi-1.15.1-cp310-cp310-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3eb6971dcff08619f8d91607cfc726518b6fa2a9eba42856be181c6d0d9515fd"},
{file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:21157295583fe8943475029ed5abdcf71eb3911894724e360acff1d61c1d54bc"},
{file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5635bd9cb9731e6d4a1132a498dd34f764034a8ce60cef4f5319c0541159392f"},
{file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2012c72d854c2d03e45d06ae57f40d78e5770d252f195b93f581acf3ba44496e"},
{file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dd86c085fae2efd48ac91dd7ccffcfc0571387fe1193d33b6394db7ef31fe2a4"},
{file = "cffi-1.15.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:fa6693661a4c91757f4412306191b6dc88c1703f780c8234035eac011922bc01"},
{file = "cffi-1.15.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:59c0b02d0a6c384d453fece7566d1c7e6b7bae4fc5874ef2ef46d56776d61c9e"},
{file = "cffi-1.15.1-cp310-cp310-win32.whl", hash = "sha256:cba9d6b9a7d64d4bd46167096fc9d2f835e25d7e4c121fb2ddfc6528fb0413b2"},
{file = "cffi-1.15.1-cp310-cp310-win_amd64.whl", hash = "sha256:ce4bcc037df4fc5e3d184794f27bdaab018943698f4ca31630bc7f84a7b69c6d"},
{file = "cffi-1.15.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:3d08afd128ddaa624a48cf2b859afef385b720bb4b43df214f85616922e6a5ac"},
{file = "cffi-1.15.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:3799aecf2e17cf585d977b780ce79ff0dc9b78d799fc694221ce814c2c19db83"},
{file = "cffi-1.15.1-cp311-cp311-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a591fe9e525846e4d154205572a029f653ada1a78b93697f3b5a8f1f2bc055b9"},
{file = "cffi-1.15.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3548db281cd7d2561c9ad9984681c95f7b0e38881201e157833a2342c30d5e8c"},
{file = "cffi-1.15.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:91fc98adde3d7881af9b59ed0294046f3806221863722ba7d8d120c575314325"},
{file = "cffi-1.15.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:94411f22c3985acaec6f83c6df553f2dbe17b698cc7f8ae751ff2237d96b9e3c"},
{file = "cffi-1.15.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:03425bdae262c76aad70202debd780501fabeaca237cdfddc008987c0e0f59ef"},
{file = "cffi-1.15.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:cc4d65aeeaa04136a12677d3dd0b1c0c94dc43abac5860ab33cceb42b801c1e8"},
{file = "cffi-1.15.1-cp311-cp311-win32.whl", hash = "sha256:a0f100c8912c114ff53e1202d0078b425bee3649ae34d7b070e9697f93c5d52d"},
{file = "cffi-1.15.1-cp311-cp311-win_amd64.whl", hash = "sha256:04ed324bda3cda42b9b695d51bb7d54b680b9719cfab04227cdd1e04e5de3104"},
{file = "cffi-1.15.1-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:50a74364d85fd319352182ef59c5c790484a336f6db772c1a9231f1c3ed0cbd7"},
{file = "cffi-1.15.1-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e263d77ee3dd201c3a142934a086a4450861778baaeeb45db4591ef65550b0a6"},
{file = "cffi-1.15.1-cp36-cp36m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:cec7d9412a9102bdc577382c3929b337320c4c4c4849f2c5cdd14d7368c5562d"},
{file = "cffi-1.15.1-cp36-cp36m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4289fc34b2f5316fbb762d75362931e351941fa95fa18789191b33fc4cf9504a"},
{file = "cffi-1.15.1-cp36-cp36m-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:173379135477dc8cac4bc58f45db08ab45d228b3363adb7af79436135d028405"},
{file = "cffi-1.15.1-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:6975a3fac6bc83c4a65c9f9fcab9e47019a11d3d2cf7f3c0d03431bf145a941e"},
{file = "cffi-1.15.1-cp36-cp36m-win32.whl", hash = "sha256:2470043b93ff09bf8fb1d46d1cb756ce6132c54826661a32d4e4d132e1977adf"},
{file = "cffi-1.15.1-cp36-cp36m-win_amd64.whl", hash = "sha256:30d78fbc8ebf9c92c9b7823ee18eb92f2e6ef79b45ac84db507f52fbe3ec4497"},
{file = "cffi-1.15.1-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:198caafb44239b60e252492445da556afafc7d1e3ab7a1fb3f0584ef6d742375"},
{file = "cffi-1.15.1-cp37-cp37m-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:5ef34d190326c3b1f822a5b7a45f6c4535e2f47ed06fec77d3d799c450b2651e"},
{file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8102eaf27e1e448db915d08afa8b41d6c7ca7a04b7d73af6514df10a3e74bd82"},
{file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5df2768244d19ab7f60546d0c7c63ce1581f7af8b5de3eb3004b9b6fc8a9f84b"},
{file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a8c4917bd7ad33e8eb21e9a5bbba979b49d9a97acb3a803092cbc1133e20343c"},
{file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0e2642fe3142e4cc4af0799748233ad6da94c62a8bec3a6648bf8ee68b1c7426"},
{file = "cffi-1.15.1-cp37-cp37m-win32.whl", hash = "sha256:e229a521186c75c8ad9490854fd8bbdd9a0c9aa3a524326b55be83b54d4e0ad9"},
{file = "cffi-1.15.1-cp37-cp37m-win_amd64.whl", hash = "sha256:a0b71b1b8fbf2b96e41c4d990244165e2c9be83d54962a9a1d118fd8657d2045"},
{file = "cffi-1.15.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:320dab6e7cb2eacdf0e658569d2575c4dad258c0fcc794f46215e1e39f90f2c3"},
{file = "cffi-1.15.1-cp38-cp38-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1e74c6b51a9ed6589199c787bf5f9875612ca4a8a0785fb2d4a84429badaf22a"},
{file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a5c84c68147988265e60416b57fc83425a78058853509c1b0629c180094904a5"},
{file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3b926aa83d1edb5aa5b427b4053dc420ec295a08e40911296b9eb1b6170f6cca"},
{file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87c450779d0914f2861b8526e035c5e6da0a3199d8f1add1a665e1cbc6fc6d02"},
{file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4f2c9f67e9821cad2e5f480bc8d83b8742896f1242dba247911072d4fa94c192"},
{file = "cffi-1.15.1-cp38-cp38-win32.whl", hash = "sha256:8b7ee99e510d7b66cdb6c593f21c043c248537a32e0bedf02e01e9553a172314"},
{file = "cffi-1.15.1-cp38-cp38-win_amd64.whl", hash = "sha256:00a9ed42e88df81ffae7a8ab6d9356b371399b91dbdf0c3cb1e84c03a13aceb5"},
{file = "cffi-1.15.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:54a2db7b78338edd780e7ef7f9f6c442500fb0d41a5a4ea24fff1c929d5af585"},
{file = "cffi-1.15.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:fcd131dd944808b5bdb38e6f5b53013c5aa4f334c5cad0c72742f6eba4b73db0"},
{file = "cffi-1.15.1-cp39-cp39-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7473e861101c9e72452f9bf8acb984947aa1661a7704553a9f6e4baa5ba64415"},
{file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6c9a799e985904922a4d207a94eae35c78ebae90e128f0c4e521ce339396be9d"},
{file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3bcde07039e586f91b45c88f8583ea7cf7a0770df3a1649627bf598332cb6984"},
{file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:33ab79603146aace82c2427da5ca6e58f2b3f2fb5da893ceac0c42218a40be35"},
{file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5d598b938678ebf3c67377cdd45e09d431369c3b1a5b331058c338e201f12b27"},
{file = "cffi-1.15.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:db0fbb9c62743ce59a9ff687eb5f4afbe77e5e8403d6697f7446e5f609976f76"},
{file = "cffi-1.15.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:98d85c6a2bef81588d9227dde12db8a7f47f639f4a17c9ae08e773aa9c697bf3"},
{file = "cffi-1.15.1-cp39-cp39-win32.whl", hash = "sha256:40f4774f5a9d4f5e344f31a32b5096977b5d48560c5592e2f3d2c4374bd543ee"},
{file = "cffi-1.15.1-cp39-cp39-win_amd64.whl", hash = "sha256:70df4e3b545a17496c9b3f41f5115e69a4f2e77e94e1d2a8e1070bc0c38c8a3c"},
{file = "cffi-1.15.1.tar.gz", hash = "sha256:d400bfb9a37b1351253cb402671cea7e89bdecc294e8016a707f6d1d8ac934f9"},
]
click = [
{file = "click-8.1.3-py3-none-any.whl", hash = "sha256:bb4d8133cb15a609f44e8213d9b391b0809795062913b383c62be0ee95b1db48"},
{file = "click-8.1.3.tar.gz", hash = "sha256:7682dc8afb30297001674575ea00d1814d808d6a36af415a82bd481d37ba7b8e"},
]
colorama = [
{file = "colorama-0.4.5-py2.py3-none-any.whl", hash = "sha256:854bf444933e37f5824ae7bfc1e98d5bce2ebe4160d46b5edf346a89358e99da"},
{file = "colorama-0.4.5.tar.gz", hash = "sha256:e6c6b4334fc50988a639d9b98aa429a0b57da6e17b9a44f0451f930b6967b7a4"},
]
cryptography = [
{file = "cryptography-38.0.1-cp36-abi3-macosx_10_10_universal2.whl", hash = "sha256:10d1f29d6292fc95acb597bacefd5b9e812099d75a6469004fd38ba5471a977f"},
{file = "cryptography-38.0.1-cp36-abi3-macosx_10_10_x86_64.whl", hash = "sha256:3fc26e22840b77326a764ceb5f02ca2d342305fba08f002a8c1f139540cdfaad"},
{file = "cryptography-38.0.1-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_24_aarch64.whl", hash = "sha256:3b72c360427889b40f36dc214630e688c2fe03e16c162ef0aa41da7ab1455153"},
{file = "cryptography-38.0.1-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:194044c6b89a2f9f169df475cc167f6157eb9151cc69af8a2a163481d45cc407"},
{file = "cryptography-38.0.1-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ca9f6784ea96b55ff41708b92c3f6aeaebde4c560308e5fbbd3173fbc466e94e"},
{file = "cryptography-38.0.1-cp36-abi3-manylinux_2_24_x86_64.whl", hash = "sha256:16fa61e7481f4b77ef53991075de29fc5bacb582a1244046d2e8b4bb72ef66d0"},
{file = "cryptography-38.0.1-cp36-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:d4ef6cc305394ed669d4d9eebf10d3a101059bdcf2669c366ec1d14e4fb227bd"},
{file = "cryptography-38.0.1-cp36-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:3261725c0ef84e7592597606f6583385fed2a5ec3909f43bc475ade9729a41d6"},
{file = "cryptography-38.0.1-cp36-abi3-musllinux_1_1_aarch64.whl", hash = "sha256:0297ffc478bdd237f5ca3a7dc96fc0d315670bfa099c04dc3a4a2172008a405a"},
{file = "cryptography-38.0.1-cp36-abi3-musllinux_1_1_x86_64.whl", hash = "sha256:89ed49784ba88c221756ff4d4755dbc03b3c8d2c5103f6d6b4f83a0fb1e85294"},
{file = "cryptography-38.0.1-cp36-abi3-win32.whl", hash = "sha256:ac7e48f7e7261207d750fa7e55eac2d45f720027d5703cd9007e9b37bbb59ac0"},
{file = "cryptography-38.0.1-cp36-abi3-win_amd64.whl", hash = "sha256:ad7353f6ddf285aeadfaf79e5a6829110106ff8189391704c1d8801aa0bae45a"},
{file = "cryptography-38.0.1-pp37-pypy37_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:896dd3a66959d3a5ddcfc140a53391f69ff1e8f25d93f0e2e7830c6de90ceb9d"},
{file = "cryptography-38.0.1-pp37-pypy37_pp73-manylinux_2_24_x86_64.whl", hash = "sha256:d3971e2749a723e9084dd507584e2a2761f78ad2c638aa31e80bc7a15c9db4f9"},
{file = "cryptography-38.0.1-pp37-pypy37_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:79473cf8a5cbc471979bd9378c9f425384980fcf2ab6534b18ed7d0d9843987d"},
{file = "cryptography-38.0.1-pp38-pypy38_pp73-macosx_10_10_x86_64.whl", hash = "sha256:d9e69ae01f99abe6ad646947bba8941e896cb3aa805be2597a0400e0764b5818"},
{file = "cryptography-38.0.1-pp38-pypy38_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5067ee7f2bce36b11d0e334abcd1ccf8c541fc0bbdaf57cdd511fdee53e879b6"},
{file = "cryptography-38.0.1-pp38-pypy38_pp73-manylinux_2_24_x86_64.whl", hash = "sha256:3e3a2599e640927089f932295a9a247fc40a5bdf69b0484532f530471a382750"},
{file = "cryptography-38.0.1-pp38-pypy38_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:c2e5856248a416767322c8668ef1845ad46ee62629266f84a8f007a317141013"},
{file = "cryptography-38.0.1-pp38-pypy38_pp73-win_amd64.whl", hash = "sha256:64760ba5331e3f1794d0bcaabc0d0c39e8c60bf67d09c93dc0e54189dfd7cfe5"},
{file = "cryptography-38.0.1-pp39-pypy39_pp73-macosx_10_10_x86_64.whl", hash = "sha256:b6c9b706316d7b5a137c35e14f4103e2115b088c412140fdbd5f87c73284df61"},
{file = "cryptography-38.0.1-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b0163a849b6f315bf52815e238bc2b2346604413fa7c1601eea84bcddb5fb9ac"},
{file = "cryptography-38.0.1-pp39-pypy39_pp73-manylinux_2_24_x86_64.whl", hash = "sha256:d1a5bd52d684e49a36582193e0b89ff267704cd4025abefb9e26803adeb3e5fb"},
{file = "cryptography-38.0.1-pp39-pypy39_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:765fa194a0f3372d83005ab83ab35d7c5526c4e22951e46059b8ac678b44fa5a"},
{file = "cryptography-38.0.1-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:52e7bee800ec869b4031093875279f1ff2ed12c1e2f74923e8f49c916afd1d3b"},
{file = "cryptography-38.0.1.tar.gz", hash = "sha256:1db3d807a14931fa317f96435695d9ec386be7b84b618cc61cfa5d08b0ae33d7"},
]
dnspython = [
{file = "dnspython-2.2.1-py3-none-any.whl", hash = "sha256:a851e51367fb93e9e1361732c1d60dab63eff98712e503ea7d92e6eccb109b4f"},
{file = "dnspython-2.2.1.tar.gz", hash = "sha256:0f7569a4a6ff151958b64304071d370daa3243d15941a7beedf0c9fe5105603e"},
]
ecdsa = [
{file = "ecdsa-0.18.0-py2.py3-none-any.whl", hash = "sha256:80600258e7ed2f16b9aa1d7c295bd70194109ad5a30fdee0eaeefef1d4c559dd"},
{file = "ecdsa-0.18.0.tar.gz", hash = "sha256:190348041559e21b22a1d65cee485282ca11a6f81d503fddb84d5017e9ed1e49"},
]
email-validator = [
{file = "email_validator-1.2.1-py2.py3-none-any.whl", hash = "sha256:c8589e691cf73eb99eed8d10ce0e9cbb05a0886ba920c8bcb7c82873f4c5789c"},
{file = "email_validator-1.2.1.tar.gz", hash = "sha256:6757aea012d40516357c0ac2b1a4c31219ab2f899d26831334c5d069e8b6c3d8"},
]
fastapi = [
{file = "fastapi-0.83.0-py3-none-any.whl", hash = "sha256:694a2b6c2607a61029a4be1c6613f84d74019cb9f7a41c7a475dca8e715f9368"},
{file = "fastapi-0.83.0.tar.gz", hash = "sha256:96eb692350fe13d7a9843c3c87a874f0d45102975257dd224903efd6c0fde3bd"},
]
fastapi-mail = [
{file = "fastapi-mail-1.1.4.tar.gz", hash = "sha256:6ff9a189f338c1a6b2236adbee1eb7930470e00bd0ae5cc382b878bca6b9d29c"},
{file = "fastapi_mail-1.1.4-py3-none-any.whl", hash = "sha256:bb381dd88588a2f90db7333878c66f458b470d762f3b724c3ecc92b0acbce67d"},
]
greenlet = [
{file = "greenlet-1.1.3-cp27-cp27m-macosx_10_14_x86_64.whl", hash = "sha256:8c287ae7ac921dfde88b1c125bd9590b7ec3c900c2d3db5197f1286e144e712b"},
{file = "greenlet-1.1.3-cp27-cp27m-manylinux1_x86_64.whl", hash = "sha256:870a48007872d12e95a996fca3c03a64290d3ea2e61076aa35d3b253cf34cd32"},
{file = "greenlet-1.1.3-cp27-cp27m-manylinux2010_x86_64.whl", hash = "sha256:7c5227963409551ae4a6938beb70d56bf1918c554a287d3da6853526212fbe0a"},
{file = "greenlet-1.1.3-cp27-cp27m-win32.whl", hash = "sha256:9fae214f6c43cd47f7bef98c56919b9222481e833be2915f6857a1e9e8a15318"},
{file = "greenlet-1.1.3-cp27-cp27m-win_amd64.whl", hash = "sha256:de431765bd5fe62119e0bc6bc6e7b17ac53017ae1782acf88fcf6b7eae475a49"},
{file = "greenlet-1.1.3-cp27-cp27mu-manylinux1_x86_64.whl", hash = "sha256:510c3b15587afce9800198b4b142202b323bf4b4b5f9d6c79cb9a35e5e3c30d2"},
{file = "greenlet-1.1.3-cp27-cp27mu-manylinux2010_x86_64.whl", hash = "sha256:9951dcbd37850da32b2cb6e391f621c1ee456191c6ae5528af4a34afe357c30e"},
{file = "greenlet-1.1.3-cp310-cp310-macosx_10_15_x86_64.whl", hash = "sha256:07c58e169bbe1e87b8bbf15a5c1b779a7616df9fd3e61cadc9d691740015b4f8"},
{file = "greenlet-1.1.3-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:df02fdec0c533301497acb0bc0f27f479a3a63dcdc3a099ae33a902857f07477"},
{file = "greenlet-1.1.3-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9c88e134d51d5e82315a7c32b914a58751b7353eb5268dbd02eabf020b4c4700"},
{file = "greenlet-1.1.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7b41d19c0cfe5c259fe6c539fd75051cd39a5d33d05482f885faf43f7f5e7d26"},
{file = "greenlet-1.1.3-cp310-cp310-win_amd64.whl", hash = "sha256:6f5d4b2280ceea76c55c893827961ed0a6eadd5a584a7c4e6e6dd7bc10dfdd96"},
{file = "greenlet-1.1.3-cp311-cp311-macosx_10_15_x86_64.whl", hash = "sha256:184416e481295832350a4bf731ba619a92f5689bf5d0fa4341e98b98b1265bd7"},
{file = "greenlet-1.1.3-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:dd0404d154084a371e6d2bafc787201612a1359c2dee688ae334f9118aa0bf47"},
{file = "greenlet-1.1.3-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7a43bbfa9b6cfdfaeefbd91038dde65ea2c421dc387ed171613df340650874f2"},
{file = "greenlet-1.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce5b64dfe8d0cca407d88b0ee619d80d4215a2612c1af8c98a92180e7109f4b5"},
{file = "greenlet-1.1.3-cp35-cp35m-macosx_10_14_x86_64.whl", hash = "sha256:903fa5716b8fbb21019268b44f73f3748c41d1a30d71b4a49c84b642c2fed5fa"},
{file = "greenlet-1.1.3-cp35-cp35m-manylinux1_x86_64.whl", hash = "sha256:0118817c9341ef2b0f75f5af79ac377e4da6ff637e5ee4ac91802c0e379dadb4"},
{file = "greenlet-1.1.3-cp35-cp35m-manylinux2010_x86_64.whl", hash = "sha256:466ce0928e33421ee84ae04c4ac6f253a3a3e6b8d600a79bd43fd4403e0a7a76"},
{file = "greenlet-1.1.3-cp35-cp35m-win32.whl", hash = "sha256:65ad1a7a463a2a6f863661329a944a5802c7129f7ad33583dcc11069c17e622c"},
{file = "greenlet-1.1.3-cp35-cp35m-win_amd64.whl", hash = "sha256:7532a46505470be30cbf1dbadb20379fb481244f1ca54207d7df3bf0bbab6a20"},
{file = "greenlet-1.1.3-cp36-cp36m-macosx_10_14_x86_64.whl", hash = "sha256:caff52cb5cd7626872d9696aee5b794abe172804beb7db52eed1fd5824b63910"},
{file = "greenlet-1.1.3-cp36-cp36m-manylinux1_x86_64.whl", hash = "sha256:db41f3845eb579b544c962864cce2c2a0257fe30f0f1e18e51b1e8cbb4e0ac6d"},
{file = "greenlet-1.1.3-cp36-cp36m-manylinux2010_x86_64.whl", hash = "sha256:e8533f5111704d75de3139bf0b8136d3a6c1642c55c067866fa0a51c2155ee33"},
{file = "greenlet-1.1.3-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9537e4baf0db67f382eb29255a03154fcd4984638303ff9baaa738b10371fa57"},
{file = "greenlet-1.1.3-cp36-cp36m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f8bfd36f368efe0ab2a6aa3db7f14598aac454b06849fb633b762ddbede1db90"},
{file = "greenlet-1.1.3-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b0877a9a2129a2c56a2eae2da016743db7d9d6a05d5e1c198f1b7808c602a30e"},
{file = "greenlet-1.1.3-cp36-cp36m-win32.whl", hash = "sha256:88b04e12c9b041a1e0bcb886fec709c488192638a9a7a3677513ac6ba81d8e79"},
{file = "greenlet-1.1.3-cp36-cp36m-win_amd64.whl", hash = "sha256:4f166b4aca8d7d489e82d74627a7069ab34211ef5ebb57c300ec4b9337b60fc0"},
{file = "greenlet-1.1.3-cp37-cp37m-macosx_10_15_x86_64.whl", hash = "sha256:cd16a89efe3a003029c87ff19e9fba635864e064da646bc749fc1908a4af18f3"},
{file = "greenlet-1.1.3-cp37-cp37m-manylinux1_x86_64.whl", hash = "sha256:5b756e6730ea59b2745072e28ad27f4c837084688e6a6b3633c8b1e509e6ae0e"},
{file = "greenlet-1.1.3-cp37-cp37m-manylinux2010_x86_64.whl", hash = "sha256:9b2f7d0408ddeb8ea1fd43d3db79a8cefaccadd2a812f021333b338ed6b10aba"},
{file = "greenlet-1.1.3-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:44b4817c34c9272c65550b788913620f1fdc80362b209bc9d7dd2f40d8793080"},
{file = "greenlet-1.1.3-cp37-cp37m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d58a5a71c4c37354f9e0c24c9c8321f0185f6945ef027460b809f4bb474bfe41"},
{file = "greenlet-1.1.3-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1dd51d2650e70c6c4af37f454737bf4a11e568945b27f74b471e8e2a9fd21268"},
{file = "greenlet-1.1.3-cp37-cp37m-win32.whl", hash = "sha256:048d2bed76c2aa6de7af500ae0ea51dd2267aec0e0f2a436981159053d0bc7cc"},
{file = "greenlet-1.1.3-cp37-cp37m-win_amd64.whl", hash = "sha256:77e41db75f9958f2083e03e9dd39da12247b3430c92267df3af77c83d8ff9eed"},
{file = "greenlet-1.1.3-cp38-cp38-macosx_10_15_x86_64.whl", hash = "sha256:1626185d938d7381631e48e6f7713e8d4b964be246073e1a1d15c2f061ac9f08"},
{file = "greenlet-1.1.3-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:1ec2779774d8e42ed0440cf8bc55540175187e8e934f2be25199bf4ed948cd9e"},
{file = "greenlet-1.1.3-cp38-cp38-manylinux2010_x86_64.whl", hash = "sha256:f2f908239b7098799b8845e5936c2ccb91d8c2323be02e82f8dcb4a80dcf4a25"},
{file = "greenlet-1.1.3-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0b181e9aa6cb2f5ec0cacc8cee6e5a3093416c841ba32c185c30c160487f0380"},
{file = "greenlet-1.1.3-cp38-cp38-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2cf45e339cabea16c07586306a31cfcc5a3b5e1626d365714d283732afed6809"},
{file = "greenlet-1.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6200a11f003ec26815f7e3d2ded01b43a3810be3528dd760d2f1fa777490c3cd"},
{file = "greenlet-1.1.3-cp38-cp38-win32.whl", hash = "sha256:db5b25265010a1b3dca6a174a443a0ed4c4ab12d5e2883a11c97d6e6d59b12f9"},
{file = "greenlet-1.1.3-cp38-cp38-win_amd64.whl", hash = "sha256:095a980288fe05adf3d002fbb180c99bdcf0f930e220aa66fcd56e7914a38202"},
{file = "greenlet-1.1.3-cp39-cp39-macosx_10_15_x86_64.whl", hash = "sha256:cbc1eb55342cbac8f7ec159088d54e2cfdd5ddf61c87b8bbe682d113789331b2"},
{file = "greenlet-1.1.3-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:694ffa7144fa5cc526c8f4512665003a39fa09ef00d19bbca5c8d3406db72fbe"},
{file = "greenlet-1.1.3-cp39-cp39-manylinux2010_x86_64.whl", hash = "sha256:aa741c1a8a8cc25eb3a3a01a62bdb5095a773d8c6a86470bde7f607a447e7905"},
{file = "greenlet-1.1.3-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a3a669f11289a8995d24fbfc0e63f8289dd03c9aaa0cc8f1eab31d18ca61a382"},
{file = "greenlet-1.1.3-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:76a53bfa10b367ee734b95988bd82a9a5f0038a25030f9f23bbbc005010ca600"},
{file = "greenlet-1.1.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2fb0aa7f6996879551fd67461d5d3ab0c3c0245da98be90c89fcb7a18d437403"},
{file = "greenlet-1.1.3-cp39-cp39-win32.whl", hash = "sha256:5fbe1ab72b998ca77ceabbae63a9b2e2dc2d963f4299b9b278252ddba142d3f1"},
{file = "greenlet-1.1.3-cp39-cp39-win_amd64.whl", hash = "sha256:ffe73f9e7aea404722058405ff24041e59d31ca23d1da0895af48050a07b6932"},
{file = "greenlet-1.1.3.tar.gz", hash = "sha256:bcb6c6dd1d6be6d38d6db283747d07fda089ff8c559a835236560a4410340455"},
]
h11 = [
{file = "h11-0.13.0-py3-none-any.whl", hash = "sha256:8ddd78563b633ca55346c8cd41ec0af27d3c79931828beffb46ce70a379e7442"},
{file = "h11-0.13.0.tar.gz", hash = "sha256:70813c1135087a248a4d38cc0e1a0181ffab2188141a93eaf567940c3957ff06"},
]
idna = [
{file = "idna-3.3-py3-none-any.whl", hash = "sha256:84d9dd047ffa80596e0f246e2eab0b391788b0503584e8945f2368256d2735ff"},
{file = "idna-3.3.tar.gz", hash = "sha256:9d643ff0a55b762d5cdb124b8eaa99c66322e2157b69160bc32796e824360e6d"},
]
Jinja2 = [
{file = "Jinja2-3.1.2-py3-none-any.whl", hash = "sha256:6088930bfe239f0e6710546ab9c19c9ef35e29792895fed6e6e31a023a182a61"},
{file = "Jinja2-3.1.2.tar.gz", hash = "sha256:31351a702a408a9e7595a8fc6150fc3f43bb6bf7e319770cbc0db9df9437e852"},
]
Mako = [
{file = "Mako-1.2.3-py3-none-any.whl", hash = "sha256:c413a086e38cd885088d5e165305ee8eed04e8b3f8f62df343480da0a385735f"},
{file = "Mako-1.2.3.tar.gz", hash = "sha256:7fde96466fcfeedb0eed94f187f20b23d85e4cb41444be0e542e2c8c65c396cd"},
]
MarkupSafe = [
{file = "MarkupSafe-2.1.1-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:86b1f75c4e7c2ac2ccdaec2b9022845dbb81880ca318bb7a0a01fbf7813e3812"},
{file = "MarkupSafe-2.1.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f121a1420d4e173a5d96e47e9a0c0dcff965afdf1626d28de1460815f7c4ee7a"},
{file = "MarkupSafe-2.1.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a49907dd8420c5685cfa064a1335b6754b74541bbb3706c259c02ed65b644b3e"},
{file = "MarkupSafe-2.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:10c1bfff05d95783da83491be968e8fe789263689c02724e0c691933c52994f5"},
{file = "MarkupSafe-2.1.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b7bd98b796e2b6553da7225aeb61f447f80a1ca64f41d83612e6139ca5213aa4"},
{file = "MarkupSafe-2.1.1-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:b09bf97215625a311f669476f44b8b318b075847b49316d3e28c08e41a7a573f"},
{file = "MarkupSafe-2.1.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:694deca8d702d5db21ec83983ce0bb4b26a578e71fbdbd4fdcd387daa90e4d5e"},
{file = "MarkupSafe-2.1.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:efc1913fd2ca4f334418481c7e595c00aad186563bbc1ec76067848c7ca0a933"},
{file = "MarkupSafe-2.1.1-cp310-cp310-win32.whl", hash = "sha256:4a33dea2b688b3190ee12bd7cfa29d39c9ed176bda40bfa11099a3ce5d3a7ac6"},
{file = "MarkupSafe-2.1.1-cp310-cp310-win_amd64.whl", hash = "sha256:dda30ba7e87fbbb7eab1ec9f58678558fd9a6b8b853530e176eabd064da81417"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:671cd1187ed5e62818414afe79ed29da836dde67166a9fac6d435873c44fdd02"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3799351e2336dc91ea70b034983ee71cf2f9533cdff7c14c90ea126bfd95d65a"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e72591e9ecd94d7feb70c1cbd7be7b3ebea3f548870aa91e2732960fa4d57a37"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:6fbf47b5d3728c6aea2abb0589b5d30459e369baa772e0f37a0320185e87c980"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:d5ee4f386140395a2c818d149221149c54849dfcfcb9f1debfe07a8b8bd63f9a"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:bcb3ed405ed3222f9904899563d6fc492ff75cce56cba05e32eff40e6acbeaa3"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:e1c0b87e09fa55a220f058d1d49d3fb8df88fbfab58558f1198e08c1e1de842a"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-win32.whl", hash = "sha256:8dc1c72a69aa7e082593c4a203dcf94ddb74bb5c8a731e4e1eb68d031e8498ff"},
{file = "MarkupSafe-2.1.1-cp37-cp37m-win_amd64.whl", hash = "sha256:97a68e6ada378df82bc9f16b800ab77cbf4b2fada0081794318520138c088e4a"},
{file = "MarkupSafe-2.1.1-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:e8c843bbcda3a2f1e3c2ab25913c80a3c5376cd00c6e8c4a86a89a28c8dc5452"},
{file = "MarkupSafe-2.1.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:0212a68688482dc52b2d45013df70d169f542b7394fc744c02a57374a4207003"},
{file = "MarkupSafe-2.1.1-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8e576a51ad59e4bfaac456023a78f6b5e6e7651dcd383bcc3e18d06f9b55d6d1"},
{file = "MarkupSafe-2.1.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4b9fe39a2ccc108a4accc2676e77da025ce383c108593d65cc909add5c3bd601"},
{file = "MarkupSafe-2.1.1-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:96e37a3dc86e80bf81758c152fe66dbf60ed5eca3d26305edf01892257049925"},
{file = "MarkupSafe-2.1.1-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:6d0072fea50feec76a4c418096652f2c3238eaa014b2f94aeb1d56a66b41403f"},
{file = "MarkupSafe-2.1.1-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:089cf3dbf0cd6c100f02945abeb18484bd1ee57a079aefd52cffd17fba910b88"},
{file = "MarkupSafe-2.1.1-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:6a074d34ee7a5ce3effbc526b7083ec9731bb3cbf921bbe1d3005d4d2bdb3a63"},
{file = "MarkupSafe-2.1.1-cp38-cp38-win32.whl", hash = "sha256:421be9fbf0ffe9ffd7a378aafebbf6f4602d564d34be190fc19a193232fd12b1"},
{file = "MarkupSafe-2.1.1-cp38-cp38-win_amd64.whl", hash = "sha256:fc7b548b17d238737688817ab67deebb30e8073c95749d55538ed473130ec0c7"},
{file = "MarkupSafe-2.1.1-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:e04e26803c9c3851c931eac40c695602c6295b8d432cbe78609649ad9bd2da8a"},
{file = "MarkupSafe-2.1.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:b87db4360013327109564f0e591bd2a3b318547bcef31b468a92ee504d07ae4f"},
{file = "MarkupSafe-2.1.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:99a2a507ed3ac881b975a2976d59f38c19386d128e7a9a18b7df6fff1fd4c1d6"},
{file = "MarkupSafe-2.1.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:56442863ed2b06d19c37f94d999035e15ee982988920e12a5b4ba29b62ad1f77"},
{file = "MarkupSafe-2.1.1-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3ce11ee3f23f79dbd06fb3d63e2f6af7b12db1d46932fe7bd8afa259a5996603"},
{file = "MarkupSafe-2.1.1-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:33b74d289bd2f5e527beadcaa3f401e0df0a89927c1559c8566c066fa4248ab7"},
{file = "MarkupSafe-2.1.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:43093fb83d8343aac0b1baa75516da6092f58f41200907ef92448ecab8825135"},
{file = "MarkupSafe-2.1.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:8e3dcf21f367459434c18e71b2a9532d96547aef8a871872a5bd69a715c15f96"},
{file = "MarkupSafe-2.1.1-cp39-cp39-win32.whl", hash = "sha256:d4306c36ca495956b6d568d276ac11fdd9c30a36f1b6eb928070dc5360b22e1c"},
{file = "MarkupSafe-2.1.1-cp39-cp39-win_amd64.whl", hash = "sha256:46d00d6cfecdde84d40e572d63735ef81423ad31184100411e6e3388d405e247"},
{file = "MarkupSafe-2.1.1.tar.gz", hash = "sha256:7f91197cc9e48f989d12e4e6fbc46495c446636dfc81b9ccf50bb0ec74b91d4b"},
]
mypy-extensions = [
{file = "mypy_extensions-0.4.3-py2.py3-none-any.whl", hash = "sha256:090fedd75945a69ae91ce1303b5824f428daf5a028d2f6ab8a299250a846f15d"},
{file = "mypy_extensions-0.4.3.tar.gz", hash = "sha256:2d82818f5bb3e369420cb3c4060a7970edba416647068eb4c5343488a6c604a8"},
]
passlib = [
{file = "passlib-1.7.4-py2.py3-none-any.whl", hash = "sha256:aa6bca462b8d8bda89c70b382f0c298a20b5560af6cbfa2dce410c0a2fb669f1"},
{file = "passlib-1.7.4.tar.gz", hash = "sha256:defd50f72b65c5402ab2c573830a6978e5f202ad0d984793c8dde2c4152ebe04"},
]
pathspec = [
{file = "pathspec-0.10.1-py3-none-any.whl", hash = "sha256:46846318467efc4556ccfd27816e004270a9eeeeb4d062ce5e6fc7a87c573f93"},
{file = "pathspec-0.10.1.tar.gz", hash = "sha256:7ace6161b621d31e7902eb6b5ae148d12cfd23f4a249b9ffb6b9fee12084323d"},
]
platformdirs = [
{file = "platformdirs-2.5.2-py3-none-any.whl", hash = "sha256:027d8e83a2d7de06bbac4e5ef7e023c02b863d7ea5d079477e722bb41ab25788"},
{file = "platformdirs-2.5.2.tar.gz", hash = "sha256:58c8abb07dcb441e6ee4b11d8df0ac856038f944ab98b7be6b27b2a3c7feef19"},
]
psycopg2-binary = [
{file = "psycopg2-binary-2.9.4.tar.gz", hash = "sha256:a6a2d3d75d8698dee492f4af7ad07606d0734e581edf9e2ce2f74b6fce90f42e"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-macosx_10_15_x86_64.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl", hash = "sha256:e72491d72870c3cb2f0d6f4174485533caec0e9ed7e717e2859b7cc7ff2ae1c4"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:2903bf90b1e6bfc9bbfc94a1db0b50ffa9830a0ca4c042fbc38d93890c02ce08"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:15e0ac0ed8a85f6049e836e95ddee627766561c85be8d23f4b3edb6ddbaa7310"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:edf0a66ce9517365c7dcfed597894d8dd1f27b59e550b77a089054101435213b"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-manylinux_2_24_aarch64.whl", hash = "sha256:61c6a258469c66412ae8358a0501df6ccb3bb48aa9c43b56624571ff9767f91d"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-manylinux_2_24_ppc64le.whl", hash = "sha256:704f1fcdc5b606b70563ea696c69bda90caee3a2f45ffc9cee60a901b394a79f"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:30200b07779446760813eef06098ec6d084131e4365b4e023eb43100de758b11"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:f5fbb3b325c65010e04af206a9243e2df8606736c510c7f268aca6a93e5294a9"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-musllinux_1_1_ppc64le.whl", hash = "sha256:52383e932e6de5595963f9178cf2af7b9e1f3daacf5135b9c0e21aabbc5bf7c4"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:0d8e0c9eec79fe1ae66691e06e3cc714da6fbd77981209bf32fa823c03dbaff8"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-win32.whl", hash = "sha256:161dc52a617f0bb610a87d391cb2e77fe65b89ebfbd752f4f3217dde701ea196"},
{file = "psycopg2_binary-2.9.4-cp310-cp310-win_amd64.whl", hash = "sha256:33ac8b4754e6b6b21f3ee180da169d8526d91aee9408ec1fc573c16ab32b0207"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-macosx_10_14_x86_64.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl", hash = "sha256:7751b11cd7f6b952b4b5ec5b93b5be9ce20faba786c18c25c354f5d8717a173c"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b216a15e13f6e763db40ac3beb74b588650bc030d10a78fde182b88d273b82b5"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0eae72190be519bf2629062eab7ac8d4ceec5bd132953cefa1596584d86964fe"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-manylinux_2_24_aarch64.whl", hash = "sha256:fb639a0e65dce4a9cccbcbdd8ddd0c8c6ab10bca317b827a5c52ac3c3a4ad60a"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-manylinux_2_24_ppc64le.whl", hash = "sha256:80ed219ce6cb21a5b53ead0edf5b56b6d23de4cb95389ac606f47670474f4816"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-musllinux_1_1_aarch64.whl", hash = "sha256:f78cafa25731e0b5aa16fe20bea1abf643d4e853f6bfb8a64421b06b878e2b88"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-musllinux_1_1_i686.whl", hash = "sha256:34fd249275faa782c3a2016e86ac2330636ac58d731a1580e7d686e3976b9536"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-musllinux_1_1_ppc64le.whl", hash = "sha256:24d627ed69e754c48dd142a914124858c600b4108c92546eb0ba822e63c0c6e2"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-musllinux_1_1_x86_64.whl", hash = "sha256:65d5f4e70a2d3fbaa1349236968792611088f3f2dccead36c1626e1d183cc327"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-win32.whl", hash = "sha256:ae5b41dbf7731b838021923edfbe3b5ccdec84d92d5795f5229c0d08d32509d9"},
{file = "psycopg2_binary-2.9.4-cp36-cp36m-win_amd64.whl", hash = "sha256:97e4f3d9b17d12e7c00cb1c29c0040044135cd5146838da4274615dbe0baae78"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-macosx_10_15_x86_64.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl", hash = "sha256:8660112e9127a019969a23c878e1b4a419e8a6427f9a9050c19830f152628c8a"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ea8d5cd689fa7225d81ae0a049ba03e0165f4ed9ca083b19a405be9ad0b36845"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:63edc507f8cbfbb5903adb75bad8a99f9798981c854df9119dbebab2ec3ee0e1"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-manylinux_2_24_aarch64.whl", hash = "sha256:25e0517ad7ee3c5c3c69dbe3c1d95504c811e42f452b39a3505d0763b1f6caa0"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-manylinux_2_24_ppc64le.whl", hash = "sha256:0a9465f0aa36480c8e7614991cbe8ca8aa16b0517c5398a49648ce345e446c19"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:aff258af03dda9a990960a53759d10c3a9b936837c71fe2f3b581acd356b9121"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:576b9dfbcd154a0e8b5d9dae6316d037450e64a3b31df87dec71d88e2a2d5e5f"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-musllinux_1_1_ppc64le.whl", hash = "sha256:044b6ab68613de7ea1e63856627deea091bfea09dea5ab4f050b13250fd18cab"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:7b47643c45e7619788c081d42e1d9d98c7c8a4933010a9967d097cc3c4c29f41"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-win32.whl", hash = "sha256:82df4a8600999c4c0cb7d6614df1bbdb3c74732f63e79f78487893ffbed3d083"},
{file = "psycopg2_binary-2.9.4-cp37-cp37m-win_amd64.whl", hash = "sha256:8d7bc25729bb6d96b44f49ad78fde0e27a1a867cb205322b7e5f5b49e04d6f1f"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-macosx_10_15_x86_64.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl", hash = "sha256:2f1ded23d17af0d738e7e78087f0b88a53228887845b1989b03af4dfd3fef703"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:f225784812b2b57d340f2eb0d2cebef989dcc82c288f5553e28ee9767c7c8344"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:89a86c2b35460700d04b4d6461153ab39ee85af5a5385acac9563a8310e6320a"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:59a3010d566a48b919490a982f6807f68842686941dc12d568e129d9cd7703d6"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-manylinux_2_24_aarch64.whl", hash = "sha256:02cde837df012fa5d579b9cf4bc8e1feb460f38d61f7a4ab4a919d55a9f6eeef"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-manylinux_2_24_ppc64le.whl", hash = "sha256:226f11be577b70a57f4910c0ee28591d4d9fcb3d455e966267179156ae2e0c41"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:181ac372a5a5308b4076933601a9b5f0cd139b389b0aa5e164786a2abbcdb978"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:d5f27b1d1b56470385faa2b2636fcb823e7ac5b5b734e0aa76b14637c66eb3b7"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-musllinux_1_1_ppc64le.whl", hash = "sha256:55137faec669c4277c5687c6ce7c1fbc4dece0e2f14256ee808f4a652f0a2170"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:ffb2f288f577a748cc23c65a818290755a4c2da1f87a40d7055b61a096d31e20"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-win32.whl", hash = "sha256:451550e0bb5889bbabbf92575a6d6eafced941cc28c86be6ae4667f81bf32d67"},
{file = "psycopg2_binary-2.9.4-cp38-cp38-win_amd64.whl", hash = "sha256:b23b25b1243576b952689966205ef7d4285688068b966a1ca0e620bcb390d483"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-macosx_10_15_x86_64.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl", hash = "sha256:7ad9d032dc1a31a86ca7b059f43554a049a2bfda8fe32d1492ad25f6686aff03"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:7b01d07006a0ac2216921b69a220b9f0974345d0b1b36efaeabdc7550b1cc4f8"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:eb5341fc7c53fdd95ac2415be77b1de854ab266488cff71174ebb007baf0e675"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a431deb6ffdfa551f7400b3a94fa4b964837e67f49e3c37aa26d90dc75970816"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-manylinux_2_24_aarch64.whl", hash = "sha256:d6ba33f39436191ece7ea2b3d0b4dff00af71acd5c6e6f1d6b7563aa7286e9f2"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-manylinux_2_24_ppc64le.whl", hash = "sha256:d6c5e1df6f427d7a82606cf8f07cf3ba9fb3f366804b01e65f1f00f8df6b54f1"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:1c22c59ab7d9dc110d409445f111f58556bf699b0548f3fc5176684a29c629c4"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:b896637091cde69d170a89253dde9aee814b25ca204b7e213fd0a6462e666638"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-musllinux_1_1_ppc64le.whl", hash = "sha256:2535f44b00f26f6af0e949c825e6aecb9adcb56c965c17af5b97137fb69f00c0"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:6a1618260a112a9c93504511f0b6254b4402a8c41b7130dc6d4c9e39aff3aa0c"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-win32.whl", hash = "sha256:e02f77b620ad6b36564fe41980865436912e21a3b1138cdde175cf24afde1bc5"},
{file = "psycopg2_binary-2.9.4-cp39-cp39-win_amd64.whl", hash = "sha256:44f5dc9b4384bafca8429759ce76c8960ffc2b583fcad9e5dfb3e5f4894269e4"},
]
pyasn1 = [
{file = "pyasn1-0.4.8-py2.4.egg", hash = "sha256:fec3e9d8e36808a28efb59b489e4528c10ad0f480e57dcc32b4de5c9d8c9fdf3"},
{file = "pyasn1-0.4.8-py2.5.egg", hash = "sha256:0458773cfe65b153891ac249bcf1b5f8f320b7c2ce462151f8fa74de8934becf"},
{file = "pyasn1-0.4.8-py2.6.egg", hash = "sha256:5c9414dcfede6e441f7e8f81b43b34e834731003427e5b09e4e00e3172a10f00"},
{file = "pyasn1-0.4.8-py2.7.egg", hash = "sha256:6e7545f1a61025a4e58bb336952c5061697da694db1cae97b116e9c46abcf7c8"},
{file = "pyasn1-0.4.8-py2.py3-none-any.whl", hash = "sha256:39c7e2ec30515947ff4e87fb6f456dfc6e84857d34be479c9d4a4ba4bf46aa5d"},
{file = "pyasn1-0.4.8-py3.1.egg", hash = "sha256:78fa6da68ed2727915c4767bb386ab32cdba863caa7dbe473eaae45f9959da86"},
{file = "pyasn1-0.4.8-py3.2.egg", hash = "sha256:08c3c53b75eaa48d71cf8c710312316392ed40899cb34710d092e96745a358b7"},
{file = "pyasn1-0.4.8-py3.3.egg", hash = "sha256:03840c999ba71680a131cfaee6fab142e1ed9bbd9c693e285cc6aca0d555e576"},
{file = "pyasn1-0.4.8-py3.4.egg", hash = "sha256:7ab8a544af125fb704feadb008c99a88805126fb525280b2270bb25cc1d78a12"},
{file = "pyasn1-0.4.8-py3.5.egg", hash = "sha256:e89bf84b5437b532b0803ba5c9a5e054d21fec423a89952a74f87fa2c9b7bce2"},
{file = "pyasn1-0.4.8-py3.6.egg", hash = "sha256:014c0e9976956a08139dc0712ae195324a75e142284d5f87f1a87ee1b068a359"},
{file = "pyasn1-0.4.8-py3.7.egg", hash = "sha256:99fcc3c8d804d1bc6d9a099921e39d827026409a58f2a720dcdb89374ea0c776"},
{file = "pyasn1-0.4.8.tar.gz", hash = "sha256:aef77c9fb94a3ac588e87841208bdec464471d9871bd5050a287cc9a475cd0ba"},
]
pycparser = [
{file = "pycparser-2.21-py2.py3-none-any.whl", hash = "sha256:8ee45429555515e1f6b185e78100aea234072576aa43ab53aefcae078162fca9"},
{file = "pycparser-2.21.tar.gz", hash = "sha256:e644fdec12f7872f86c58ff790da456218b10f863970249516d60a5eaca77206"},
]
pydantic = [
{file = "pydantic-1.10.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:bb6ad4489af1bac6955d38ebcb95079a836af31e4c4f74aba1ca05bb9f6027bd"},
{file = "pydantic-1.10.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:a1f5a63a6dfe19d719b1b6e6106561869d2efaca6167f84f5ab9347887d78b98"},
{file = "pydantic-1.10.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:352aedb1d71b8b0736c6d56ad2bd34c6982720644b0624462059ab29bd6e5912"},
{file = "pydantic-1.10.2-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:19b3b9ccf97af2b7519c42032441a891a5e05c68368f40865a90eb88833c2559"},
{file = "pydantic-1.10.2-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:e9069e1b01525a96e6ff49e25876d90d5a563bc31c658289a8772ae186552236"},
{file = "pydantic-1.10.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:355639d9afc76bcb9b0c3000ddcd08472ae75318a6eb67a15866b87e2efa168c"},
{file = "pydantic-1.10.2-cp310-cp310-win_amd64.whl", hash = "sha256:ae544c47bec47a86bc7d350f965d8b15540e27e5aa4f55170ac6a75e5f73b644"},
{file = "pydantic-1.10.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a4c805731c33a8db4b6ace45ce440c4ef5336e712508b4d9e1aafa617dc9907f"},
{file = "pydantic-1.10.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:d49f3db871575e0426b12e2f32fdb25e579dea16486a26e5a0474af87cb1ab0a"},
{file = "pydantic-1.10.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:37c90345ec7dd2f1bcef82ce49b6235b40f282b94d3eec47e801baf864d15525"},
{file = "pydantic-1.10.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7b5ba54d026c2bd2cb769d3468885f23f43710f651688e91f5fb1edcf0ee9283"},
{file = "pydantic-1.10.2-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:05e00dbebbe810b33c7a7362f231893183bcc4251f3f2ff991c31d5c08240c42"},
{file = "pydantic-1.10.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:2d0567e60eb01bccda3a4df01df677adf6b437958d35c12a3ac3e0f078b0ee52"},
{file = "pydantic-1.10.2-cp311-cp311-win_amd64.whl", hash = "sha256:c6f981882aea41e021f72779ce2a4e87267458cc4d39ea990729e21ef18f0f8c"},
{file = "pydantic-1.10.2-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:c4aac8e7103bf598373208f6299fa9a5cfd1fc571f2d40bf1dd1955a63d6eeb5"},
{file = "pydantic-1.10.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:81a7b66c3f499108b448f3f004801fcd7d7165fb4200acb03f1c2402da73ce4c"},
{file = "pydantic-1.10.2-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bedf309630209e78582ffacda64a21f96f3ed2e51fbf3962d4d488e503420254"},
{file = "pydantic-1.10.2-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:9300fcbebf85f6339a02c6994b2eb3ff1b9c8c14f502058b5bf349d42447dcf5"},
{file = "pydantic-1.10.2-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:216f3bcbf19c726b1cc22b099dd409aa371f55c08800bcea4c44c8f74b73478d"},
{file = "pydantic-1.10.2-cp37-cp37m-win_amd64.whl", hash = "sha256:dd3f9a40c16daf323cf913593083698caee97df2804aa36c4b3175d5ac1b92a2"},
{file = "pydantic-1.10.2-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:b97890e56a694486f772d36efd2ba31612739bc6f3caeee50e9e7e3ebd2fdd13"},
{file = "pydantic-1.10.2-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:9cabf4a7f05a776e7793e72793cd92cc865ea0e83a819f9ae4ecccb1b8aa6116"},
{file = "pydantic-1.10.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:06094d18dd5e6f2bbf93efa54991c3240964bb663b87729ac340eb5014310624"},
{file = "pydantic-1.10.2-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cc78cc83110d2f275ec1970e7a831f4e371ee92405332ebfe9860a715f8336e1"},
{file = "pydantic-1.10.2-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:1ee433e274268a4b0c8fde7ad9d58ecba12b069a033ecc4645bb6303c062d2e9"},
{file = "pydantic-1.10.2-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:7c2abc4393dea97a4ccbb4ec7d8658d4e22c4765b7b9b9445588f16c71ad9965"},
{file = "pydantic-1.10.2-cp38-cp38-win_amd64.whl", hash = "sha256:0b959f4d8211fc964772b595ebb25f7652da3f22322c007b6fed26846a40685e"},
{file = "pydantic-1.10.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:c33602f93bfb67779f9c507e4d69451664524389546bacfe1bee13cae6dc7488"},
{file = "pydantic-1.10.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:5760e164b807a48a8f25f8aa1a6d857e6ce62e7ec83ea5d5c5a802eac81bad41"},
{file = "pydantic-1.10.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6eb843dcc411b6a2237a694f5e1d649fc66c6064d02b204a7e9d194dff81eb4b"},
{file = "pydantic-1.10.2-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:4b8795290deaae348c4eba0cebb196e1c6b98bdbe7f50b2d0d9a4a99716342fe"},
{file = "pydantic-1.10.2-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:e0bedafe4bc165ad0a56ac0bd7695df25c50f76961da29c050712596cf092d6d"},
{file = "pydantic-1.10.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:2e05aed07fa02231dbf03d0adb1be1d79cabb09025dd45aa094aa8b4e7b9dcda"},
{file = "pydantic-1.10.2-cp39-cp39-win_amd64.whl", hash = "sha256:c1ba1afb396148bbc70e9eaa8c06c1716fdddabaf86e7027c5988bae2a829ab6"},
{file = "pydantic-1.10.2-py3-none-any.whl", hash = "sha256:1b6ee725bd6e83ec78b1aa32c5b1fa67a3a65badddde3976bca5fe4568f27709"},
{file = "pydantic-1.10.2.tar.gz", hash = "sha256:91b8e218852ef6007c2b98cd861601c6a09f1aa32bbbb74fab5b1c33d4a1e410"},
]
python-dateutil = [
{file = "python-dateutil-2.8.2.tar.gz", hash = "sha256:0123cacc1627ae19ddf3c27a5de5bd67ee4586fbdd6440d9748f8abb483d3e86"},
{file = "python_dateutil-2.8.2-py2.py3-none-any.whl", hash = "sha256:961d03dc3453ebbc59dbdea9e4e11c5651520a876d0f4db161e8674aae935da9"},
]
python-dotenv = [
{file = "python-dotenv-0.21.0.tar.gz", hash = "sha256:b77d08274639e3d34145dfa6c7008e66df0f04b7be7a75fd0d5292c191d79045"},
{file = "python_dotenv-0.21.0-py3-none-any.whl", hash = "sha256:1684eb44636dd462b66c3ee016599815514527ad99965de77f43e0944634a7e5"},
]
python-jose = [
{file = "python-jose-3.3.0.tar.gz", hash = "sha256:55779b5e6ad599c6336191246e95eb2293a9ddebd555f796a65f838f07e5d78a"},
{file = "python_jose-3.3.0-py2.py3-none-any.whl", hash = "sha256:9b1376b023f8b298536eedd47ae1089bcdb848f1535ab30555cd92002d78923a"},
]
python-multipart = [
{file = "python-multipart-0.0.5.tar.gz", hash = "sha256:f7bb5f611fc600d15fa47b3974c8aa16e93724513b49b5f95c81e6624c83fa43"},
]
rsa = [
{file = "rsa-4.9-py3-none-any.whl", hash = "sha256:90260d9058e514786967344d0ef75fa8727eed8a7d2e43ce9f4bcf1b536174f7"},
{file = "rsa-4.9.tar.gz", hash = "sha256:e38464a49c6c85d7f1351b0126661487a7e0a14a50f1675ec50eb34d4f20ef21"},
]
sib-api-v3-sdk = [
{file = "sib-api-v3-sdk-7.5.0.tar.gz", hash = "sha256:5c7cee4504132e512f7dd8d068c9d0c4b9654984e09939e749bbe8e3805bbf19"},
]
six = [
{file = "six-1.16.0-py2.py3-none-any.whl", hash = "sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254"},
{file = "six-1.16.0.tar.gz", hash = "sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926"},
]
sniffio = [
{file = "sniffio-1.3.0-py3-none-any.whl", hash = "sha256:eecefdce1e5bbfb7ad2eeaabf7c1eeb404d7757c379bd1f7e5cce9d8bf425384"},
{file = "sniffio-1.3.0.tar.gz", hash = "sha256:e60305c5e5d314f5389259b7f22aaa33d8f7dee49763119234af3755c55b9101"},
]
SQLAlchemy = [
{file = "SQLAlchemy-1.4.41-cp27-cp27m-macosx_10_14_x86_64.whl", hash = "sha256:13e397a9371ecd25573a7b90bd037db604331cf403f5318038c46ee44908c44d"},
{file = "SQLAlchemy-1.4.41-cp27-cp27m-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:2d6495f84c4fd11584f34e62f9feec81bf373787b3942270487074e35cbe5330"},
{file = "SQLAlchemy-1.4.41-cp27-cp27m-win32.whl", hash = "sha256:e570cfc40a29d6ad46c9aeaddbdcee687880940a3a327f2c668dd0e4ef0a441d"},
{file = "SQLAlchemy-1.4.41-cp27-cp27m-win_amd64.whl", hash = "sha256:5facb7fd6fa8a7353bbe88b95695e555338fb038ad19ceb29c82d94f62775a05"},
{file = "SQLAlchemy-1.4.41-cp27-cp27mu-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:f37fa70d95658763254941ddd30ecb23fc4ec0c5a788a7c21034fc2305dab7cc"},
{file = "SQLAlchemy-1.4.41-cp310-cp310-macosx_10_15_x86_64.whl", hash = "sha256:361f6b5e3f659e3c56ea3518cf85fbdae1b9e788ade0219a67eeaaea8a4e4d2a"},
{file = "SQLAlchemy-1.4.41-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0990932f7cca97fece8017414f57fdd80db506a045869d7ddf2dda1d7cf69ecc"},
{file = "SQLAlchemy-1.4.41-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:cd767cf5d7252b1c88fcfb58426a32d7bd14a7e4942497e15b68ff5d822b41ad"},
{file = "SQLAlchemy-1.4.41-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5102fb9ee2c258a2218281adcb3e1918b793c51d6c2b4666ce38c35101bb940e"},
{file = "SQLAlchemy-1.4.41-cp310-cp310-win32.whl", hash = "sha256:2082a2d2fca363a3ce21cfa3d068c5a1ce4bf720cf6497fb3a9fc643a8ee4ddd"},
{file = "SQLAlchemy-1.4.41-cp310-cp310-win_amd64.whl", hash = "sha256:e4b12e3d88a8fffd0b4ca559f6d4957ed91bd4c0613a4e13846ab8729dc5c251"},
{file = "SQLAlchemy-1.4.41-cp311-cp311-macosx_10_15_x86_64.whl", hash = "sha256:90484a2b00baedad361402c257895b13faa3f01780f18f4a104a2f5c413e4536"},
{file = "SQLAlchemy-1.4.41-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b67fc780cfe2b306180e56daaa411dd3186bf979d50a6a7c2a5b5036575cbdbb"},
{file = "SQLAlchemy-1.4.41-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ad2b727fc41c7f8757098903f85fafb4bf587ca6605f82d9bf5604bd9c7cded"},
{file = "SQLAlchemy-1.4.41-cp311-cp311-win32.whl", hash = "sha256:59bdc291165b6119fc6cdbc287c36f7f2859e6051dd923bdf47b4c55fd2f8bd0"},
{file = "SQLAlchemy-1.4.41-cp311-cp311-win_amd64.whl", hash = "sha256:d2e054aed4645f9b755db85bc69fc4ed2c9020c19c8027976f66576b906a74f1"},
{file = "SQLAlchemy-1.4.41-cp36-cp36m-macosx_10_14_x86_64.whl", hash = "sha256:4ba7e122510bbc07258dc42be6ed45997efdf38129bde3e3f12649be70683546"},
{file = "SQLAlchemy-1.4.41-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c0dcf127bb99458a9d211e6e1f0f3edb96c874dd12f2503d4d8e4f1fd103790b"},
{file = "SQLAlchemy-1.4.41-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:e16c2be5cb19e2c08da7bd3a87fed2a0d4e90065ee553a940c4fc1a0fb1ab72b"},
{file = "SQLAlchemy-1.4.41-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f5ebeeec5c14533221eb30bad716bc1fd32f509196318fb9caa7002c4a364e4c"},
{file = "SQLAlchemy-1.4.41-cp36-cp36m-win32.whl", hash = "sha256:3e2ef592ac3693c65210f8b53d0edcf9f4405925adcfc031ff495e8d18169682"},
{file = "SQLAlchemy-1.4.41-cp36-cp36m-win_amd64.whl", hash = "sha256:eb30cf008850c0a26b72bd1b9be6730830165ce049d239cfdccd906f2685f892"},
{file = "SQLAlchemy-1.4.41-cp37-cp37m-macosx_10_15_x86_64.whl", hash = "sha256:c23d64a0b28fc78c96289ffbd0d9d1abd48d267269b27f2d34e430ea73ce4b26"},
{file = "SQLAlchemy-1.4.41-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8eb8897367a21b578b26f5713833836f886817ee2ffba1177d446fa3f77e67c8"},
{file = "SQLAlchemy-1.4.41-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:14576238a5f89bcf504c5f0a388d0ca78df61fb42cb2af0efe239dc965d4f5c9"},
{file = "SQLAlchemy-1.4.41-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:639e1ae8d48b3c86ffe59c0daa9a02e2bfe17ca3d2b41611b30a0073937d4497"},
{file = "SQLAlchemy-1.4.41-cp37-cp37m-win32.whl", hash = "sha256:0005bd73026cd239fc1e8ccdf54db58b6193be9a02b3f0c5983808f84862c767"},
{file = "SQLAlchemy-1.4.41-cp37-cp37m-win_amd64.whl", hash = "sha256:5323252be2bd261e0aa3f33cb3a64c45d76829989fa3ce90652838397d84197d"},
{file = "SQLAlchemy-1.4.41-cp38-cp38-macosx_10_15_x86_64.whl", hash = "sha256:05f0de3a1dc3810a776275763764bb0015a02ae0f698a794646ebc5fb06fad33"},
{file = "SQLAlchemy-1.4.41-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0002e829142b2af00b4eaa26c51728f3ea68235f232a2e72a9508a3116bd6ed0"},
{file = "SQLAlchemy-1.4.41-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:22ff16cedab5b16a0db79f1bc99e46a6ddececb60c396562e50aab58ddb2871c"},
{file = "SQLAlchemy-1.4.41-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ccfd238f766a5bb5ee5545a62dd03f316ac67966a6a658efb63eeff8158a4bbf"},
{file = "SQLAlchemy-1.4.41-cp38-cp38-win32.whl", hash = "sha256:58bb65b3274b0c8a02cea9f91d6f44d0da79abc993b33bdedbfec98c8440175a"},
{file = "SQLAlchemy-1.4.41-cp38-cp38-win_amd64.whl", hash = "sha256:ce8feaa52c1640de9541eeaaa8b5fb632d9d66249c947bb0d89dd01f87c7c288"},
{file = "SQLAlchemy-1.4.41-cp39-cp39-macosx_10_15_x86_64.whl", hash = "sha256:199a73c31ac8ea59937cc0bf3dfc04392e81afe2ec8a74f26f489d268867846c"},
{file = "SQLAlchemy-1.4.41-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4676d51c9f6f6226ae8f26dc83ec291c088fe7633269757d333978df78d931ab"},
{file = "SQLAlchemy-1.4.41-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:036d8472356e1d5f096c5e0e1a7e0f9182140ada3602f8fff6b7329e9e7cfbcd"},
{file = "SQLAlchemy-1.4.41-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2307495d9e0ea00d0c726be97a5b96615035854972cc538f6e7eaed23a35886c"},
{file = "SQLAlchemy-1.4.41-cp39-cp39-win32.whl", hash = "sha256:9c56e19780cd1344fcd362fd6265a15f48aa8d365996a37fab1495cae8fcd97d"},
{file = "SQLAlchemy-1.4.41-cp39-cp39-win_amd64.whl", hash = "sha256:f5fa526d027d804b1f85cdda1eb091f70bde6fb7d87892f6dd5a48925bc88898"},
{file = "SQLAlchemy-1.4.41.tar.gz", hash = "sha256:0292f70d1797e3c54e862e6f30ae474014648bc9c723e14a2fda730adb0a9791"},
]
sqlalchemy2-stubs = [
{file = "sqlalchemy2-stubs-0.0.2a29.tar.gz", hash = "sha256:1bbc6aebd76db7c0351a9f45cc1c4e8ac335ba150094c2af091e8b87b9118419"},
{file = "sqlalchemy2_stubs-0.0.2a29-py3-none-any.whl", hash = "sha256:ece266cdabf3797b13ddddba27561b67ae7dedc038942bf66e045e978a5e3a66"},
]
sqlmodel = [
{file = "sqlmodel-0.0.8-py3-none-any.whl", hash = "sha256:0fd805719e0c5d4f22be32eb3ffc856eca3f7f20e8c7aa3e117ad91684b518ee"},
{file = "sqlmodel-0.0.8.tar.gz", hash = "sha256:3371b4d1ad59d2ffd0c530582c2140b6c06b090b32af9b9c6412986d7b117036"},
]
starlette = [
{file = "starlette-0.19.1-py3-none-any.whl", hash = "sha256:5a60c5c2d051f3a8eb546136aa0c9399773a689595e099e0877704d5888279bf"},
{file = "starlette-0.19.1.tar.gz", hash = "sha256:c6d21096774ecb9639acad41b86b7706e52ba3bf1dc13ea4ed9ad593d47e24c7"},
]
tomli = [
{file = "tomli-2.0.1-py3-none-any.whl", hash = "sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc"},
{file = "tomli-2.0.1.tar.gz", hash = "sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f"},
]
typing-extensions = [
{file = "typing_extensions-4.3.0-py3-none-any.whl", hash = "sha256:25642c956049920a5aa49edcdd6ab1e06d7e5d467fc00e0506c44ac86fbfca02"},
{file = "typing_extensions-4.3.0.tar.gz", hash = "sha256:e6d2677a32f47fc7eb2795db1dd15c1f34eff616bcaf2cfb5e997f854fa1c4a6"},
]
urllib3 = [
{file = "urllib3-1.26.12-py2.py3-none-any.whl", hash = "sha256:b930dd878d5a8afb066a637fbb35144fe7901e3b209d1cd4f524bd0e9deee997"},
{file = "urllib3-1.26.12.tar.gz", hash = "sha256:3fa96cf423e6987997fc326ae8df396db2a8b7c667747d47ddd8ecba91f4a74e"},
]
uvicorn = [
{file = "uvicorn-0.18.3-py3-none-any.whl", hash = "sha256:0abd429ebb41e604ed8d2be6c60530de3408f250e8d2d84967d85ba9e86fe3af"},
{file = "uvicorn-0.18.3.tar.gz", hash = "sha256:9a66e7c42a2a95222f76ec24a4b754c158261c4696e683b9dadc72b590e0311b"},
]
