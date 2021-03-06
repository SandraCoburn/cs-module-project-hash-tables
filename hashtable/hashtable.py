class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.data = [None] * capacity
        self.slots = 0
       # print("this is data: ", self.data)
        print("this is the head", self.head)

    def get_num_slots(self):

        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load_factor = self.slots / self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        #Returns the FNV-1a has of a string
        fnvPrime = 16777619
        fnvhash = 2166136261
        for string in key:
            charCode = ord(string)
            #Mask to get the first octed, and add it to the has
            firstOctet = (charCode & 0xFF)
            fnvhash = fnvhash ^ firstOctet
            #Btiwise OR with zero to ensure a 32bit integer
            fnvhash = (fnvhash * fnvPrime) | 0
            #shift to get the second byte, and add it to the hash
            secondOctet = (charCode >> 8)
            fnvhash = fnvhash ^ secondOctet
            fnvhash = (fnvhash * fnvPrime) | 0
        return fnvhash
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        x = key[0] << 7
        for chr in key[1:]:
            x = ((100003 * x) ^ chr) & (1<<32)
        return x


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #Day 2
        index = self.hash_index(key)
        #entry = self.data[index]
        #cur = self.head 
        self.slots += 1
        if self.data[index] is None:
            self.data[index] = HashTableEntry(key, value)
        else:
            node = self.data[index]
            while node is not None:
                #check if key exists and overwrite
                if node.key == key:
                    node.value = value
                    return
                #check if there is next and assign
                elif node.next:
                    node = node.next 
                #If none, create a new HashTable Entry for next node
                else: 
                    node.next = HashTableEntry(key, value)
                    return
        
      
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #Day 1:
        #self.data[index] = HashTableEntry(key, value)
        #Day 2 
        index = self.hash_index(key)   
        node = self.data[index]
            #check that current key is equal to key 
        self.slots -= 1 
        while node:
            if node.key == key:
                node.value = None
                return
            else:
                if node.next is not None:
                    node = node.next  
               
        return None 
        # else:
        #     print("Key could not be found")


    def get(self,key):
        index = self.hash_index(key)
        #return self.data[index]
        if self.data[index] is not None:
            node = self.data[index]
            
            while node:
                #check that key is the same
                if node.key == key:
                    return node.value
                else:
                    #If key is not the same, check next node
                    node = node.next       
        return None
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    # ht.put("line_13", "Adn doost awhile in thought.")
    # print(ht.get("line_13"))
    ht.delete("line_11")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
