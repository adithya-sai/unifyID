import urllib2

import threading
_LOCK = threading.Lock()

base_url = "https://www.random.org/integers/?num={0}&min={1}&max={2}&col={3}&base={4}&format=plain&rnd=new"

def randomNumberGenerator(minimum, maximum, num=1):
    link = base_url.format(num, minimum, maximum, 1, 10)
    with _LOCK:
        source_code = urllib2.urlopen(link).read()

    return [int(x) for x in source_code.splitlines()]
