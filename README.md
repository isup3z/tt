

# TikTok Username Checker

This is a Python script that generates random usernames and checks if they are available on TikTok. The script allows you to specify the length and type of the username (letters only or letters and numbers), and also supports using proxies to avoid getting blocked by TikTok.

## Dependencies

The script requires the following dependencies:

- `requests`: to send HTTP requests to TikTok's website
- `beautifulsoup4`: to parse the HTML responses from TikTok's website

You can install these dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage

To run the script, simply execute the `main.py` file using Python 3:

```
python3 main.py
```

The script will prompt you to enter the username length, type, and proxy list file path (if you want to use proxies). If you don't want to use proxies, leave the proxy list file path empty.

The script will continuously generate random usernames and check if they are available on TikTok. If a username is available, the script will print it to the console and write it to a file named `results.txt`.

Note that TikTok may block your IP address if you send too many requests in a short period of time. Using proxies can help avoid getting blocked, but there's no guarantee that it will work. Use this script responsibly and at your own risk.

## License

This code is released under the MIT License. Feel free to use it, modify it, and distribute it as you see fit.
