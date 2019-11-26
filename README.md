# Huffman coding

### Python implementation of the Huffman coding compression method.
#### Read about it on [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding) or [GeeksforGeeks](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/).

### Sample data
|   Key | Frequency  |
|:---:|:---:|
|  1 | 144  |
|  2 | 20  |
| 3  |  8 |
|  4|100   |
|   5|25   |


### Tree formed

```
   _297_____
  /         \
144        _153___
          /       \
        100       _53___
                 /      \
                25      _28
                       /   \
                      20    8
```

### New representation
|   Key | Sequence  |
|:---:|:---:|
|  1 | 0 |
|  2 | 1110  |
| 3  |  1111 |
|  4| 10 |
|   5|110  |

### Compression ratio:
 
```
Compression ratio = Number of bits used before compression / = 2376 / 531  = 4.47
                    Number of bits used after compresssion

```
