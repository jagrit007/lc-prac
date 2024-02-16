class Solution {
    public int countPrimes(int n) {
        // Sieve of Eratosthenes approach
        boolean sqaureOfPrime[] = new boolean[n+1];
        int count = 0;
        for(int i=2; i*i <=n; i++){
            if (sqaureOfPrime[i] == false){
                for(int j=i*i; j<=n; j+=i){
                    sqaureOfPrime[j] = true;
                }
            }
        }
        for(int i=2; i<n; i++){
            if(sqaureOfPrime[i] == false){
                count++;
                }
        }
        return count;

    }
}