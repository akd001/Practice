class BinarySearch
{
    int binarySearchRecursive(int arr[], int l, int r, int x) {
        if (r>=l) {
            int mid = l + (r - l)/2;
 
            if (arr[mid] == x)
               return mid;
 
            if (arr[mid] > x)
               return binarySearchRecursive(arr, l, mid-1, x);
 
            return binarySearchRecursive(arr, mid+1, r, x);
        }
 
        return -1;
    }

    int binarySearchIterative(int arr[], int x) {
        int l = 0;
        int r = arr.length-1;
        while (l<=r) {
            int mid = l + (r-l)/2;

            if (arr[mid] == x)
                return mid;
                
            if (arr[mid]>x)
                r = mid-1;
            else
                l = mid+1;
        }
        return -1;
    }
 
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2,3,4,10,40};
        int n = arr.length;
        int x = 10;
        // int result = ob.binarySearchRecursive(arr,0,n-1,x);
        int result = ob.binarySearchIterative(arr,x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index "+result);
    }
}