// Author : Shreya Prabhu

class RearrangeArray {

    void rearrange(int arr[], int n)
    {
        for (int i = 0; i < n; i++)
            arr[i] += (arr[arr[i]] % n) * n;
        for (int i = 0; i < n; i++)
            arr[i] /= n;
    }

    void printArr(int arr[], int n)
    {
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        System.out.println("");
    }

    public static void main(String[] args)
    {
        RearrangeArray rearrange = new RearrangeArray();
        int numberOfElements = Integer.parseInt(args[0]);

        int arr[] = new int[numberOfElements];
        for (int i = 0; i < numberOfElements; i++)
            arr[i] = Integer.parseInt(args[i+1]);

        int n = arr.length;

        System.out.println("Given Array is :");
        rearrange.printArr(arr, n);

        rearrange.rearrange(arr, n);

        System.out.println("Modified Array is :");
        rearrange.printArr(arr, n);
    }
}

