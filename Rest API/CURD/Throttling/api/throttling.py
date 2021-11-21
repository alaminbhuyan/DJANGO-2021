# this file use for apply different throttling in different class

from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope = 'jack'
    # Go setting.py file and use 'jack' to apply 'rate' in particular class