from threading import Lock
from collections import deque
import time


class SlidingWindowCounter:
    def __init__(self, window_size, limit):
        """
        Initializes a SlidingWindowCounter object.

        Args:
            window_size (float): The size of the sliding window in seconds.
            limit (int): The maximum number of requests allowed within the window.
        """
        self.window_size = window_size
        self.limit = limit
        self.requests = deque()

    def increment_count(self):
        """
        Increments the request count and removes expired requests from the sliding window.
        """
        current_time = time.time()
        self.requests.append(current_time)

        while self.requests and self.requests[0] < current_time - self.window_size:
            self.requests.popleft()

    def count_requests(self):
        """
        Returns the current number of requests within the sliding window.

        Returns:
            int: The number of requests.
        """
        return len(self.requests)

    def is_allowed(self):
        """
        Checks if a new request is allowed based on the current request count.

        Returns:
            bool: True if the request is allowed, False otherwise.
        """
        return self.count_requests() < self.limit
