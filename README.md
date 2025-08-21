# UUID Payload Loader

This project demonstrates a Windows technique for decoding and executing a payload from an array of UUID strings. The payload is stored as UUIDs, converted back into raw shellcode at runtime, and executed through a callback function pointer.  

## How It Works
1. **Payload Encoding**  
   - The shellcode is represented as an array of UUID strings (`uuids` in `payload.h`).

2. **Heap Allocation**  
   - A RWX (read-write-execute) heap is created with `HeapCreate` and `HeapAlloc`.

3. **UUID Decoding**  
   - Each UUID string is converted back into 16 bytes of binary data using `UuidFromStringA`.  
   - The decoded payload is written sequentially into the allocated heap.

4. **Execution**  
   - The payload is executed indirectly by passing its address as a callback to `EnumSystemLocalesA`.

##References
- [UUID Shellcode Execution](https://blog.sunggwanchoi.com/eng-uuid-shellcode-execution)
- [RIFT: Analysing a Lazarus Shellcode Execution Method](https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method)
