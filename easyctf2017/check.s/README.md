下下来这么一个汇编文件(check.s)
```
check（int, int）:
        pushq   %rbp
        movq    %rsp, %rbp
        movl    %edi, -36(%rbp)
        movl    %esi, -40(%rbp)
        movl    -36(%rbp), %eax
        xorl    -40(%rbp), %eax
        movl    %eax, -4(%rbp)
        movl    -4(%rbp), %eax
        addl    $98, %eax
        movl    %eax, -8(%rbp)
        movl    -8(%rbp), %eax
        notl    %eax
        movl    %eax, %edx
        movl    -40(%rbp), %eax
        addl    %edx, %eax
        movl    %eax, -12(%rbp)
        movl    -12(%rbp), %eax
        xorl    -36(%rbp), %eax
        movl    %eax, -16(%rbp)
        movl    -40(%rbp), %eax
        imull   -4(%rbp), %eax
        cltd
        idivl   -8(%rbp)
        movl    %eax, %edx
        movl    -36(%rbp), %eax
        leal    (%rdx,%rax), %ecx
        movl    -12(%rbp), %edx
        movl    -16(%rbp), %eax
        addl    %edx, %eax
        xorl    %ecx, %eax
        movl    %eax, -20(%rbp)
        cmpl    $-814, -20(%rbp)
        sete    %al
        popq    %rbp
        ret

```
粗略看了一下 是一个汇编写的函数，想笔算的，后来发现太恶心了，于是想到内联汇编的方法。
代码具体如下
新建一个main.c
```c
#include<stdio.h>
int check(int,int);
int main(){
	int argv1,argv2;
	scanf("%d",argv1);
	scanf("%d",argv2);
	check(argv1,argv2);
	printf("%d",argv1);
	return 0;
}

```
为了调用.s文件中的汇编代码 修改.s文件
只改动前三行
```
.type check, @function
.global check
check:
        pushq   %rbp
```
然后编译
```
#as -o check.o check.s
#gcc -o main main.c check.o
```
生成的main文件直接丢到IDA里 然后f5大法 双击进入check函数体
```c
bool __fastcall check(int a1, int a2)
{
  return (((a2 ^ a1) * a2 / ((a2 ^ a1) + 98) + a1) ^ (~((a2 ^ a1) + 98) + a2 + (a1 ^ (~((a2 ^ a1) + 98) + a2)))) == -814;
}
```
然后就随意写个东西对这行代码进行xxoo 本来想着从int最小值开始跑，基友发现从0到500就有n多个结果，然后随便找了一个200:300提交 done！
