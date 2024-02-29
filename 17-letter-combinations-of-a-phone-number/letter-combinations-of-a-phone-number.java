import java.util.ArrayList;
import java.util.List;

class Solution {
    static String combinations[] = {" ", ".", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        ArrayList<String> list = new ArrayList<>();
        printCombinations(digits, 0, "", list);
        return list;
    }

    static void printCombinations(String text, int index, String newStr, List<String> list) {
        if (index == text.length()) {
            if(newStr != ""){
                list.add(newStr);
            }
            return;
        }
        char currChar = text.charAt(index);
        String mapping = combinations[currChar - '0'];

        for (int i = 0; i < mapping.length(); i++) {
            printCombinations(text, index + 1, newStr + mapping.charAt(i), list);
        }
    }
}
