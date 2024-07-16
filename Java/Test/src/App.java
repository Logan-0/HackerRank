import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class App {

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

    static List<String> gridArrList = Arrays.asList("ebacd", "fghij", "olmkn", "trpqs", "xywuv");

    public static void main(String[] args) throws Exception {
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
        System.out.println(gridChallenge(gridArrList));
        System.out.println();

        System.out.println("Testing SuperDigit");
        System.out.println(superDigit("1234", 3));
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
            if (numVal > 65 && numVal < 90) {

                // # if the shift value makes the letter a symbol
                // # subtract or add the alphabet length to shift to the start or end of the
                // alphabet string
                // # set the newChar = char(incrementVal(k) + asciiValue(numVal))
                if ((numVal + rotation) > 90) {
                    rotation -= 25;
                    newChar = (char) (numVal + rotation);
                } else if ((numVal + rotation) < 65) {
                    rotation += 25;
                    newChar = (char) (numVal + rotation);
                } else {
                    newChar = (char) (numVal + rotation);
                }

                // # if the letter is 97 > x < 122 its uppercase
            } else if (numVal > 97 && numVal < 122) {

                if ((numVal + rotation) > 122) {
                    rotation -= 25;
                    newChar = (char) (numVal + rotation);
                } else if ((numVal + rotation) < 97) {
                    rotation += 25;
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

    public static String gridChallenge(List<String> grid) {

        // Sort the Array
        for (int i = 0; i < grid.get(i).length() - 1; i++) {
            char[] tempArr = grid.get(i).toCharArray();
            Arrays.sort(tempArr);
            grid.set(i, new String(tempArr));
        }
        for (int i = 0; i < grid.get(i).length() - 1; i++) {
            for (int j = 0; j < grid.get(j).length() - 1; j++) {
                if (grid.get(i).charAt(j) > grid.get(i).charAt(j + 1)) {
                    return "NO";
                }
            }
        }

        return "YES";
    }

    public static int superDigit(String n, int k) {
        if (n.length() == 1) {
            return Integer.parseInt(n);
        }

        int count = 0;
        for (int i = 0; i < n.length(); i++) {
            int charVal = Character.getNumericValue(n.charAt(i));
            count += charVal;
        }
        count *= k;

        return superDigit(String.valueOf(count), 1);
    }
}
