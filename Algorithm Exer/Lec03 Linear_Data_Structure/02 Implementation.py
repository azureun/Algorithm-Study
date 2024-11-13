# Linked list

#Look-up : O(n)
#Insert : O(n)
#Delete : O(n)
#Append : O(1)
#Prepend : O(1)

class Node():
    def __init__(self, data):
        self.data = data    #매개변수로 입력 받은 data를 self.data에 대입
        self.next = None    #초기에는 다음 노드 가리키는 next는 none


class LinkedList():
    def __init__(self):     # 초기화
        self.head = None    # 처음에 머리노드에 아무것도 없음.
        self.tail = None    # 꼬리노드도
        self.length = 0     # self.length도 0으로 초기화

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()

    # Append (꼬리에 새로운 노드 추가) - "노드(new_node) 삽인한 후," 꼬리 노드를 참조(중요)
    def append(self, data):
        new_node = Node(data)
        if self.head == None:       #list가 비어있는지 확인 : head가 비었다면,
            self.head = new_node    #새로운 노드가 head임을 가리키게
            self.tail = self.head   #추가된 노드를 tail에도 추가
            self.length += 1         #길이 1 증가
        else:
            self.tail.next = new_node   #기존 tail 노드의 next 속성에 새로 만든 new_node를 연결 -> 기존 리스트 끝에 새로운 노드 추가
            self.tail = new_node        #새로 추가된 new_node를 리스트의 새로운 tail로 업데이트. 리스트의 마지막 노드를 새 노드로 갱신
            self.length += 1            #리스트 길이 1 증가

    # Prepend (머리에 새로운 노드 추가) - "new_node 삽입하기 전의 머리 노드(self.head)"를 참조(중요)
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head   # 머리노드 self.head를 next에 대입
            self.head = new_node
            self.length += 1
        
    # Insert (특정 위치에 새로운 노드를 추가)
    ## 리스트보다 특정 위치 길면 append() 메서드 사용과 동일
    ## 특정 위치가 0이면 prepend() 메서드 사용과 동일
    ## 특정 위치의 바로 이전을 찾아야 함. -> new_node의 next는 이전 node의 next와 동일, 현재 node는 다음을 새로운 node로 할당.
    def insert(self, position, data):
        if position >= self.length:
            if position > self.length:
                print("This position is not available. Inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length +=1

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delte.")
            return
        
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        
        while current_node.next != None and current_node.data != data:
            #if current_node.data == data:
            # previous_node.next = current_node.next
            # return
            current_node = current_node.next
        
        if current_node.next != None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")

    #Another functionality of linked lists
    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        
        if position >= self.length:
            position = self.length - 1
        
        current_node = self.head
        for i in range(position -1):
            current_node = current_node.next
        current_node = current_node.next.next

        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

if __name__ == '__main__':
    my_linked_list = LinkedList()
    my_linked_list.print_list()

    # Empty
    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()
    
    #5 2 9
    my_linked_list.prepend(4)
    my_linked_list.print_list()

    #4 5 2 9
    my_linked_list.insert(2,7)
    my_linked_list.print_list()
    
    #4 5 7 2 9
    my_linked_list.insert(0, 0)
    my_linked_list.insert(6, 0)
    my_linked_list.insert(9, 3)
    my_linked_list.print_list()


    #This position is not available. Inserting at the end of the list
    #0 4 5 7 2 9 0 3
    my_linked_list.delete_by_value(3)
    my_linked_list.print_list()

    #0 4 5 7 2 9 0
    my_linked_list.delete_by_value(0)
    my_linked_list.print_list()

    #4 5 7 2 9 0
    my_linked_list.delete_by_position(3)
    my_linked_list.print_list()

    #4 5 7 9 0
    my_linked_list.delete_by_position(0)
    my_linked_list.print_list()

    #5 7 9 0
    my_linked_list.delete_by_position(8)
    my_linked_list.print_list()
    
    #5 7 9
    print(my_linked_list.length)

