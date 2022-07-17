from m3u_parser import M3uParser
url = "data/PlayMe.m3u"
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
parser = M3uParser(timeout=5, useragent=useragent)
parser.parse_m3u(url)
print(len(parser.get_list()))
print(parser)
parser.to_file('data/PlayMe.json')
