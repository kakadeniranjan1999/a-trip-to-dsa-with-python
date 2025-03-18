from utils.hash_tables import HashTable


hash_table = HashTable(
    [
        ['march 6', 6],
        ['march 8', 8]
    ]
)
print(len(hash_table))
print(hash_table._get_hash('march 6'))
