# primenumbers-technologies-Assignment

#### Defined Series elements are,
  0, 1, 2, 2, *0, -4, -8, -8,* 0, 16, 32, 32, *0, -64, -128, -128,* 0, 256, 512, 512, 0, -1024, -2048, -2048, 0, 4096, 8192, 8192, 0, -16384, -32768,...
* From the observation, these elements are **series of powers of 2**.
 
  Checking the given integer is *power of 2*:
  ```python
  pow_val = math.log2(abs(elem))
  if math.ceil(pow_val) == math.floor(pow_val):
      return True
  ```
* And in the sequence some of them are negative with series distance is *4*
  
  * Positive elements from the series **1, 2, 16, 32, 256, 512, 4096,8192...** with power values **0,1,4,5,8,9,12,13,16,17,...**
    
    The power values are in merged sequence of two arithmetic sequence i.e.,
    ```
    a = 0, d=4 Series:- 0, 4, 8, 12, 16,...
    a = 1, d=4 Series:- 1, 5, 9, 13, 17,...
    ```
  
  * Negative elements from the series **-4,-8,-64,-128,-1024,-2048,-16384...** with power values **2,3,6,7,10,11,14,15,18,19...**

    The power values are in merged sequence of two arithmetic sequence i.e.,
    ```
    a = 2, d=4 Series:- 2, 6, 10, 14, 18,...
    a = 3, d=4 Series:- 3, 7, 11, 15, 19,...
    ```
    
    Check the power value belongs to one of the arithmetic sequence:
    ```python
       def is_member_of_AP(a,d, num):
           return ((num - a)%d == 0 & int((num - a)/d) >= 0)
       
       neg_status = elem<0
       if neg_status and (is_member_of_AP(2,4,pow_val) or is_member_of_AP(3,4,pow_val)):
           return True
       if not neg_status and (is_member_of_AP(0,4,pow_val) or is_member_of_AP(1,4,pow_val)):
           return True
    ```
    
    
