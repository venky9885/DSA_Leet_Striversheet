

class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        arr = self.d[key]
        left, right = 0, len(arr) - 1
        
        # Binary search to find the largest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the requested timestamp is smaller than the smallest timestamp in the list
        # L11- check right is -1
        if right == -1:
            return ""
        
        # Return the value corresponding to the largest timestamp <= given timestamp
        #L11- put right instead mid
        return arr[right][1]
# while doing this problem  everythin done in binsearch function and right is not taken care ,after that it is corrected
#modifications check with L11 searching
    
#check code below one also
class TimeMap:

    def __init__(self):
        # Initialize a defaultdict with lists to store key-value pairs.
        self.structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append a new pair [value, timestamp] to the list associated with the key.
        self.structure[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Initialize an empty string to store the result.
        ans = ""
        # Retrieve the list of pairs associated with the given key.
        temp = self.structure.get(key, [])

        # Perform binary search within the list of pairs.
        low, high = 0, len(temp) - 1
        while low <= high:
            mid = (low + high) // 2

            # If the timestamp at mid is less than or equal to the target timestamp,
            # update the result and move the search to the right half.
            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                low = mid + 1
            # If the timestamp at mid is greater than the target timestamp,
            # move the search to the left half.
            else:
                high = mid - 1

        return ans                