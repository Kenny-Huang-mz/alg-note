
# BellmanFord算法

## 介绍
BellmanFord算法是用来处理单源汇的最短路算法，与Dijkstra不同的是它可以用来处理负权边，并且可以判断是否存在负环

## 过程
假设图中有n个节点，m条边，dist[a]为节点 a 到源点的最短距离，w 为某两个节点之间的边权。

该算法循环遍历 n - 1 次，并且每一次遍历就对所有节点进行松弛操作，dist[b] = min(dist[b], dist[a] + w)。

需要注意的是，每次外层循环一次，相当于每次可以走的边数又增加了一条（可能说的有点抽象）。意思是，当 i = 1 时，现在求的是从源点开始向后走一条边，到达的点离源点的最短距离。为了加强理解，放一个例题在这里给大家参考 [有边数限制的最短路](https://www.acwing.com/problem/content/855/)

这道题可以说是BellmanFord的板子题了，就直接贴上代码。
```
#include <bits/stdc++.h>
using namespace std;

const int N = 510, M = 10010;

int n, m, k;
int dist[N], backup[N];

struct edge {
    int a, b, w;
} Edge[M];

void bellman_ford() {
    memset(dist, 0x3f3f3f3f, sizeof dist);
    dist[1] = 0;
    for(int i = 1; i <= k; i++) {
        memcpy(backup, dist, sizeof backup);
        for(int j = 1; j <= m; j++) {
            int a = Edge[j].a, b = Edge[j].b, w = Edge[j].w;
            dist[b] = min(dist[b], backup[a] + w);
        }
    }
    return ;
}

int main() {
    cin >> n >> m >> k;
    for(int i = 1; i <= m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        Edge[i] = {a, b, w};
    }
    
    bellman_ford();
    
    if(dist[n] > 0x3f3f3f3f / 2) cout << "impossible" << endl;
    else cout << dist[n] << endl;
    
    return 0;
}
```

## Question
- 为什么需要backup数组？这个数组是用来干啥的？
> 这个可以说是该算法的关键了，首先，该算法应用的是动态规划的思想。通俗来说，从源点出发，每次向后执行一条边，同时更新该节点的最短距离。而为了保证每次只向后更新一条边，就需要在每次松弛的时候，用上一个点未更新的距离来更新该节点的距离（感觉我说的还是不太好，所以等会还是直接上图来理解吧）。因此，我们之前写的代码其实是有问题的，~~其实我是故意这样的~~ 。
正确的松弛方法应该是 dist[b] = min(dist[b], backup[a] + w) 也就是用上次还未更新的路径去更新。
<br> 假设我们有三个节点a, b, c，现求边数不超过1的，a 到 c 的最短路径
!(E:/alg-note/image/BellmanFord_p1)


- 为什么该算法可以检测负环？
> 该图一共有 n 个节点，因此从1号节点即源点，到 n 号点的最短路最多遍历 n - 1 条边，如果在进行了n - 1次松弛后，仍然还可以继续更新最短距离