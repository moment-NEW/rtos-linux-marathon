//这部分用来练习多线程。这里就实现一个简单的多线程网页接受吧



#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#include <memory.h>

#define XOR_LIST(a, b) ((Node_t*)((uintptr_t)(a) ^ (uintptr_t)(b)))
//异或列表，原理是next可以是前一个节点的地址和后一个节点地址的异或值
//于是，只要知道节点1的地址就可以获取下两个节点2,3的地址
//这块属于是路径依赖了，本来yeild其实类似协程，不需要链表用来排就绪什么的
typedef struct {
    int data;
    uintptr_t next;
}Node_t;
//用于malloc创建的TCB，使用一个数字标识标签
typedef struct {
    uint8_t* label;
} TCB_t;

void get_next_node(Node_t* node, Node_t** next, Node_t** prev)
{
    *next = XOR_LIST(node->next, *prev);
    *prev = node;
}
TCB_t* TCB_create(uint8_t* label)
{
    if(label == NULL)
    {
       
        return NULL;
    }
    TCB_t* tcb = (TCB_t*)malloc(sizeof(TCB_t));
    tcb->label = label;
    return tcb;
}
//模拟的压栈弹栈
void TCB_pop(TCB_t* tcb, uint8_t* label)
{
    if(tcb == NULL)
    {
        return;
    }
    label = tcb->label;
    tcb->label = NULL;
    

}
void TCB_push(TCB_t* tcb, uint8_t* label)
{
    if(tcb == NULL)
    {
        return;
    }
    tcb->label = label;
}




void Yeild(TCB_t *target,TCB_t *now)//泛型指针，用于传入标签地址
{
   //这里是简单的让出CPU运行的函数。实际使用goto模拟吧
   switch(*target->label)
   {
       case 1:\
         goto thread1;
       case 2:\
         goto thread2;
       case 3:\
         goto thread3;
   }
   
}


//GCC拓展的缘故，不能用太多函数封装，写一起得了。反正本来也就是类汇编的东西。之后再用汇编写个正儿八经的吧
//下次试试arm汇编这样
int main(int argc, char* argv[])
{
    //GCC拓展，可以把标签的地址放到数组里，然后通过goto *labels[i]来跳转
    void *labels[]={
        &&thread1,
        &&thread2,
        &&thread3,
        &&thread4,
       
    };
    uint8_t text = 1;
    uint8_t image = 2;
    uint8_t video = 3;
    uint8_t current = 0;
    TCB_t* tcb1 = TCB_create(&text);
    TCB_t* tcb2 = TCB_create(&image);
    TCB_t* tcb3 = TCB_create(&video);
    base:
    goto *labels[current];
    //Text
    thread1:

    //Image
    thread2:

    //Video
    thread3:
    //结束
    thread4:
    return 0;
}