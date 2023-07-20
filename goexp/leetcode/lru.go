package leetcode

// https://leetcode.com/problems/lru-cache

import "fmt"


type CacheNode struct {
	key int
	value int
	prev, next *CacheNode
}


type LRUCache struct {
    capacity int
	head, tail *CacheNode
	cache map[int]*CacheNode
}


func Constructor(capacity int) LRUCache {
	temp := $CacheNode{}

	return LRUCache{
		capacity: capacity, 
		head: temp,
		tail: temp,
		cache: make(map[int]*CacheNode)
	}
    
}

func RemoveCacheNode(lru LRUCache, key int) LRUCache {
	nodeUpForDeletion := lru.cache[key]
	if (nodeUpForDeletion.prev) nodeUpForDeletion.prev.next = nodeUpForDeletion.next
	if (nodeUpForDeletion.next) nodeUpForDeletion.next.prev = nodeUpForDeletion.prev
	delete(lru.cache, key)
	return lru
}


func (this *LRUCache) Get(key int) int {
    
}


func (this *LRUCache) Put(key int, value int)  {
	node := &CacheNode{
		key: key
		value: value
	}

	// if number of elements is less than capacity
	if (len(this.cache) < this.capacity) {
		// if key already exists, remove existing node
		if (this.cache[key]) {
			RemoveCacheNode(this, key)
		}
		// add new node at head
		node.next = this.head
		this.head = node
		// update cache value
		this.cache[key] = node
		// if this is the only node present, tail points to itself
		if (len(this.cache)==1) this.tail = node
	} 
	// if number of elements is equal to (or more than - which is improbable if this logic is correct)
	else {
		// remove tail
		if this.head 
	}

}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */