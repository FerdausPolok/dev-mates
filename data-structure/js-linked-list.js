// custom dataStructure linked list of JavaScript with in built data structure like array oject etc
class LinkedList {
    constructor() {
        this.head = null; //first element of the list
        this.tail = null; //last element of the list
    }

    //add at the end of the list
    append(value) {
        const newNode = { value: value, next: null };
        if (this.tail) { //tail !== null
            this.tail.next = newNode;
        }
        this.tail = newNode;

        if (!this.head) { //tail === null
            this.head = newNode;
        }
    }

    //add at the beginning of the list
    prepend(value) {
        const newNode = { value: value, next: this.head };
        this.head = newNode;

        if (!this.tail === null) { //tail === null
            newNode = { value: value, next: null };
        }
    }

    //delete a specific element
    delete(value) {
        if (!this.head) {
            return;
        }

        while (this.head && this.head.value === value) {
            this.head = this.head.next;
        }

        let cureNode = this.head;
        while (cureNode.next) {
            if (cureNode.next.value === value) {
                cureNode.next = cureNode.next.next;
            } else {
                cureNode = cureNode.next;
            }
        }

        if (this.tail.value === value) {
            this.tail = cureNode;
        }
    }

    //find the first node if there is any exact and return that
    find(value) {
        if (!this.head) {
            return null;
        }

        let curNode = this.head;

        while (curNode) {
            if (curNode.value === value) {
                return curNode;
            }
            curNode = curNode.next;
        }

        return null;
    }

    // convert to array of lists to see the full linked list
    toArray() {
        const elements = [];

        let curNode = this.head;

        while (curNode) {
            elements.push(curNode);
            curNode = curNode.next;
        }

        return elements;
    }

    //insert a value after specific node
    insertAfter(value, afterValue) {
        const existingNode = this.find(afterValue);

        if (existingNode) {
            const newNode = { value: value, next: existingNode.next };
            existingNode.next = newNode;
        }
    }

    length() {
        let curNode = this.head;
        let length = 0;

        while (curNode) {
            length += 1;
            curNode = curNode.next;
        }

        return length;
    }

}

const linkedList1 = new LinkedList();
linkedList1.append("veryFirstEl");
linkedList1.append(2);
linkedList1.append("Polok");
linkedList1.append(2);
linkedList1.append("Polok");
linkedList1.append("2nd element");
linkedList1.append(true);
linkedList1.append(1000);

console.log(linkedList1.toArray());

linkedList1.delete("veryFirstEl");
linkedList1.delete("Polok");
linkedList1.delete(2);
linkedList1.delete(1000);

console.log(linkedList1.toArray());

console.log(linkedList1.find("2nd element"));
console.log(linkedList1.find("Max"));

linkedList1.insertAfter("new value", "2nd element");

console.log(linkedList1.toArray());
console.log(linkedList1.length());
