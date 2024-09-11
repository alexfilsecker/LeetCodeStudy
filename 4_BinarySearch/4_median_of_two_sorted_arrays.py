from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Make sure A is the smallest
        if len(A) > len(B):
            A, B = B, A

        # Binary search through A (smallest)
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2  # mid of array A
            mid_b = half - mid - 2  # Substract 2 because of 0 index start

            # Get the max and min values for the partitions in A and B
            A_left = A[mid] if mid >= 0 else float("-inf")
            B_left = B[mid_b] if mid_b >= 0 else float("-inf")
            A_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
            B_right = B[mid_b + 1] if mid_b + 1 < len(B) else float("inf")

            # Partition is correct
            if A_left <= B_right and B_left <= A_right:
                # odd
                if total % 2:
                    return min(A_right, B_right)

                return (max(A_left, B_left) + min(A_right, B_right)) / 2

            # There is too many elements in A
            elif A_left > B_right:
                right = mid - 1
            # There is too many elements from B
            else:
                left = mid + 1


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
