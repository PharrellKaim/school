package org.example;

import java.util.ArrayList;
import java.util.List;

public class BinarySearch {

    private List<Integer> list = addingItems();

    private List<Integer> addingItems() {
        List list = new ArrayList<Integer>();

        list.add(10);
        list.add(40);
        list.add(60);
        list.add(100);
        return list;
    }

    public int binarySearch(int searchedValue) {
        int iterations = 0;
        int low = 0;
        int high = list.size() - 1;
        int mid = 0;

        while (low <= high) {
            iterations = iterations + 1;

            mid = (high + low) / 2;


            if (list.get(mid) < searchedValue) {
                low = mid +1;
            } else if (list.get(mid) > searchedValue) {
                high = mid - 1;
            } else {
                return mid;
            }
        }
        return iterations;
    }
}

class MainBinary {
    public static void main(String[] args) {
        BinarySearch algorithm = new BinarySearch();
        System.out.println(algorithm.binarySearch(60));
    }
}
