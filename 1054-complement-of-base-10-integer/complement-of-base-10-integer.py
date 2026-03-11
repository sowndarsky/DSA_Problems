class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bi = format(n,'b')
        b = ''.join('1' if i == '0' else '0' for i in bi)
        return int(b,2)
