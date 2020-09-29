# https://leetcode.com/problems/web-crawler-multithreaded/
# https://www.digitalocean.com/community/tutorials/how-to-use-threadpoolexecutor-in-python-3
from concurrent import futures
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        visited = {startUrl}
        
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in visited and hostname(startUrl) == hostname(url):
                        visited.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        return list(visited)