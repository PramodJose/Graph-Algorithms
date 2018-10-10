#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Vertex
{
public:
	char vName;
	unsigned int indegree, adjacentVertices;
	Vertex **adjVertVec;

	/*Vertex()
	{
		indegree = 0;
		vName = 0;
		adjacentVertices = 0;
		adjVertVec = NULL;
	}*/

	Vertex(int num)
	{
		vName = 'A' + num - 1;
		indegree = 0;
		adjacentVertices = 0;
		adjVertVec = NULL;
	}
};

class Edge
{
private:
	static short int count;
public:
	short int eName;
	int weight;
	Vertex *from, *to;

	Edge()
	{
		eName = count++;
		from = to = NULL;
		weight = 0;
	}

	~Edge()
	{
		--count;
	}
};

short int Edge::count = 1;

class Graph
{
public:
	Vertex **v;
	vector<Edge> e;
	int vertices;
	int edges;

	Graph(int size)
	{
		vertices = size;
		edges = 0;

		v = new Vertex*[vertices];
		for(int i = 0; i < vertices; ++i)	// Create all the vertices.
			v[i] = new Vertex(i + 1);

		for(int i = 0; i < vertices; ++i)
		{
			int n;
			cout << "Enter number of vertices adjacent to Vertex " << (char)('A' + i)<< " : ";
			cin >> v[i]->adjacentVertices;
			n = v[i]->adjacentVertices;
			edges += n;

			v[i]->adjVertVec = new Vertex*[n];			// Create an array of Vertex pointers of size n, i.e. the number of adjacent vertices.
			for(int j = 0; j < n; ++j)
			{
				int adjVertex, weight;
				Edge newEdge;
				cout << "Enter vertex number: ";
				cin >> adjVertex;
				v[i]->adjVertVec[j] = v[adjVertex -1];
				v[adjVertex - 1]->indegree++;
				cout << "Enter the edge weight: ";
				cin >> weight;
				newEdge.weight = weight;
				newEdge.from = v[i];
				newEdge.to = v[adjVertex -1];
				e.push_back(newEdge);
			}

		}
	}

	Vertex* operator[](int pos)
	{
		if (pos < 0 || pos >= vertices)
			return NULL;
		return v[pos];
	}

	friend ostream & operator << (ostream &out, const Graph &g); 
    //friend istream & operator >> (istream &in,  Graph &g); 
};

ostream& operator <<(ostream &out, const Graph &g)
{
	out << "The graph is:-\n";

	for(int i = 0; i < g.vertices; ++i)
	{
		out << g.v[i]->vName << " --> ";

		for(int j = 0; j < g.v[i]-> adjacentVertices; ++i)
			out << g.v[i]->adjVertVec[j]->vName << " -> ";

		out << "NULL\n";
	}

	return out;
}

int main()
{
	Graph g(3);
	cout << g;
}