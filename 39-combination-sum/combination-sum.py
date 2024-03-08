class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Auto-generated docstring and comments:
        Finds all unique combinations of candidates that sum up to the target.

        Args:
            candidates (List[int]): A list of candidate numbers.
            target (int): The target sum.

        Returns:
            List[List[int]]: A list of lists containing all unique combinations of candidates that sum up to the target.
        """

        result = []

        def helper(current_sum, index, current_combination):
            """
            Recursive helper function to find combinations.

            Args:
                current_sum (int): The current sum of the elements in current_combination.
                index (int): The current index in the candidates list.
                current_combination (List[int]): The current combination being formed.

            Returns:
                bool: True if a valid combination is found, False otherwise.
            """
            # Base case: If the current sum equals target, add the combination to result
            if current_sum == target:
                # Check if the combination is not already in result to avoid duplicates
                if current_combination not in result:
                    result.append(current_combination[:])  # Append a copy of the combination
                    return True

            # Base case: If the current sum exceeds target or all candidates are exhausted, stop recursion
            if current_sum > target or index == len(candidates):
                return False

            # Explore all possible combinations starting from index
            for j in range(index, len(candidates)):
                current_combination.append(candidates[j])
                # Recursively call helper with updated sum, index, and combination
                helper(current_sum + candidates[j], j, current_combination)
                current_combination.pop()  # Backtrack: Remove the last element for the next iteration

        # Start the recursion with initial parameters
        helper(0, 0, [])
        return result
