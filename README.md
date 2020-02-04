# Man in the browser

This repository contains a simple Python script for intercepting data in the `PR_Write` hook of the `Firefox API`. The script will grab the user/password o whatever any other form-related information (browser API calls) that will be sent to the server just before it goes encrypted by an `SSL tunnel`.

In a few steps, it starts by throwing a `Firefox process`, then we `debug` and `intercept function for API calls`, extract the data and continue their normal flow.

## How it works

Firefox uses a function called `PR_Write` inside a dll module called `nss3.dll` to write or submit data. By setting up a break-point at that function, we should see the data in clear-text, just before it goes encrypted.

Internally the `PR_WRITE` writes data into a `TCP socket`, that's the exact point when the form data is in plain-text.

This is accomplished by using the `winappdbg-1.5` python package. The `firefox.py` script really is a starting point. You can output the whole execution to a `txt` file, or filter email and password in a clean-text login a specific target and send it to the attacker machine. It's up to you.

Take fact that this will affect the speed processing data of the file, can have delay, and can also generate a crash to the process.

The default `firefox API` data is present of a `HEX` representation, you will need to translate to `ASCII` in order to get a fully understandable data.

Check the `twitter-extract.txt` for a real-life example.

## Environment

The lab setup for this script is a `Windows 7` machine with `Firefox 45` installed.

## Manual process

This can be done using the `Immunity Debugging` software, by attaching the `firefox.exe`, locating the `nss3` module and setting a break-point directly on the `PR_Write`, then check the memory content (stack pointer) and analyze the `memory dumps` until find the `auth` data in clear-text

## How to use

Simple: `python firefox.py`

For this PoC, you will need to start the script right before submitting data to a login form. You can use the `twitter` login page for that.
Just make sure that the name `password` is present on any `form input` for testing.

## Binary for post-exploitation

You can use the `setup.py` file in order to generate a `exe` file with `py2exe` Python package.

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
