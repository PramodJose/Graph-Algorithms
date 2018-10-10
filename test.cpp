#include <iostream>
using namespace std;

class Vertex
{
public:
	char vName;
	unsigned int indegree, adjacentVertices;
	Vertex **adjVertVec;

	Vertex()
	{
		indegree = 0;
		vName = 0;
		adjacentVertices = 0;
		adjVertVec = NULL;
	}

	Vertex(int num)
	{
		vName = 'A' + num - 1;
		indegree = 0;
		adjacentVertices = 0;
		adjVertVec = NULL;
	}
};

class Graph
{
public:
	Vertex **v;
	int vertices;

	Graph(int size)
	{
		vertices = size;
		v = new Vertex*[vertices];
		for(int i = 0; i < vertices; ++i)	// Create all the vertices.
			v[i] = new Vertex(i + 1);

		for(int i = 0; i < vertices; ++i)
		{
			int n;
			cout << "Enter number of vertices adjacent to Vertex " << i + 1<< " : ";
			cin >> v[i]->adjacentVertices;
			n = v[i]->adjacentVertices;

			v[i]->adjVertVec = new Vertex*[n];			// Create an array of Vertex pointers of size n, i.e. the number of adjacent vertices.
			for(int j = 0; j < n; ++j)
			{
				int adjVertex;
				cout << "Enter vertex number: ";
				cin >> adjVertex;
				v[i]->adjVertVec[j] = v[adjVertex -1];
				v[adjVertex - 1]->indegree++;
			}

		}
	}

	Vertex* operator[](int pos)
	{
		return v[pos];
	}
};

int main()
{
	Graph g(7);
}