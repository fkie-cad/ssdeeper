# Last segment bug

If the last byte of the input triggers an anchor point, an empty last segment will be appended to the similarity hash value. This can be a critical error if it leads to the selection of a block size that has a much smaller hash of length 32 characters. The fnv hash is initialized to 0x27, which corresponds to the base64 character 'n', as can be seen in the following hash. 

768:6WAU41W2CS9MXcjtKOTiHxC1j/ZDeUl/wC/wmFK9xhFRpoCwi96n:61DbCdcjoD811D3wC//FGxhFryn,"forensic_last_segment.txt"

The error is within the digest construction after processing the input. 

``` 
uint32_t h = roll_sum(&self->roll);
if (h != 0){
    add character to digest
}
else if(last_b64 != '\0'){
    add character to digest
}
``` 

which has been exchanged with:

```
uint32_t h = roll_sum(&self->roll);
if ((h+1)==0 || ((h+1) % SSDEEP_BS(bi))){
    add character to digest
}
``` 
768:6WAU41W2CS9MXcjtKOTiHxC1j/ZDeUl/wC/wmFK9xhFRpoCwi96:61DbCdcjoD811D3wC//FGxhFry,"forensic_last_segment.txt"
