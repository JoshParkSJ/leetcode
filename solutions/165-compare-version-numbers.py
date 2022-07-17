# O(n + m) time | O(n + m) space
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        
        for idx in range(max(len(ver2), len(ver1))):
            subver1 = subver2 = "0"
            if idx < len(ver1):
                subver1 = ver1[idx]
            if idx < len(ver2):
                subver2 = ver2[idx]
            comparison = self.compare(subver1, subver2)
            
            if comparison == 1 or comparison == -1:
                return comparison
            
        return 0
    
    def compare(self, ver1, ver2):
        start1 = start2 = 0
        
        while start1 < len(ver1) and ver1[start1] == "0":
            start1 += 1
        while start2 < len(ver2) and ver2[start2] == "0":
            start2 += 1
        
        version1 = ver1[start1:]
        version2 = ver2[start2:]

        if not version1 and not version2:
            return 0
        if not version1:
            return -1
        if not version2:
            return 1
        
        versionNum1 = int(version1)
        versionNum2 = int(version2)
        
        if versionNum1 > versionNum2:
            return 1
        if versionNum1 < versionNum2:
            return -1
        return 0
