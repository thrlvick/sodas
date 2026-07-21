#include <stdio.h>//that's the callback pattern. the executor doesn't decide behavior — the caller does, by choosing which function to hand in.

int ascending(int a, int b) {
    return a > b;

}
int descending(int a, int b) {
    return a < b;

}
void bubble_sort(int arr[], int size, int(*compare)(int, int)){
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < size - i - 1; j++){
            if (compare(arr[j], arr[j+1])) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
void print_array(int arr[], int size){
    for (int i = 0; i < size; i++){
        printf("%d", arr[i]);
    }
    printf("\n");
}
int equal(int a, int b) {
    return a == b;
}
int main() {
    int nums[] = {5, 2, 8, 1, 9};
    int size = 5;

    bubble_sort(nums, size, ascending);
    printf("Ascending: ");
    print_array(nums, size);

    // reset
    int nums2[] = {5, 2, 8, 1, 9};
    bubble_sort(nums2, size, descending);
    printf("Descending: ");
    print_array(nums2, size);
    //ignored 
    int nums3[] = {5, 2, 8, 1, 9};
    bubble_sort(nums3, size, equal);
    printf("equal: ");
    print_array(nums3, size);

    return 0;
}

