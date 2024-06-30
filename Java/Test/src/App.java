import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class App {

    static class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    static class SinglyLinkedList {
        public SinglyLinkedListNode head;
        public SinglyLinkedListNode tail;

        public SinglyLinkedList() {
            this.head = null;
            this.tail = null;
        }

        public void insertNode(int nodeData) {
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

            if (this.head == null) {
                this.head = node;
            } else {
                this.tail.next = node;
            }

            this.tail = node;
        }
    }

    public static void printSinglyLinkedList(SinglyLinkedListNode node) throws IOException {
        System.out.println("Merged Lists:");
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
    }

    // Variables
    static int[] intArray = { 4, 7, -3, 5, 0, -1, 0, -13 };

    // Time String [00:00:00PM]
    static String timeString = "07:05:45PM";

    // # Pyramid Small Test Array, unique is 7, pos and neg values
    static int[] smallDuplicateValueArray = { -999, -999, -999, 999, 999, 999, -42, -42, 11, 11, 7 };

    // # Small Square Matrix
    static int[][] smallSquareMatrix = { { 11, 2, 4 }, { 4, 5, 6 }, { 10, 8, -12 } };

    // # Large Test Array
    static int[] largeTestArray = { 63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12,
            83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18,
            21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70,
            95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33 };

    // # Alphabetgrid len(grid)=5, height(grid)=5
    static String[] alphabetGrid = { "ebacd", "fghij", "olmkn", "trpqs", "xywuv" };

    // Artificial QueueUsingTwoStacks
    // Normally just involves a parse, but to keep Java simple and a single File
    // will pre interpret commands to focus on queueing
    static String[] stackCommands = { "1 42", "2", "1 14", "3", "1 28", "3", "1 60", "1 78", "2", "2" };

    static String brackets = "{{[[(())]]}}";

    public static void main(String[] args) throws Exception {

        // Singly Linked List 1 & 2
        SinglyLinkedList singlyLinkedList1 = new SinglyLinkedList();
        singlyLinkedList1.insertNode(1);
        singlyLinkedList1.insertNode(3);
        singlyLinkedList1.insertNode(6);

        SinglyLinkedList singlyLinkedList2 = new SinglyLinkedList();
        singlyLinkedList2.insertNode(2);
        singlyLinkedList2.insertNode(4);
        singlyLinkedList2.insertNode(5);

        System.out.println("Testing Plus Minus");
        plusMinus(intArray);
        System.out.println();

        System.out.println("Testing MiniMax");
        miniMax(intArray);
        System.out.println();

        System.out.println("Testing Time Conversion");
        System.out.println(timeConversion(timeString));
        System.out.println();

        System.out.println("Testing Lone Integer");
        System.out.println(lonelyInteger(smallDuplicateValueArray));
        System.out.println();

        System.out.println("Testing DiagonalDifference");
        System.out.println(diagonalDifference(smallSquareMatrix));
        System.out.println();

        System.out.println("Testing CountingSort1");
        System.out.println(Arrays.toString(countingSort1(largeTestArray)));
        System.out.println();

        System.out.println("Testing TowerBreakers");
        System.out.println(towerBreakers(7, 4));
        System.out.println();

        System.out.println("Testing CaeserCypher");
        System.out.println(caeserCypher("middle-Outz", 2));
        System.out.println();

        System.out.println("Testing Grid Challenge");
        System.out.println(gridChallenge(alphabetGrid));
        System.out.println();

        System.out.println("Testing SuperDigit");
        System.out.println(superDigit("9875", 4));
        System.out.println();

        System.out.println("Testing MergeLists");
        printSinglyLinkedList(mergeLists(singlyLinkedList1.head, singlyLinkedList2.head));
        System.out.println();
        System.out.println();

        System.out.println("Testing QueueUsingTwoStacks");
        queueUsingTwoStacks(stackCommands);
        System.out.println();

        System.out.println("Testing Balanced Brackets");
        System.out.println(balancedBrackets(brackets));
        System.out.println();
    }

    //
    //
    //
    //
    private static void plusMinus(int[] numbers) {
        int pos = 0, neg = 0, zero = 0, length = numbers.length;
        for (int num : numbers) {
            if (num > 0) {
                pos++;
            } else if (num < 0) {
                neg++;
            } else {
                zero++;
            }
        }
        System.out.println("Positive Ratio: " + (double) pos / length);
        System.out.println("Negaive Ratio: " + (double) neg / length);
        System.out.println("Zeroes Ratio: " + (double) zero / length);
    }

    public static void miniMax(int[] numbers) {
        int minSum = 0;
        int maxSum = 0;
        Arrays.sort(numbers);
        for (int i = 0; i < numbers.length - 1; i++) {
            minSum += numbers[i];
        }
        for (int i = 1; i < numbers.length; i++) {
            maxSum += numbers[i];
        }

        System.out.println(minSum + " " + maxSum);
    }

    public static String timeConversion(String timeToConvert) {
        StringBuilder time = new StringBuilder("");

        String hourString = timeToConvert.substring(0, 2);
        int hourInt = Integer.parseInt(hourString);
        String minuteString = timeToConvert.substring(3, 5);
        int minuteInt = Integer.parseInt(minuteString);
        String secondString = timeToConvert.substring(6, 8);
        int secondInt = Integer.parseInt(secondString);
        String pm = timeToConvert.substring(8, 9);

        if (pm.equals("P") && hourInt < 12) {
            hourInt += 12;
        }

        // # if the hour is less than 10 adjust formatting to include leading '0' or two
        // if it is midnight
        if (hourInt < 10) {
            hourString = "0" + hourInt + ":";
        } else if (hourInt == 12 && pm.equals("pm")) {
            hourString = "00" + ":";
        } else {
            hourString = hourInt + ":";
        }

        // # repeat the alterations occuring for the hour segment for minutes, but no
        // check for 12 on the dot.
        if (minuteInt < 10) {
            minuteString = "0" + minuteInt + ":";
        } else {
            minuteString = minuteInt + ":";
        }

        // # repeat for seconds
        if (secondInt < 10) {
            secondString = "0" + secondInt;
        } else {
            secondString = secondInt + "";
        }

        // # concatonate the string and write out the final form.
        time.append(hourString + minuteString + secondString);
        return time.toString();
    }

    public static int lonelyInteger(int[] duplicateNumberArray) {
        int zero = 0;
        int loneInt = 0;
        for (int i = 0; i < duplicateNumberArray.length; i++) {
            loneInt = zero ^ duplicateNumberArray[i];
        }
        return loneInt;
    }

    public static int diagonalDifference(int[][] matrix) {
        int difference = 0;
        int diagOne = 0;
        int diagTwo = 0;
        int length = matrix.length;

        for (int i = 0; i < length; i++) {
            diagOne += matrix[i][i];
            diagTwo += matrix[i][(length - 1) - i];
        }

        difference = Math.abs(diagOne - diagTwo);
        return difference;
    }

    public static int[] countingSort1(int[] array) {
        int[] bigArray = new int[100];
        Arrays.fill(bigArray, 0);
        for (int num : array) {
            bigArray[num] += 1;
        }
        return bigArray;
    }

    public static int towerBreakers(int numOfTowers, int heightOfTowers) {
        if (heightOfTowers == 1 || numOfTowers % 2 == 0) {
            return 2;
        } else {
            return 1;
        }
    }

    public static String caeserCypher(String secret, int rotation) {
        StringBuilder coded = new StringBuilder("");

        // # for each char letter in the string
        for (int i = 0; i < secret.length(); i++) {

            // # get the ascii value and get a temp char ready
            int numVal = (int) secret.charAt(i);
            Character newChar = ' ';

            // # if the letter is 65 > x < 90 its lowercase
            if (numVal >= 65 && numVal <= 90) {

                // # if the shift value makes the letter a symbol
                // # subtract or add the alphabet length to shift to the start or end of the
                // alphabet string
                // # set the newChar = char(incrementVal(k) + asciiValue(numVal))
                if ((numVal + rotation) > 91) {
                    rotation -= 26;
                    newChar = (char) (numVal + rotation);
                } else if ((numVal + rotation) < 65) {
                    rotation += 26;
                    newChar = (char) (numVal + rotation);
                } else {
                    newChar = (char) (numVal + rotation);
                }

                // # if the letter is 97 > x < 122 its uppercase
            } else if (numVal >= 97 && numVal <= 122) {

                if ((numVal + rotation) > 122) {
                    rotation -= 26;
                    newChar = (char) (numVal + rotation);
                } else if ((numVal + rotation) < 97) {
                    rotation += 26;
                    newChar = (char) (numVal + rotation);
                } else {
                    newChar = (char) (numVal + rotation);
                }

            } else {
                // # if not an alphancharacter originally don't shift just add it to the end
                newChar = (char) (numVal);
            }
            coded.append(newChar);
        }
        return coded.toString();
    }

    public static String gridChallenge(String[] gridArray) {
        for (int i = 0; i < gridArray.length; i++) {
            char[] charArr = gridArray[i].toCharArray();
            Arrays.sort(charArr);
            gridArray[i] = new String(charArr);
        }
        System.out.println(Arrays.toString(gridArray));
        for (int i = 0; i < gridArray[0].length(); i++) {
            for (int j = 1; j < gridArray[0].length() - 1; j++) {
                if (gridArray[j].charAt(i) > gridArray[j + 1].charAt(i)) {
                    return "NO";
                }
            }
        }
        return "Yes";
    }

    public static int superDigit(String original, int concats) {
        int superDigit = 0;
        int length = original.length();

        if (length == 1) {
            return Integer.parseInt(original);
        } else {
            for (int i = 0; i < length; i++) {
                char x = original.charAt(i);
                superDigit += Character.getNumericValue(x);
            }
            superDigit *= concats;
        }

        String newOriginal = String.valueOf(superDigit);
        return superDigit(newOriginal, 1);
    }

    public static SinglyLinkedListNode mergeLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        if (head1 == null && head2 == null) {
            return null;
        }

        if (head1 == null) {
            return head2;
        } else if (head2 == null) {
            return head1;
        }

        SinglyLinkedListNode mHead = null;
        SinglyLinkedListNode mTail = null;

        if (head1.data < head2.data) {
            mHead = head1;
            mTail = head1;
            head1 = head1.next;
        } else {
            mHead = head2;
            mTail = head2;
            head2 = head2.next;
        }

        while (head1 != null && head2 != null) {
            if (head1.data < head2.data) {
                mTail.next = head1;
                mTail = mTail.next;
                head1 = head1.next;
            } else {
                mTail.next = head2;
                mTail = mTail.next;
                head2 = head2.next;
            }
        }

        while (head1 == null && head2 != null) {
            mTail.next = head2;
            mTail = mTail.next;
            head2 = head2.next;
        }
        while (head2 == null && head1 != null) {
            mTail.next = head1;
            mTail = mTail.next;
            head1 = head1.next;
        }

        return mHead;
    }

    public static void queueUsingTwoStacks(String[] array) {
        Queue<String> cmdLines = new LinkedList<String>();
        for (String line : array) {
            cmdLines.add(line);
        }

        Stack<String> endStack = new Stack<String>();
        for (int i = 0; i < cmdLines.size(); i++) {
            String[] splited = cmdLines.poll().trim().split(" ");
            switch (splited[0]) {
                case "1":
                    endStack.push(splited[1]);
                    break;
                case "2":
                    endStack.pop();
                    break;
                case "3":
                    System.out.println(endStack.peek());
                    break;
            }
        }
    }

    public static String balancedBrackets(String checkLine) {
        ArrayList<Character> bracks = new ArrayList<>();
        char test = ' ';
        for (int i =0; i < checkLine.length(); i++) {
            if (checkLine.charAt(i) == '(' || checkLine.charAt(i) == '[' || checkLine.charAt(i) == '{') {
                bracks.add(checkLine.charAt(i));
            } else if (checkLine.charAt(i) == ']') {
                test = bracks.removeLast();
                if (test != '[') {
                    return "NO";
                } 
            } else if (checkLine.charAt(i) == ')') {
                test = bracks.removeLast();
                if (test != '(') {
                    return "NO";
                } 
            } else if (checkLine.charAt(i) == '}') {
                test = bracks.removeLast();
                if (test != '{') {
                    return "NO";
                } 
            }
        };
    
        return "YES";
    }
}
