class Solution {
    public long minimumPerimeter(long neededApples) {
        long n=0, sum=0;
        while(sum<neededApples){
            n++;
            sum += (12*n*n);
        }
        return 8*n;
    }
}