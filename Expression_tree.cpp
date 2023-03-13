#include <iostream>
#include <stack>
using namespace std;
bool isOperator(char x) {
  switch (x) {
  case '+':
  case '-':
  case '/':
  case '*':
  case '^':
  case '%':
    return true;
  }
  return false;
}
string preToInfix(string pre_exp) {
  stack<string> s;
  int length = pre_exp.size();
  for (int i = length - 1; i >= 0; i--) { 
    if (isOperator(pre_exp[i])) {
      string op1 = s.top();   s.pop();
      string op2 = s.top();   s.pop();
      string temp = "(" + op1 + pre_exp[i] + op2 + ")";
      s.push(temp);
    }
    else {
 
      s.push(string(1, pre_exp[i]));
    }
  }
  return s.top();
}

typedef struct node
{
    char data;
    struct node *left, *right;
} * nptr;
nptr newNode(char c)
{
    nptr n = new node;
    n->data = c;
    n->left = n->right = nullptr;
    return n;
}
nptr build(string& s)
{
    stack<nptr> stN;
    stack<char> stC;
    nptr t, t1, t2;
    int p[123] = { 0 };
    p['+'] = p['-'] = 1, p['/'] = p['*'] = 2, p['^'] = 3,
    p[')'] = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(') {
            stC.push(s[i]);
        }
        else if (isalpha(s[i]))
        {
            t = newNode(s[i]);
            stN.push(t);
        }
        else if (p[s[i]] > 0)
        {
            while (
                !stC.empty() && stC.top() != '('
                && ((s[i] != '^' && p[stC.top()] >= p[s[i]])
                    || (s[i] == '^'
                        && p[stC.top()] > p[s[i]])))
            {
                t = newNode(stC.top());
                stC.pop();
                t1 = stN.top();
                stN.pop();
                t2 = stN.top();
                stN.pop();
                t->left = t2;
                t->right = t1;
                stN.push(t);
            }
            stC.push(s[i]);
        }
        else if (s[i] == ')') {
            while (!stC.empty() && stC.top() != '(')
            {
                t = newNode(stC.top());
                stC.pop();
                t1 = stN.top();
                stN.pop();
                t2 = stN.top();
                stN.pop();
                t->left = t2;
                t->right = t1;
                stN.push(t);
            }
            stC.pop();
        }
    }
    t = stN.top();
    return t;
}
void postorder(nptr root)
{
    if (root)
    {
        postorder(root->left);
        postorder(root->right);
        cout << root->data;
    }
}
int main() {
  string pre_exp = "+--a*bc/def";
  cout << "Infix : " << preToInfix(pre_exp)<<endl;
  string s = preToInfix(pre_exp);
  s = "(" + s;
  s += ")";
  nptr root = build(s);
  cout<<"Post Order Traversal:";
  postorder(root);
  return 0;
}