# Security Policy

## Supported Versions

All versions tagged with a ✅ are yet maintained and still supported.
Any version with a :x: is not maintained by me. Using any version with the :x: is not recommended due to potential bugs or (what I not hope) security issues
Any version tagged with ✅ and LTS behind the version number is considered a stable version with a Long Time Support.
Versions which are deprecated may not be compatible with newer versions.

I guess you have understood the system. Right?\
✅: good to go\
LTS and  ✅: YAYYY LONG TERM SUPPORT\
🚧: This is a development version and not yet stable.\
:x:: Keep your fingers away




| Version | Supported          |
| ------- | ------------------ |
| <1.0.0 | 🚧|


## Reporting a Vulnerability

All uploaded code was written with good intentions and checked properly. I try my best to keep all libraries updated and to check if any of the libraries are considered potentially vulnerable to a computer system.
Some parts of the code are built on existing thrid party software. Since I have (obviously) not developed all thrid party tools and software by myself, external libraries can get infected. A good example is the in 2021 discovered virus Log4Shell [Log4Shell](https://en.wikipedia.org/wiki/Log4Shell). Log4Shell is a zero-day exploit which is based on a popular Java Framework Log4J. Since 2013 the vulnerability existed and potentially scraped billions of data on hundreds of million devices. 
Hence, there is no guarantee that all libraries I use are **100%** secure. In case you find any vulnerability or anything I forgot to secure properly (e.g. authentification systems) you are more than welcome to contact me. Please make clear in the issue description that it is important.

For incidents which potentially are dangerous to anyone who uses the code or anything related to a life or death situation has to be reported immideately. Please use the title **URGENT INCIDENT:** <description>
For situations where I made a coding mistake in a critical system (e.g. potential password leak during authentification), please consider using **IMPORTANT BUG:** <decription>


Thank you so much for your help!

Cheers,
