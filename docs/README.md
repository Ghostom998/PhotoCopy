# Pics2Word

A command line program to copy pictures into a word document.

Usage can be found using

`$ pics2word -h help`

## Installation

Installing the Pics2Word software:

1. Install [Python](https://www.python.org/downloads/) (Latest version of 3.X series, NOT 2.7). This is a dependency that is required for the program to work and allows us to install pics2word with pip. (Pip is a recursive acronym for pip installs packages)

2. When that is installed, open the Terminal / Command Line / PowerShell and then type:

    `$ pip install pics2word`

    This installs the latest version of pics2word onto the system.

    From the latest Windows 10 update, the PowerShell can be opened from windows file explorer > File > Open Windows PowerShell
    From Linux you may need root privillages. If the above does not work, try

    `$ sudo pip install pics2word --user`

3. You can now run “pics2word” from the command line anywhere. Type:

    `$ pics2word –h help`

    for information on how to use it.

Note: pics2word can be updated to the latest release with:

`$ pip install --upgrade pics2word`

note the two dashes before upgrade.

## Reporting bugs

Please report all issues to [GitHub](https://github.com/Ghostom998/pics2word/issues)
Raise a new issue then:

- Please describe the issue as accurately as possible with the ouput from the log file and any error message given in the terminal window.
- Please describe exactly what you did to trigger the event including the commands that were passed
- Note the operating system, version of python used and pics2word version
- Include any further relavent information you deem useful.

## Useful supplementary third party software

- [Caesium](https://saerasoft.com/caesium/) – image compression software. Useful if dealing with a large number of pictures to reduce the file size of the word document and speed up image processing.
- [Bulk Rename Utility](http://www.bulkrenameutility.co.uk/Download.php) – allows large numbers of files to be renamed automatically. Especially useful if following a format such as “Photo 1, Photo 2... Photo X”

## New to this release 0.9.5

- The path command is fixed
- Modules are now saved in a standard folder so that they can be loaded anywhere
- Modules are now saved in JSON format to be more human readable
- Help text is now saved in a JSON for good practise

## TODO tasks

### High Priority

#### Features

#### Bug fix's

### Low Priority

#### Features

- Option to preserve aspect ratio or not. (i.e. stretch pictures to cells)
- Allow the user to omit the picture name, i.e. a "Picture-only" mode

#### Bug fix's
